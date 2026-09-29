# Compliance Evidence the Pipeline Already Produces

**Niche:** [[niches/ci-cd-platforms/self-managed-enterprise-ci/profile|Self-Managed & Enterprise CI]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Change control evidence, segregation of duties and build provenance are all produced as a by-product of running a pipeline, and are assembled by hand into a spreadsheet at audit time.
**Tags:** #graph-theory #descriptive-statistics #bert #evaluation-metrics #confidence-intervals #compliance #automation #data-integration
**Contested on:** Every serious competitor here is fighting to give an organisation hosted-grade pipelines inside its own boundary — with the evidence, the hardware and the control it requires — and whoever does that takes the enterprise, because the alternative is that they keep operating it themselves.

## The Problem
An auditor asks for evidence that every production change in the last year was reviewed by someone other than its author, tested, approved and traceable to a requirement. The pipeline enforced all of this on every change and recorded it. Producing the evidence nonetheless takes a team several weeks, because the records are in four systems, the audit wants a specific format, and nobody built the export. This happens annually, and in between the same organisation adds manual approval steps because that is what the last auditor asked for.

## What Already Exists
Continuous control monitoring and compliance automation platforms; provenance attestation frameworks from the software supply chain world; evidence collection integrations in the security compliance category; policy engines; and audit logging in every CI product. The control objectives themselves are published and stable.

## The Customization Gap
The adaptation is to a delivery pipeline as the control. It requires: (1) mapping control objectives to pipeline facts explicitly — segregation of duties to the reviewer and author identities, change control to the approval record, testing to the executed suite — which is the translation nobody has written down and is the reusable asset; (2) evidence emitted continuously in a retained, tamper-evident form rather than assembled at audit time, which converts a multi-week exercise into an export; (3) coverage reporting, so the organisation knows which changes lacked which evidence before the auditor does, which is the difference between a finding and a fix; (4) accommodation of the emergency path, since every organisation has a break-glass process and pretending otherwise produces evidence that is obviously incomplete — the right treatment is to record and justify exceptions rather than to hide them; and (5) an auditor-facing presentation, since the consumer is not an engineer and evidence they cannot read will be supplemented by manual controls, which is how the manual approvals accumulated in the first place.

## Target Customer
Regulated enterprises in finance, healthcare, government and defence; CI vendors selling into them; and compliance automation vendors for whom delivery pipelines are an adjacent evidence source.

## Impact If Solved
The pipeline enforces the controls and records the evidence and nobody exports it, which turns an automated control into an annual manual exercise. The control-objective-to-pipeline-fact mapping is the reusable piece, and coverage reporting is what turns audit findings into pre-audit fixes.
