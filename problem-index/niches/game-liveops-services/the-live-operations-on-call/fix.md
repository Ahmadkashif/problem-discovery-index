# Three in the Morning on a Holiday Weekend

**Niche:** [[niches/game-liveops-services/the-live-operations-on-call/profile|The Live Operations On-Call]]
**Industry:** [[industries/game-liveops-services|Game LiveOps Services]]
**Type:** Fix (Pain Point)
**One-liner:** Something is wrong with a live event, the person on call cannot reach anyone who can authorise a fix, and the game is running in every timezone.
**Tags:** #worker-facing #quick-win #workflow-orchestration #automation #compliance #evaluation-metrics #descriptive-statistics #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to make one person responsible for a game running in every timezone on a holiday weekend into something survivable — and whoever does it takes the account.

## The Problem
The defining experience of this role: an incident that is clearly damaging, at an hour when nobody senior is reachable, requiring a decision the on-call person is not authorised to make. Acting risks blame for an economic change made unilaterally. Not acting means the damage compounds for hours. The person spends the night refreshing dashboards and messaging a chat channel that nobody is reading, and this recurs several times a year.

## Why It's Still Broken
Authority was never delegated — a responder with a pager and no decision rights can only escalate, and at three in the morning on a holiday there is nobody to escalate to. Nobody defined what may be done unilaterally. The incidents are varied enough to feel unprecedented. And the burden is invisible because it happens out of hours.

## What a Fix Looks Like
Delegate the authority before the night happens. Write down what the on-call person may do without approval, which is the fix and costs a meeting rather than a project. Define a small set of safe mitigations — disable, revert, pause — that are always permitted, since almost every incident is containable by one of them. Provide a documented reversal path for each, which is what makes pre-authorisation acceptable to leadership. Set a standing rule that containing damage is never penalised, because fear of blame is the actual blocker. Name a reachable secondary for genuinely ambiguous calls rather than a channel. Automate detection of the recurring incident types so the night starts earlier and shorter. Keep an incident log so the fifth occurrence is not treated as the first. Staff holiday and weekend coverage explicitly rather than by default assignment. Measure and report out-of-hours incident volume, as an unmeasured burden is never resourced. And review the pre-authorised list quarterly so it stays current with the game.

## Who Feels the Pain
On-call staff spending nights unable to act; players in a broken event for hours; live teams cleaning up compounded damage; and the attrition that follows in a role that requires continuity.

## Impact If Fixed
A responder with a pager and no decision rights can only escalate, and at three in the morning on a holiday there is nobody to escalate to. A written list of pre-authorised mitigations turns a night of refreshing dashboards into a contained incident.
