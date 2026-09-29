# Employee Report Triage

**Parent Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Category:** Highly Automatable
**Contested on:** Whether the reporting stream the programme creates is handled as a detection source or dumped on a security team that never asked for it.

## Profile

**Market Size:** ~$120M
**Share of Parent Industry:** ~4%
**Digital Adoption:** Moderate — a button and a queue
**Target Buyer:** Security operations, awareness programme owners
**Automation Potential:** Very high — most of the queue is mechanically resolvable

## What Makes This a Distinct Niche

The programme trains people to report suspicious messages. They do. The reports arrive as an unmanageable queue at a security team that never asked for them, where most are legitimate mail.

This is the programme's most valuable output being handled as a burden. Employee reports are a genuine detection source — they catch the messages that got past the gateway, which is by definition the ones that matter — and they arrive faster than most automated detection for novel campaigns.

The queue is also the mechanism by which the programme's central behavioural goal succeeds or fails. An employee who reports something and hears nothing, or waits a week, learns that reporting is pointless. One who reports and receives an acknowledgement within minutes learns the opposite. The response to the queue determines whether the reporting behaviour the whole programme is built to produce actually persists.

Most of the queue is resolvable mechanically. Duplicates of the same campaign, messages already blocked by the gateway, known-legitimate senders, the organisation's own simulations, and ordinary marketing mail account for the large majority.

## Current Tools & Gaps

A report button in the mail client, submitting to a mailbox or a ticket queue. Some integration into security orchestration. Automated acknowledgement in better implementations. Deduplication of identical reports in some platforms. Gateway lookup to check whether the message was already blocked.

The gaps are that the mechanical majority is handled by people. Duplicates across a campaign are frequently triaged individually. Simulation reports — the organisation's own campaigns, reported by employees doing exactly what they were asked — arrive in the same queue as real threats and consume analyst time. Known-legitimate senders are re-assessed every time. Acknowledgement is inconsistent, so the behavioural reinforcement is lost. And the value of the stream as a detection source is not measured, so it is treated as a cost rather than as a capability.

## Problems

- [[niches/security-awareness-training/report-triage/build|🔨 Build: A Queue That Resolves Itself]]
- [[niches/security-awareness-training/report-triage/buy|🛒 Buy: Triage Automation From Security Operations]]
- [[niches/security-awareness-training/report-triage/fix|🔧 Fix: They Reported It and Heard Nothing]]
