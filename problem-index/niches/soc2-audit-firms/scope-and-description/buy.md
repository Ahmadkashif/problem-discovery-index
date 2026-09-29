# Buy: Data Flow Observation From Privacy Engineering

**Niche:** Scope & System Description
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Privacy engineering is building observed data maps from network, cloud and identity telemetry, and audit scope is still established by asking.
**Tags:** #graph-theory #evaluation-metrics #confidence-intervals #compliance #data-integration #automation #change-point-detection
**Contested on:** Whether the boundary of the audit is derived from where the data actually goes, or drawn in a document the audited party writes.

## The Problem

Establishing where data actually lives and moves, from the systems rather than from a survey, is the problem privacy engineering has been working on. Cloud security posture and data security posture products enumerate data stores and classify their contents across an estate. Attack surface management enumerates what an organisation exposes. Identity governance enumerates which third parties hold access. Data lineage traces flows through the analytics stack.

Audit scope asks the same question — what is in the system, where does the data go, which third parties are involved — and answers it with a document the client writes.

The two disciplines are addressing the same underlying fact about an organisation. One is building observation and the other is relying on assertion, and the observation is commercially available.

## What Already Exists

Data security posture management: Cyera, Sentra, Dig and the DSPM category, discovering and classifying data across cloud estates.

Cloud security posture: Wiz, Orca and Prisma, with complete cloud asset inventories and relationship mapping.

Attack surface management: external asset enumeration, which finds the systems an organisation exposes including the ones nobody registered.

Identity governance: the record of which third parties and applications hold access, described in [[industries/grc-compliance-platforms|GRC & Compliance Platforms]].

Privacy data mapping: the observed-flow work described in [[industries/privacy-tech-vendors|Privacy Tech Vendors]], which is the closest existing capability to what audit scope needs.

## The Customization Gap

**Scope asks a different question of the same data.** Privacy asks where personal data goes. Audit asks what is in the system boundary. Both are answered by the same observed estate, and nobody has pointed the observation at the audit question.

**The auditor does not have the access.** These tools run inside the client's environment with the client's credentials. An auditor would need access or would need the client to run the extraction, which is a different evidence pattern from the current one.

**Independence constrains the arrangement.** An auditor deploying tooling in the client's environment raises questions that need handling, and the workable answer is likely client-run extraction with auditor verification.

**Scope boundaries are logical, not just technical.** A system boundary is partly a business definition, so the observed estate informs rather than determines it — the value is in the comparison and the explanation, not in an automated boundary.

**Third-party enumeration is the strongest single input.** Which processors actually hold access is observable from identity data and is exactly what carve-out disclosure depends on.

**The client may not have the tooling.** Not every audited organisation runs DSPM or ASM, though most run enough cloud and identity infrastructure to support a basic derivation.

## Target Customer

DSPM and cloud posture vendors, for whom an audit-facing scope verification output is an adjacent use of what they already compute and a new buyer in the same accounts.

Audit firms, who could require a client-run extraction as part of scoping evidence, which is a request rather than an integration.

Compliance platform vendors, who already sit between the client and the auditor and could produce the observed estate as a scoping artefact.

## Impact If Solved

An observed estate is available commercially and would convert audit scope from an assertion into a comparison, which is the single largest change available in this niche.

Third-party access enumeration from identity data is the strongest input and directly addresses carve-out completeness, which is where a reader is most often misled.

And the comparison rather than the automation is the product — the observed estate informs the boundary discussion, and the value is in requiring an explanation for the difference.
