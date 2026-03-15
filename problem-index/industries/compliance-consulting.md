# Compliance Consulting Firms

## Profile
**Category:** Legal
**Market Size:** ~$12B annually in SMB and mid-market compliance consulting in the US; GRC (Governance, Risk, Compliance) market including enterprise totals ~$50B
**Tech Maturity:** Medium — enterprise GRC platforms (RSA Archer, ServiceNow GRC, LogicGate) exist but serve large organizations; SMB and mid-market compliance consulting is largely spreadsheet-based; AI tooling is essentially absent at the consultant level
**Workforce:** Compliance consultants, risk analysts, auditors, regulatory specialists, technical writers — boutique compliance firms typically run 5-30 consultants across industry verticals (healthcare, financial services, manufacturing, food safety)

## Key Pain Themes
Compliance consulting is a labor-intensive practice where 60-70% of project cost is reading, interpreting, and documenting the alignment between a client's current practices and a regulatory standard. The three core deliverables — gap analysis, remediation roadmap, and audit evidence package — are all produced largely by hand, even when the underlying regulatory standards are stable and the gaps are structurally similar across clients in the same industry. Regulatory change monitoring is a perpetual overhead: consultants must track changes to their relevant regulatory frameworks (FDA 21 CFR Part 11, HIPAA Security Rule, SOC 2, ISO 27001, OSHA standards, PCI DSS) across federal agencies, state regulators, and international bodies, and then interpret how each change affects active client engagements. The audit evidence collection phase — gathering screenshots, logs, policies, and attestations that prove control effectiveness to an auditor — is manually coordinated across client IT, operations, HR, and legal teams, often spanning months and generating hundreds of artifacts to organize. Report writing is the final bottleneck: compliance reports follow a highly structured format but are written from scratch for each client, consuming 20-40 hours of consultant time.

## Current Tech Landscape
ServiceNow GRC, Vanta, and Drata have automated SOC 2 and ISO 27001 evidence collection for technology companies — a specific niche of compliance automation that has reached product-market fit. Vanta in particular has demonstrated that automated control monitoring and evidence collection is commercially viable. However, Vanta's model works for SaaS companies with cloud-native infrastructure and doesn't extend to manufacturing compliance (FDA, OSHA), healthcare compliance (HIPAA, CMS), or financial services compliance (FinCEN, FINRA). The consultant's role in the SMB market is precisely these harder, more manual compliance domains where automation hasn't reached.

## Problems
- [[problems/compliance-consulting/high-impact|🔴 High Impact: Automated Regulatory Change Impact Analysis and Client Notification]]
- [[problems/compliance-consulting/low-impact-1|🟡 Low Impact: Gap Analysis Report Generation from Evidence]]
- [[problems/compliance-consulting/low-impact-2|🟡 Low Impact: Audit Evidence Collection Coordination]]
- [[problems/compliance-consulting/worker-life-1|🟢 Worker Life: Regulatory Monitoring and Change Digest]]
- [[problems/compliance-consulting/worker-life-2|🟢 Worker Life: Compliance Report Writing Automation]]
- [[problems/compliance-consulting/ml-opportunity|🔵 ML Opportunities]]
- [[problems/compliance-consulting/ai-agents-platforms|🤖 AI Agents & Platforms]]
