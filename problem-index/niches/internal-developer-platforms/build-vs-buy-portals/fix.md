# The Owner Field That Names Somebody Who Left

**Niche:** [[niches/internal-developer-platforms/build-vs-buy-portals/profile|Portals & Catalogues]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The catalogue's most consulted field is ownership, it is the field that goes stale fastest, and nothing checks it against the directory that would reveal it in a second.
**Tags:** #descriptive-statistics #graph-theory #logistic-regression #evaluation-metrics #confidence-intervals #quick-win #data-integration #automation
**Contested on:** Every serious competitor here is fighting to give an organisation a portal and catalogue that stays accurate without a team operating it — and whoever does that takes the decision, because operational cost and catalogue accuracy are the two reasons these deployments fail.

## The Problem
The most common reason anybody opens the service catalogue is to find out who owns something. The owner field is populated by whoever created the entry and is updated when somebody remembers. People leave, teams reorganise, services transfer, and the field does not change. A developer trying to report a problem contacts a team that no longer exists or a person who left last year, which is worse than an empty field because it produces a confident wrong answer. The directory system knows that person has left, and nothing has ever asked it.

## Why It's Still Broken
The catalogue's fields are free text or loosely typed identifiers, and validating them against a directory requires an integration nobody prioritised. Ownership changes are organisational events that happen outside the platform's view and produce no trigger. The staleness is invisible because a wrong owner renders identically to a right one. And nobody measures how often the field is wrong, so the scale of the problem is unknown to the team maintaining the catalogue.

## What a Fix Looks Like
Validate continuously against the systems that know. Check every owner reference against the directory and flag or correct those naming departed people and dissolved teams, which is a daily job against an interface every organisation has and removes the worst class of wrongness immediately. Infer the likely current owner from commit activity, deployment identity and on-call rotation, and propose it rather than leaving the field wrong. Show the field's age and its evidence, so a reader can weigh it — a field validated yesterday against the directory is different from one typed in 2022. Reconcile at organisational events, since a reorganisation invalidates many entries at once and is knowable from the directory. Report the catalogue's own accuracy — proportion of fields validated, proportion stale, proportion unresolvable — which is a quality metric for the catalogue that nobody currently has and which is the honest measure of whether the portal can be trusted. And make correcting a field trivially easy from the place the reader discovers it is wrong, since the person who found the error is the cheapest possible corrector and is currently offered nothing.

## Who Feels the Pain
Developers contacting people who left; teams receiving reports about services they no longer own; and platform teams whose portal is distrusted because of one field.

## Impact If Fixed
Directory validation is a daily job against an interface every organisation has and eliminates the most damaging class of staleness. Showing field age and evidence preserves trust in the remainder, and the catalogue accuracy metric is the number that would let a platform team manage it at all.
