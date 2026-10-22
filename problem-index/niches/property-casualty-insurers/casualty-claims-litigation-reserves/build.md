# Escalation Triage Before the Letter of Representation

**Niche:** [[niches/property-casualty-insurers/casualty-claims-litigation-reserves/profile|Casualty Claims Litigation & Reserve Adequacy]]
**Industry:** [[industries/property-casualty-insurers|Property & Casualty Insurers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Litigation analytics score claims once they are in suit; the value is in the first weeks, before an attorney is retained, when only the adjuster's instinct is working.
**Tags:** #tacit-knowledge-ml #large-language-models #gradient-boosting #survival-analysis #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to spot, within days of first notice, the liability claims that will draw an attorney and run toward a verdict, and whoever moves those claims to early resolution or an adequate reserve before the demand letter arrives takes the account.

## The Problem
Commercial auto and general liability claims that will escalate usually look ordinary on day one. The signals are subtle and early: which clinic the claimant went to, which firm's name appears on a lien, whether the claimant stops returning calls, the venue. Senior adjusters notice them. Junior adjusters, carrying the same caseload, often do not, and the claim is reserved as routine until a demand arrives.

## Why Nobody Has Built This
Training data is awkward: escalation labels arrive years later and are changed by the handling, and adjusters' early suspicions were never recorded. Vendors built for the suit stage, where litigation data is cleaner and buyers already exist.

## What to Build
A day-3, day-10 and day-30 escalation score for every liability claim. It is trained on closed-claim outcomes and on the structured reads of senior adjusters captured prospectively, and explained in claims vocabulary with similar closed claims retrieved. Claims crossing a threshold route to early-resolution specialists, with a suggested reserve range and the cues that drove the score.

## Target Customer
Chief claims officers and casualty claims VPs at commercial auto, general liability and personal auto writers.

## Impact If Built
More escalating claims resolved before representation and reserved adequately from the start, which shows up as lower severity and less adverse development in the lines where both are concentrated.
