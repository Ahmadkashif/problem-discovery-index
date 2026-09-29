# Online Marketplaces

## Profile
**Category:** Digital Commerce
**Market Size:** ~$180B US third-party marketplace gross merchandise value outside Amazon's first-party business
**Tech Maturity:** Mature transactional layer, primitive matching — Etsy, eBay, Poshmark, Faire, Reverb, StockX and the vertical marketplaces have solved listings, payments, messaging and dispute handling. What they have not solved is the thing that determines whether a marketplace works, which is putting the right buyer in front of the right seller at the moment both are ready.
**Workforce:** Trust and safety reviewers, seller support and appeals staff, search relevance engineers, category and taxonomy managers, marketplace operations analysts, payments and fraud staff

## Key Pain Themes
A marketplace is a matching problem wearing a commerce interface. Liquidity — the probability that a listing finds a buyer and a buyer finds what they want — determines whether both sides stay, and it is hardest exactly where marketplaces are most valuable: unique, one-of-a-kind or long-tail inventory where no two listings are the same and there is no reference price. Around it sit two persistent burdens: category taxonomy and search relevance, where generic e-commerce search works badly on inventory described by amateurs; and seller onboarding, where listing quality determines discoverability and new sellers produce the worst listings at exactly the moment they are deciding whether to stay. The people absorbing the consequences are trust and safety reviewers making judgement calls at volume on policy edges, and seller support staff handling suspension appeals where the seller's livelihood is at stake and the reviewer cannot explain the decision.

## Current Tech Landscape
Search and recommendation are the core technical investment at every serious marketplace, with learned ranking now standard and multimodal understanding of listing images increasingly deployed. Payments, escrow and dispute resolution are mature and largely commoditised. Trust and safety combines automated detection with human review, with the automation catching volume and the humans catching nuance. Shipping integration is standard. Authentication services have emerged in categories where counterfeits are endemic. Seller tools for pricing and listing optimisation are offered inconsistently and are frequently better outside the platform than inside it.

## Problems
- [[problems/online-marketplaces/high-impact|🔴 High Impact: Liquidity for Unique Inventory]]
- [[problems/online-marketplaces/low-impact-1|🟡 Low Impact: Category Taxonomy and Search Relevance]]
- [[problems/online-marketplaces/low-impact-2|🟡 Low Impact: Seller Onboarding and Listing Quality]]
- [[problems/online-marketplaces/worker-life-1|🟢 Worker Life: Trust and Safety Reviewer]]
- [[problems/online-marketplaces/worker-life-2|🟢 Worker Life: Seller Support on a Suspension Appeal]]
- [[problems/online-marketplaces/ml-opportunity|🧠 ML Opportunities]]
- [[problems/online-marketplaces/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Marketplaces hold the complete record of demand that went unmet: every search that returned nothing anyone wanted, every listing that expired unsold, every buyer who browsed and left. That is a direct measurement of where supply and demand fail to meet, and it is the single most actionable dataset for a business whose entire job is matching. Most marketplaces analyse conversion on the transactions that happened and treat the failures as absence rather than as signal.
