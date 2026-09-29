# Which Defect Actually Stopped Them

**Niche:** [[niches/digital-accessibility-firms/blocker-attribution/profile|Blocker Attribution & Evidence]]
**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The flow failed, twelve defects were encountered, and nothing says which one was the barrier.
**Tags:** #causal-inference #evaluation-metrics #compliance #confidence-intervals #descriptive-statistics #graph-theory #data-integration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to say which specific defect blocked which task, how much that matters, and in a form a product team will act on and a legal process will respect — and whoever states that takes the account.

## The Problem
A tester walks a flow and encounters a dozen problems: unlabelled controls, poor focus order, an unannounced state change, low contrast, a keyboard trap. The flow does not complete. The report lists all twelve against their criteria. It does not say which one was the barrier, which were inconveniences, and which the user worked around. The product team receives a list and no basis for choosing, and the thing that actually blocked the task is buried among things that did not.

## Why Nobody Has Built This
Reports are structured by criterion because the standard is, and the standard has no concept of a task. Severity is assigned by convention rather than by observed impact. Attribution requires the test to record where the flow stopped, which most do not. And nobody has asked for a barrier list rather than a findings list.

## What to Build
Attribute the failure and rank by consequence. Record where a flow stopped and attribute the stop to the specific defect, which is the core and is what turns twelve findings into one barrier and eleven items. Classify each finding by whether it blocked, degraded or merely irritated, which is the distinction that makes a list actionable. Estimate the affected population from the assistive technology combinations the defect appears in and the client's own user data, so severity reflects reach as well as depth. Rank the remediation list by task impact rather than by criterion, which is what a product team needs to prioritise against everything else in its backlog. Produce evidence in a form a legal process can rely on — what was tested, by whom, with what, and what happened — which is increasingly what the client is buying. Keep the criterion mapping so conformance reporting remains available alongside. Record the workaround where the user found one, since that distinguishes a barrier from a difficulty. Report the same defect's impact across several flows, as a shared component's defect blocks many tasks and looks like one finding. Present a small barrier list at the top and the full findings beneath. And state the confidence in each attribution honestly, because a mistaken attribution sends a team at the wrong defect.

## Target Customer
Accessibility firms, client accessibility and engineering leadership, legal and compliance functions, and procurement and assurance providers.

## Impact If Built
Twelve findings are reported and nothing says which one was the barrier, so the team cannot prioritise. Attributing the stop to a specific defect and ranking by task impact turns a list into a decision.
