# SOC 2 & Attestation Audit Firms

## Profile
**Category:** Trust, Safety & Security
**Market Size:** ~$3B US in SOC 2, ISO 27001 and related security attestation work, performed by specialist firms including A-LIGN, Schellman, Prescient, Johanson and Coalfire alongside the assurance practices of the large accounting firms
**Tech Maturity:** Professional methodology, industrial delivery, commodity pricing. The work follows established attestation standards with defined evidence and sampling requirements, and the market that buys it treats the output as a binary artefact — so competition has run toward speed and price, and a report from a rigorous audit and one from a permissive audit look identical to the buyer's customer.
**Workforce:** Audit associates and senior associates performing fieldwork, managers and partners signing opinions, technical specialists in cloud and application security, report writers and quality reviewers

## Key Pain Themes
The buyer of an audit is not the party relying on it. A company purchases an attestation so that its enterprise customers will buy from it, which means the purchaser's interest is a clean report obtained quickly and cheaply, while the party relying on it wants the audit to have been searching. Those interests diverge, and the market has no mechanism to price rigour because the deliverable does not express it.

The second theme is sampling. An attestation tests a sample of each control's population — a number of access reviews, a number of change tickets, a number of onboarding records — and the report states an opinion about the period. That inference is methodologically standard and it is also the point where a control can operate badly for most of the year and pass, and where the reader's understanding of what was examined and the auditor's are very different.

The third is that the system description is written by the party being audited. The scope, the boundaries and the description of the controls are the client's document, reviewed by the auditor, and an in-scope boundary drawn to exclude the awkward systems is a choice made before any testing happens.

## Current Tech Landscape
Attestation standards define the framework, the evidence expectations and the reporting format. Compliance platforms — Vanta, Drata, Secureframe — have industrialised the client side and now supply much of the evidence directly through integrations, which has compressed audit fieldwork substantially and shifted the auditor's role toward reviewing platform output. Audit management software handles workpapers and workflow. Sampling methodology follows professional guidance. Peer review and oversight regimes govern the profession with varying reach over security attestation specifically.

## Problems
- [[problems/soc2-audit-firms/high-impact|🔴 High Impact: The Report Cannot Tell a Searching Audit From a Permissive One]]
- [[problems/soc2-audit-firms/low-impact-1|🟡 Low Impact: Sampling When the Population Is Available in Full]]
- [[problems/soc2-audit-firms/low-impact-2|🟡 Low Impact: Scope and the Client's Own System Description]]
- [[problems/soc2-audit-firms/worker-life-1|🟢 Worker Life: The Associate in Busy Season]]
- [[problems/soc2-audit-firms/worker-life-2|🟢 Worker Life: The Auditor Who Found Something]]
- [[problems/soc2-audit-firms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/soc2-audit-firms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
This is an assurance market with the classic structure: the party paying selects the auditor, the party relying cannot observe quality, and the output is binary. The result is price and speed competition and a report whose informational content is thin. What is unusual here, and what makes it addressable, is that the evidence has moved. Compliance platforms now hold continuous, complete control populations for most clients, which means the methodological compromise that sampling exists to resolve has largely dissolved — an auditor could test the full population of access reviews or change tickets rather than twenty-five of them. A firm that did so, and said so in a form the reader could evaluate, would be selling something the current report cannot express.
