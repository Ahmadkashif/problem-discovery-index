# Cycle Time Measured and Never Decomposed

**Niche:** [[niches/contract-lifecycle-platforms/contract-negotiation/profile|Contract Negotiation]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every legal team reports contract cycle time and none of them can say which clauses, which approvers or which counterparties account for the delay.
**Tags:** #survival-analysis #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #workflow-orchestration #automation
**Contested on:** Every serious competitor here is fighting to get to an agreed contract faster and on better terms — and that contest splits between removing the routine edits and knowing which positions are achievable, which is why this niche is not terminal and is decomposed below.

## The Problem
The legal operations dashboard reports an average contract cycle time of nineteen days, up from seventeen. This is presented quarterly and produces a discussion about resourcing. Nobody can say that the indemnity clause accounts for a third of the elapsed time, that contracts requiring one particular approver wait four days on average for that approval, that agreements with a specific counterparty type take twice as long, or that the median is nine days and the mean is dragged by a long tail of stuck agreements that each have an identifiable cause.

## Why It's Still Broken
Cycle time was the first metric the category could report and it stuck. Decomposing it requires attributing elapsed time to states, parties and clauses, which needs the workflow to be instrumented at a finer grain than most implementations bother with. Averages also conceal the structure of the distribution, which here is strongly bimodal — most contracts move quickly and a minority get stuck — and reporting a mean of a bimodal distribution is close to reporting nothing. And the metric is used for status reporting rather than for improvement, so nobody has needed it to be diagnostic.

## What a Fix Looks Like
Decompose the time. Attribute elapsed time to states — with legal, with the counterparty, awaiting approval, awaiting signature — which immediately shows that a large share of the wait is not with legal at all, and that finding usually changes the conversation. Attribute to clauses, by linking exchanges to the provisions they concerned, which names the three or four clauses that cause most of the delay and is directly actionable in the playbook. Report the distribution rather than the mean, and treat the stuck tail as a separate population with its own causes. Identify approver bottlenecks by person and by rule, since a single approval step with a slow approver frequently accounts for more delay than the entire negotiation. Compare counterparty types and deal sizes, so expectations are set against comparable agreements rather than against a global average. And measure whether changes helped, which requires the decomposition to persist over time and is the whole reason to build it.

## Who Feels the Pain
Legal teams blamed for delays that occur elsewhere in the process; sales and procurement waiting on contracts with no explanation; and legal operations leaders managing a number they cannot influence because they cannot decompose it.

## Impact If Fixed
The decomposition is a reporting change over workflow data most systems already capture, and it reliably shows that much of the delay sits outside legal. Clause-level attribution converts the metric into a specific playbook change rather than a resourcing argument.
