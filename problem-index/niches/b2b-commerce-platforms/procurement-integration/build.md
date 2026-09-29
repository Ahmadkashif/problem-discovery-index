# A Decades-Old Standard That Takes Weeks

**Niche:** [[niches/b2b-commerce-platforms/procurement-integration/profile|Procurement Integration]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Punchout and electronic ordering standards have existed for decades and are supported by every platform, and connecting to each large customer's procurement system remains a per-customer project measured in weeks.
**Tags:** #data-integration #automation #workflow-orchestration #evaluation-metrics #compliance #graph-theory #descriptive-statistics #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to connect to a large customer's purchasing system in hours rather than weeks — and whoever does that takes the account, because the connection is the condition of the relationship and its cost decides which customers are worth having.

## The Problem
A new customer requires punchout from their procurement platform and electronic order transmission. Both sides support the standard. The project takes six weeks: agreeing the catalogue format and the required fields, mapping units of measure and tax codes, matching identifiers, configuring the session handshake, producing a catalogue file to their specification, testing through their environment on their schedule, and resolving the differences between what the standard says and what their platform actually does. The distributor has done this ninety times and does it substantially from scratch each time, because the variation lives in configuration nobody has catalogued.

## Why Nobody Has Built This
The integration work is billable or is absorbed as cost of acquisition, so it has a home and no urgency. Each connection feels bespoke because each customer's configuration differs, which conceals that the space of variation is small and enumerable. Specialist providers exist and have an interest in the work remaining project-shaped. And nobody has assembled the profile of each procurement platform's actual behaviour, which is the asset that would collapse the cost.

## What to Build
Turn the variation into configuration. Build a profile library per procurement platform capturing its actual behaviour — the handshake variant, the catalogue format, the required and optional fields, the identifier conventions, the confirmation expectations — since the platforms number in the dozens and the customers in the thousands, and this profile set is the asset that turns six weeks into an afternoon. Generate the customer's catalogue file automatically to their profile, rather than producing it by hand each time. Provide a self-service connection flow for the common cases, so a mid-market customer can connect without a project, which opens a segment the cost floor currently excludes. Test without the customer's schedule by simulating their platform from the profile, which removes the critical path from the project. Handle the customer-specific deltas as declarative overrides on the profile rather than as custom code. Monitor the connection continuously, which the fix note develops. Capture each new integration's learnings back into the profile, so the ninety-first connection is faster than the ninetieth. And report time-to-connect as the metric, because it determines which customers are economic and is currently unmeasured.

## Target Customer
Distributors and manufacturers, their customers' procurement teams, platform vendors, and the specialist integration providers.

## Impact If Built
The variation lives in configuration nobody has catalogued, which makes each of ninety connections feel bespoke. A profile library per procurement platform turns six weeks into an afternoon, and self-service connection opens the mid-market that the cost floor currently excludes.
