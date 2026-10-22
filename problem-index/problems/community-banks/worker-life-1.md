# The BSA Analyst and the Alert Queue

**Industry:** [[community-banks|Community Banks]]
**Type:** Worker Life Changing
**One-liner:** A community bank BSA analyst spends most of each day clearing transaction-monitoring alerts she already knows are noise, rebuilding the same case file by hand each time, while the 30-day SAR clock runs on the few that matter.
**Tags:** #gradient-boosting #large-language-models #graph-theory #evaluation-metrics #worker-facing #compliance #automation

## The Problem
At a $1B community bank, the BSA department is often a BSA officer and ~two to four analysts (estimate). The monitoring system (Verafin, Abrigo BAM+, or the core vendor's module) generates alerts every night: cash deposits just under $10,000, wires to a new country, rapid movement through a new business account, a customer's activity departing from their profile. Each alert means opening the customer's record in the core, pulling twelve months of transactions, checking the customer due diligence file and any beneficial owner certification, searching for prior alerts and prior SARs, looking at related accounts, and writing a disposition. Most alerts close as explained: the landscaper who deposits cash every Friday, the farmer who wires for equipment every spring, the church that deposits the collection plate on Monday. The analyst knows these customers and still has to document each one as if she did not.

When something is suspicious, the clock starts. The SAR is due 30 calendar days after the bank determines the activity is suspicious, at most 60 if no suspect has been identified, and the narrative has to tell an investigator who has never heard of the bank what happened, who did it and why it is suspicious. Continuing activity reviews add more. An examiner will sample closed alerts and ask why each was closed.

## Why It Matters to the Worker
The work is repetitive and the stakes are asymmetric. Clearing a hundred legitimate alerts earns nothing; missing the one that mattered becomes an examination finding with her initials on the disposition. Compliance professionals report high stress and burnout in industry surveys, and at a small bank there is no one to cover when she is out; alerts age, and aged alerts are themselves a finding. Experienced analysts carry the institution's memory of which customers are normal and which patterns preceded past SARs, but none of that memory is in the system, so every new analyst starts from zero and every departure costs the bank years of context.

## What a Solution Looks Like
Each alert arrives already assembled: the customer profile, the transaction history around the flagged activity, prior alerts and their dispositions, related parties and shared addresses or devices, and a comparison with the customer's own seasonal pattern. A model trained on the bank's own past dispositions ranks alerts by likelihood of escalation and drafts the disposition rationale for the routine ones, which the analyst confirms or corrects. For escalated cases, a draft SAR narrative in the five-W structure examiners expect, with the 30-day deadline tracked from the date of determination. Her corrections become the training data.

## Impact If Solved
Cutting the time spent assembling and documenting routine alerts by half or more (estimate) gives a small BSA team back hours every day, moves attention to the cases that produce SARs, shortens the time from alert to filing, and gives the next analyst the department's memory instead of an empty queue.
