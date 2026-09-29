# Buy: Continuous Testing From the Pipeline Vendors

**Niche:** Application Security Testing
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Application security platforms already watch every commit and every deploy, and none of them tell a penetration tester what changed since the last engagement.
**Tags:** #large-language-models #graph-theory #evaluation-metrics #transfer-learning #data-integration #workflow-orchestration #automation
**Contested on:** Whether assessment can keep pace with a codebase that ships daily, or whether a point-in-time test is obsolete before the report is written.

## The Problem

The client's engineering organisation is already thoroughly instrumented. Static analysis runs on every pull request. Dependency scanning runs continuously. Dynamic testing runs against staging. Application security posture management platforms consolidate findings across the lifecycle and map them to services and owners. The pipeline knows, in detail, what changed, when, by whom and with what risk signal.

The penetration tester arriving for the annual engagement knows none of it. They are handed a URL and credentials and start from the beginning, re-walking an application whose stable eighty per cent has not changed since the last test and whose risky twenty per cent — the new payment flow, the reworked permission model, the endpoint added last month — is indistinguishable from the rest.

So the engagement spreads effort uniformly across an application whose risk is concentrated, and the most useful available input — a diff of what has changed and where the pipeline's own signals are weakest — sits one integration away and is never used.

## What Already Exists

Application security platforms: Snyk, Semgrep, Checkmarx, Veracode, GitHub Advanced Security and GitLab's security features, running continuously in the pipeline with full repository and change history.

Posture management: Apiiro, Cycode, Legit Security, Ox Security and the ASPM category generally, which consolidate findings across the lifecycle, map code to services and owners, and — most relevantly — perform risk-based change analysis, flagging material changes to sensitive code paths. Apiiro's change-risk analysis is the closest existing capability to what a tester needs and is sold entirely to engineering teams.

Testing platforms: Cobalt, Synack, HackerOne and Bugcrowd, offering managed or crowdsourced testing with some continuous models.

API discovery: Salt, Noname, Traceable and the API gateways, which enumerate live endpoints and their traffic patterns — a far better scope input than an asset list.

## The Customization Gap

**Nothing produces a tester-facing change brief.** ASPM platforms compute change risk for engineering prioritisation. The same computation, rendered as "here is what changed since your last engagement and where your attention is worth most", would transform repeat testing and does not exist as an output.

**Tenancy again is inverted.** These are client-tenanted products. A testing firm needs scoped, time-boxed, read-only access across many clients, granted for the engagement and revoked after — which is the same access problem every advisory profession has and which no product in this category models.

**Pipeline findings are not surfaced to the tester as exclusions.** A tester should begin knowing what the client's own tooling already reports, so they do not spend time rediscovering it. This is a straightforward export and is essentially never provided, partly because neither side has thought to ask.

**The platforms do not know what they cannot see.** Static analysis has well-understood blind spots — authorisation semantics, business logic, cross-service flows. A capability map showing where the pipeline's coverage is structurally weak would be the ideal input for directing human effort, and no vendor publishes their own blind spots in an actionable form.

**No path back from manual findings into the pipeline.** A logic flaw found by a tester should become a permanent regression test. Nothing carries findings from an engagement into the client's continuous testing, so the same class returns.

**Continuous testing offerings are commercially awkward.** Retainer models exist and sit uneasily with a business built on time-boxed utilisation, which is why they are offered more than they are sold.

## Target Customer

The ASPM vendors — Apiiro, Cycode, Legit — are the most credible adapters. Change-risk analysis is already their core capability and a tester-facing brief is a new output for an audience they do not serve, opening a channel into every organisation their customers hire testers from.

The testing platforms are the alternative route, closer to the buyer and needing the pipeline integration built.

Buyers are application security firms and, jointly, the application security leaders who commission them and would like their expensive manual engagement pointed at the right twenty per cent.

## Impact If Solved

Repeat engagements stop re-walking stable code. Concentrating manual effort on what changed is the single largest efficiency gain available in this service line and requires only information the client already has.

Handing the tester the pipeline's existing findings at the start removes the duplication that currently makes manual testing look expensive relative to what it uniquely provides.

And routing manual findings back into the pipeline as regression tests is what would finally stop the annual rediscovery described in [[niches/penetration-testing-firms/remediation-verification/profile|🎯 Remediation Verification]].
