# Subscription Commerce

## Profile
**Category:** Digital Commerce
**Market Size:** ~$45B US subscription box, replenishment and curated commerce
**Tech Maturity:** Well-tooled billing, unexamined churn — Recharge, Ordergroove, Chargebee and the Shopify subscription ecosystem handle recurring billing, plan management and dunning capably. The reason customers leave in the first three cycles, which is where nearly all the churn happens, is diagnosed at almost no company in the category.
**Workforce:** Retention and lifecycle marketers, merchandising and curation staff, fulfilment planners, customer experience agents, supply chain and procurement staff, subscription operations analysts

## Key Pain Themes
Churn in subscription commerce is front-loaded to a degree that surprises people outside it: a large share of cancellations occur within the first three deliveries, and the reasons are specific and fixable — the first box did not match what the sign-up implied, the cadence is wrong for actual consumption, an item arrived damaged, the value was not obvious. Companies measure churn as a monthly rate and treat it as a marketing problem, which is why acquisition spend keeps rising against a leaky retention base. Around it sit two operational challenges: curation and personalisation, where matching contents to a customer determines satisfaction and is done by rules; and flexibility management, where skip, pause and swap are the tools that prevent cancellation and are usually buried because product teams fear they reduce revenue. Fulfilment planners absorb the consequences of demand that arrives in a monthly wave, and retention agents work a cancel flow where the customer has already decided.

## Current Tech Landscape
Recharge dominates Shopify-based subscriptions with Ordergroove and Skio competing; Chargebee and Recurly serve broader recurring billing. Dunning and card updater services are standard. Personalisation ranges from quiz-based rules to genuine recommendation systems at the larger players. Fulfilment is either in-house or through third-party logistics providers who charge for the peak the subscription cycle creates. Retention tooling focuses on the cancel flow — offers, pauses, surveys — which is late in the decision. Cohort analytics are available in every platform and are reported rather than acted on.

## Problems
- [[problems/subscription-commerce/high-impact|🔴 High Impact: Diagnosing Early-Cycle Churn]]
- [[problems/subscription-commerce/low-impact-1|🟡 Low Impact: Curation and Personalisation]]
- [[problems/subscription-commerce/low-impact-2|🟡 Low Impact: Skip, Pause and Swap Flexibility]]
- [[problems/subscription-commerce/worker-life-1|🟢 Worker Life: Fulfilment Planner on the Monthly Wave]]
- [[problems/subscription-commerce/worker-life-2|🟢 Worker Life: Retention Agent in the Cancel Flow]]
- [[problems/subscription-commerce/ml-opportunity|🧠 ML Opportunities]]
- [[problems/subscription-commerce/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
A subscription business has an unusually complete view of its customers: what they signed up for, what they received, what they skipped, what they swapped, what they returned, what they said and exactly when they left. Almost no other commerce model observes the same customer repeatedly against a known expectation. That makes churn diagnosis genuinely tractable here in a way it is not elsewhere, and the category persistently treats retention as a marketing discipline rather than a product one.
