# Policy Engines and Continuous Control Monitoring

**Niche:** [[niches/web-data-extraction-firms/collection-governance-record/profile|Collection Governance Record]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Compliance platforms built continuous control monitoring and policy-as-code so that a control is evidenced constantly rather than attested annually, and collection governance is a document from onboarding.
**Tags:** #compliance #automation #workflow-orchestration #evaluation-metrics #data-integration #descriptive-statistics #change-point-detection #quick-win
**Contested on:** Every serious competitor in this niche is fighting to maintain a continuous, queryable account of what is being collected, from where, under what permission and for whose purpose — and whoever does that takes the account, because it is the evidence that makes the whole business defensible.

## The Problem
Moving compliance from a periodic attestation to a continuously evidenced control is what the governance and compliance platform category did, and it works: controls are defined as code, evaluated continuously against live systems, evidence is collected automatically, and drift raises an exception. The whole apparatus is directly applicable to collection permissions, and this industry runs a legal review at onboarding and files it.

## What Already Exists
Policy-as-code engines with declarative rules and decision logging; continuous control monitoring with automated evidence collection; governance platforms mapping controls to evidence and exceptions; configuration drift detection; and audit trail infrastructure designed to be presented to a third party.

## The Customization Gap
The adaptation is to a control whose subject is somebody else's website. It requires: (1) the target's stated permissions as an external, changing input to the policy, which no compliance platform models — controls normally evaluate your own configuration, and here the rule itself moves; (2) the customer's declared purpose as a policy input, since permissibility depends on use and the platform has to carry purpose from a sales conversation into a request-time decision; (3) evaluation at request time rather than on a monitoring interval, because a collection that has become impermissible should stop rather than be flagged in the next scan; (4) evidence designed for an adversarial reader, since the audience is opposing counsel rather than an auditor and the standard is different; and (5) handling genuine legal uncertainty, because several of the relevant questions have no settled answer and a policy engine that requires a definite rule cannot express the firm's actual position — recording the reasoning and its uncertainty is the honest design.

## Target Customer
Extraction firms, their compliance functions, and the governance platform vendors for whom externally-defined controls are an unserved shape.

## Impact If Solved
Continuous control monitoring is mature and assumes the rule is yours to set. Carrying a customer's declared purpose into a request-time decision, against a target's changing stated permissions, is the adaptation — and recording uncertainty honestly is the design the unsettled law actually requires.
