# Digital Forensics Firms

## Profile
**Category:** Trust, Safety & Security
**Market Size:** ~$5B US in incident response and digital forensics services, spanning breach response retainers, insurer panel work, litigation support and internal investigations
**Tech Maturity:** Exceptional practitioners working with evidence that frequently does not exist. Mandiant, Kroll, Aon's Stroz Friedberg, Unit 42, Arete, Coveware and a wide field of specialists are called into organisations mid-incident and asked to establish what happened — from logs that were not retained, endpoints that were not monitored, and cloud audit trails that were never enabled.
**Workforce:** Incident response consultants, forensic examiners, malware reverse engineers, threat hunters, engagement and crisis managers, expert witnesses and report writers

## Key Pain Themes
The question that governs everything downstream — what did the attacker actually access — is frequently unanswerable from the evidence available, and the answer determines regulatory notification, contractual obligations, litigation exposure and public statements. Firms are routinely asked to state a scope they can only bound, under a statutory clock, to clients whose lawyers want certainty and whose insurers want limits.

The second theme is that evidence quality is decided long before the incident. Whether logs were retained, whether endpoint monitoring covered the affected systems, whether cloud audit logging was enabled, and whether backups are intact determine what can be established — and the organisations that most need response are frequently the ones least prepared, so the hardest investigations have the worst evidence.

The third is that the work runs on people at their limit. Incidents arrive without notice, run continuously for weeks, and demand the most senior practitioners during the first days. Utilisation models, insurer panel obligations and a chronically scarce labour pool combine into a working pattern the field openly acknowledges is unsustainable and has not changed.

## Current Tech Landscape
Endpoint detection platforms from CrowdStrike, SentinelOne and Microsoft are the primary evidence source when deployed and are frequently deployed during the response itself. Forensic tooling from Magnet, Cellebrite and open-source suites handles acquisition and analysis. Timeline construction tools exist and require substantial manual curation. Cloud providers supply audit logs whose retention and coverage depend on configuration set long before. Ransomware negotiation and recovery has become a specialised adjacent practice. Cyber insurers structure much of the market through panel arrangements and coverage terms.

## Problems
- [[problems/digital-forensics-firms/high-impact|🔴 High Impact: Establishing What Was Accessed From Logs Nobody Kept]]
- [[problems/digital-forensics-firms/low-impact-1|🟡 Low Impact: Evidence Acquisition and Timeline Construction]]
- [[problems/digital-forensics-firms/low-impact-2|🟡 Low Impact: Attribution With Calibrated Confidence]]
- [[problems/digital-forensics-firms/worker-life-1|🟢 Worker Life: The Responder in Week Four]]
- [[problems/digital-forensics-firms/worker-life-2|🟢 Worker Life: The Examiner Building a Timeline by Hand]]
- [[problems/digital-forensics-firms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/digital-forensics-firms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
This industry accumulates, across thousands of investigations, the most detailed record anywhere of how intrusions actually unfold — initial access, movement, persistence, staging, exfiltration — with the outcomes and the evidence gaps attached. That corpus supports two things nobody has built: an honest inference layer that states what can and cannot be established from a given evidence set, with calibrated bounds rather than a narrative; and a readiness assessment that tells an organisation, before an incident, which of its logging gaps will make the notification decision unanswerable. The field's expertise is exceptional and almost entirely tacit, held by a scarce and exhausted population, and it is the same expertise the corpus would make transferable.
