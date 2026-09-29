# The Compliance Manager Chasing Evidence

**Industry:** [[grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Worker Life Changing
**One-liner:** Automation collects most of the evidence and the rest is obtained by asking engineers for things they consider a distraction, repeatedly, before an audit deadline.
**Tags:** #large-language-models #gradient-boosting #time-series-forecasting #change-point-detection #evaluation-metrics #worker-facing #workflow-orchestration #compliance

## The Problem
A compliance manager owns the certification programme. The platform collects what it can automatically, and the residue — the things no integration covers — falls to them: a policy that needs review and sign-off, a vendor assessment, a training completion record, a documented justification for an exception, a screenshot from a system nobody integrated, a signature from a manager on leave.

Obtaining it means asking people whose work this is not. Engineers regard compliance requests as an interruption with no product value, respond slowly, and provide the minimum. The manager has no authority over them and an audit date that does not move, so the interaction is repeated asking with escalating urgency.

Audit periods compress everything. Weeks before an assessment, the manager is chasing dozens of items across teams, several of which require someone to do a task they should have done months ago — an access review that was skipped, a risk assessment nobody ran.

And the platform surfaces findings continuously, each of which is remediation work for a team that did not ask for it. The manager is the person who converts a red item into a request, and the person who is asked why it is still red.

## Why It Matters to the Worker
This is responsibility without authority in a particularly pure form. The manager is accountable for a certification that depends entirely on work performed by people who report elsewhere and regard the request as overhead.

The relationship damage is cumulative. Being the person who asks engineers for things they do not want to do, repeatedly, makes the role unpopular in a way that is nothing to do with the individual, and compliance managers describe the social cost as the hardest part of the job.

The work is also invisible when it succeeds. A clean audit is unremarkable; a finding is a problem the manager is associated with. There is no version of the outcome that reflects well on the person.

And the framing is unhelpful. Compliance is widely regarded internally as theatre — a view the manager frequently shares privately — which makes it hard to motivate anyone, including themselves, when the evidence that any of it reduces risk does not exist.

## What a Solution Looks Like
Close the manual gaps by extending automation into them. Many residual items are manual because an integration was not built rather than because they are inherently manual, and prioritising integration work by how much chasing each unautomated item generates is a straightforward product decision nobody makes.

Predict the audit-period crunch. Which items will be outstanding at the audit date is forecastable from current state and each team's historical response time, and surfacing it two months out converts a crisis into a schedule.

Make requests self-serve and specific. A request that arrives with exactly what is needed, why, the deadline, and a one-click path to supply it, in the tool the engineer already uses, gets a different response from an email asking for a screenshot.

Route by evidence, not by team. Many requests go to a team because that is who owns the system, when the evidence exists elsewhere already — in a ticket, a log, a previous audit. Checking before asking removes a share of requests entirely.

And give the manager the risk argument. If control quality can be related to outcomes at all, even weakly, a compliance manager arguing for an access review has something better than the framework says so — which is the thing that would change how these requests are received.

## Impact If Solved
Compliance managers spend their time asking people for things, with no authority and a fixed deadline, in a function the organisation privately regards as theatre. Extending automation into the manual residue, forecasting the crunch, making requests specific and self-serve, and checking for existing evidence before asking would remove most of the chasing — and an evidence-based risk argument would change the reception of the requests that remain.
