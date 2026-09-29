# Programme Effectiveness Measurement

**Parent Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Category:** High Market Share
**Contested on:** Whether a programme can show that its spend bought security, or only that it bought submissions.

## Profile

**Market Size:** ~$330M
**Share of Parent Industry:** ~22%
**Digital Adoption:** Very low — activity reported as outcome
**Target Buyer:** Programme owners, security leadership, budget holders
**Automation Potential:** High — the counterfactual data mostly exists

## What Makes This a Distinct Niche

A programme reports spend, submission volume, valid findings, severity mix and time to triage. None of those is an outcome. They are measures of activity, and a programme could improve every one of them while buying nothing that made the organisation safer.

The questions a budget holder actually has are different. Would this vulnerability have been found by our own scanning, our own testing, or the next release? What does the marginal bounty dollar buy — is the tenth thousand as productive as the first? Has the programme reduced incidents, or reduced the severity of what reaches production? Should we spend the next hundred thousand on bounties, on internal application security engineers, or on a contracted assessment?

None of these is answerable with what the category reports, and the reason is that nobody constructed the counterfactual. This is the same gap that runs through every assurance business in this cluster: an industry selling confidence and reporting activity, because the outcome data was never assembled.

## Current Tools & Gaps

Platform dashboards reporting submissions, validity rate, severity distribution, payout totals, time to triage and time to resolution. Benchmarking against anonymised peer programmes at some platforms. Programme maturity models offered as consulting. Internal vulnerability management tracks remediation of bounty findings alongside everything else.

The gaps are the whole niche. Nothing compares a bounty finding against what the organisation's own tooling had already reported, despite that being a straightforward join. Nothing models the marginal return of additional spend, so budgets are set by last year's number. Nothing compares bounty findings to contracted testing findings on the same estate, so the two channels are never evaluated against each other. Duplicate rate against internal findings is never computed, which is the single clearest signal of whether a programme is buying anything new. And no programme can say whether its existence changed what reached production, which is the claim the category is ultimately making.

## Problems

- [[niches/bug-bounty-platforms/programme-effectiveness/build|🔨 Build: What the Marginal Dollar Buys]]
- [[niches/bug-bounty-platforms/programme-effectiveness/buy|🛒 Buy: Marketing Measurement Applied to Security Spend]]
- [[niches/bug-bounty-platforms/programme-effectiveness/fix|🔧 Fix: Activity Reported as Assurance]]
