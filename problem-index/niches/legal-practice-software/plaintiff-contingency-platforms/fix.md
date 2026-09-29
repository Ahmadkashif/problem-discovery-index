# The Case Nobody Has Touched in Ninety Days

**Niche:** [[niches/legal-practice-software/plaintiff-contingency-platforms/profile|Plaintiff & Contingency Firm Platforms]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Fix (Pain Point)
**One-liner:** Every contingency firm has cases sitting still — waiting on a record request nobody chased, a client nobody reached, a lien nobody started — and the aging report shows how old they are rather than what is blocking them.
**Tags:** #change-point-detection #survival-analysis #evaluation-metrics #descriptive-statistics #workflow-orchestration #automation #worker-facing #quick-win
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A case is stalled because a medical provider has not responded to a records request sent eleven weeks ago. Nobody knows, because nothing failed — no deadline passed, no alert fired, the case simply sat. The firm's aging report lists it among two hundred other cases sorted by days open, which is the wrong sort: an old case moving steadily is fine and a young case that has not moved in six weeks is a problem. Stalled cases are pure carrying cost in a contingency practice, they push cash further out, and the ones that stall are disproportionately the ones that eventually resolve badly, because delay degrades evidence and client contact.

## Why It's Still Broken
Practice management systems model deadlines and not momentum. A deadline is an external date the system can be told about; momentum is the absence of activity, and absence has no event to fire on. Building it means defining, per matter type and stage, what ought to have happened by now — which requires the platform to have an opinion about legal work rather than merely record it, and vendors have been unwilling to hold one. The workaround is a paralegal who reviews the list, which works until the list is longer than a person.

## What a Fix Looks Like
Compute expected dwell time per stage from the firm's own history and flag the cases exceeding it, with the specific blocker named rather than a generic alert. Most blockers are identifiable from the record: an outstanding request with no response, a client with no logged contact, a lien not opened, a demand drafted and never sent. Rank by carrying cost and expected value at risk rather than by age, so the list a paralegal works on Monday morning is ordered by what it is costing the firm. Chase the mechanical ones automatically — a records request follow-up is a letter and a clock, not a judgment call — and reserve human attention for the cases where something is actually wrong.

## Who Feels the Pain
Paralegals reviewing aging reports by hand and being blamed for what the list did not surface; clients whose cases sat for a quarter; and partners whose cash flow is pushed out by delay they cannot see.

## Impact If Fixed
Firms that instrument dwell time typically find a meaningful minority of open cases stalled on a single unchased request, and clearing that backlog pulls cash forward by weeks per case. Automating records-request follow-up alone removes one of the largest blocks of low-value paralegal time in the segment, and it is the part of the fix that needs no modelling at all.
