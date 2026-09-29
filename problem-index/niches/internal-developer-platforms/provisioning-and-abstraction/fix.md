# Nobody Records What the Abstraction Could Not Express

**Niche:** [[niches/internal-developer-platforms/provisioning-and-abstraction/profile|Provisioning & Abstraction]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every time the platform cannot do what a team needs, that is a requirement, and it is recorded only when the team is patient enough to file a ticket.
**Tags:** #descriptive-statistics #k-means-clustering #bert #evaluation-metrics #confidence-intervals #quick-win #worker-facing #automation
**Contested on:** Every serious competitor here is fighting to hide infrastructure complexity in a way that does not collapse the first time a team needs something the abstraction cannot express — and whoever does that takes the platform, because the leak is what determines adoption.

## The Problem
The platform team's backlog comes from tickets. Tickets come from teams who hit a limitation, decided to wait, and wrote it up. The teams who hit the same limitation and worked around it — which is most of them, particularly under deadline — wrote nothing. The backlog therefore represents a biased sample of the platform's gaps, weighted toward the patient and the well-resourced, and the platform team builds against it believing it reflects demand. The limitations that cause teams to leave silently are, by construction, the ones least represented.

## Why It's Still Broken
The only recording mechanism is a ticket, which requires an act from somebody who is by definition busy and frustrated. Attempts that fail produce an error and nothing else. Nobody reconciles what the platform provisioned against what exists, which would reveal the departures. And the platform team experiences their backlog as demand because it is the only demand they can see, which is the same survivorship problem the constrained-network niche describes in a different industry.

## What a Fix Looks Like
Capture the attempt, not just the ticket. Log every failed attempt against the platform with what was being requested, which is the cheapest possible capture and requires no action from the developer — the error the platform already returns can be recorded with its context. Make reporting a gap a single action at the moment of failure, with the context pre-filled, since a developer who has just hit a limitation will click once and will not write a ticket. Reconcile provisioned infrastructure against actual infrastructure periodically, which finds the resources teams created outside the platform and is the strongest evidence of what is missing. Cluster the failures and the escapes semantically, so recurring needs are visible as one requirement rather than as scattered incidents. Weight by how many teams hit each gap rather than by how many complained. Close the loop by telling the teams who hit a gap when it is addressed, since the ones who worked around it will not otherwise return. And report the gap rate as a platform health metric, because a rising one indicates an abstraction falling behind the estate.

## Who Feels the Pain
Teams whose needs are invisible because they worked around them; platform teams building against a biased backlog; and organisations whose platform coverage declines while its reported adoption holds steady.

## Impact If Fixed
Logging failed attempts costs nothing and converts a biased ticket backlog into a representative one. Reconciling provisioned against actual infrastructure finds the silent departures, which are the gaps the current process structurally cannot see.
