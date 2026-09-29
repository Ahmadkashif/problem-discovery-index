# Affiliate Networks

## Profile
**Category:** Adtech & Martech
**Market Size:** ~$12B US affiliate marketing spend, driving well over $100B in tracked retail sales; network and platform take rates of 10-30% of commission
**Tech Maturity:** Old plumbing, new surface. Impact, Partnerize and Awin have modernised the platform layer; CJ, Rakuten Advertising and ShareASale run on infrastructure whose attribution logic predates the smartphone. The tracking model — a click, a cookie, a last-touch commission — is essentially unchanged since the early 2000s and is the source of most of the category's problems.
**Workforce:** Affiliate and partnership managers, publisher recruitment teams, compliance and fraud analysts, integration and tracking engineers, network account managers

## Key Pain Themes
The category pays on last click, which means it systematically pays the party closest to the checkout button. That is usually a coupon or cashback browser extension activating on a payment page the shopper had already reached, or a loyalty toolbar, or a search partner bidding on the merchant's own trademark. The content publisher who introduced the product three weeks earlier gets nothing. Everyone in the industry knows this; the 2024 examination of browser extension attribution made it public in a way the trade press had been describing for a decade.

The second theme is that affiliate is a performance channel whose performance is unverified. Merchants pay commission on sales the network attributes, almost never with a holdout, so the channel reports a ROAS that is definitionally close to infinite and is close to unfalsifiable. Fraud sits alongside — cookie stuffing, trademark bidding, incentivised traffic, coupon code leakage — policed by rules and manual review.

The third is administrative weight. Affiliate managers validate transactions by hand, negotiate commission rates in email, recruit partners from marketplace listings and spreadsheets, and reconcile returns that claw back commissions months after payout. On the publisher side, a creator earning across five networks has five dashboards, five payment terms and no way to know which of their content actually earns.

## Current Tech Landscape
Impact and Partnerize represent the modern platform tier with real API depth and flexible commissioning; Awin, CJ, Rakuten Advertising and ShareASale hold the long tail of merchant relationships. Amazon Associates remains the single largest programme and sets creator expectations. The creator-commerce layer — LTK, ShopMy, Howl — has grown around the networks rather than through them. Compliance tooling from BrandVerity and TrafficGuard addresses trademark bidding and click fraud. Multi-touch attribution vendors exist and are rarely wired into commissioning, which is precisely where they would matter.

## Problems
- [[problems/affiliate-networks/high-impact|🔴 High Impact: Paying the Last Click, Which Is Usually the Party That Did the Least]]
- [[problems/affiliate-networks/low-impact-1|🟡 Low Impact: Partner Discovery and Recruitment]]
- [[problems/affiliate-networks/low-impact-2|🟡 Low Impact: Fraud and Compliance Monitoring]]
- [[problems/affiliate-networks/worker-life-1|🟢 Worker Life: The Affiliate Manager Validating Transactions]]
- [[problems/affiliate-networks/worker-life-2|🟢 Worker Life: The Publisher Who Cannot Tell What Earns]]
- [[problems/affiliate-networks/ml-opportunity|🧠 ML Opportunities]]
- [[problems/affiliate-networks/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
An affiliate network sees the entire click path across thousands of merchants and hundreds of thousands of publishers, and joins it to confirmed transactions — a rare dataset in which both the touch sequence and the outcome are held by the same party. It uses that dataset to execute a rule: whoever was last gets paid. The entire apparatus of the industry exists to enforce, dispute and defraud that rule. The network is the only party positioned to measure what each partner type actually contributes, and doing so would move a substantial share of $12B in commission from extensions and trademark bidders to content and creators — which is both the correct outcome and the reason the incumbent networks, whose largest publishers are often the extensions, have not done it.
