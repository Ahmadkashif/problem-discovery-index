# Build: Severity in Context

**Niche:** The Security Engineer Receiving the Report
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A re-scoring layer that takes a report's findings and recomputes priority against the client's own architecture, data sensitivity, exposure and compensating controls.
**Tags:** #gradient-boosting #graph-neural-networks #evaluation-metrics #confidence-intervals #bayesian-inference #data-integration #automation #worker-facing
**Contested on:** Whether severity reflects what a finding means in this organisation's architecture, or a rating assigned by someone who has never seen it.

## The Problem

A penetration test severity is a judgement made from outside, with almost none of the information that determines actual risk. The tester knows the vulnerability class, the exploitability they demonstrated, and a general sense of impact. They do not know that this service sits behind an internal-only gateway, that this database holds synthetic data, that this component is scheduled for deletion, that this path is already covered by a network control, or that this apparently minor issue is on the one system that touches cardholder data.

So the report's ordering is wrong for this organisation, in both directions, and the security engineer spends their first week re-triaging eighty findings against knowledge only they have. That re-triage is the most valuable analytical work in the whole cycle and it happens in a spreadsheet, is never recorded anywhere durable, is not visible to the firm, and is redone from scratch next year by whoever holds the role then.

The information needed to do it systematically exists in the organisation's own systems — asset inventories, data classification, network topology, cloud configuration, service ownership, deployment status. None of it is joined to the findings, and the engineer does the join in their head.

## Why Nobody Has Built This

**The data is scattered and inconsistent.** Asset inventory, data classification, network topology and service ownership live in different systems at different levels of completeness, and the completeness problem is the same one that makes penetration testing necessary in the first place.

**Nobody owns the receiving side.** The testing firm's engagement ends at the report. The vulnerability management vendors serve continuous scanner output rather than periodic manual reports. The security engineer has no budget. The gap between the firm and the platform is nobody's product.

**Re-scoring implies the firm's severities are wrong.** Selling a product whose premise is that the expensive report's priorities need correcting is commercially awkward for a firm and slightly insulting to a tester, which is why it has to be framed as adding context rather than fixing errors.

**Context is partly tacit.** A significant share of what the engineer knows — this team is overloaded, this system is being replaced, this control is not actually enforced despite the documentation — is not in any system, and a model that ignores it will be confidently wrong in ways the engineer will notice immediately.

**Findings arrive as prose.** A PDF of narrative findings has to be parsed into structured objects before anything can be computed, which is a genuine obstacle and is why most organisations retype them.

## What to Build

**Ingest the report as structured findings.** Parse from the document, or ideally take a structured export from the firm's platform, producing findings as objects with class, location, evidence and the tester's stated severity.

**Join to the organisation's own context.** Asset inventory and ownership, data classification, network reachability, cloud configuration, deployment status and business criticality — whatever exists, with the gaps stated rather than assumed. Reachability in particular is the highest-value single input, because the most common severity error is a high rating on something not actually exposed.

**Recompute priority, showing the adjustment.** Present the tester's severity and the context-adjusted priority side by side, with the reason for each change. Transparency matters more than accuracy here: an engineer who can see why the score moved will trust and correct it, and one who is handed a black-box number will ignore it.

**Let the engineer override, and keep the override.** Tacit context enters as an explicit adjustment with a note, recorded durably so it survives the person and applies automatically to similar findings next year. This is the mechanism that turns one engineer's head into an organisational asset.

**Cluster findings into systemic issues.** The same weakness class across eleven services is one engineering problem, not eleven tickets. Presenting it as one root issue with instances is what makes a framework-level fix arguable, and is the difference between fixing a pattern and closing a list.

**Route to owning teams with developer-facing context.** Tickets in the team's own format, describing the fix in terms an engineer who has never read a penetration test can act on, with the reproduction and the remediation, mapped to the owner from the service catalogue.

**Send the override signal back to the firm.** Where severities were systematically adjusted, that is information the firm needs and never receives. A feedback channel would improve next year's report and is trivially cheap.

## Target Customer

Client-side application security and security engineering leadership at organisations large enough to receive several reports a year and to have a service catalogue worth joining against — which is where the triage burden becomes a named person's full-time problem.

Testing firms are a secondary channel and a good one: offering context-aware triage as a post-delivery service is a natural extension, keeps the firm engaged past handover, and produces exactly the remediation visibility described in [[niches/penetration-testing-firms/remediation-verification/profile|🎯 Remediation Verification]].

## Impact If Built

The report's ordering starts reflecting this organisation's risk rather than a generic one. Effort currently spent on findings that do not matter here gets redirected to the ones that do, which is a large reallocation of scarce engineering attention.

Clustering into systemic issues changes what gets fixed. Eleven instances closed individually leaves the cause intact; one framework fix closes the class and prevents the next eleven.

And capturing the engineer's overrides durably preserves the most valuable and most perishable knowledge in the cycle — the architectural context that currently exists only in one person's head and leaves with them.
