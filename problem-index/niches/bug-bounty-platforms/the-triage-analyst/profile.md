# The Triage Analyst

**Parent Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Category:** Underserved Audience
**Contested on:** Whether the person reading the queue is supported as a specialist making consequential judgements, or measured as a throughput worker.

## Profile

**Market Size:** ~$105M
**Share of Parent Industry:** ~7%
**Digital Adoption:** Low — a queue and a clock
**Target Buyer:** Platform triage operations, programme managers
**Automation Potential:** Moderate — assistance automates, the judgement does not

## What Makes This a Distinct Niche

A triage analyst is a skilled security practitioner who spends the day reading mostly invalid submissions, and whose worst possible mistake — closing a real vulnerability as a non-issue — produces no feedback and occasionally produces a breach.

The working conditions follow from that. High volume, a time target, and a queue whose contents are mostly not worth the attention of someone who could be doing security research. The work is repetitive in a way that specifically degrades the faculty it depends on: sustained exposure to low-quality submissions trains a pattern of quick dismissal, and the one real finding in a hundred arrives looking, at first glance, much like the ninety-nine.

They also carry the relationship. Every rejection is delivered to a researcher who invested unpaid time, some of whom argue, some of whom escalate publicly. The analyst is the human face of a decision they made under a throughput target, and the disputes land on them personally.

This is an underserved audience because the role is treated as a cost centre staffed by interchangeable people, when it is actually the quality control point for the entire product. The platform's value proposition rests on these judgements and nothing measures whether they are good.

## Current Tools & Gaps

A submission queue with workflow states, canned responses, manual duplicate search and reputation-ordered prioritisation. Time-to-triage service levels. Escalation to programme staff for hard cases. Career progression, where it exists, tends to lead out of triage rather than through it.

The gaps are the same ones that make the operation expensive. Nothing predicts which submissions deserve depth, so attention is uniform across a non-uniform queue. Reproduction is manual, which is the most repetitive part of the job. Duplicate search is keyword-based and fails on paraphrase. No calibration reference exists, so an analyst has no way to know whether their severity assessments are typical or whether their dismissal rate is high. Specialism is not routed for, so analysts work outside their strongest areas routinely. And nothing measures the error that matters, which means the quality of the work is unknown to the analyst and to the operation.

## Problems

- [[niches/bug-bounty-platforms/the-triage-analyst/build|🔨 Build: Support for a Consequential Judgement]]
- [[niches/bug-bounty-platforms/the-triage-analyst/buy|🛒 Buy: Analyst Support From Security Operations]]
- [[niches/bug-bounty-platforms/the-triage-analyst/fix|🔧 Fix: Measured on Speed, Judged on the One They Missed]]
