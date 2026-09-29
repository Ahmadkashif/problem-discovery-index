# Remediation Prioritisation and Developer Workflow

**Industry:** [[digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The audit delivers four thousand findings into a backlog that already has everything else in it, with no statement of which ones actually stop anyone doing anything.
**Tags:** #gradient-boosting #graph-neural-networks #large-language-models #k-means-clustering #evaluation-metrics #compliance #automation #workflow-orchestration

## The Problem
A remediation engagement ends with a report. The client's development team receives it and has to turn it into work. The report is organised by WCAG criterion and by page; the team works in components and sprints. A single finding repeated across eight hundred pages is one component fix, and nothing in the report says so.

Prioritisation is by WCAG conformance level, which is a statement about the standard rather than about impact. A Level A violation on a page nobody visits outranks a Level AA violation in the checkout flow, and the team works the list in the order it was given.

So the backlog absorbs the report and the report ages. Six months later a rescan finds most of it outstanding, the client is frustrated, and the firm is asked why the last engagement did not fix anything. The common answer — that the findings were delivered and not acted on — is true and is also a description of a service that does not work.

## What Already Exists
Platforms from Level Access, Siteimprove, Deque and Evinced integrate findings into Jira and other trackers, and several offer component-level grouping. CI integrations catch regressions at commit time, which is the genuinely effective intervention where it is adopted. Deque and others provide remediation guidance and code examples per issue type. Design system accessibility work — accessible component libraries — is the structural fix that reduces the finding rate at source.

## The Customisation Gap
Prioritisation needs to be by blocking impact on real tasks, which requires knowing which flows matter to this client and which technology classes are affected — information that exists in the client's analytics and in the audit's own task testing, and is not currently combined.

Grouping needs to be by fix rather than by finding. Four thousand findings usually reduce to a few dozen component or template defects, and presenting the fix with its blast radius — this change resolves eleven hundred findings across the site — is what makes the work legible to a team estimating sprints.

Effort estimation is the third gap. A prioritised list without effort is only half a decision, and effort for a given fix type in a given codebase is estimable from the team's own history.

And the durable fix is upstream. Findings cluster by component, and routing them to the design system rather than to the page team is the difference between remediation and permanent improvement — plus a CI check that prevents reintroduction, which is the only mechanism that stops the rescan finding it all again.

## Impact If Solved
The gap between an audit and a remediated site is where this industry's value evaporates, and it is a workflow problem rather than an expertise problem. Impact-based prioritisation, fix-level grouping with blast radius, effort estimates and routing to the design system convert an unactionable document into a plan a development team can execute — which is the difference between a client who renews and one who concludes accessibility work does not achieve anything.
