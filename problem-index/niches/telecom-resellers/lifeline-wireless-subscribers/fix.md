# The Non-Usage Notice Sent to a Phone Nobody Checks

**Niche:** [[niches/telecom-resellers/lifeline-wireless-subscribers/profile|Lifeline Wireless Subscribers]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Fix (Pain Point)
**One-liner:** A free Lifeline line that goes quiet triggers a de-enrolment warning sent to that same quiet line, so the people most likely to miss it are the ones it is sent to.
**Tags:** #logistic-regression #change-point-detection #feature-engineering #compliance #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche (Lifeline modules in MVNO BSS platforms, enrolment and verification tools, and compliance outsourcers) is fighting to keep each claimed subscriber both eligible and actively using service through National Verifier checks, annual recertification and non-usage rules, and whoever keeps claims clean without dropping eligible subscribers takes the account.

## The Problem
Lifeline rules require providers to stop claiming lines that aren't used for a set period and to warn the subscriber first (a 30-day window and a cure notice, recalled). The rule exists for a good reason, since unused lines shouldn't draw subsidy. In practice the warning goes by text to the inactive phone. A subscriber whose phone broke, who uses the line only for incoming calls from a clinic, or who is in hospital loses service without ever seeing the notice.

## Why It's Still Broken
Providers apply the rule as a batch job on usage counters and send notices through the cheapest channel. Nothing distinguishes a line that was abandoned from one whose owner can't currently use it, and nobody measures how many de-enrolled subscribers were eligible and came back through an agent weeks later.

## What a Fix Looks Like
Detect the change in a line's usage pattern early, before the window runs out, and classify the likely reason: a device problem, incoming-only use, or abandonment. Reach the subscriber through an alternate contact recorded at enrolment, with the cure step made as easy as one call or reply. Report re-enrolments of previously de-enrolled subscribers as a measure of wrongful loss.

## Who Feels the Pain
Low-income subscribers who lose their only phone; providers who pay twice to enrol the same person; and compliance teams who want clean claims without dropping eligible people.

## Impact If Fixed
The rule keeps doing its job for abandoned lines while fewer eligible subscribers are cut off for a notice they could never have read.
