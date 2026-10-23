# Exclusion and Licence Matches With Stated Confidence

**Niche:** [[niches/investigation-and-screening-firms/regulated-workforce-screening/profile|Regulated-Workforce Screening & Monitoring]]
**Industry:** [[industries/investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Monthly checks against exclusion lists and licence boards return name hits that compliance staff clear one by one, with no estimate of which ones are real.
**Tags:** #gradient-boosting #k-nearest-neighbors #word-embeddings #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to catch every disqualifying event on a workforce already hired — a new arrest, a lapsed or disciplined licence, an exclusion-list entry — and whoever raises the fewest false alerts while missing none that an auditor or surveyor later finds takes the account.

## The Problem
A health system checks its entire workforce and its contractors every month against the federal exclusion list, the federal procurement debarment list and the state Medicaid exclusion lists its operating states maintain, plus licence boards for clinical staff. Many lists carry a name, a city and a date and little else. Common names produce dozens of hits a month; each must be cleared by comparing whatever identifiers exist and documented in case an auditor asks. A true hit missed means claims paid for an excluded person's services that must be repaid.

## Why Nobody Has Built This
Exclusion screening vendors compete on list coverage, not on match quality, and compliance teams have learned to treat every hit as manual work. The decisive identifiers sit in different systems — HR, credentialing, payroll — and are not joined to the screening run.

## What to Build
A matcher that joins each list entry to the employer's own identifiers (prior names, addresses, licence numbers, dates of birth where lists carry them), estimates the probability that a hit is the same person, attaches the evidence for and against, and routes only uncertain hits to a person. Calibrate on the compliance team's past clearance decisions, and report recall on known true exclusions as the headline.

## Target Customer
Compliance officers at hospital systems, home health agencies and pharmacy chains, and the screening firms that sell them monitoring.

## Impact If Built
Compliance staff clear a fraction of today's hits, true exclusions surface faster, and every clearance carries a documented reason an auditor will accept.
