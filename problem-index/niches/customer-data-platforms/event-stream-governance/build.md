# A Tracking Plan Nobody Updates

**Niche:** [[niches/customer-data-platforms/event-stream-governance/profile|Event Stream Governance]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The whole system depends on product teams sending consistent events, product teams ship weekly, and the tracking plan is a spreadsheet nobody updates.
**Tags:** #data-integration #workflow-orchestration #compliance #automation #evaluation-metrics #change-point-detection #descriptive-statistics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to make the event stream a contract product teams cannot break by accident — and whoever does that removes the failure mode that silently corrupts everything downstream.

## The Problem
A dozen product teams emit events. The tracking plan describing what those events should be is a spreadsheet maintained by a data engineer who is not in any of those teams' planning meetings. A team renames an event during a refactor, another stops sending a property because the field was removed from the interface, a third starts sending the same event name with a different meaning. None of this is caught, because nothing enforces the plan at the point where the change is made. Downstream, profiles change shape, segments stop matching, journeys stop firing, and someone eventually investigates a revenue chart.

## Why Nobody Has Built This
The tracking plan lives outside the codebase, so it is documentation rather than a contract — a specification that cannot fail a build is a suggestion, and that is the whole mechanism. Product teams have no incentive to maintain instrumentation that serves someone else's system. Enforcement requires being in the development workflow, which the data platform is not. And the failures are downstream and delayed, so the causal link is weak in everyone's mind.

## What to Build
Make the plan a contract in the codebase. Define events as typed schemas held in version control alongside the application code, which is the fix and converts documentation into something a build can check. Generate the emitting code from the schema, so an event that does not match the contract cannot be sent by construction. Fail the build on a breaking change, with an explicit path to make a versioned change deliberately, which is what makes evolution possible rather than forbidden. Validate at the boundary as well, since not everything can be generated and runtime validation catches the rest. Detect semantic drift rather than only structural change, which is the fix note's subject and is invisible to type checking. Give product teams ownership of their own events with visible downstream consumers, because a team that can see who depends on an event behaves differently from one that cannot. Make the plan discoverable and current by generating it from the schemas, so the spreadsheet disappears. Version events properly, allowing old and new to coexist during a transition rather than forcing a breaking cutover. Report instrumentation coverage and health per team, which creates the accountability the arrangement currently lacks. And measure time from a breaking change to detection, because the current answer is weeks and everything downstream is corrupted throughout.

## Target Customer
Data engineering and product engineering leadership, customer data platform vendors, and the organisations whose downstream systems silently change behaviour every release.

## Impact If Built
A specification that cannot fail a build is a suggestion, which is why the tracking plan is always out of date. Schemas in version control with generated emitting code make a breaking change impossible by construction rather than detectable weeks later.
