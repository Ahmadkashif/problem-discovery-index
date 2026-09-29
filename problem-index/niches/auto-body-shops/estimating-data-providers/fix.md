# The Database Never Learns From the Repairs It Priced

**Niche:** [[niches/auto-body-shops/estimating-data-providers/profile|Collision Estimating Data Providers]]
**Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Type:** Fix (Pain Point)
**One-liner:** The platform sees the estimate, the supplements, the parts actually ordered, the cycle time, and the final invoice — and the research organization that set the numbers sees none of it, because production data and research data have never been joined.
**Tags:** #data-integration #feature-engineering #gradient-boosting #evaluation-metrics #descriptive-statistics #change-point-detection #causal-inference #workflow-orchestration #worker-facing

## The Problem
Two halves of the same company face each other across a gap nobody owns. On one side, a research organization of several hundred people maintaining millions of database entries, working from OEM documentation and time studies. On the other, a transaction platform carrying a large share of US collision claims end to end — initial estimate, supplements, parts orders, cycle time, final settlement. The research side is the reason the platform has customers; the platform is the reason the research side could be right. They are not connected. Researchers cannot ask which of their entries are most often overridden, which vehicles generate the most disputed lines, or whether a revision they published last quarter changed anything downstream. They find out their entries are wrong the way anyone else would: through complaints.

## Why It's Still Broken
The two sides were built separately and are governed separately. Research data is a published product with editorial controls, release cycles, and a versioning discipline; transaction data is operational, high-volume, and governed by customer contracts that restrict how it may be used. The contractual boundary is the real obstacle — the permission to use claim data for internal product improvement is often present in principle and unmapped in practice, so nobody can say with confidence which analyses are allowed and the safe answer is none. Organizationally, no role sits across the two, so the join has no owner, and the effort required is large enough that it needs one.

## What a Fix Looks Like
A governed analytical layer between the two halves. Every database entry carries a stable identifier that appears on the estimate lines derived from it, which is the join key that does not currently exist; without it, no downstream analysis is possible at all. Above that, a permissions model that resolves each customer's contract terms into machine-checkable rules about what the data may be used for, so analyses are approved by construction rather than by legal review each time. On that foundation the research organization gets a standing view of its own product in the field: override and dispute rates by entry, revision effect measured before and after publication, coverage gaps ranked by claim volume rather than by vehicle popularity. All of it aggregate, none of it customer-identifying, which is both the contractual requirement and the analytically correct level.

## Who Feels the Pain
Researchers maintaining entries with no feedback on accuracy; the product organization unable to prioritize research investment by where the industry actually disagrees; insurers and shops arguing over numbers that could be empirically supported and are not; and the company's competitive position, since the transaction platform is its unique asset and the research product does not benefit from it.

## Impact If Fixed
Closes the loop that makes the whole business defensible. Any competitor can hire researchers and read OEM documentation; none can observe what happened on millions of repairs written against their own numbers. Joining the two converts a scale advantage in transactions into a quality advantage in content, which is the only durable form of the moat. It also settles the industry's most persistent argument — whether published labor times reflect real work — with evidence rather than assertion.
