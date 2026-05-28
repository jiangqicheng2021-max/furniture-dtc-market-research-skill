#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proferlo DTC Furniture Last-Mile Shipping & Zone Density Analyzer (v1.1)
Author: Co-created with Antigravity
-------------------------------------------------------------------------
Changes in v1.1:
1. Added (Length + Girth > 105) Additional Handling rule.
2. Added Over-Maximum-Limits (Girth > 165" or Weight > 150 lbs) Critical Warning (FedEx/UPS Refusal & $1,150 Fine).
3. Added 3PL Warehouse Outbound Pick & Pack Fee ($10.00 standard).
4. Added option for "Non-Stackable" pallet-surcharge check.
"""

import math

class USShippingRateAnalyzer:
    def __init__(self, item_name, weight_lbs, length_in, width_in, height_in, 
                 is_non_stackable=False, warehouse_fulfillment_fee=10.00):
        self.item_name = item_name
        self.actual_weight = float(weight_lbs)
        self.l = float(length_in)
        self.w = float(width_in)
        self.h = float(height_in)
        self.is_non_stackable = is_non_stackable
        self.warehouse_fulfillment_fee = float(warehouse_fulfillment_fee)
        
        # 1. 算定体积重 (Dimensional Weight Formula: L * W * H / 139)
        self.dim_weight = (self.l * self.w * self.h) / 139.0
        self.billable_weight = max(self.actual_weight, self.dim_weight)
        
        # 2. 算定美国快递大件周长 (Girth = L + 2*(W + H))
        self.girth = self.l + 2 * (self.w + self.h)

    def _calculate_surcharges(self):
        """
        审计 FedEx/UPS Ground 针对大件家具极其致命的隐形附加费矩阵
        """
        surcharges = {
            "ADDITIONAL_HANDLING_DIM": 0.0,
            "ADDITIONAL_HANDLING_WT": 0.0,
            "OVERSIZE_CHARGE": 0.0,
            "NON_STACKABLE_SURCHARGE": 0.0,
            "RESIDENTIAL_DELIVERY": 5.25, # 标准住宅区配送附加费
            "WAREHOUSE_PICK_PACK": self.warehouse_fulfillment_fee # 3PL出库包装拣货工时费
        }
        
        # ⚠️ 规则A：尺寸超规附加费 (Additional Handling - Dimension)
        # 最长边 > 48" 或 第二长边 > 30" 或 (最长边 + 周长 > 105" 且 <= 130")
        sorted_sides = sorted([self.l, self.w, self.h], reverse=True)
        if sorted_sides[0] > 48.0 or sorted_sides[1] > 30.0 or (105.0 < self.girth <= 130.0):
            surcharges["ADDITIONAL_HANDLING_DIM"] = 34.00
            
        # ⚠️ 规则B：超重附加费 (Additional Handling - Weight)
        # 实际重量 > 50 lbs
        if self.actual_weight > 50.0:
            surcharges["ADDITIONAL_HANDLING_WT"] = 31.50
            
        # ⚠️ 规则C：顶格超大件惩罚 (Oversize Charge)
        # 周长超过 130 英寸 (但不超过快递极限 165 英寸)
        if self.girth > 130.0 and self.girth <= 165.0:
            surcharges["OVERSIZE_CHARGE"] = 160.00
            # 触发 Oversize 后，上述的基础尺寸/重量额外处理费将被免除，不重复收取
            surcharges["ADDITIONAL_HANDLING_DIM"] = 0.0
            surcharges["ADDITIONAL_HANDLING_WT"] = 0.0

        # ⚠️ 规则D：非堆叠附加费 (仅针对特殊卡车托盘或大件)
        if self.is_non_stackable:
            surcharges["NON_STACKABLE_SURCHARGE"] = 125.00
            
        return surcharges

    def check_maximum_limits(self):
        """
        拦截足以毁灭公司现金流的 Over Maximum Limits (快递拒收/天花板红线罚款) 状态
        """
        violations = []
        if self.actual_weight > 150.0:
            violations.append(f"实际毛重超过极限 ({self.actual_weight} lbs > 150 lbs)")
        if self.girth > 165.0:
            violations.append(f"周长超过快递限界值 ({self.girth:.2f} inches > 165.00 inches)")
            
        return violations

    def evaluate_all_zones(self):
        """
        基于美国内陆 Zone 2 到 Zone 8 阶梯费率矩阵，动态推演双仓履约成本
        """
        violations = self.check_maximum_limits()
        surcharges = self._calculate_surcharges()
        total_surcharge_pool = sum(surcharges.values())
        
        # 2026年美区大件快递基础运费阶梯倍率骨架 (Base Rate Per Lbs depending on Zones)
        zone_rate_multipliers = {
            "Zone 2": 0.45, "Zone 3": 0.58, "Zone 4": 0.72, 
            "Zone 5": 0.88, "Zone 6": 1.05, "Zone 7": 1.22, "Zone 8": 1.45
        }
        
        print("=" * 85)
        print(f" 🧮 PROFERLO REAL-TIME LAST-MILE COST MATRIX FOR: [{self.item_name.upper()}] ")
        print("=" * 85)
        print(f"[-] 物理权重: 实际毛重 {self.actual_weight} lbs | 体积重 {self.dim_weight:.2f} lbs")
        print(f"[-] 计费重量: {self.billable_weight:.2f} lbs | 外箱周长(Girth): {self.girth:.2f} inches")
        print(f"[-] 3PL出库出箱费: ${self.warehouse_fulfillment_fee:.2f} (已算入下表附加费总计中)")
        
        if violations:
            print("\n" + "🛑" * 15 + " 【致命合规警告 - OVER MAXIMUM LIMITS】 " + "🛑" * 15)
            for v in violations:
                print(f"  👉 [违规警告]: {v}")
            print("  ⚠️ [财务惩罚]: 该产品超出了 FedEx/UPS Ground 快递承运的极限死线！")
            print("  ⚠️ 实际发货中将触发 **$1,150.00/件** 的天价超限罚款，或者直接被海外仓扣留拒发！")
            print("  💡 [解决方案]: 必须强制工厂修改包装为‘双箱发货’以分摊重量，或者二期改走卡车物流 (LTL)！")
            print("🛑" * 40 + "\n")
            
        print("-" * 85)
        print(f"| 目的分区 (US Zone) | 基础运费 (Base) | 附加费总计 (Surcharge) | 最终单件尾程成本 (Total) |")
        print(f"| :--- | :--- | :--- | :--- |")
        
        zone_costs = {}
        for zone, multiplier in zone_rate_multipliers.items():
            base_rate = 25.0 + (self.billable_weight * multiplier)
            final_cost = base_rate + total_surcharge_pool
            zone_costs[zone] = final_cost
            print(f"| {zone:<18} | ${base_rate:<13.2f} | ${total_surcharge_pool:<22.2f} | ${final_cost:<23.2f} |")
            
        print("-" * 85)
        self._print_routing_strategy(zone_costs)

    def _print_routing_strategy(self, zone_costs):
        """
        根据多仓智能路由（DOM）逻辑，为市场调研报告输出高含金量的决策支撑
        """
        print("💡 【多仓分拨智能路由（DOM）调研结论】:")
        print(f"  1. [美东主场优势圈 (新泽西仓发货)] -> 覆盖大纽约及美东核心消费带 (Zone 2-3): 平均单件尾程运费仅需 **${zone_costs['Zone 3']:.2f}**。")
        print(f"  2. [跨区流血警戒线 (单仓跨全美模式)] -> 若不设美西仓，直接由美东单仓横跨全美发往加州西海岸 (Zone 8):")
        print(f"     单件尾程暴涨至 **${zone_costs['Zone 8']:.2f}**！将直接吞噬 {((zone_costs['Zone 8'] - zone_costs['Zone 3'])/zone_costs['Zone 3'])*100:.1f}% 的物流毛利空间。")
        print(f"  👉 结论：要确保综合利润率，首发 12 SKU 必须采用‘美西分摊大盘、美东精准锁死纽约’的双仓对配策略。")
        print("=" * 85)

if __name__ == "__main__":
    # 测试输入：我们 12 首发 MVP 中的超大件 BED-S-04 气压液压升降床
    # 模拟其未经优化的一整箱暴力包装（毛重 152 lbs，最长边 82 英寸，宽 32，高 24）
    analyzer = USShippingRateAnalyzer(
        item_name="Proferlo-BED-S-04-SingleBox(Extreme-Draft)", 
        weight_lbs=152, 
        length_in=82, 
        width_in=32, 
        height_in=24,
        is_non_stackable=False
    )
    analyzer.evaluate_all_zones()
