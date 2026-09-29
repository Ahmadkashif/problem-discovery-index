# Free Text Against a Fixed Clock

**Niche:** [[niches/neobanks/disputes-and-reg-e/profile|Disputes & Reg E Operations]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Disputes arrive as a member's free-text description of what went wrong and must become a coded claim against a network deadline, and the clock does not adjust for volume.
**Tags:** #large-language-models #workflow-orchestration #compliance #automation #evaluation-metrics #confidence-intervals #bert #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn a member's description of what went wrong into a coded claim before a regulatory clock expires — and whoever does that handles volume growth without either breaching deadlines or writing off valid claims.

## The Problem
A member writes that they did not make a charge, or that a subscription they cancelled kept billing, or that they paid for something that never arrived. Each of those is a different claim type with different evidence requirements, different network rules and different chances of success. Somebody must read the message, classify it, gather the transaction record, the device history, the communication log and any merchant evidence, and file within a deadline. Volume grows with the customer base and the deadline does not move. When the queue exceeds the capacity, claims are filed badly or credited without contest, and both are expensive.

## Why Nobody Has Built This
Dispute handling was built as a case management workflow with a person at the centre, which was correct when volumes were small and does not scale — the design assumption outlived the conditions. Classification from free text was not reliably automatable until recently. The regulatory clock creates an incentive to resolve rather than to contest, which absorbs the problem financially. And the write-offs appear as a cost line rather than as an operational failure.

## What to Build
Automate the intake and the evidence. Classify the claim from the member's own words, which is now reliable and is the step that determines everything downstream — a misclassification at intake cannot be recovered later and is the single most consequential moment in the process. Ask the clarifying questions automatically where the description is ambiguous, since a short structured follow-up at the moment of reporting is far more effective than an analyst chasing later. Assemble the evidence automatically from the institution's own systems, which is most of the case preparation and is mechanical. Track the deadline per claim with escalation, so nothing expires silently in a queue. Predict the representment outcome, since contesting a claim that will not win wastes effort and conceding one that would have won is a loss — and the institution has the history to learn this and does not use it. Prioritise the queue by value and deadline rather than by arrival, which is the ordinary triage that a fixed clock makes essential. Detect the patterns — a merchant generating disproportionate disputes, a member with an implausible claim history — which are both actionable and invisible in per-case handling. Give the member a clear status, since the uncertainty is the complaint as much as the outcome. Feed dispute outcomes into the risk models, connecting to the measurement niche, since a confirmed fraud claim is a label. And report deadline compliance and representment win rate, which are the two numbers that describe whether this function is working.

## Target Customer
Operations and compliance leadership at digital banks, dispute processing vendors, and the sponsor banks whose exposure includes their programmes' dispute handling.

## Impact If Built
The workflow put a person at the centre when volumes were small and the assumption outlived the conditions. Classification from the member's own words is now reliable and is the moment that determines the outcome, and evidence assembly is mechanical.
