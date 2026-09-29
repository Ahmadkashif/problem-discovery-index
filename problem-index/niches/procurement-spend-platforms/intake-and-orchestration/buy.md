# Workflow Orchestration With Parallelism and Dependencies

**Niche:** [[niches/procurement-spend-platforms/intake-and-orchestration/profile|Intake & Orchestration]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Orchestration engines run dependent tasks in parallel with retries and escalation as a matter of course, and a procurement request commonly visits legal, security, privacy and finance one after another because that is the order somebody configured.
**Tags:** #workflow-orchestration #graph-theory #dynamic-programming #optimization-fundamentals #evaluation-metrics #confidence-intervals #automation #descriptive-statistics
**Contested on:** Every serious competitor in procurement intake is fighting to take a request from someone who does not know what procurement needs and route it correctly without a human help desk — and whoever routes most requests unassisted takes the account.

## The Problem
A software purchase requires a security assessment, a privacy review, a legal review of the terms and a finance approval. None of the four depends on any other, and in most implementations they run in sequence, because the workflow was built as a chain. The elapsed time is the sum rather than the maximum, which on four reviews with a few days each is the difference between a fortnight and four days. The requester experiences a procurement process that takes a month, and the cause is a configuration decision nobody revisited.

## What Already Exists
Workflow and business process orchestration engines handle parallel branches, joins, conditional paths, timeouts, escalation and compensation as standard, with mature commercial and open options. Case management platforms handle human tasks with deadlines. The procurement intake vendors are built on exactly this kind of engine. The capability is present in the products; the configurations do not use it.

## The Customization Gap
The adaptation is to reviews performed by people with other jobs. It requires: (1) genuine dependency modelling rather than sequence — most reviews are independent and a few genuinely depend on another's output, and stating which is which is a one-time exercise that collapses cycle time; (2) partial-information starts, since a security review can frequently begin before legal has finished and waiting for a complete package is a convention rather than a requirement; (3) reviewer capacity and availability as real constraints, because the most common delay is a reviewer on leave with no delegation and a chain that has no concept of it; (4) escalation on elapsed time with a defined fallback, since procurement requests currently stall indefinitely when a reviewer does not respond and nobody owns the unblocking; and (5) requester-visible status showing what is outstanding and with whom, which is the thing that generates most of the chasing and is trivial to provide.

## Target Customer
Procurement intake and orchestration vendors, procurement operations teams whose cycle time is dominated by sequential reviews, and the legal, security and privacy functions who receive the requests.

## Impact If Solved
Parallelising independent reviews is a configuration change that can halve elapsed time, which is the single largest determinant of whether employees use the process at all. Reviewer availability and escalation address the tail, which is what people actually remember and what drives them to a card.
