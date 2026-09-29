# Regression Testing Against the Release Treadmill

**Industry:** [[saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The platform ships three major releases a year, every customisation is a candidate for breakage, and regression testing is a spreadsheet of manual scripts that gets cut when the window is tight.
**Tags:** #gradient-boosting #graph-neural-networks #large-language-models #change-point-detection #evaluation-metrics #automation #workflow-orchestration #feature-engineering

## The Problem
Enterprise SaaS platforms release on a fixed cadence and customers cannot opt out. Each release changes behaviour somewhere, and a heavily configured tenant has hundreds of automations, validation rules, integrations and interface customisations that may depend on the behaviour that changed.

Testing that is hard. The complete regression suite for a mature implementation is large; running it manually takes weeks the release window does not contain; and automating it on these platforms is genuinely awkward because the interfaces are generated, the selectors are unstable and the test data has to be constructed inside the tenant.

So most organisations test a subset chosen by judgement — the critical paths, whatever broke last time — and accept the risk on the rest. Failures arrive in production, are reported by users, and are diagnosed under pressure without certainty about whether the release caused them.

Managed services partners carry this for many customers simultaneously, which means the same release is assessed independently dozens of times by dozens of engineers looking at dozens of tenants.

## What Already Exists
Provar, Copado Robotic Testing, Testim, Tricentis and Leapwork provide test automation aimed at these platforms with varying degrees of resilience to generated interfaces. Platforms provide sandbox previews of upcoming releases and publish release notes and known-issue lists. Some vendors offer impact analysis tooling that maps release changes to tenant metadata. Partners maintain regression scripts per customer, usually in a spreadsheet or a test management tool.

## The Customisation Gap
Impact analysis is the piece that would make the problem tractable and it is generic where it needs to be specific. What a customer needs is a ranked list of which of their customisations are at risk from this particular release, derived from the dependency structure of their own configuration crossed with the specific behaviour changes in the release notes — not a general advisory.

That is computable: configuration metadata gives the dependency graph, release notes give the changed behaviours, and matching one to the other narrows a suite of eight hundred tests to the forty that matter. Nobody ships it, largely because it requires reading release notes as structured change descriptions and maintaining a dependency model of a configured tenant.

The second gap is cross-tenant learning, which only a managed services partner can do. If a release breaks a particular pattern in one customer's tenant, every other tenant with that pattern is at risk, and the partner knows which those are. Turning the first failure into a proactive check across the estate is the highest-value use of the partner's position and is currently done by an engineer remembering.

And test maintenance needs to survive the interface. Tests that break because a generated selector changed, rather than because behaviour changed, are the reason automation efforts on these platforms are abandoned.

## Impact If Solved
Release regression is a recurring, scheduled, known risk that most organisations meet with a judgement call and a spreadsheet. Configuration-aware impact analysis narrows the work to what is actually exposed; cross-tenant propagation turns one customer's production failure into a prevented failure everywhere else the partner operates, which is a capability no single customer can buy and no platform vendor provides.
