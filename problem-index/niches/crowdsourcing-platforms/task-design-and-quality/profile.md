# Task Design & Quality Enforcement

**Parent Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Category:** High Market Share
**Contested on:** Whether a disagreement means the worker was careless, the item was ambiguous, or the instructions were unclear.

## Profile
**Market Size:** ~$810M — 27% of the US microtask and research-participant market
**Share of Parent Industry:** ~27%
**Digital Adoption:** Low — attention checks and agreement thresholds
**Target Buyer:** Requesters; platform quality and trust teams
**Automation Potential:** High for diagnosis; the allocation rule is not a technical question

## What Makes This a Distinct Niche

Quality is enforced with attention checks and agreement thresholds, which punish workers who disagree with the majority on genuinely ambiguous items.

This is the mechanism through which nearly all of the industry's harm runs. A worker's answers are compared to the majority; deviation is treated as carelessness; and the consequences are rejection, withheld payment, a damaged approval rate and lost access to better-paid work. The mechanism cannot distinguish a careless worker from a careful one answering a genuinely ambiguous item, or from one following instructions that could be read two ways.

Meanwhile most bad crowd data is caused by unclear instructions, and the requester who wrote them is the person least able to notice.

The niche is distinct because it is simultaneously the requester's data quality problem and the worker's livelihood problem, and the same evidence resolves both.

## Current Tools & Gaps

Attention and trap items. Gold-standard questions with known answers. Inter-annotator agreement statistics. Approval rate as a qualification gate. Majority-vote aggregation. Some platforms offer worker qualification tests and requester-side quality dashboards.

The gaps are diagnosis and allocation. Nothing distinguishes the three causes of disagreement, so all of them are charged to the worker. Item-level ambiguity is not identified, though it is highly visible in the response pattern. Instruction defects are not detected, though the signals — clarification questions, abandonment, time variance, systematic split answers — are all recorded. And the cost of every one of these falls on whoever submitted the answer.

### Contested sub-niches

- [[niches/crowdsourcing-platforms/instruction-quality/profile|🎯 Instruction & Task Design Quality]]
- [[niches/crowdsourcing-platforms/error-cost-allocation/profile|🎯 Error Cost Allocation]]

## Problems
- [[niches/crowdsourcing-platforms/task-design-and-quality/build|🔨 Build: Disagreement Diagnosis Instead of Majority Punishment]]
- [[niches/crowdsourcing-platforms/task-design-and-quality/buy|🛒 Buy: Annotation Quality Tooling Adapted to an Open Crowd]]
- [[niches/crowdsourcing-platforms/task-design-and-quality/fix|🔧 Fix: The Attention Check That Is Itself Ambiguous]]
