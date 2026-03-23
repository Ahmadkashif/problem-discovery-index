# Industrial OT/ICS Security

**Parent Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSP]]
**Category:** High Market Share

## Profile
**Market Size:** $5B
**Share of Parent Industry:** 17%
**Digital Adoption:** Medium — MSSPs use specialized OT monitoring tools (Claroty, Nozomi Networks, Dragos) alongside traditional IT SIEM, but the IT/OT convergence creates alert correlation gaps that remain manually bridged.
**Target Buyer:** OT security practice directors at MSSPs, and SOC managers responsible for monitoring industrial clients (manufacturing, utilities, oil & gas, water treatment).
**Automation Potential:** Medium-High — OT alert triage follows protocol-specific patterns (Modbus, DNP3, OPC-UA anomalies), but the safety implications of false positives require human verification before response actions.

## What Makes This a Distinct Niche
Industrial OT security monitoring differs fundamentally from IT security. OT networks use proprietary protocols (Modbus, DNP3, OPC-UA, EtherNet/IP) that IT SIEM platforms cannot parse natively. Patching OT systems is dangerous — applying a security patch to a PLC controlling a chemical process could cause a safety incident. Alert response in OT cannot follow IT playbooks — you cannot "isolate and remediate" a compromised PLC that is controlling an active production line without coordinating with plant operations. MSSPs serving industrial clients need analysts who understand both cybersecurity and industrial control systems — a rare skillset commanding premium rates.

## Current Tools & Gaps
Claroty, Nozomi Networks, and Dragos provide OT-specific network monitoring and asset discovery. These tools detect anomalies in OT protocols but generate alerts that IT-trained SOC analysts cannot contextualize. Microsoft Sentinel and Splunk ingest OT alerts but cannot correlate them with IT events meaningfully (an IT phishing attack that pivots to the OT network appears as two unrelated alerts). No platform provides a unified IT/OT SOC workflow where analysts can see the full attack chain from initial IT compromise to OT impact.

## Problems
- [[niches/cybersecurity-mssp/industrial-ot-security/build|🔨 Build: IT/OT Attack Chain Correlation Engine]]
- [[niches/cybersecurity-mssp/industrial-ot-security/buy|🛒 Buy: OT-Safe Incident Response Playbooks]]
- [[niches/cybersecurity-mssp/industrial-ot-security/fix|🔧 Fix: OT Asset Inventory Staleness]]
