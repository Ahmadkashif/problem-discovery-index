# Acknowledgement Deadlines Set from Evidence

**Niche:** [[niches/answering-services/oncall-routing-paging/profile|On-Call Routing & Paging]]
**Industry:** [[industries/answering-services|Telephone Answering Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every account says "re-page after ten minutes, then call the backup", a number someone picked once; nobody knows how fast each physician actually answers at 3 a.m., or when silence means trouble.
**Tags:** #survival-analysis #gradient-boosting #hypothesis-testing #workflow-orchestration #compliance #feature-engineering
**Contested on:** Every serious competitor in this niche is fighting to get each urgent patient call to the correct on-call clinician, acknowledged inside the practice's time limit, with a record that will stand up in a negligence claim, and whoever closes the most urgent pages inside the limit without waking a clinician for a routine call takes the account.

## The Problem
Escalation chains run on fixed timeouts. A physician who reliably answers in two minutes and one who takes fifteen get the same ten-minute window, so the first one's rare silence is noticed late and the second one's backup is woken unnecessarily. The service holds years of page and acknowledgement timestamps and uses none of them to set the timeouts.

## Why Nobody Has Built This
Acknowledgement events are scattered across pager networks, secure apps and voice callbacks that the platform logs separately, and old pagers give no read receipt at all. Services have treated the timeout as a client preference, not a measurable quantity.

## What to Build
A time-to-acknowledge model per physician, by hour, day, channel and call type, built on survival analysis with censoring when the chain moves on. Timeouts are set so that a given share of urgent pages are acknowledged before the practice's limit. An alert fires when a normally fast responder is out of pattern, and each practice gets a monthly report of its own physicians' response distribution.

## Target Customer
Operations directors at multi-site medical answering services; platform vendors adding it to on-call modules.

## Impact If Built
Urgent pages reach a responsive clinician sooner, unnecessary backup escalations fall, and the service can show each practice where delay actually comes from, which is often the practice's own physicians rather than the service.
