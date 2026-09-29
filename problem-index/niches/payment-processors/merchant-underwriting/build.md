# The Same Registries, Rebuilt Everywhere

**Niche:** [[niches/payment-processors/merchant-underwriting/profile|Merchant Underwriting]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every acquirer independently rebuilds business verification and risk underwriting against the same public registries, and grades it against fraud losses it never attributes back to the decision.
**Tags:** #data-integration #gradient-boosting #compliance #evaluation-metrics #confidence-intervals #graph-theory #revenue-impact #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to decide whether a business is safe to process for, against the same registries everyone else uses, and to learn from the outcome — and whoever closes that loop stops grading a decision against losses it never attributes back.

## The Problem
A business applies to a processor. The processor checks company registries, sanctions lists, beneficial ownership, the website, the business model and any processing history, and decides whether to approve and on what terms. The same business applies to another processor next month and the entire exercise is repeated, against the same sources, by a different team, reaching a possibly different conclusion. Meanwhile the losses that eventually arrive — fraud, excessive chargebacks, a business that turns out to be selling something it did not declare — are recorded against the merchant and never joined back to the underwriting decision that admitted them.

## Why Nobody Has Built This
Underwriting is treated as a competitive function and its inputs as proprietary, when the inputs are public registries everyone queries identically — the confusion between the judgement and the evidence is why the evidence is rebuilt rather than shared. Losses arrive months later and are owned by a different team than the one that approved. Onboarding speed is the measured metric because it is immediate and competitive. And a declined merchant who would have been fine is invisible forever.

## What to Build
Share the evidence and close the loop on the judgement. Build the verification layer once — registry data, ownership, sanctions, website classification, business model assessment — as shared infrastructure rather than as each acquirer's private build, which is the fix for the wasteful half and is the piece that is genuinely common. Keep the risk judgement proprietary, since that is where the competition legitimately is and conflating it with the evidence is what has prevented the sharing. Join underwriting decisions to subsequent outcomes, which is the fix note's subject and is the only route to knowing whether the judgement is any good. Model loss probability from the application rather than scoring by category convention, since merchant category is a crude proxy that penalises legitimate businesses in risky-looking sectors. Set reserves and limits from predicted exposure rather than from a table, which is where the merchant experience and the acquirer's capital efficiency both improve. Measure the declined-but-safe population deliberately, by approving a sample near the threshold, since that error is invisible and is where growth is lost. Use the network view of the business across acquirers where permitted, which is the processor's structural advantage over any single underwriter. Classify the website and the business model automatically, which is now reliable and is most of the manual review. Handle the changing merchant, since a business that changes what it sells after approval is a common and undetected exposure. And report underwriting accuracy in both directions, because an acquirer that only counts losses will keep tightening.

## Target Customer
Acquirer risk and onboarding leadership, the verification vendors who could supply the shared layer, and the merchants verified from scratch by every processor they approach.

## Impact If Built
The judgement is competitive and the evidence is a public registry, and conflating the two is why every acquirer rebuilds the same lookups. Joining decisions to subsequent losses is the only route to knowing whether the judgement works, and it has never been done because the two live in different teams.
