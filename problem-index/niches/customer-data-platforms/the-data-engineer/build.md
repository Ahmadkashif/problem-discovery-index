# Accountable for Teams You Do Not Control

**Niche:** [[niches/customer-data-platforms/the-data-engineer/profile|The Data Engineer]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** One data engineer is accountable for the consistency of an event stream produced by a dozen product teams who have no reason to care, and finds out about every change after it ships.
**Tags:** #worker-facing #workflow-orchestration #data-integration #automation #evaluation-metrics #change-point-detection #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to give the one person accountable for event consistency a way to enforce it on teams they do not control — and whoever does that resolves an accountability gap the whole architecture creates.

## The Problem
The engineer maintains the tracking plan, answers every question about why a number changed, and is named when the customer data platform produces something wrong. The events come from a dozen product teams with their own roadmaps, their own definitions of done, and no metric that includes instrumentation quality. The engineer is not in their planning, not in their code review, and learns about a breaking change when an alert fires days after deployment. They ask nicely, the team apologises, and it happens again with the next team. This is not a tooling gap so much as an organisational one that tooling could largely close.

## Why Nobody Has Built This
The data platform sits organisationally downstream of product engineering with no gate, which is a structural arrangement nobody designed deliberately and everybody inherited. Tools in this category are built for the data team's own workflow, not for reaching into someone else's. Product teams' incentives genuinely do not include this. And the engineer has no authority to impose anything, so tooling that assumes authority is unusable to them.

## What to Build
Give them leverage without authority. Put the check in the product team's own workflow — in the pull request, in the build, in their own tooling — which is the fix, because a warning in the data team's dashboard reaches nobody and a failing check in a code review reaches the person making the change. Show the downstream consumers of an event in the place the change is being made, since a developer who can see that eleven audiences depend on this field usually behaves differently, and this single piece of context does more than any policy. Make the correct thing the easy thing through generated code and clear schemas, so compliance is the default path rather than an extra step. Notify before deployment rather than after, which converts a retrospective complaint into a prospective question. Attribute breaks to teams with their consequences, which creates visibility that is fairer than an escalation and more effective. Give the engineer a roadmap view of upcoming product changes affecting instrumentation, which is the information they most lack. Automate the investigation of what broke, since that work currently consumes the time they would spend preventing the next one. Provide a template for the instrumentation conversation, since this engineer is having the same conversation with a dozen teams and building the argument each time. Make instrumentation quality visible to product leadership, since that is where an incentive could be created. And measure how many changes reach production without review, because that number describes the arrangement precisely and nobody currently has it.

## Target Customer
Data engineering leadership and the engineers themselves, product engineering organisations, and platform vendors whose tooling serves only the data team.

## Impact If Built
The engineer has responsibility without authority and tooling that reaches only their own dashboard. Putting the check into the product team's pull request, with the downstream consumers shown, reaches the person making the change at the moment they can still choose differently.
