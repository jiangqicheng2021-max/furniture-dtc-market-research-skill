# 🔍 美区 DTC 家具出海失败案例实时联网审计与诊断协议 (Dynamic Failure Case Auditor)

本文件非静态案例库，而是一套强制 AI Agent（Antigravity）执行的**实时联网搜索、数据清洗与失败闭环审计协议**。每当启动新类目或新 SKU 的调研时，AI 必须调用此协议进行全网动态检索与诊断，严禁使用历史离线记忆主观臆断。

---

## 🛰️ 1. 实时联网检索矩阵 (Live Search & Scraping Matrix)

当用户输入目标品类（如 `${CATEGORY}` = `6 Drawer Dresser` 或 `Modular Sofa`）时，AI 必须立刻启用实时联网工具，执行以下组合交叉搜索，抓取过去 3 年内（含 2025-2026 年最新动态）北美市场的闭店、破产、重组或面临严重财务危机的家具品牌：

### 🔍 核心检索词库（组合运行）：
- `"${CATEGORY}" + "DTC brand" + ("bankrupt" OR "liquidated" OR "shut down" OR "out of business")`
- `"${CATEGORY}" + "furniture e-commerce" + ("chapter 11" OR "asset sale" OR "distressed") + "US market"`
- `"DTC furniture" + "layoffs" OR "supply chain crisis" + "2025" OR "2026"`

---

## 🧮 2. 失败模式动态诊断框架 (5-Step Post-Mortem Framework)

对于联网抓取到的每一个匹配失败案例，AI 必须严格按照以下五个结构化维度进行深度解构，提炼量化风控指标：

### 🛑 维度 A：流量与 CAC 击穿审计 (Traffic & Customer Acquisition Burn Rate)
- **诊断指标**：该品牌在倒闭前是否过度依赖 Meta/Google 的付费流量广告？
- **量化清洗**：检索或推算其综合获客成本（CAC）与客单价（AOV）的比例是否失调（以 `CAC > 30% of AOV` 为亏损预警线）。

### 💵 维度 B：中端价格带卡位与生态位塌陷 (Price Tier & Value Prop Collapse)
- **诊断指标**：该品牌是否落入 \$400 - \$1,000 的中端价格红海，且未能建立核心壁垒？
- **量化清洗**：分析其对比 Amazon 白牌（低价红海）是否具备物理改良优势，对比 Burrow/Article（高端大牌）是否具备极致性价比，诊断其是否因“两头不讨好”导致转化率（CVR）跌破 1.1% 安全线。

### 🚢 维度 C：体积超规与海外仓流血速率 (Cube & Carrying Cost Haemorrhage)
- **诊断指标**：分析其产品的物理包装结构。是传统的不可拆卸整体大件，还是模块化平板包装？
- **量化清洗**：审计由于动销停滞导致的海外仓惩罚性长库费（Storage Carried Cost）及资金占用成本（WACC）占其总运营成本的比重趋势。

### 🚨 维度 D：逆向物流与退货清算盲区 (Reverse Logistics Inefficiency)
- **诊断指标**：该品牌在面对美东/美西本土退货时，采取了何种处置手段？
- **量化清洗**：审计其是否由于缺乏本地清仓流转商（如 FloorFound/ShareTown），导致退货直接转为固定资产坏账和仓储二次负荷。

### ⚖️ 维度 E：合规、原产地与反倾销税清算 (AD/CVD Regulatory Violation)
- **诊断指标**：追踪该品牌的工厂供应链源头。
- **量化清洗**：是否因为落入美国商务部（DOC）对特定地区木制或软体家具的反倾销/反补贴（AD/CVD）Scope 范围而被顶格追缴惩罚性税款。

---

## 📊 3. 动态输出格式规范 (Output Schema for Leadership)

AI 运行完实时联网审计后，在向用户输出“避坑防线报告”时，必须自动渲染为以下结构化格式：

### [实时联网诊断报告：${CATEGORY} 品类前车之鉴]

| 被审计失败品牌 | 核心失败诱因 (Primary Catalyst) | 核心量化受损指标 (Data Point) | 对应 Proferlo 的防守红线 (Our Defense Line) |
| :--- | :--- | :--- | :--- |
| *[实时抓取的品牌A]* | *[如：非模块化导致长库费爆发]* | *[如：月均持仓费暴涨 400%]* | *[调用库内 simulator.py 进行前置拦截]* |
| *[实时抓取的品牌B]* | *[如：中端卡位被Amazon白牌低价绞杀]* | *[如：独立站 CVR 长期低至 0.6%]* | *[强化快装/静音等功能差异化和GEO代码注入]* |
| *[实时抓取的品牌C]* | *[如：触碰反倾销税清算 Scope]* | *[如：被 CBP 追缴 120% 惩罚税]* | *[执行清关行 HS Code 预审与产地多元化对冲]* |

> **⚠️ 战略总结：** AI 必须基于本次实时检索到的失败案例公约数，为 Proferlo 动态推演出一条**“出厂 FOB 价格死线”**和**“月度最低动销流速警告线”**，作为向管理层汇报时的核心风控抗辩依据。
