# Hosting Capacity Graded Against the Reviews That Followed

**Niche:** [[niches/electric-utilities/der-interconnection-hosting-capacity/profile|DER Interconnection & Hosting Capacity]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Utilities publish hosting-capacity values and run supplemental reviews on the same feeders, and nobody compares the two to learn where the map is wrong.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #hypothesis-testing #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to clear rooftop, storage and EV-charger applications against a hosting-capacity number that later studies confirm, and whoever sends the fewest applications to full study without a later violation takes the account.

## The Problem
A hosting-capacity map says a feeder section can take 1.2 MW of new solar. An applicant designs to that number, applies, fails a screen, and the supplemental review finds 400 kW. Or the map says zero and the review finds plenty. Each disagreement costs applicants design work and the utility review time, and it undermines trust in the map that was meant to reduce applications.

## Why Nobody Has Built This
Hosting maps and supplemental reviews are produced by different teams with different tools, and the map's assumptions (load profiles, DER output, protection limits) are rarely stored with each value. Disagreements are handled one application at a time.

## What to Build
A grading layer: every supplemental-review result is joined to the hosting value the map showed for that location at the time, and to the assumptions behind it. Models learn which feeder characteristics (long rural runs, regulators, existing DER mix, minimum-load conditions) predict map error. The map is then corrected with an uncertainty band, and applications are routed accordingly: confident passes go fast-track, likely failures are told early, uncertain ones get review.

## Target Customer
DER interconnection managers at utilities in states with mandated hosting maps and high application volume.

## Impact If Built
~20%–30% fewer failed fast-track applications and fast-track decisions in days rather than weeks (estimate), plus a published map applicants can believe, which is what the regulators who mandated it wanted.
