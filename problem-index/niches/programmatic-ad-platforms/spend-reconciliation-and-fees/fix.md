# The Log Files You Are Not Allowed to Have

**Niche:** [[niches/programmatic-ad-platforms/spend-reconciliation-and-fees/profile|Spend Reconciliation & Fees]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The advertiser's contract grants audit rights, the platform supplies a summary, and the analysis that would answer the question requires the rows nobody will hand over.
**Tags:** #compliance #data-integration #evaluation-metrics #workflow-orchestration #quick-win #descriptive-statistics #automation #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to account for the gap between what the buyer paid and what the publisher received, impression by impression — and whoever can enumerate it recovers a quarter of the money for whoever hired them.

## The Problem
The advertiser's agreement says they may audit. In practice the platform supplies aggregated reports, the exchange supplies a different aggregation on a different key, one intermediary supplies nothing citing confidentiality, and the fields needed to join any of them to each other are withheld as commercially sensitive. The audit therefore reconciles summaries against summaries and concludes that the numbers are broadly consistent, which was never in doubt. Audit rights are exercised annually, cost a great deal, and are structurally incapable of answering the question they were negotiated to answer.

## Why It's Still Broken
Contracts specify a right to audit without specifying the data, the format, the fields or the timeliness, which makes the right unenforceable in practice — this drafting gap is the actual defect and it is repeated across the industry. Confidentiality is a legitimate-sounding refusal that is difficult to test. Each platform's log schema differs, so even granted data does not join. And advertisers negotiate these terms with less expertise than the counterparties.

## What a Fix Looks Like
Make the right specific and the data joinable. Specify in contract the exact fields, schema, granularity and delivery frequency rather than a general right to audit, which is the fix, costs nothing, and is the single highest-leverage change available to any advertiser signing a new agreement. Require a common transaction identifier to be carried and returned, since without it no reconciliation is possible and its absence is the mechanism by which the right is defeated. Take delivery continuously rather than annually, because continuous data is analysable and an annual dump is an archaeology project. Standardise the schema through an industry body, as bilateral formats guarantee incompatibility and no single advertiser can impose one. Make confidentiality claims specific and testable, so a refusal names the field and the reason instead of the request. Use a neutral intermediary to hold and join data where parties will not share directly, which is a well-understood pattern and resolves most genuine confidentiality objections. Reconcile on a sample where full coverage is refused, since a rigorous sample answers the question and is far harder to refuse. Report which parties supplied what, because the pattern of non-cooperation is itself a finding and a commercial lever. Tie renewal to data cooperation, which is the only enforcement an advertiser actually has. And publish the resulting standard terms, since every advertiser negotiating alone is how the current position was reached.

## Who Feels the Pain
Advertisers with audit rights that cannot be exercised; auditors reconciling summaries they know prove nothing; and publishers equally unable to see their own revenue chain.

## Impact If Fixed
A right to audit without specified fields, schema and frequency is unenforceable, and that drafting gap is the defect. Specifying the data and requiring a carried transaction identifier costs nothing at signature and is what makes every downstream analysis possible.
