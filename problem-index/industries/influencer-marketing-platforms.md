# Influencer Marketing Platforms

## Profile
**Category:** Adtech & Martech
**Market Size:** ~$10B US brand spend on creator partnerships; the platform and agency layer takes roughly $1.5-2B of it in software and service fees
**Tech Maturity:** Moderate and mostly clerical. CreatorIQ, Aspire, Grin, Traackr, Captiv8, Mavrck and Upfluence have built solid workflow systems — discovery, contracting, briefing, approvals, payments — on top of a measurement model that is still follower count and engagement rate. The hard question, which creator will produce sales for this brand, is answered by proxies everyone knows are gameable.
**Workforce:** Influencer and partnership managers, creator recruitment specialists, campaign coordinators, content review and rights administrators, measurement analysts, platform solutions teams

## Key Pain Themes
Creator selection is the decision that determines whether a campaign works, and it is made on metrics that describe the creator rather than the match. Follower count is purchasable. Engagement rate is inflated by pods and bots and is anti-correlated with account size in ways that make cross-tier comparison meaningless. Neither says anything about whether this creator's audience contains people who would buy this product and are not already the brand's customers, which is the only question that matters.

The outcome, as everywhere in this cluster, is held by someone else. Sales land in the brand's commerce system; the platform sees a discount code redemption, a link click, or an aggregate lift figure weeks later, and rarely at a granularity that could improve the next selection. So the category has built excellent tooling for executing campaigns and almost none for learning from them.

The third theme is administrative load, which is unusually heavy here because every partnership is bespoke. Contracts, briefs, content review rounds, usage rights with expiry dates, whitelisting permissions, FTC disclosure compliance, and payment — per creator, per campaign, at volumes of hundreds. On the creator side the same process looks like unpriced negotiation and ninety-day invoice chasing.

## Current Tech Landscape
CreatorIQ and Aspire lead the enterprise tier; Grin is strong in direct-to-consumer; Traackr focuses on measurement and Captiv8 on scale discovery. Meta, TikTok and YouTube all run their own creator marketplaces, which have the identity data nobody else does and use it narrowly. LTK and ShopMy sit between influencer marketing and affiliate and have better outcome data than the platforms do. Audience authenticity vendors like HypeAuditor and Modash address the fraud problem with their own opaque scores. Social listening tools — Brandwatch, Sprout — overlap at the edges. Nothing in the stack routinely connects a creator partnership to an incremental sale.

## Problems
- [[problems/influencer-marketing-platforms/high-impact|🔴 High Impact: Selecting Creators on Follower Count Because Outcomes Never Come Back]]
- [[problems/influencer-marketing-platforms/low-impact-1|🟡 Low Impact: Creator Discovery and Brand Safety Vetting]]
- [[problems/influencer-marketing-platforms/low-impact-2|🟡 Low Impact: Campaign Workflow, Rights and Payments]]
- [[problems/influencer-marketing-platforms/worker-life-1|🟢 Worker Life: The Manager Chasing Approvals and Usage Rights]]
- [[problems/influencer-marketing-platforms/worker-life-2|🟢 Worker Life: The Creator Pricing Blind and Waiting Ninety Days]]
- [[problems/influencer-marketing-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/influencer-marketing-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These platforms hold the largest record of creator partnerships ever assembled — which creators worked with which brands, with what content, at what price, against what response — across thousands of campaigns. That corpus contains the answer to the only question the category is asked, and the platforms use it to power a search filter. The obstacle is the same one that runs through every business in this cluster: the outcome is observed by the brand and never returned in a form that can improve the next decision. The difference here is that the unit of decision is a person rather than an impression, the number of decisions is small enough to reason about individually, and a modest amount of returned outcome data would go a very long way.
