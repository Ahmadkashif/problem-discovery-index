# Robo-Advisors

## Profile
**Category:** Fintech
**Market Size:** ~$1.5T US assets under management across digital advice platforms, generating roughly $4B in fee revenue at compressed basis-point pricing
**Tech Maturity:** Excellent portfolio construction and trading automation on top of a client understanding built from a six-question form — Betterment, Wealthfront, Schwab Intelligent Portfolios, Vanguard Digital Advisor and Fidelity Go rebalance, harvest losses and allocate flawlessly, and know almost nothing about the client beyond an age, a stated goal and a risk score assigned at signup.
**Workforce:** Portfolio and quantitative staff, licensed advisors and client service associates, compliance and supervision, trading and operations, product and engineering

## Key Pain Themes
The product's value depends almost entirely on a behaviour it does not manage: whether the client stays invested when markets fall. Fee compression has made scale the only viable model, and scale means the client relationship is a mobile app. The platform observes every login, every allocation change, every panic sale and every funding pause — a continuous behavioural record of exactly the thing that determines outcomes — and it assigns risk tolerance once, from a questionnaire, at account opening, and rarely revisits it.

Around that sit the mechanics that are genuinely automated and genuinely imperfect: tax-loss harvesting whose value is asserted in marketing and rarely measured per client, wash-sale exposure across accounts the platform cannot see, held-away assets that make the advice incomplete, and a licensed service function that becomes the entire business on the worst market days of the decade.

## Current Tech Landscape
Portfolio construction runs on mean-variance or risk-parity variants over low-cost ETFs with glide paths by goal and horizon. Rebalancing and tax-loss harvesting are automated with drift bands and wash-sale rules applied within the platform's own accounts. Custody is internal or through Apex, Pershing or Schwab. Aggregation of held-away accounts uses Plaid, MX or Yodlee where the client connects them. Client communication runs through email and push, supervised under the usual marketing and communications rules. Compliance monitors communications and suitability. The fiduciary obligation applies, and what discharging it means for an algorithm that has met the client once is not fully settled.

## Problems
- [[problems/robo-advisors/high-impact|🔴 High Impact: Risk Tolerance Assessed Once and Never Validated]]
- [[problems/robo-advisors/low-impact-1|🟡 Low Impact: Tax-Loss Harvesting Value and Wash-Sale Exposure]]
- [[problems/robo-advisors/low-impact-2|🟡 Low Impact: Held-Away Account Aggregation]]
- [[problems/robo-advisors/worker-life-1|🟢 Worker Life: The Licensed Advisor on a Down Day]]
- [[problems/robo-advisors/worker-life-2|🟢 Worker Life: The Supervision Analyst Reading Everything]]
- [[problems/robo-advisors/ml-opportunity|🧠 ML Opportunities]]
- [[problems/robo-advisors/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
A digital advice platform holds the cleanest behavioural finance dataset that has ever existed: millions of investors, each with a stated risk tolerance recorded before any market event, followed by a complete record of what they actually did through every drawdown since. The questions this could settle are the discipline's central ones — whether questionnaire risk tolerance predicts behaviour at all, which interventions actually prevent a panic sale, what the realised cost of that behaviour is in basis points. The industry publishes occasional white papers from it and manages clients from the questionnaire. The gap between what these platforms could know about investor behaviour and what they act on is, in practice, the whole of their remaining alpha.
