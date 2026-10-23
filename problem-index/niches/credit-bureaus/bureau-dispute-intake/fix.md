# Identity Theft Claims Lost in the General Queue

**Niche:** [[niches/credit-bureaus/bureau-dispute-intake/profile|Bureau Dispute Intake & Triage]]
**Industry:** [[industries/credit-bureaus|Credit Bureaus]]
**Type:** Fix (Pain Point)
**One-liner:** An identity theft victim's block request has a shorter statutory clock than an ordinary dispute, and it waits in the same queue.
**Tags:** #bert #large-language-models #evaluation-metrics #compliance #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to separate the genuine error from the templated flood at intake — routing identity theft, mixed-file and real inaccuracy claims to investigation inside the five-business-day furnisher notice — and whoever cuts the bureau's cost per dispute without wrongly dismissing a genuine claim takes the account.

## The Problem
Under FCRA §605B a bureau must block information resulting from identity theft within four business days of receiving proof of identity, an identity theft report and the consumer's statement (recalled rule text). Victims' submissions arrive mixed with ordinary disputes and templated letters that also claim fraud, and are sorted by the same agents in the same order.

## Why It's Still Broken
Intake routes by channel and arrival time, not by legal path; templated "this is not my account" letters make real fraud claims harder to see.

## What a Fix Looks Like
Route at intake on the presence of identity theft documentation (an FTC identity theft report or police report, identity proof, a statement), start the four-day block clock, and send templated fraud claims without documentation down the ordinary dispute path with a request for the missing items.

## Who Feels the Pain
Identity theft victims trying to close a mortgage or lease with fraudulent accounts on file; agents and compliance teams exposed on the shortest clock in the statute.

## Impact If Fixed
Blocks applied inside the statutory window, and victims separated from the volume that imitates them.
