#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DTC Furniture Unit Economics & Oversize Penalty Calculator
Designed for Proferlo Market Research and Leadership Reporting.
"""

import math

def calculate_unit_economics(srp, fob, length, width, height, weight, ocean_freight, return_rate=0.12, cpc=1.5, cvr=0.018):
    """
    计算单件大件家具的全链路跨境单体经济模型，并自动进行美国尾程（FedEx/UPS）超规罚款判定。
    
    参数:
    srp: 建议零售价 (USD)
    fob: 工厂出厂价 (USD)
    length, width, height: 纸箱包装外箱尺寸 (inch)
    weight: 纸箱包装毛重 (lbs)
    ocean_freight: 单个40HQ集装箱的美东/美西干线海运总成本 (USD)
    return_rate: 预估退货率 (默认 12%)
    cpc: 平均点击成本 (USD, 默认 1.5)
    cvr: 独立站广告转化率 (默认 1.8%)
    """
    
    print("=" * 60)
    print(f" 📊 PROFERLO UNIT ECONOMICS & RISK AUDIT REPORT ")
    print("=" * 60)
    
    # 1. 体积重判定 (Dimensional Weight Calculation)
    # 美国快递大盘标准公式：长 * 宽 * 高 / 139
    dim_weight = (length * width * height) / 139.0
    billable_weight = max(weight, dim_weight)
    
    print(f"[-] 包装尺寸: {length} x {width} x {height} 英寸")
    print(f"[-] 实际毛重: {weight} lbs | 算定体积重: {dim_weight:.2f} lbs")
    print(f"[-] 计费重量 (Billable Weight): {billable_weight:.2f} lbs")
    
    # 2. 尾程超规红线判定 (FedEx/UPS Oversize & Heavy Penalty Audit)
    # 周长公式 = L + 2*(W + H)
    girth = length + 2 * (width + height)
    is_oversize = False
    oversize_penalty = 0.0
    warnings = []
    
    if length > 108:
        warnings.append("⚠️ 触发【最长边超规】: 单边长度超过 108 英寸！")
        is_oversize = True
    if girth > 130 and girth <= 165:
        warnings.append("⚠️ 触发【FedEx/UPS Oversize Charge】: 长+两倍阔度超过 130 英寸！")
        is_oversize = True
        oversize_penalty += 150.0  # 基础超规罚款标准
    if girth > 165:
        warnings.append("❌ 严重超规【拒收红线】: 长+两倍阔度超过 165 英寸，快递巨头将直接拒收或顶格罚款 $1000+！")
        is_oversize = True
        oversize_penalty += 1000.0
    if weight > 150:
        warnings.append("❌ 严重超 heavy【超重红线】: 单箱重量超过 150 lbs，触发卡车派送强制线！")
        oversize_penalty += 450.0
    elif weight > 90:
        warnings.append("⚠️ 触发【超重附加费】: 单箱重量超过 90 lbs！")
        oversize_penalty += 50.0

    if is_oversize or oversize_penalty > 0:
        print("\n💥 【物流红线警报 (LOGISTICS WARNINGS)】:")
        for w in warnings:
            print(w)
        print(f"👉 预计额外扣减超规附加罚款: ${oversize_penalty:.2f} / 每单")
    else:
        print("\n✅ 物流物理指标安全：未触发 FedEx/UPS 大件顶格罚款红线。")
        
    # 3. 供应链与干线物流成本精算 (Cube Utilization)
    # 标准 40HQ 有效装载容积约为 2350 立方英尺 (约 66.5 CBM)，计入打架损耗按 85% 算定有效容积 = 2000 cft
    box_cft = (length * width * height) / 1728.0 # 立方英寸转立方英尺
    est_units_per_container = math.floor(2000.0 / box_cft)
    single_unit_ocean_cost = ocean_freight / max(1, est_units_per_container)
    
    print(f"\n🚢 【干线海运与装载率优化】:")
    print(f"[-] 单件产品占用空间: {box_cft:.2f} 立方英尺 (cft)")
    print(f"[-] 单个 40'HQ 集装箱预计最大可容纳: {est_units_per_container} 件")
    print(f"[-] 单件分摊干线海运费: ${single_unit_ocean_cost:.2f} (基于整柜 ${ocean_freight:.2f} 测算)")

    # 4. 财务单体利润推演 (Unit Economics Engine)
    # 综合美国本地 3PL 大件内陆转运、打单、面单费基准值 (按计费重量梯度粗算)
    base_us_delivery = 45.0 + (billable_weight * 0.65) + oversize_penalty
    
    # 纯线上数字化获客成本 (CAC) = CPC / CVR
    cac = cpc / cvr
    
    # 关税成本 (假设常规家具进口基础关税及商检费综合为货值的 8%)
    duty_cost = fob * 0.08
    
    # 大件退货折旧损耗准备金 (退货运费损耗 + 包装破损二次流转折价损耗 = 综合损耗按 SRP 的 40% 算)
    return_loss_provision = srp * 0.40 * return_rate
    
    total_cost = fob + duty_cost + single_unit_ocean_cost + base_us_delivery + cac + return_loss_provision
    net_profit = srp - total_cost
    net_margin = (net_profit / srp) * 100
    
    print(f"\n💵 【单体财务模型分析 (Unit Economics Breakdown)】:")
    print(f"[-] 建议零售价 (SRP): ${srp:.2f}")
    print(f"[-] 工厂出厂成本 (FOB): ${fob:.2f}")
    print(f"[-] 进口基础税费 (Estimated Duties): ${duty_cost:.2f}")
    print(f"[-] 美东/美西末端物流派送总成本: ${base_us_delivery:.2f}")
    print(f"[-] 数字化客获成本 (CAC): ${cac:.2f} (基于 CPC:${cpc} / CVR:{cvr*100}%)")
    print(f"[-] 大件退货风险拨备金 (Return Loss Provision): ${return_loss_provision:.2f} (基于 {return_rate*100}% 退货率)")
    print("-" * 40)
    print(f"💡 最终核算单件净利润 (Net Profit): ${net_profit:.2f}")
    print(f"💡 最终核算单件净利润率 (Net Margin): {net_margin:.2f}%")
    
    # 5. 管理层汇报死线预警 (Leadership Threshold)
    print("-" * 40)
    if net_margin < 15.0:
        print("🚨 【管理层风控拒绝红线】: 本品类综合净利润率低于 15% 安全底线！")
        print("💡 建议行动：1. 强制逼迫工厂压缩 FOB；2. 优化结构缩小外包装以解除 Oversize 附加费；3. 提高零售价。")
    else:
        print("🚀 【项目可行性优良】: 财务结构健康，利润率通过风控底线，具备向领导层汇报说服力。")
    print("=" * 60)

# 测试用例模拟运行 (以一款典型的中端组合沙发包装参数为例)
if __name__ == "__main__":
    # 模拟输入：售价 $899，FOB $180，包装尺寸 65x32x28 英寸，重 110 lbs，海运费 $6000
    calculate_unit_economics(
        srp=899, 
        fob=180, 
        length=65, 
        width=32, 
        height=28, 
        weight=110, 
        ocean_freight=6000
    )
