# DTC Competitor Monitoring Guide

## 🎯 What to Track About Competitors

### 1. **Website & Traffic Metrics**

#### Tools to Use:
- **SimilarWeb**: Overall traffic trends, traffic sources, audience demographics
- **Ahrefs**: Organic search traffic, keyword rankings, backlinks
- **SEMrush**: Paid ad spend, keyword performance, content strategy
- **Google Trends**: Search interest over time

#### Key Metrics to Monitor:
- Monthly unique visitors
- Traffic growth rate (YoY)
- Traffic source breakdown (organic, paid, direct, referral, social)
- Average session duration
- Pages per session
- Bounce rate
- Mobile vs desktop split
- Top landing pages

#### Frequency: Weekly (automated), detailed review monthly

---

### 2. **SEO & Organic Search**

#### Tools:
- **Ahrefs** (primary): Keyword rankings, search volume, difficulty
- **SEMrush**: Rank tracking, keyword gap analysis
- **Moz**: Domain authority, on-page SEO analysis
- **Google Search Console** (if access available)

#### What to Track:
- Top 100 ranking keywords
- Search volume for top keywords
- Keyword difficulty scores
- Click-through rates (CTR) from search
- Ranking positions (track changes monthly)
- Content strategy (blogs, guides, how-tos)
- Internal linking structure
- Meta descriptions and title tags

#### Action Items:
- Identify unmet keyword opportunities (gaps)
- Reverse-engineer their top-performing content
- Track keyword ranking shifts

#### Frequency: Monthly detailed audit, weekly spot checks

---

### 3. **Pricing Strategy**

#### Tools:
- **Price2Spy**: Automated price monitoring
- **Prisync**: Price intelligence platform
- **Keepa**: Amazon price tracking (if on Amazon)
- **Manual Tracking**: Spreadsheet with SKUs

#### What to Track:
- Base prices for 20-30 key SKUs
- Price changes and timing
- Promotional discounts
- Volume discounts/tiering
- Seasonal pricing patterns
- BNPL availability
- Shipping costs
- Hidden fees (assembly, installation)

#### Price Categories to Monitor:
- **Entry-Level**: $300-800 (chairs, accent pieces)
- **Mid-Range**: $800-2,500 (sofas, beds)
- **Premium**: $2,500-5,000 (high-end sofas, sectionals)
- **Luxury**: $5,000+ (custom, designer)

#### Frequency: Weekly for key SKUs, bi-weekly for full catalog

---

### 4. **Marketing & Campaigns**

#### Channels to Monitor:
1. **Email Marketing**
   - Subscribe to newsletter
   - Track email frequency
   - Note promotions, offers, messaging
   - Analyze subject lines and CTAs
   - Tools: Mailmodo, Hyperise

2. **Social Media**
   - **Instagram**: Follower count, post frequency, engagement rates, hashtags
   - **TikTok**: View counts, engagement, virality patterns
   - **Pinterest**: Pins, boards, traffic from Pinterest
   - **Facebook**: Ad spend estimation, audience targeting
   - Tools: Social Blade, Brandwatch, Hootsuite

3. **Paid Advertising**
   - **Google Ads**: Keywords, ad copy, landing pages
   - **Facebook/Instagram Ads**: Ad creative, audiences, estimated spend
   - **TikTok Ads**: Video content, engagement
   - Tools: SEMrush, Pathmatics, Ad Library (Meta, Google)

4. **Content Marketing**
   - Blog posts and guides
   - Video content (YouTube, TikTok)
   - Podcast appearances
   - Webinars and educational content
   - Tools: Buzzsumo, ContentStudio

#### Frequency: Daily social monitoring, weekly email/ad analysis, monthly content audit

---

### 5. **Product Strategy**

#### What to Track:
- **New Product Launches**: Timing, categories, price points
- **Product Discontinuations**: Which products being phased out
- **Color/Fabric Options**: Available variants
- **Customization Features**: Made-to-order options
- **Product Descriptions**: Keywords, benefits emphasized
- **Technical Specs**: Dimensions, materials, certifications

#### Frequency: Weekly product catalog checks

---

### 6. **Customer Reviews & Feedback**

#### Platforms to Monitor:
- **Trustpilot**: Aggregate ratings, review volume, recent feedback
- **Google Reviews**: Local/regional sentiment
- **Reddit**: r/furniture, r/InteriorDesign communities
- **Facebook Reviews**: Engagement, response rates
- **YouTube Comments**: On review videos
- **Sitejabber**: Alternative review platform

