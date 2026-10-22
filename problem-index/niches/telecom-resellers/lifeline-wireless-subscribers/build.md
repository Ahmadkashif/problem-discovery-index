# Recertification Outreach for People Without Stable Contact

**Niche:** [[niches/telecom-resellers/lifeline-wireless-subscribers/profile|Lifeline Wireless Subscribers]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Eligible Lifeline subscribers lose service every year because they miss an annual recertification they never saw, and the provider loses a subscriber it was entitled to keep.
**Tags:** #survival-analysis #gradient-boosting #feature-engineering #large-language-models #worker-facing #compliance
**Contested on:** Every serious competitor in this niche (Lifeline modules in MVNO BSS platforms, enrolment and verification tools, and compliance outsourcers) is fighting to keep each claimed subscriber both eligible and actively using service through National Verifier checks, annual recertification and non-usage rules, and whoever keeps claims clean without dropping eligible subscribers takes the account.

## The Problem
Each Lifeline subscriber must recertify eligibility every year. Where the National Verifier can't confirm eligibility automatically from a state or federal database, the subscriber has to respond. Providers send texts and robocall-style reminders to the Lifeline phone. Subscribers who changed phones, ran out of airtime, moved or don't read English miss the window and are de-enrolled, often while still eligible. Many re-enrol later through an agent, at a fresh acquisition cost.

## Why Nobody Has Built This
Lifeline providers optimise for enrolment, which they pay agents for, rather than retention, and outreach tools treat everyone alike. The subscribers least likely to respond are those with the least stable contact, and nobody models that.

## What to Build
A model of each subscriber's probability of missing recertification, from tenure, past responses, usage patterns, language, device changes and whether the automated database check is likely to succeed. High-risk subscribers get early, repeated outreach in their language through the channels they actually use, such as in-app messages, calls at the hours they are active, and partner community organisations. The outreach should help them through the steps without collecting anything the rules don't require.

## Target Customer
Lifeline compliance and subscriber-operations leaders at wireless ETCs.

## Impact If Built
More eligible people keep their service through recertification, providers stop paying to re-acquire subscribers they lost to a missed text, and enrolment pressure on agents eases.
