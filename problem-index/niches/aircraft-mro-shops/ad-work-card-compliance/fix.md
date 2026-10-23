# Recurring AD Intervals Counted From the Wrong Baseline

**Niche:** [[niches/aircraft-mro-shops/ad-work-card-compliance/profile|AD & Work-Card Compliance Checking]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Fix (Pain Point)
**One-liner:** A recurring AD inspection is due "within 500 hours after the last inspection or the effective date of this AD, whichever occurs later", and the next-due figure is computed from the wrong one.
**Tags:** #compliance #evaluation-metrics #automation #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to prove every work card cites the current AD revision and an approved method of compliance for that serial number, and whoever has the lowest missed-applicability rate takes the account.

## The Problem
Recurring ADs carry compliance times with several baselines (hours, cycles, calendar, "whichever occurs first/later", from the effective date, from the last accomplishment, from a component's installation). When an AD is revised or superseded, the baseline may reset or carry over. A next-due figure computed wrong in the tracking record or on the work card makes the aircraft overdue without anyone knowing.

## Why It's Still Broken
The compliance paragraph is written in legal prose and interpreted by a person once, when the AD is entered, then trusted. Revisions are entered as new items without re-checking how the baseline carries over. Nobody re-derives next-due dates from source.

## What a Fix Looks Like
Parse each recurring AD's compliance time into a structured rule (units, baselines, first-or-later logic, supersedure carry-over), recompute next-due dates from the aircraft's own accomplishment history, and flag any tracking-record or work-card figure that disagrees, quoting the paragraph.

## Who Feels the Pain
Inspectors and records clerks who own AD status; owners who learn at a pre-buy that an AD has been overdue for two years; mechanics whose signatures are on the overdue entries.

## Impact If Fixed
A recompute pass that catches even one overdue recurring AD per hundred tracked aircraft a year (estimate) prevents an unairworthy operation each time. It costs minutes per aircraft once the rules are parsed.