#### What to Analyze:
- **Average Rating**: Track changes
- **Review Volume**: How many reviews monthly
- **Sentiment**: Positive vs negative themes
- **Common Complaints**: Product quality, delivery, customer service
- **Response Rate**: How brand responds to negative reviews
- **Review Velocity**: New reviews per week

#### Key Questions:
- What are the top 3 complaints?
- What do customers praise most?
- How does brand respond to criticism?
- What's the trend (improving/declining)?

#### Frequency: Weekly review checks, monthly sentiment analysis

---

### 7. **Brand & Positioning**

#### What to Track:
- **Brand Story**: How they position themselves
- **Target Audience**: Marketing language, imagery, demographics
- **Key Messaging**: Value propositions, unique selling points
- **Tone & Voice**: How they communicate
- **Visual Identity**: Logo, colors, design language
- **Partnerships**: Influencers, brands, collaborations

#### Frequency: Quarterly brand analysis

---

### 8. **Company Information**

#### Research Sources:
- **LinkedIn**: Company size, leadership, recent hires
- **Crunchbase**: Funding, investors, company trajectory
- **Company Website**: About page, press releases, team
- **News/Press**: Growth announcements, expansions
- **SEC Filings**: If public company

#### What to Track:
- **Headcount**: Growing or shrinking
- **Funding**: Raises, valuation
- **Expansion**: New markets, categories
- **Key Hires**: Leadership changes
- **Partnerships**: Strategic alliances

#### Frequency: Monthly or as news breaks

---

## 📊 Tracking Template

Create a spreadsheet or JSON file with this structure:

```json
{
  "competitor_name": "Burrow",
  "website": "www.burrow.com",
  "date_tracked": "2026-05-28",
  "traffic": {
    "monthly_visitors": 150000,
    "trend": "stable",
    "organic_traffic_pct": 45,
    "traffic_growth_yoy": 12
  },
  "seo": {
    "top_keywords": [
      {"keyword": "modular sofa", "volume": 12100, "rank": 2},
      {"keyword": "furniture delivery", "volume": 8100, "rank": 15}
    ],
    "estimated_organic_keywords": 2450
  },
  "pricing": {
    "products_tracked": 25,
    "avg_price_change": 0,
    "promotions_active": ["Free shipping"],
    "price_range": "$599-$3999"
  },
  "social_media": {
    "instagram": {"followers": 125000, "posts_per_week": 3.5},
    "tiktok": {"followers": 45000, "avg_views": 50000},
    "facebook": {"followers": 80000}
  },
  "reviews": {
    "rating": 4.7,
    "review_count": 2340,
    "trend": "positive",
    "top_complaint": "Delivery delays"
  }
}
```

---

## 🔄 Monitoring Frequency Recommendations

| Metric | Frequency | Tool |
|--------|-----------|------|
| Website Traffic | Weekly automated, monthly review | SimilarWeb |
| SEO Rankings | Monthly detailed, weekly spot checks | Ahrefs |
| Pricing | Weekly | Price2Spy or manual |
| Social Media | Daily engagement, weekly analytics | Native platforms |
| Email Campaigns | 2-3x per week | Email capture |
| Product Changes | Weekly | Manual catalog check |
| Customer Reviews | Weekly sentiment, monthly deep dive | Trustpilot |
| Brand News | Real-time | Google Alerts |
| Competitor Financials | Quarterly | Crunchbase |

---

## 🛠️ Tools Setup Checklist

- [ ] SimilarWeb account (free tier available)
- [ ] Ahrefs subscription (if budget allows)
- [ ] SEMrush subscription
- [ ] Email subscription list (all competitors)
- [ ] Price tracking spreadsheet or tool
- [ ] Google Alerts for brand names
- [ ] Social media tracking tool
- [ ] Review aggregation platform subscription
- [ ] Browser bookmarks for competitor sites
- [ ] Shared spreadsheet/dashboard for tracking

---

## 📈 Analysis Framework

When reviewing competitor data:

1. **What Changed?** (vs. last period)
2. **Why Did It Change?** (market conditions, actions, campaigns)
3. **What's the Implication?** (threat, opportunity, insight)
4. **How Should We Respond?** (competitive action)
5. **What Are They Testing?** (new strategies to learn from)

---

## 🎯 Actionable Questions to Answer

- Which competitors are gaining/losing market share?
- What marketing channels drive the most traffic to competitors?
- What price points are most common in the market?
- Which messaging resonates best with customers?
- What product features are competitors highlighting?
- How fast are competitors launching new products?
- What customer complaints are recurring?
- Which competitors have the happiest customers?
- What's the average CAC range in the market?
- How do delivery/return policies vary?
