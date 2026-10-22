# A Graded Ledger of Discretionary Decisions

**Niche:** [[niches/trust-companies/personal-trust-administration/profile|Personal Trust Administration]]
**Industry:** [[industries/trust-companies|Trust Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Trust companies record every distribution they pay and almost none of the reasoning, so the senior officer's judgement is neither reusable by the next officer nor graded against what happened to the family.
**Tags:** #tacit-knowledge-ml #large-language-models #k-nearest-neighbors #survival-analysis #evaluation-metrics #compliance #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to make each discretionary decision on an old instrument consistent, documented and defensible at a caseload no officer can hold in memory, and whoever makes the senior officer's judgement repeatable and reviewable takes the account.

## The Problem
A mid-sized trust company handles ~10,000 or more discretionary requests a year (estimate). Each produces a ledger entry if paid and a memo if escalated; declines and informal screens often leave nothing. Two officers can decide near-identical requests under near-identical language differently, and nobody notices until a sibling's lawyer compares them. Senior officers carry the reads that matter — escalation, exploitation, equalisation risk — and those reads leave with them.

## Why Nobody Has Built This
Trust accounting vendors sell ledgers to operations buyers; the decision layer belongs to the fiduciary side, which buys rarely. Outcomes are rare and slow, so nobody could show a model working. And the legal constraint — the trustee must exercise its own discretion — made vendors wary of anything that looks like an automated decision.

## What to Build
A decision ledger drafted automatically from requests and memos: request type and amount, governing standard, other resources, prior pattern, remainder positions, decision and reason, captured in one click for declines. Precedent retrieval across the firm's history by instrument language and situation. Risk flags learned from senior officers' reviews and later outcomes, with the evidence shown. Consistency reports for the chief fiduciary officer. Everything informs; nothing decides.

## Target Customer
Chief fiduciary officers and heads of personal trust at national banks, independent trust companies and bank trust departments with several thousand discretionary accounts.

## Impact If Built
Memo preparation falls from ~1–3 hours to ~30 minutes (estimate), new officers inherit families in weeks rather than months, and the trustee can show a consistent, documented exercise of discretion to an examiner or a court — the defence that matters most when a decision is challenged.
