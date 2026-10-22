# The Declination Nobody Logged

**Niche:** [[niches/reinsurers/facultative-underwriting/profile|Facultative Reinsurance Underwriting]]
**Industry:** [[industries/reinsurers|Reinsurers]]
**Type:** Fix (Pain Point)
**One-liner:** Most fac submissions are declined by a one-line email, so the reinsurer never learns what it turned away or whether it was right to.
**Tags:** #large-language-models #evaluation-metrics #feature-engineering #quick-win #workflow-orchestration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to read an individual-risk submission (engineering survey, statement of values, loss runs) and return a priced line inside the broker's turnaround, and whoever answers fastest without missing the risk's worst feature takes the account.

## The Problem
Declined risks leave no structured trace. When the same risk returns next year through another broker, or burns, nobody can say why it was declined or whether the reason still holds.

## Why It's Still Broken
Declining takes seconds and logging takes minutes, and nothing in the workflow asks for a reason.

## What a Fix Looks Like
Capture every declination with the risk identity and a reason code drafted from the underwriter's reply, link resubmissions automatically, and periodically match declined risks to later public loss events.

## Who Feels the Pain
Fac underwriters re-reading resubmissions; heads of fac who cannot show their appetite works; brokers who get inconsistent answers.

## Impact If Fixed
A record of the risks turned away, which is half of what a fac underwriter's judgement consists of, and a way to grade it.
