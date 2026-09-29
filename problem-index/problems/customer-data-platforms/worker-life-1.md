# The Engineer Whose Tracking Plan Nobody Reads

**Industry:** [[customer-data-platforms|Customer Data Platforms]]
**Type:** Worker Life Changing
**One-liner:** One data engineer is accountable for the consistency of an event stream produced by a dozen product teams who have no reason to care, and finds out about every change after it ships.
**Tags:** #change-point-detection #bert #large-language-models #time-series-forecasting #gradient-boosting #evaluation-metrics #worker-facing #workflow-orchestration

## The Problem
The person who owns the customer data platform inside an organisation is usually a single data engineer or a small team. They own the tracking plan, the pipeline, the identity configuration and the downstream activations, and they depend entirely on product engineering teams implementing events correctly — teams that report to different managers, have their own roadmaps, and treat analytics instrumentation as an afterthought at the end of a ticket.

The work is reactive by construction. A marketer reports that a campaign stopped working; the engineer traces it back through the audience to an event that stopped arriving after a release three weeks ago. A report shows a drop; the engineer determines whether it is real. A new product surface launches with events nobody agreed, in a naming convention nobody else uses, and now the taxonomy has a third dialect.

Requests arrive continuously and are usually urgent: add this trait, build this audience, connect this new tool, explain why these two numbers differ. Each is small; together they consume the week. The work that would reduce the inflow — governance, documentation, monitoring, actually rationalising the taxonomy — never starts.

## Why It Matters to the Worker
This is responsibility without authority, in the specific form where the dependency is on peers who have no incentive to cooperate. The engineer cannot make product teams follow a tracking plan; they can only ask, and then clean up. Over time that becomes a posture of permanent low-grade negotiation with people who find the request annoying.

The failures are attributed to them anyway. When data is wrong, the data person is asked why, and the honest answer — a team changed an event without telling anyone — sounds like blame-shifting even when it is simply what happened. Repeated often enough it damages the engineer's standing regardless of fault.

The role is also isolated. There is frequently one person who understands the whole customer data path, from a click through the identity graph into a downstream tool, and that person is a single point of failure who cannot take a holiday without something breaking. Handover is close to impossible because most of the system's real behaviour is undocumented and lives in their head.

## What a Solution Looks Like
Make the system report its own health. Per-event arrival monitoring with deployment correlation turns the three-week discovery into a same-day alert with the release identified, which removes both the loss and the archaeology. Property-level distribution monitoring catches the subtler drift.

Move the feedback to where the change happens. Dependency information — this event feeds these four audiences and two journeys — belongs in the pull request, not in a wiki. Engineers generally do not want to break things; they break them because the consequence is invisible at the moment of the change.

Make the taxonomy self-documenting. Deriving the actual event and property catalogue from what is arriving, with owners, first-seen dates, volumes and downstream dependencies, replaces a stale spreadsheet with something true. Semantic mapping proposals handle the dialects without requiring a governance victory first.

Let the requests self-serve. Most incoming requests are audience builds and "why do these numbers differ" questions, and both are answerable by a well-built interface with the definitional caveats attached, which removes the largest share of the interruption load.

## Impact If Solved
This role is a single point of failure at most organisations running a customer data platform, and it burns people out through a combination of reactive interruption and blame for other teams' changes. Self-reporting health, dependency visibility at the point of change, and a derived catalogue convert the job from firefighting into maintenance — and make the system survivable when the person who built it leaves, which is currently the largest unmanaged risk in most martech stacks.
