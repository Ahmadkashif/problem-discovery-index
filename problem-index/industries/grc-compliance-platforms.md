# GRC & Compliance Platforms

## Profile
**Category:** Trust, Safety & Security
**Market Size:** ~$9B US in governance, risk and compliance software; Vanta, Drata and Secureframe lead the automated-certification tier while AuditBoard, LogicGate, Archer, OneTrust and ServiceNow hold the enterprise risk and compliance estate
**Tech Maturity:** Integration engineering applied to a question nobody has validated. These platforms connect to cloud providers, identity systems, device managers and ticketing tools, collect evidence continuously, map it to framework controls and produce audit-ready artefacts. Whether a company with every control green is meaningfully safer than one without is an empirical question the category has never asked about itself.
**Workforce:** Integration and platform engineers, compliance and framework specialists, customer success and audit liaison staff, risk analysts, security engineers on the customer side supplying evidence

## Key Pain Themes
The product measures control implementation and is bought as an assurance signal. A SOC 2 report or an ISO certificate is used by enterprise buyers, insurers and partners as evidence of security, and the relationship between the controls a framework specifies and the incidents an organisation actually suffers has never been measured — not by the platforms, who hold the largest control-state dataset in existence, and not by the frameworks, which are consensus documents rather than empirical ones.

The second theme is that the work has moved rather than disappeared. Automated evidence collection removed a great deal of screenshotting, and the remaining burden fell on engineers: answering the questions the integrations cannot, remediating findings surfaced by the platform, and above all completing the security questionnaires that every enterprise customer sends and that no framework certificate has replaced.

The third is mapping. Organisations pursue several frameworks with substantially overlapping requirements, and reconciling them is done with crosswalk spreadsheets that are maintained by hand and go stale when a framework revises.

## Current Tech Landscape
Vanta, Drata and Secureframe automated the mid-market certification path through deep integrations with cloud, identity, endpoint and ticketing systems. Enterprise GRC from Archer, LogicGate, ServiceNow and AuditBoard handles broader risk registers, policy management and audit workflow. OneTrust and peers cover the privacy-specific side. Audit firms consume the output and perform the attestation. Trust centres and questionnaire exchanges have emerged to reduce duplicate questionnaire work and are unevenly accepted. Control frameworks themselves — SOC 2 criteria, ISO 27001, NIST — are revised on multi-year cycles by committee.

## Problems
- [[problems/grc-compliance-platforms/high-impact|🔴 High Impact: Every Control Green and Nobody Has Measured What That Buys]]
- [[problems/grc-compliance-platforms/low-impact-1|🟡 Low Impact: Mapping Between Frameworks That Overlap]]
- [[problems/grc-compliance-platforms/low-impact-2|🟡 Low Impact: Evidence Integrations and Control Drift]]
- [[problems/grc-compliance-platforms/worker-life-1|🟢 Worker Life: The Compliance Manager Chasing Evidence]]
- [[problems/grc-compliance-platforms/worker-life-2|🟢 Worker Life: The Engineer Filling In the Fortieth Questionnaire]]
- [[problems/grc-compliance-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/grc-compliance-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These platforms hold continuous control state across tens of thousands of organisations — which controls are implemented, how consistently, in what configurations, with what exceptions — and that is the only dataset in existence that could relate control implementation to security outcomes. The frameworks being certified against are consensus artefacts, written by committee, revised slowly, and never validated against incident data. A platform that joined its control corpus to breach and incident outcomes could tell the industry which controls actually matter, which is both the most valuable thing anyone could say about security compliance and commercially uncomfortable for a business that sells certification against all of them equally.
