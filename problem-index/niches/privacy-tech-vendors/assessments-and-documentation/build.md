# Build: Assessments That Track Their Own Mitigations

**Niche:** Assessments & Documentation
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Assessments triggered automatically from observed change, with every mitigation tracked to implementation and verified, so the conclusion rests on safeguards that exist.
**Tags:** #evaluation-metrics #confidence-intervals #change-point-detection #gradient-boosting #compliance #workflow-orchestration #automation #data-integration
**Contested on:** Whether an impact assessment changes what gets built, or documents a decision already taken.

## The Problem

An impact assessment concludes that the processing is acceptable given specified mitigations: data will be pseudonymised before it reaches the analytics system, retention will be limited to ninety days, access will be restricted to a named team, and the third party will be bound by a data processing agreement.

The assessment is approved and filed. The mitigations are commitments made in a document.

Nothing tracks whether any of them were implemented. The pseudonymisation may have been descoped when the deadline tightened. The retention period may never have been configured. The access restriction may exist in the assessment and not in the identity system. The agreement may still be in legal review.

So the organisation holds an approved assessment concluding that a risk is acceptable, conditional on safeguards that do not exist. In a regulatory enquiry this is a worse position than no assessment at all, because it documents that the organisation identified the risk and stated how it would be addressed.

The second failure is triggering. Assessments happen when someone initiates one. Processing that nobody flagged — a new integration, an expanded use of existing data, a new third party added through the tag manager — is never assessed, because the trigger is a human recognising that an assessment is needed.

## Why Nobody Has Built This

**Assessments are modelled as documents.** The product is a form, a workflow and a store. Mitigations are text inside the document rather than objects with owners and states, so tracking them was never possible.

**Tracking mitigations creates visible failure.** A dashboard showing that forty per cent of committed mitigations were never implemented is an accurate and unwelcome artefact.

**Automatic triggering requires observation.** Detecting that new processing has begun means watching the systems, which is the data flow observation capability the category has not built.

**Verification needs technical access.** Confirming that pseudonymisation is applied or retention is configured requires reading system state, which the privacy function does not have.

**The assessment's purpose has drifted.** It was conceived as a design instrument and is used as a compliance artefact, and a product built for the second use has no reason to track outcomes.

**Nobody is measured on mitigation implementation.** The assessment being approved is the completion event. What happens afterwards is nobody's metric.

## What to Build

**Model mitigations as tracked objects.** Each with an owner, a due date, an implementation state and a verification method — not as sentences in a document. This single change converts an assessment from a filing into a programme with follow-through.

**Verify mitigations technically where possible.** Retention configured, access restricted, pseudonymisation applied, agreement signed. Many mitigations are checkable against system state or against the contract repository, and checking them is what makes the assessment's conclusion true rather than aspirational.

**Trigger assessments from observed change.** A new third-party recipient, a new cross-border flow, a new data category appearing in a system, a new model trained on personal data. Each should raise an assessment automatically, which catches the processing nobody thought to flag.

**Reassess when the basis changes.** An assessment concluding that data stays in one region is invalid when a subprocessor changes jurisdiction. Linking assessments to the facts they depend on, and re-opening them when those facts move, is the same event-triggered pattern that fixes most of this category.

**Reuse the analysis across frameworks.** The same processing assessed under several regimes shares most of its analysis. Writing it once and rendering per framework is straightforward and nobody does it.

**Report the mitigation backlog.** Committed mitigations outstanding, by age and by assessment. This is the single most useful management artefact a privacy programme could produce and no platform generates it.

**Bring the assessment forward.** Trigger from design artefacts — a product specification, an architecture document, a new data source in a pipeline definition — so the assessment arrives while the design is still movable.

## Target Customer

Privacy programme managers and counsel, for whom the mitigation backlog is directly actionable and directly addresses their largest documented exposure.

Privacy engineering as co-buyer for the verification half, which requires their access.

The privacy platforms, for whom mitigation tracking is a modest extension of an existing product that would meaningfully change what an assessment is.

## Impact If Built

The assessment's conclusion becomes conditional on safeguards that demonstrably exist, rather than on commitments nobody followed up.

Automatic triggering from observed change catches the processing that currently escapes assessment entirely — which is, by definition, the processing nobody was thinking carefully about.

And a mitigation backlog report would surface the gap between what organisations said they would do and what they did, which is the most consequential unmeasured quantity in a privacy programme.
