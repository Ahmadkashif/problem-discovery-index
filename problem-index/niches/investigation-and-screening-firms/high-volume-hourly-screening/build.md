# Identity Completeness Captured at the Application

**Niche:** [[niches/investigation-and-screening-firms/high-volume-hourly-screening/profile|High-Volume Hourly & Gig Screening]]
**Industry:** [[industries/investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Most delays in volume screening start with what the applicant typed on a phone in two minutes, and nothing checks it before the searches run.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to clear an hourly or gig applicant before that applicant accepts another offer, and whoever returns the largest share of complete, accurate reports within one business day takes the account.

## The Problem
An hourly applicant fills in the consent and identity form on a phone: name, date of birth, Social Security number, current address. Prior names, prior addresses and nicknames are optional or skipped. The screener then runs an address history trace, picks counties to search and matches court records against what the applicant gave. A wrong date of birth, a missing maiden name or an unlisted county where the applicant lived two years ago produces a possible match that needs manual review, a re-run, or a missed record. Where courts hide identifiers — as California's *Hamrick* ruling forced from 2021 — the screener has even less to match on.

## Why Nobody Has Built This
Candidate forms are owned by the applicant tracking system or the screener's consent flow and are designed to minimise drop-off, so every extra field is resisted. Nobody measures which form inputs cause downstream delay.

## What to Build
A pre-search check that runs while the applicant is still on the form: compare entered identity against the address-history trace and flag gaps ("we found an address in another state in 2023 — did you live there?"), prompt for prior names only when the trace suggests them, validate dates of birth against format and plausibility, and predict which counties will need identifiers the applicant has not supplied. Learn from the firm's own history which missing inputs caused delays and ask only for those.

## Target Customer
Screening firms' product leaders and gig platforms' trust and safety teams, where same-day clearance is the renewal criterion.

## Impact If Built
Fewer stalled possible-match reviews and re-runs would lift the same-day clear rate, and the corrected inputs would also lower wrong-person matches.
