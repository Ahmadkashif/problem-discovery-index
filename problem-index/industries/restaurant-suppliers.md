# Restaurant Suppliers

## Profile
**Category:** Agriculture & Food
**Market Size:** ~$60B in independent/specialty restaurant supply distribution (excluding Sysco/US Foods direct)
**Tech Maturity:** Low — most independent distributors run basic ERP (often NetSuite, SAP B1, or legacy AS/400 systems) with minimal analytics layered on top; sales still runs on spreadsheets and personal notebooks
**Workforce:** Sales reps (80-150 accounts each), delivery drivers, warehouse workers, buyers/merchandisers, meat cutters, produce handlers

## Key Pain Themes
Independent restaurant suppliers compete against Sysco, US Foods, and Performance Food Group on relationship depth rather than price. Sales reps manage 80-150 restaurant accounts each, placing orders via phone, text, and in-person visits — with no systematic way to detect which accounts are drifting toward a competitor. Warehouse operations handle perishable, custom-cut, and portioned products where a single mis-pick on a $400 seafood order destroys margin. Procurement buyers must commit to perishable inventory 3-7 days ahead of demand without reliable forecasting, leading to either costly spoilage (2-5% of perishable revenue) or stockouts that push chefs to call a competitor.

## Current Tech Landscape
Most independent distributors use a combination of legacy ERP (SAP Business One, Sage 100, Aptean) and bolt-on route accounting systems like Rutherford & Associates or Encompass. CRM adoption is low — reps track accounts in personal notebooks or basic spreadsheets. E-commerce ordering portals exist (BlueCart, Cut+Dry, Pepper) but penetration among independents is under 30%, and most orders still come in via phone or text message.

## Problems
- [[problems/restaurant-suppliers/high-impact|🔴 High Impact: Sales Rep Account Churn Prevention]]
- [[problems/restaurant-suppliers/low-impact-1|🟡 Low Impact: Menu-Driven Demand Forecasting]]
- [[problems/restaurant-suppliers/low-impact-2|🟡 Low Impact: Restaurant-Specific Catalog Search]]
- [[problems/restaurant-suppliers/worker-life-1|🟢 Worker Life: Sales Rep Route and Visit Prioritization]]
- [[problems/restaurant-suppliers/worker-life-2|🟢 Worker Life: Custom-Cut Order Accuracy]]
- [[problems/restaurant-suppliers/ml-opportunity|🔵 ML Opportunities]]
- [[problems/restaurant-suppliers/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Restaurant supply distribution is a relationship business where technology adoption lags because incumbents built their edge on personal trust, not software. The highest-leverage interventions target the sales rep's decision-making (who to visit, what to pitch, which account is at risk) and the procurement buyer's forecasting (what to order from producers 5 days out). ML opportunities cluster around tabular customer behavior data that already exists in ERP order history but is never analyzed systematically.
