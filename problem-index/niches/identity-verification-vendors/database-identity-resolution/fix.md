# No Record Found

**Niche:** [[niches/identity-verification-vendors/database-identity-resolution/profile|Database Identity Resolution]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The check returns the same failure whether the person does not exist in the data or the data says something different, and the two need opposite responses.
**Tags:** #quick-win #data-integration #evaluation-metrics #descriptive-statistics #automation #confidence-intervals #compliance #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to confirm that a claimed identity exists and belongs to this person from records that were never built for the purpose — and whoever resolves thin-file and frequently-moving populations best serves the people everyone else cannot see.

## The Problem
Two applicants fail the database check. The first has no credit file because they are twenty and have never borrowed; the sources simply contain nothing about them. The second has a file showing a different address, which could be a stale record, a recent move, or a genuine impersonation. These are entirely different situations requiring entirely different responses, and the system returns the same failure code, so both get the same rejection.

## Why It's Still Broken
The check was built to return a match decision, so an absence and a contradiction both resolve to "not matched" — a boolean output cannot carry the distinction and nobody widened it. Downstream policy was written against the boolean. Failure reason breakdowns are not reported. And the coverage gap is uncomfortable to name.

## What a Fix Looks Like
Separate the two and respond differently. Return distinct outcomes for no-record, weak-match and contradicted-match, which is the fix and is information the check already has internally. Route no-record applicants to an alternative path rather than a rejection, since they have done nothing wrong and cannot fix an absence. Route contradicted matches to review with the specific discrepancy shown, because a recent move and an impersonation look different once the detail is visible. Report the proportion of failures in each category, which nobody currently produces and which will reveal how much of the rejection rate is coverage rather than risk. Break it down by applicant age, tenure and geography, as the pattern will be stark and is the basis for fixing it. Tell the customer which failures are theirs to decide policy on, since many would accept a thin-file applicant with a document check and are not given the option. Show the applicant what would help, because a person told they need a different document can act and a person told they failed cannot. Time-bound stale records rather than treating an old address as a contradiction. Track how many no-record applicants succeed on an alternative path, which measures whether the rejection was ever justified. And feed the categories into the coverage reporting, since that is where the systemic fix lives.

## Who Feels the Pain
Young and newly arrived applicants rejected for absence rather than risk; people who recently moved treated as impostors; customers whose rejection rate is mostly coverage; and reviewers given no detail to work with.

## Impact If Fixed
A boolean output cannot carry the distinction between an absence and a contradiction, and nobody widened it. Separating no-record from contradicted-match sends two opposite situations down two appropriate paths using information the check already has.
