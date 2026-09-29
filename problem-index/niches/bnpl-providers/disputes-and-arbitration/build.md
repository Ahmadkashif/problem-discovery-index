# Arbitrating on Evidence Nobody Supplies

**Niche:** [[niches/bnpl-providers/disputes-and-arbitration/profile|Disputes & Arbitration]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** One team arbitrates between consumers who say the goods never arrived and merchants who say they did, on evidence neither side supplies, several hundred times a week.
**Tags:** #workflow-orchestration #large-language-models #evaluation-metrics #confidence-intervals #compliance #graph-theory #automation #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to adjudicate between a consumer and a merchant on evidence neither supplies — and whoever builds that evidence base decides a dispute rather than splitting the difference.

## The Problem
The consumer says the parcel never came. The merchant says the carrier marked it delivered. The provider holds the instalment plan and must decide whether the consumer keeps paying. It has no independent knowledge of whether a parcel arrived at a door. Both parties have an interest and both supply only what helps them. An agent decides in a few minutes, several hundred times a week, and whichever way they decide one relationship is damaged. The provider is structurally in the middle of a factual question it cannot answer, and does so at volume.

## Why Nobody Has Built This
The provider was never designed to be an arbiter and acquired the role by sitting between the two parties — a position inherited rather than chosen, which is why no evidence apparatus was built for it. Carrier data is available in principle and integrated rarely. Both parties' claim histories exist and are not used. Consistency is unmeasured because nobody has defined a comparable case. And the volume makes per-case investigation uneconomic.

## What to Build
Assemble evidence rather than adjudicating assertions. Integrate carrier tracking directly rather than accepting a merchant's screenshot, which is the fix for a large share of delivery disputes and is a data source the provider can obtain independently. Use both parties' histories, since a consumer with a pattern of non-delivery claims and a merchant with a pattern of disputed deliveries are both informative and both currently invisible in the individual case. Surface base rates — this merchant's dispute rate, this carrier's delivery reliability in this area — which reframes a credibility contest as a probability and is the most useful thing the provider can add. Recommend an outcome with reasoning, leaving consequential cases to a person, since the provider's decision affects a consumer's obligation and a merchant's revenue. Auto-resolve the clear cases, which are a large share and consume the same attention as the difficult ones. Ask each party for the specific evidence that would decide it, rather than accepting whatever they send. Record decisions and outcomes structurally, which enables the consistency measurement that is the fix note's subject. Feed dispute patterns into merchant risk, since a merchant generating disproportionate delivery disputes is a commercial signal. Give both parties a clear explanation, because an unexplained decision damages the relationship more than the outcome does. And measure consistency and reversal rate rather than throughput, since the function's quality is whether like cases are decided alike.

## Target Customer
Operations leadership at instalment providers, merchants and consumers on either side of these decisions, and the dispute resolution vendors serving the segment.

## Impact If Built
The arbiter role was inherited by sitting between two parties rather than chosen, which is why no evidence apparatus exists for it. Integrating carrier data directly and surfacing merchant and consumer base rates turns a credibility contest into a probability.
