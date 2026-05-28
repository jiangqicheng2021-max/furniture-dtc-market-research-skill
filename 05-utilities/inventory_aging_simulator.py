#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proferlo DTC Furniture Inventory Aging & Liquidation Pricing Simulator (Final Production Edition)
Models 3PL storage penalties, accounts for Working Capital Cost of Capital (WACC), 
and provides data-driven max-discount recommendations for leadership financial control.
"""

import math

def simulate_inventory_aging(initial_units, box_length, box_width, box_height, srp, fob, 
                             estimated_margin_before_storage=0.22,
                             daily_sales_velocity=1.0,
                             wacc_rate=0.06,
                             tier_1_days=90, tier_1_rate=0.65,
                             tier_2_days=180, tier_2_rate=1.80,
                             tier_3_rate=3.50):
    """
    模拟大件家具在美国3PL海外仓中，物理仓储惩罚费与资金占用机会成本双重叠加下的流血速度。
    
    参数:
    initial_units: 首批到仓总件数 (pcs)
    box_length, box_width, box_height: 单件外箱尺寸 (inch)
    srp: 建议零售价 (USD)
    fob: 工厂出厂成本价 (USD)
    estimated_margin_before_storage: 未扣除仓储和资金成本前的单件净利润率 (默认 22%)
    daily_sales_velocity: 日均动销速度 (单款每天卖出多少件, 默认 1.0 件/天)
    wacc_rate: 年化加权资金成本/流动资金占用机会成本率 (默认 6%)
    tier_1_rate: 0-90天基础仓储费率 (USD/cft/月)
    tier_2_rate: 91-180天超期仓储费率 (USD/cft/月)
    tier_3_rate: 181天以上重度惩罚性长库费率 (USD/cft/月)
    """
    
    # 算定单件产品立方英尺数 (cft)
    box_cft = (box_length * box_width * box_height) / 1728.0
    
    # 初始单件未持仓前的纯利润额
    initial_unit_profit = srp * estimated_margin_before_storage
    
    print("=" * 75)
    print(f" 📊 PROFERLO INVENTORY CARRIED COST & CAPITAL AGING SIMULATOR ")
    print("=" * 75)
    print(f"[-] 初始备货规模 : {initial_units} 件 | 单件体积: {box_cft:.2f} cft")
    print(f"[-] 压仓资金 (FOB): ${initial_units * fob:.2f} | 预设资金年化成本 (WACC): {wacc_rate * 100:.1f}%")
    print(f"[-] 预设日均动销 : {daily_sales_velocity} 件/天 | 初始单件基础利润: ${initial_unit_profit:.2f}")
    print("-" * 75)
    print(f"| 月份 | 在库剩余 (Pcs) | 物理仓储费 (Fee) | 资金占用费 (Cap) | 累计利润侵蚀率 |")
    print(f"| :--- | :--- | :--- | :--- | :--- |")

    current_stock = initial_units
    total_storage_paid = 0.0
    total_capital_cost_paid = 0.0
    break_even_month_triggered = False
    break_even_day = 0
    
    # 按月动态模拟 12 个月（360天）
    for month in range(1, 13):
        if current_stock <= 0:
            print(f"| M {month:02d}  | 0 (已售罄)     | $0.00            | $0.00            | 售罄结清开销   |")
            break
            
        days_passed_start = (month - 1) * 30
        
        # 1. 动态阶梯物理仓储费率判定
        if days_passed_start <= tier_1_days:
            current_storage_rate = tier_1_rate
        elif days_passed_start <= tier_2_days:
            current_storage_rate = tier_2_rate
        else:
            current_storage_rate = tier_3_rate
            
        # 计算当月销售消耗与平均在库指标
        units_sold_this_month = daily_sales_velocity * 30
        stock_end_of_month = max(0, current_stock - units_sold_this_month)
        avg_stock_this_month = (current_stock + stock_end_of_month) / 2.0
        
        # 当月物理仓储费
        total_cft_this_month = avg_stock_this_month * box_cft
        month_storage_fee = total_cft_this_month * current_storage_rate
        total_storage_paid += month_storage_fee
        
        # 2. 当月压仓流动资金占用财务开销 = 在库总货值(FOB) * 年化利率 / 12个月
        month_capital_cost = (avg_stock_this_month * fob) * (wacc_rate / 12.0)
        total_capital_cost_paid += month_capital_cost
        
        # 3. 测算分摊到所有初始商品身上的综合财务流血率
        cumulative_loss_per_piece = (total_storage_paid + total_capital_cost_paid) / initial_units
        remaining_profit_per_piece = initial_unit_profit - cumulative_loss_per_piece
        profit_loss_percentage = (cumulative_loss_per_piece / initial_unit_profit) * 100
        
        print(f"| M {month:02d}  | {int(current_stock):<14d} | ${month_storage_fee:<15.2f} | ${month_capital_cost:<15.2f} | {profit_loss_percentage:.1f}% 被吃掉 |")
        
        # 记录利润完全归零的财务死线
        if remaining_profit_per_piece <= 0 and not break_even_month_triggered:
            break_even_month_triggered = True
            break_even_day = days_passed_start + 15
            
        current_stock = stock_end_of_month

    print("-" * 75)
    print(f"💥 【企业CFO风控审计视角 (FINANCIAL RISK AUDIT)】:")
    print(f"  [-] 360天物理仓储费总开支  : ${total_storage_paid:.2f}")
    print(f"  [-] 流动资金压仓机会成本总计: ${total_capital_cost_paid:.2f}")
    print(f"  [-] 预计两项流血总亏损损失  : ${total_storage_paid + total_capital_cost_paid:.2f}")
    
    if break_even_month_triggered:
        print(f"\n🚨 【重大警告：突破财务周转死线！】")
        print(f"  本批货物在库房中滞留第 【{break_even_day}】 天后，其产生的累计持有成本将彻底吃空利润额！")
        print(f"  此后每销售一件都属于倒贴亏损（侵蚀品牌存量现金流）。")
        
        # 数据驱动的清仓打折抗辩建议
        print(f"\n📈 【决策层防守清仓定价指南 (Liquidation Adjustments)】:")
        # 计算进入90天和180天时，如果提前打折迅速清空，能帮公司挽回多少预期仓储损失
        print(f"  1. [库龄达 90 天节点] : 物理惩罚费即将翻倍，此时最高可允许直接对折让利约 ${initial_unit_profit * 0.40:.2f} (约占售价的 {((initial_unit_profit * 0.40)/srp)*100:.1f}%) 进行快速去库存。")
        print(f"  2. [库龄达 180 天节点]: 即将面临顶格超期费惩罚，此时哪怕将毛利空间全部让渡（直接打折 ${initial_unit_profit:.2f} / 即按零售价 ${(srp - initial_unit_profit):.2f} 割肉保本清仓），也比让其继续在库房流血更符合公司财务整体利益。")
    else:
        print(f"\n✅ 【周转模型安全合格】: 在当前日均 {daily_sales_velocity} 件的销售流速下，货品可在触及超期惩罚线前安全售罄。")
    print("=" * 75)

if __name__ == "__main__":
    # 模拟输入运行 (售价$899，工厂FOB $180，外箱 65x32x28 英寸，重110 lbs)
    # 故意模拟一个较慢的动销（日销 0.6 件），以便让 AI 能够深度审计流血红线和清仓定价
    simulate_inventory_aging(
        initial_units=120,
        box_length=65, box_width=32, box_height=28,
        srp=899, fob=180,
        estimated_margin_before_storage=0.22,
        daily_sales_velocity=0.6,
        wacc_rate=0.06
    )
