#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proferlo DTC Furniture NY Metro Regional Preference & Return Heatmap Engine (v3.0)
—— 纽约大都市圈三州都会区工业级多维精算引擎
二次审核升级版：引入整箱销售包装折算、新泽西都会区分裂、住房空间-整箱体积梯度比、STURDY Act安全合规惩罚。
"""

import json
import sys
import io

# 强制将标准输出与标准错误重定向为 UTF-8 编码，防止 Windows 中文环境 (GBK) 打印 emoji 发生 UnicodeEncodeError
if sys.platform.startswith('win'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

class NYMetroGeoPreferenceMapperV3:
    def __init__(self, sku_id, category_name, unit_volume_cft, unit_weight_lbs, pack_qty=1, sturdy_compliant=True):
        self.sku_id = sku_id
        self.category = category_name.lower().strip()
        self.pack_qty = int(pack_qty) # 一箱装几件 (如餐椅1箱2只, pack_qty=2)
        
        # 整箱发运数据折算 (FedEx/3PL只认整箱物理 Carton 的体积和毛重)
        self.unit_volume = float(unit_volume_cft)
        self.unit_weight = float(unit_weight_lbs)
        self.carton_volume = self.unit_volume * (1.1 if self.pack_qty > 1 else 1.0) # 成组发运外箱体积常有 10% 缓冲溢出
        self.carton_weight = self.unit_weight * self.pack_qty
        self.sturdy_compliant = bool(sturdy_compliant) # 针对斗柜的 STURDY Act 防倾倒安全合规性

        # 纽约大都市圈细分都会区精算底座 (NY Metro Micro-Targeting Database)
        # 精细拆分新泽西为都会公寓高密带(NJ-HUD)与郊区别墅区(NJ-SUB)
        self.ny_metro_matrix = {
            "NYC-MAN": {
                "name": "Manhattan (曼哈顿核心都会区)", 
                "avg_home_size": 850, 
                "apt_ratio": 0.88, 
                "walkup_prob": 0.38, 
                "coi_required": 0.90,       # 90%大楼要求COI入楼凭证
                "bridge_toll_penalty": 25.0 # 曼哈顿拥堵与隧道附加费
            },
            "NYC-OUT": {
                "name": "Outer Boroughs (布鲁克林/皇后区多层)", 
                "avg_home_size": 1200, 
                "apt_ratio": 0.58, 
                "walkup_prob": 0.45,       # 窄楼道walkup最高区
                "coi_required": 0.30, 
                "bridge_toll_penalty": 15.0
            },
            "NJ-HUD": {
                "name": "Hudson Waterfront NJ (哈德逊都会公寓带)", 
                "avg_home_size": 1050, 
                "apt_ratio": 0.70,         # 泽西市/霍博肯高层密集
                "walkup_prob": 0.12, 
                "coi_required": 0.75, 
                "bridge_toll_penalty": 0.0 # 无跨河尾程费惩罚
            },
            "NJ-SUB": {
                "name": "Suburban New Jersey (新泽西中产别墅区)", 
                "avg_home_size": 2200, 
                "apt_ratio": 0.15, 
                "walkup_prob": 0.02, 
                "coi_required": 0.05, 
                "bridge_toll_penalty": 0.0
            },
            "NY-LI": {
                "name": "Long Island (长岛中产大别墅区)", 
                "avg_home_size": 2400, 
                "apt_ratio": 0.08, 
                "walkup_prob": 0.00, 
                "coi_required": 0.00, 
                "bridge_toll_penalty": 0.0
            },
            "CT-SOU": {
                "name": "Southern Connecticut (康州超高净值墅区)", 
                "avg_home_size": 2600, 
                "apt_ratio": 0.05, 
                "walkup_prob": 0.00, 
                "coi_required": 0.00, 
                "bridge_toll_penalty": 0.0
            }
        }

    def _is_single_man_friendly(self):
        """核心物理折算：以整箱(Carton)体积与毛重判定是否符合70lbs以下、窄楼道单人配送黄金线"""
        return self.carton_volume <= 14.0 and self.carton_weight <= 70.0

    def _is_dresser(self):
        """判定是否为斗柜品类"""
        return "dresser" in self.category or "chest" in self.category

    def _is_upholstered(self):
        """判定是否为软体布艺品类（沙发、床）"""
        return any(x in self.category for x in ["sofa", "bed", "couch", "seating", "chair"])

    def generate_ny_heatmap(self):
        """
        纽约大都市圈精算算法 v3.0:
        结合整箱物理数据、都会区COI限制、Walk-up、拥堵隧道费，大件空间窒息扣分梯度以及STURDY Act合规惩罚。
        """
        heatmap_report = {}
        
        for region_code, metrics in self.ny_metro_matrix.items():
            # I. 计算市场购买偏好契合度 (Market Fit Score: 1-10分)
            fit_score = 5.0  # 基础分
            
            if self._is_upholstered():
                # 软包与卧室产品在小户型、高租售率的公寓区（MAN, OUT, NJ-HUD）是刚需
                if metrics["apt_ratio"] > 0.50:
                    fit_score += 3.5
                else:
                    fit_score += 1.5
                # 平板轻量化在都会高层和walkup额外加分
                if self._is_single_man_friendly() and metrics["walkup_prob"] > 0.25:
                    fit_score += 1.5
            else:
                # 重型硬木家具（如大餐桌/斗柜）在大空间（长岛, 康州, 新泽西郊区）更受欢迎
                if metrics["avg_home_size"] > 2000:
                    fit_score += 4.5
                else:
                    fit_score += 1.0
                
            # 空间窒息扣分梯度算法 (Space-to-Volume Ratio Penalty):
            # 重型大体积整箱大件（>22 cft）塞入小户型大楼（<1500 sqft），空间极其压抑，契合度阶梯扣减
            if metrics["avg_home_size"] < 1500 and self.carton_volume > 22.0:
                # 面积越小，扣分越重，曼哈顿核心直接封顶扣减 3.5 分
                space_squeeze = (1500 - metrics["avg_home_size"]) / 200.0
                fit_score -= min(3.5, space_squeeze)

            # II. 计算纽约大件退货风险概率指数 (NY Return Risk Score: 1-10分)
            # 退货基本成因：末端配送物理障碍 + 过路拥堵费战损率 + 大楼COI拒收 + STURDY安全恐慌惩罚
            return_risk = 1.5  # 基础风险
            
            # 公运与窄楼道摩擦（退货第一大元凶）
            return_risk += metrics["apt_ratio"] * 3.5
            return_risk += metrics["walkup_prob"] * 4.5
            
            # 高层公寓大楼 COI (Certificate of Insurance) 拒收与约送摩擦
            return_risk += metrics["coi_required"] * 2.0
            
            # 拥堵费与过河隧道费对快递服务质量与时效的负向拉扯
            if metrics["bridge_toll_penalty"] > 0:
                return_risk += (metrics["bridge_toll_penalty"] / 10.0) * 0.5
                
            # 🛡️ 补缺红线：STURDY Act 斗柜防倾倒安全合规惩罚
            # 如果是木质斗柜类产品，且工厂没有做过防倾倒拉力合规（sturdy_compliant=False），
            # 在高年轻家庭密集的曼哈顿与哈德逊都会区，会面临极其高昂的安全隐患恐慌退货！
            if self._is_dresser() and not self.sturdy_compliant:
                # 都会公寓家庭对儿童倾倒隐患极度敏感，强行惩罚增加 2.5 风险分
                return_risk += 2.5
                
            # 物理降维补偿：如果产品整箱(Carton)实现了单人友好型平板包装（ Carton重量<70lbs 且 Carton体积<14cft），
            # 都会区末端摩擦将自动整体对折削减 40%
            if self._is_single_man_friendly():
                return_risk *= 0.60
                
            # 边界值锁定
            fit_score = min(10.0, max(1.0, fit_score))
            return_risk = min(10.0, max(1.0, return_risk))
            
            # III. 动态推演纽约大都市圈 Shopify/Meta 超级地域广告定向策略 (Ad & Logistics Route)
            if fit_score >= 8.5 and return_risk <= 4.8:
                strategy = "🔥 黄金都会特区：都会刚需，主投曼哈顿/外城/哈德逊，广告主打‘榫卯免工具/单箱轻量化’"
            elif fit_score >= 7.0 and return_risk > 4.8:
                strategy = "⚠️ 都会高摩擦区：有爆单需求但末端极度摩擦，必须强制分箱发货、大楼前置约COI并提供搬运附加费"
            elif fit_score < 6.0 and metrics["avg_home_size"] > 2000:
                strategy = "🪵 经典郊区吞吐带：适合别墅重货（大板桌/大斗柜），物流摩擦接近0，广告100%投向长岛与康州"
            else:
                strategy = "❄️ 广告避让带：户型严重过窄导致空间窒息，且末端逆向物流极贵，建议广告受众直接拉黑排除"

            heatmap_report[region_code] = {
                "region_name": metrics["name"],
                "fit": fit_score,
                "risk": return_risk,
                "strategy": strategy
            }
            
        self._print_markdown_table(heatmap_report)

    def _print_markdown_table(self, report):
        print("=" * 115)
        print(f" 🗺️  [v3.0 PROFERLO NY METRO PRECISION HEATMAP] SKU: [{self.sku_id}] ")
        print(f" 📊  CATEGORY MODEL: [{self.category.upper()}]  |  STURDY COMPLIANT: [{self.sturdy_compliant if self._is_dresser() else 'N/A'}]")
        print("=" * 115)
        print(f"[-] 单体规格: 体积 {self.unit_volume} cft, 重量 {self.unit_weight} lbs | 销售包装: 一箱装 {self.pack_qty} 只")
        print(f"[-] 发运 Carton 物理基准: 整箱体积 {self.carton_volume:.1f} cft | 整箱毛重 {self.carton_weight:.1f} lbs (单人友好: {self._is_single_man_friendly()})")
        print("-" * 115)
        print(f"| 区域代码 | 纽约周边细分市场定义 (NY Metro Sub-Region) | 市场契合度 | 退货风险分 | 核心数字营销与区域供应链对策 |")
        print(f"| :--- | :--- | :--- | :--- | :--- |")
        
        for code, res in report.items():
            print(f"| {code:<8} | {res['region_name']:<35} | {res['fit']:>8.1f}/10 | {res['risk']:>7.1f}/10 | {res['strategy']:<55} |")
            
        print("-" * 115)
        print("💡 【PROFERLO 纽约市场调研地域卡位精算洞察】:")
        print("  - 1. **成套包装转换机制**：我们不仅看单体，还以整箱运单为核算单位。单人友好型发运（整箱<70lbs）是都会大楼低风险运行的核心钥匙。")
        print("  - 2. **空间窒息算法**：体积重超规（>22 cft）的非拆装家具在曼哈顿等小户型大楼会引发惨烈退货，市场契合度呈梯度断崖式下跌。")
        print("  - 3. **STURDY Act 强制合规**：对于斗柜类，没有做防倾倒配重与五金的工厂，在年轻家庭聚集地会面临极高额的安全退货风险。")
        print("  - 4. **新泽西美仓红利**：郊区新泽西(NJ-SUB)与新泽西都会(NJ-HUD)均无跨河过江费，且为美东仓Zone 2底盘，是全品类利润的基本盘。")
        print("=" * 115)

if __name__ == "__main__":
    # 用例 1：首发 12 SKU 战队中的：模块化轻量软包双人床架 (BED-S-02) (Pack Qty=1)
    # 单箱体积 12.5 cft，重量 68 lbs（完美控制在 70 lbs 黄金线以下，符合小户型单人配送友好型）
    sku_bed = NYMetroGeoPreferenceMapperV3(
        sku_id="Proferlo-BED-S-02", 
        category_name="Modular Upholstered Bed Frame", 
        unit_volume_cft=12.5, 
        unit_weight_lbs=68,
        pack_qty=1
    )
    sku_bed.generate_ny_heatmap()
    
    print("\n" + "  " * 28 + "成套包装多量折算测试 (Set of 2)" + "  " * 28 + "\n")
    
    # 用例 2：首发 12 SKU 战队中的：中端经典 Wishbone 骨叉藤编餐椅 (DIN-C-04) (Set of 2)
    # 单把椅子：体积 6.5 cft，重量 15 lbs。但成箱销售发运（1箱2只）：整箱体积 14.3 cft，重量 30 lbs
    sku_chair = NYMetroGeoPreferenceMapperV3(
        sku_id="Proferlo-DIN-C-04-PAIR", 
        category_name="Solid Wood Wishbone Dining Chair Pair", 
        unit_volume_cft=6.5, 
        unit_weight_lbs=15,
        pack_qty=2 # 一箱装2把
    )
    sku_chair.generate_ny_heatmap()
    
    print("\n" + "  " * 25 + "STURDY Act 安全合规缺失惩罚测试 (Dresser)" + "  " * 25 + "\n")
    
    # 用例 3：首发 12 SKU 战队中的：中世纪实木六斗柜 (DRE-04) (未通过安全防倾倒测试)
    # 体积 26 cft，重量 125 lbs，sturdy_compliant = False
    sku_dresser_uncompliant = NYMetroGeoPreferenceMapperV3(
        sku_id="Proferlo-DRE-04-UNSAFE", 
        category_name="Mid-Century Modern 6-Drawer Dresser", 
        unit_volume_cft=26.0, 
        unit_weight_lbs=125,
        pack_qty=1,
        sturdy_compliant=False # 工厂没做配重和防倾倒五金
    )
    sku_dresser_uncompliant.generate_ny_heatmap()

    print("\n" + "  " * 28 + "大型重家具空间挤压惩罚测试" + "  " * 28 + "\n")

    # 用例 4：首发 12 SKU 战队中的：72英寸大型白橡木长餐桌 (DIN-T-05)
    # 体积 38.0 cft，重量 165 lbs（超重超规，体积重惩罚）
    sku_table = NYMetroGeoPreferenceMapperV3(
        sku_id="Proferlo-DIN-T-05", 
        category_name="72-inch Solid Oak Dining Table", 
        unit_volume_cft=38.0, 
        unit_weight_lbs=165,
        pack_qty=1
    )
    sku_table.generate_ny_heatmap()
