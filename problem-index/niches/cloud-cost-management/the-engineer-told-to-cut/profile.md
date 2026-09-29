# The Engineer Told to Cut

**Parent Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor that takes this seriously is fighting to show an engineer the cost of their own decisions at the moment they make them — and whoever does that takes the engineering organisation, because the alternative is a periodic instruction to cut something with no way to know what is safe.

## Profile
**Market Size:** ~$160M US attributable to engineer-facing cost feedback
**Share of Parent Industry:** ~5% of category revenue
**Digital Adoption:** None — cost is invisible to engineers until it is an instruction
**Target Buyer:** Platform engineering nominally; the beneficiary is every engineer
**Automation Potential:** Very High — the cost of a change is computable before it is merged

## What Makes This a Distinct Niche
An engineer's experience of cloud cost is a message twice a year saying the bill is too high and asking them to reduce it. They have no continuous view of what their services cost, no idea what a design decision will cost before they make it, no way to tell which resources are safe to remove, and no feedback when something they did increased spend. Then they are blamed for a number they had no way to see. The asymmetry is stark: engineers make every decision that determines cloud spend — instance choice, retry behaviour, data retention, query patterns, architecture — and are the only participants with no cost information at the moment of decision. This is a distinct contested surface because the remedy is about delivery and timing rather than analysis: the cost of a change is computable before it is merged, and nothing computes it.

## Current Tools & Gaps
Cost portals with team-level views, budget alerts, and occasional cost-reduction initiatives. The gaps: cost arrives as a monthly report rather than at the moment a decision is made, which is the only moment it could change anything; nothing estimates the cost of a proposed change before it ships, although the infrastructure definition is in the pull request; alerts are thresholds on totals rather than attribution of an increase to its cause; there is no indication of what is safe to remove, which is the engineer's actual question; and cost is framed as a constraint imposed rather than as a property of the system they are responsible for.

## Problems
- [[niches/cloud-cost-management/the-engineer-told-to-cut/build|🔨 Build: Cut Something, We Cannot Tell You What]]
- [[niches/cloud-cost-management/the-engineer-told-to-cut/buy|🛒 Buy: Shift-Left Patterns From Security and Testing]]
- [[niches/cloud-cost-management/the-engineer-told-to-cut/fix|🔧 Fix: The Alert That Fires on a Total]]
