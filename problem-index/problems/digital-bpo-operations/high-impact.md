# Handle Time Is Measured to the Second and Resolution Is Sampled at Two Percent

**Industry:** [[digital-bpo-operations|Digital BPO Operations]]
**Type:** High Impact
**One-liner:** Every second of an agent's shift is recorded and whether the customer's problem was solved is estimated from a small sample and a survey almost nobody answers.
**Tags:** #transformers #bert #large-language-models #gradient-boosting #confidence-intervals #evaluation-metrics #causal-inference #hypothesis-testing

## The Problem
Operational measurement in this industry is extraordinarily granular on the input side. Average handle time, after-call work, hold time, adherence to schedule, occupancy, and idle seconds are all tracked continuously per agent and roll up into team, site and contract-level reporting.

Resolution is measured by two instruments and both are weak. A quality analyst scores a sample of contacts — typically a low single-digit percentage — against a rubric. And a post-contact survey goes to customers, with a response rate low enough and self-selected enough that it describes the strongly satisfied and the strongly annoyed rather than the population.

The consequence is that the metric governing behaviour and the outcome being purchased diverge, and they diverge most on the contacts that matter. A complex issue handled properly takes longer than the target, and the repeat contact it prevents is counted as a separate contact with its own handle time — so from the measurement's point of view, resolving something thoroughly looks worse than half-resolving it twice.

Agents understand this precisely and respond rationally: keep within handle time, transfer what will run long, close the contact and let the repeat land on someone else. Every experienced person in the industry knows this dynamic and the contracts continue to be written on handle time because it is unambiguous and auditable.

The measurement to fix it now exists. Automated analysis of the full contact record — transcripts, subsequent contact behaviour, downstream account activity — can estimate resolution across every interaction rather than two percent of them, which would replace an estimate with a measurement and would make the divergence undeniable. That last property is the reason it is not deployed as the primary metric.

## Why It's Unsolved
The commercial structure is built on the measurable. Outsourcing contracts specify service levels in handle time, answer rate and adherence because those are auditable and disputable, and rewriting them around resolution requires both parties to agree on a definition of resolution — which is harder, contestable, and gives the vendor an incentive to define it favourably.

Attribution to business outcome is genuinely difficult. Whether good support produced retention, additional purchase or reduced churn is a causal question requiring client data the vendor does not have and an experimental design nobody runs.

The vendor's economics are also volume-linked. A vendor paid per contact or per hour is not straightforwardly rewarded for reducing repeat contacts, and a measurable reduction in contact volume is a revenue reduction unless the contract is structured to share it — which most are not.

And there is a workforce consequence that cuts both ways. Resolution-based measurement is fairer to agents handling hard contacts and requires assessing every interaction, which is a substantial expansion of monitoring over a workforce already measured to the second. Getting that right matters: the same capability that could replace a punitive handle-time regime could equally become a more total one.

## What a Solution Looks Like
Measure resolution across everything, not a sample. Automated assessment of the full contact record — whether the stated issue was addressed, whether the customer contacted again about the same thing within a window, whether the underlying account activity indicates the problem persisted — turns quality from a sampled estimate into a measurement, with sampling error removed.

Report repeat contact as the primary quality metric. It is objective, it is in the vendor's own data, and it directly captures the failure that handle time incentivises. Repeat contact rate by issue type and by agent, adjusted for case mix, is the single most informative number this industry could adopt.

Recalibrate targets for the changed mix. Deflection has removed the simple contacts, so the remaining population is harder; handle time targets set on the old distribution are now measuring a different job. Re-deriving targets from the current mix, and by issue type rather than globally, would remove an unacknowledged and demoralising target creep.

Restructure the contract. Outcome-linked terms — sharing the value of reduced repeat contact rather than billing per contact — align the vendor with the client, and are the only way the measurement changes behaviour rather than just reporting.

And design the expanded assessment for the agent's benefit. If every contact is now assessed, the resulting information should first serve coaching and fair evaluation, with strict limits on its use in discipline — otherwise a better quality metric becomes a worse working environment.

## Impact If Solved
This industry measures the input exhaustively and estimates the output from a sample, and the two metrics conflict on precisely the contacts that matter most. Full-coverage resolution assessment removes the sampling error, repeat contact rate captures the failure that handle time rewards, and recalibrating targets for the post-deflection contact mix addresses a squeeze that agents are currently absorbing without explanation. Whether it improves working life or worsens it depends entirely on how the expanded measurement is governed.
