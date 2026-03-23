# Chef Menu-Aware Produce Demand Forecasting

**Niche:** [[niches/restaurant-suppliers/produce-specialty-suppliers/profile|Produce & Specialty Suppliers]]
**Industry:** [[industries/restaurant-suppliers|Restaurant Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product forecasts restaurant produce demand at the account-item level using menu change signals — when a chef adds a burrata salad to the summer menu, the supplier should anticipate increased heirloom tomato, arugula, and burrata orders before the first order arrives.
**Tags:** #gradient-boosting #time-series-forecasting #nlp #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
An experienced produce supplier buyer knows their chef clients' menus intimately and anticipates demand shifts before they show up in orders: summer menu launch means more heirloom tomatoes and stone fruit, fall means squash and root vegetables, a new pasta dish means more fresh herbs. This anticipatory purchasing — buying 20% more microgreens this week because three accounts are launching spring menus — prevents both stockouts (which push chefs to competitors) and spoilage (which destroys margin on 3-day-shelf-life items). A new buyer without this menu intelligence either over-buys (spoilage) or under-buys (stockouts) for 12-18 months while learning each account's seasonal patterns.

## Why Nobody Has Built This
Menu-aware demand forecasting requires two data sources that do not exist in structured form: (1) chef menu information (what is on the menu, what is about to change), which is communicated informally during sales visits and is never digitized, and (2) item-to-menu-component mapping (a "burrata salad" translates to burrata + heirloom tomatoes + arugula + basil + olive oil), which the experienced buyer computes mentally. Building this model requires either extracting menu data from restaurant websites/social media or capturing it during sales rep visits, then learning the relationship between menu changes and produce order patterns.

## What to Build
A forecasting system that: (1) ingests historical order data by account and item (2-3 years from ERP), (2) captures menu signals through rep visit notes (structured input: "Tony's launching summer menu next week, adding grilled peach salad") and/or automated menu scraping from restaurant websites and social media, (3) learns the relationship between menu signals and subsequent order changes using gradient boosting on tabular features, (4) generates account-level demand forecasts 5-7 days ahead with confidence intervals, and (5) aggregates account-level forecasts into purchasing recommendations for the buyer's 4 AM market visit.

## Target Customer
Head buyers at produce and specialty suppliers serving 50+ restaurant accounts. Approximately 1,500-2,500 US produce suppliers at this scale. Price point: $500-$1,500/month.

## Impact If Built
Spoilage reduced by 25-40% through demand-aligned purchasing, saving $50K-$200K annually. Stockout frequency reduced by 30-50%, retaining $100K-$400K in revenue from accounts that would have called a competitor. New buyer effectiveness reaches 80% of an experienced buyer's performance within 3 months vs. 12-18 months without the tool.
