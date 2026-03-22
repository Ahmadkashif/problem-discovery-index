# Audit Readiness & Evidence Automation

**Parent Industry:** [[industries/compliance-consulting|Compliance Consulting]]
**Category:** Highly Automatable

## Profile
**Market Size:** $0.5-1B (embedded across all compliance consulting engagements)
**Share of Parent Industry:** Touches all niches — audit preparation and evidence collection is 60-70% of project labor across compliance domains
**Digital Adoption:** Low-Medium — Vanta and Drata have automated evidence collection for SOC2/ISO from cloud infrastructure, but no equivalent exists for HIPAA, FDA, OSHA, EPA, or state-specific compliance frameworks
**Target Buyer:** Audit preparation consultant or evidence collection specialist working across healthcare, environmental, financial, or general compliance engagements
**Automation Potential:** Very High — evidence collection follows predictable patterns per compliance framework; the same document types are requested for every audit of a given type; and many source systems (cloud providers, HR platforms, ticketing systems) have APIs that can be used for automated evidence pulls

## What Makes This a Distinct Niche
Audit readiness is the operational core of compliance consulting — the work that consumes the most hours and generates the most billable revenue but is also the most tedious and least strategic. Regardless of the compliance domain, the workflow is the same: (1) identify what evidence the auditor will request based on the compliance framework, (2) locate that evidence in the client's systems, (3) extract it in a format the auditor can review, (4) organize it according to the audit program structure, and (5) present it with supporting documentation. For a HIPAA audit, the evidence includes access logs, training records, policy documents, risk assessments, and breach notification records. For an environmental audit, it includes permit documentation, monitoring records, emissions calculations, and waste manifests. For a financial compliance audit, it includes transaction records, internal control documentation, and board meeting minutes. The evidence lives in different systems for each compliance domain, but the collection and organization workflow is structurally identical. Vanta has proven that automated evidence collection works brilliantly for SOC2/ISO — it pulls access logs from AWS, reviews configurations in Okta, verifies encryption settings, and presents a live compliance dashboard. But Vanta only covers SOC2, ISO 27001, and limited HIPAA — it doesn't connect to EHR systems, environmental monitoring equipment, financial core banking systems, or the dozens of other source systems that hold compliance evidence for non-tech industries.

## Current Tools & Gaps
Vanta and Drata automate SOC2/ISO evidence collection from cloud infrastructure and SaaS tools. Anecdotes and Hyperproof provide GRC platforms with evidence management but require manual upload. AuditBoard serves enterprise internal audit teams. ZenGRC (Reciprocity) offers a risk and compliance platform with some evidence management. None extend automated evidence collection beyond IT infrastructure to healthcare, environmental, financial, or general workplace compliance. The gap is applying Vanta's automation philosophy — API-based continuous evidence collection with automated control testing — to compliance domains beyond SOC2/ISO.

## Problems
- [[niches/compliance-consulting/audit-readiness-automation/build|🔨 Build: Automated Evidence Collection Agent for Multi-Framework Compliance]]
- [[niches/compliance-consulting/audit-readiness-automation/buy|🛒 Buy: Multi-Framework Evidence Collection by Extending Vanta's Architecture]]
- [[niches/compliance-consulting/audit-readiness-automation/fix|🔧 Fix: Evidence Staleness and Continuous Monitoring Gap]]
