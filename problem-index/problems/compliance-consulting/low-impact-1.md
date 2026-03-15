# Gap Analysis Report Generation from Client Evidence

**Industry:** [[compliance-consulting|Compliance Consulting Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic document generation tools can assemble text but can't structure a compliance gap analysis — mapping each regulatory requirement to client evidence, assigning a compliance status, and generating a risk-scored finding with remediation priority — without deep regulatory domain knowledge.
**Tags:** #llm #text-generation #nlp #automation #workflow-orchestration

## The Problem
A gap analysis is the core deliverable of most compliance engagements: for each requirement in a regulatory framework (FDA 21 CFR, HIPAA, SOC 2, ISO 27001), the consultant assesses whether the client has a conforming control in place, documents the evidence reviewed, assigns a gap status (conforming / minor gap / major gap / absent), and writes a finding description with remediation guidance. The final report maps potentially hundreds of requirements to client evidence, and the writing is highly structured but must be accurate, precise, and calibrated to the client's specific situation. Writing this report manually takes 20-40 hours of consultant time per engagement.

## What Already Exists
Document assembly tools (HotDocs, Conga) handle template generation. Vanta and Drata automate SOC 2 evidence collection and can generate compliance reports for their supported frameworks. ServiceNow GRC generates reporting from its structured control database. None of these apply to the manual compliance consulting context — they require either a SaaS-company tech infrastructure (Vanta/Drata) or enterprise GRC platform implementation (ServiceNow). A compliance consultant working with a mid-size manufacturer on FDA 21 CFR compliance has none of these infrastructure dependencies to leverage.

## The Customisation Gap
A gap analysis report generator needs: (1) a structured mapping of the regulatory framework requirements (each numbered subpart or control) to plain-language descriptions of what conforming evidence looks like; (2) an evidence classification layer that reads the evidence documents the consultant gathered and classifies each against the relevant requirement; (3) a gap scoring logic (major vs. minor based on both the requirement's criticality and the severity of the gap); (4) a finding narrative generator that produces a consistent, professional finding description with specific remediation steps. This is achievable with an LLM fine-tuned on compliance gap analysis reports, but requires regulatory-specific knowledge that varies by framework.

## Impact If Solved
Reduces gap analysis report writing from 20-40 hours to 5-8 hours of review and customization per engagement. A consulting firm completing 20 engagements per year recovers 300-700 consultant hours — equivalent to 2-4 additional engagements per year from existing headcount.
