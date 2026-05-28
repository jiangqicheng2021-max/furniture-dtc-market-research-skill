# Furniture DTC Market Research Skill

**A comprehensive knowledge base and AI agent skill for New York furniture e-commerce market research**

## 📌 Project Overview

This repository serves as a specialized knowledge base and prompt framework for AI agents to conduct professional-grade market research on the Direct-to-Consumer (DTC) furniture e-commerce landscape, with a focus on the New York market.

### Purpose
- **Market Intelligence**: Deep understanding of DTC furniture brands and competitive landscape
- **Competitor Monitoring**: Track pricing, SEO, marketing strategies, and product development
- **Strategic Analysis**: Cost structures, supply chains, and profitability insights
- **Market Insights**: Consumer trends, purchasing behaviors, and market opportunities

### Target User
Furniture entrepreneurs planning to launch a pure online, DTC independent store model in the New York market (no physical retail).

---

## 📂 Repository Structure

```
furniture-dtc-market-research-skill/
├── README.md                                    # This file
├── .gitignore
│
├── 01-industry-knowledge/                       # Part 1: Industry Fundamentals
│   ├── market-overview.md                       # Market size, growth, segments
│   ├── consumer-insights.md                     # Demographics, preferences, behaviors
│   ├── product-categories.md                    # Product analysis and trends
│   └── market-data.json                         # Structured market data
│
├── 02-dtc-competitors/                          # Part 2: DTC Competitor Analysis
│   ├── competitor-profiles/                     # Individual brand profiles
│   │   ├── burrow.md
│   │   ├── albany-park.md
│   │   ├── article.md
│   │   ├── zinus.md
│   │   ├── interior-define.md
│   │   ├── joybird.md
│   │   ├── floyd.md
│   │   └── castlery.md
│   ├── competitor-tracker.json                  # Dynamic tracking template
│   └── monitoring-guide.md                      # How to track competitors
│
├── 03-marketing-strategy/                       # Part 3: Marketing & Operations
│   ├── social-media-strategy.md                 # TikTok, Instagram, Pinterest, YouTube
│   ├── customer-acquisition.md                  # CAC, SEO, SEM, content marketing
│   ├── conversion-optimization.md               # Pricing, UX, retention
│   └── content-ideas.md                         # Content themes and ideas
│
├── 04-operations/                               # Part 4: Operations Management
│   ├── supply-chain.md                          # Manufacturing, sourcing, partnerships
│   ├── cost-structure.md                        # Cost breakdown and margins
│   ├── logistics-analysis.md                    # Shipping, fulfillment, returns
│   ├── sku-management.md                        # Inventory, product line strategy
│   └── financial-metrics.md                     # KPIs and financial analysis
│
├── 05-research-tools/                           # Part 5: Research Tools & Methods
│   ├── competitor-monitoring-tools.md           # SimilarWeb, SEMrush, etc.
│   ├── data-sources.md                          # Public data sources
│   ├── analysis-templates.md                    # Excel/JSON templates
│   └── scripts/
│       ├── price-tracker.py
│       ├── seo-monitor.py
│       └── data-aggregator.py
│
└── 06-ai-prompts/                               # Part 6: AI Agent Prompts
    ├── competitor-analysis-prompt.md            # For analyzing competitors
    ├── market-research-prompt.md                # For market research
    ├── pricing-strategy-prompt.md               # For pricing analysis
    ├── content-ideation-prompt.md               # For content ideas
    └── system-prompt.md                         # Core system prompt
```

---

## 🎯 Quick Start for AI Agent

### 1. Load Industry Knowledge
Start by reviewing `/01-industry-knowledge/` to understand:
- Current US furniture e-commerce market (2024-2025)
- Consumer demographics and purchasing habits
- Product category trends
- New York market specifics

### 2. Study Competitor Landscape
Review `/02-dtc-competitors/` to learn:
- 8+ major DTC furniture brands and their strategies
- How to monitor competitor websites, pricing, and marketing
- Key metrics and tracking methodologies

### 3. Understand Marketing & Operations
Review `/03-marketing-strategy/` and `/04-operations/` for:
- Social media strategy differences (TikTok vs Instagram vs Pinterest)
- Customer acquisition costs and channels
- Supply chain and cost structure
- Inventory and SKU management

### 4. Use Research Tools
Reference `/05-research-tools/` for:
- Tools to monitor competitors (SimilarWeb, SEMrush, Ahrefs)
- Data sources for market research
- Templates for analysis

### 5. Activate AI Prompts
Use `/06-ai-prompts/` to generate insights:
- Analyze specific competitors
- Research market opportunities
- Develop pricing strategies
- Create content ideas

---

## 🔄 How to Use This as an AI Agent Skill

### For Prompt-Based Systems (LangChain, Semantic Kernel, etc.):
```
Use the system prompt from /06-ai-prompts/system-prompt.md
Provide context from relevant sections before asking queries
Example: "Based on the DTC competitor profiles in /02-dtc-competitors/, analyze Burrow's market position..."
```

### For API Integration:
- Structure queries with section references
- Include JSON data from `/market-data.json` and `/competitor-tracker.json`
- Chain multiple prompts for deeper analysis

---

## 📊 Key Metrics & KPIs Tracked

- **Market Metrics**: Market size, growth rate, e-commerce penetration, regional data
- **Competitor Metrics**: Website traffic, SEO rankings, social media followers, price tracking
- **Consumer Metrics**: Demographics, purchase frequency, average order value, return rates
- **Operational Metrics**: CAC, LTV, conversion rate, inventory turnover, gross margin

---

## 🛠️ Tools Included

- **Competitor Monitoring**: SimilarWeb, SEMrush, Ahrefs data integration
- **Price Tracking**: Templates for tracking competitor SKU pricing
- **Content Analysis**: Templates for evaluating competitor marketing content
- **Financial Models**: Cost structure and profitability templates

---

## 📝 Contributing Guidelines

To keep this knowledge base accurate and up-to-date:
1. Update competitor data monthly
2. Track market data quarterly
3. Review and refresh AI prompts based on performance
4. Add new competitors as they emerge

---

## 📅 Last Updated
- Initial creation: May 28, 2026
- Next major update: June 28, 2026

---

**This is a living knowledge base designed to evolve with the furniture DTC market. Regular updates ensure AI agents have the most current insights for market research and competitive analysis.**