# Buy: Policy as Code From Infrastructure

**Niche:** Policy Configuration & Deployment
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Infrastructure policy is written as code, tested, versioned and deployed through a pipeline, and content policy is prose translated into a configuration screen by hand.
**Tags:** #evaluation-metrics #compliance #workflow-orchestration #automation #data-integration #confidence-intervals
**Contested on:** Whether a written policy becomes a classifier configuration that faithfully implements it.

## The Problem

Infrastructure learned to express policy as code. Access rules, network policies and compliance constraints are written in a policy language, tested against example inputs, versioned alongside the systems they govern, reviewed through the same process as code, and deployed through a pipeline that runs the tests first.

The benefits are the ones this problem needs. The policy is unambiguous because it is executable. It is testable because you can assert what it should do with a given input. Changes are reviewed and versioned. And a change that breaks an existing expectation fails before deployment.

Content policy is prose. It is translated by a person into a configuration screen. It is not testable because there is no expression of what it should do with a given input. Changes are deployed without regression testing. And the policy document and the configuration drift apart with nothing detecting it.

The transfer is not literal — a content policy cannot be fully executable, because deciding whether content is harassment requires judgement a rule cannot express. The practices around it transfer completely.

## What Already Exists

Policy as code: Open Policy Agent, Rego, Conftest, Sentinel and the policy engines, with policy expressed as testable code and enforced in pipelines.

Policy testing: assertion frameworks letting a policy author state what should happen with a given input, run as part of the deployment pipeline.

Infrastructure as code: versioning, review and pipeline deployment applied to configuration generally.

Compliance as code: the emerging practice of expressing control requirements as executable checks.

Content policy: prose documents and vendor configuration screens.

## The Customization Gap

**Content decisions are not fully expressible as rules.** Whether a post is harassment requires judgement, so the policy cannot be code in the way an access rule can. The testing and versioning practices transfer entirely and the executable expression does not.

**The test suite is the transferable artefact.** Policy-as-code's core insight is that a policy you can test against examples is a policy whose behaviour you know. A content policy test suite — examples with intended outcomes — is exactly that and is achievable.

**Versioning together is straightforward and absent.** Policy documents and classifier configuration are versioned in different systems on different cadences with no reference between them.

**Pipeline deployment has no equivalent.** Configuration changes are made in a vendor interface without a test gate, where infrastructure policy changes cannot deploy without passing tests.

**Review is not shared.** Infrastructure policy changes are reviewed by the people who own the systems. Content configuration changes are frequently made by one person without the policy team seeing them.

**The drift is undetectable.** Infrastructure policy code and its enforcement are the same artefact. Content policy and configuration are separate, so drift is invisible by construction unless tested.

## Target Customer

Platform policy and trust and safety engineering, who own the two artefacts and have no mechanism connecting them.

Vendors, for whom test-gated configuration deployment and policy version referencing are product features that would differentiate in a category competing on model claims.

Policy-as-code vendors, for whom the testing and pipeline patterns are their core offering and content policy configuration is an adjacent application with no incumbent.

## Impact If Solved

The practices that made infrastructure policy reliable — test, version, review, gate — transfer completely even though the executable expression does not.

A policy test suite is the transferable artefact and the one that would immediately reveal the gap between what a platform's policy says and what its system does.

And gating configuration changes on the test suite would prevent the specific failure where a policy update is deployed as a configuration change that does not implement it, which is currently undetectable.
