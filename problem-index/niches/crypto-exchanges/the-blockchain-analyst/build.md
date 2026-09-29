# Working at the Case Level

**Niche:** [[niches/crypto-exchanges/the-blockchain-analyst/profile|The Blockchain Analyst]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The analyst's skill is judging what a pattern means, and their day is spent clicking through hops to assemble the pattern.
**Tags:** #graph-theory #graph-neural-networks #large-language-models #worker-facing #evaluation-metrics #confidence-intervals #automation #compliance
**Contested on:** Every serious competitor in this niche is fighting to make one analyst's hour of hop-by-hop tracing produce a defensible conclusion instead of a narrative — and whoever gives them the tooling to work at the case level rather than the hop level changes what the function can cover.

## The Problem
An alert arrives. The analyst opens the graph, expands the source address, sees six inputs, picks one, expands again, sees eleven, picks one, and continues until they have a story or run out of time. The choice at each branch is judgement, but the expansion is mechanical and consumes most of the hour. The conclusion depends heavily on which branches were chosen, which means two analysts on the same case reach different answers and nobody knows it.

## Why Nobody Has Built This
The vendor interface was built as an exploration tool for investigators, so the interaction model is manual expansion — and that model was never revisited because it looks like what investigation is supposed to feel like. Enumerating paths automatically requires deciding which are worth enumerating, which is the judgement nobody wanted to encode. Analyst output is unmeasured, so inconsistency is invisible. And the function is staffed rather than tooled.

## What to Build
Raise the unit of work from the hop to the case. Enumerate the plausible paths automatically and present them ranked, which is the core and returns the analyst's hour to judgement rather than expansion. Summarise what the paths collectively show, since the analyst's real question is what kind of case this is and they currently answer it by traversal. Rank branches by informativeness so exploration goes where it matters, because the current order is whatever the interface displays. Assemble the case evidence — addresses, amounts, timing, counterparty types, prior cases — into one record, as gathering is most of the remaining time. Draft the narrative from the assembled evidence with the analyst editing, since narrative writing is repetitive and the structure is fixed. Surface prior similar cases and what was concluded, because the same patterns recur and nothing recalls them. Measure consistency between analysts on the same case, which is currently unknown and is the clearest quality signal available. Show the analyst the outcome when one ever returns, since the role's defining condition is never learning anything. Record the judgement and its reasoning in a structured form, which feeds both consistency measurement and the evaluation problem. Preserve the analyst's authority over the conclusion, because the value of the role is the judgement and automating it away is both wrong and unusable. And track cases per analyst and time per case honestly, so capacity is a known quantity.

## Target Customer
Compliance operations leadership, the analysts themselves, blockchain analytics vendors whose interfaces stopped at exploration, and law enforcement partners consuming the conclusions.

## Impact If Built
The interaction model is manual expansion because that is what investigation was assumed to look like. Automatic path enumeration with ranked branches returns the hour to judgement and makes consistency measurable for the first time.
