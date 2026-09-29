# Threat Intelligence Vendors

## Profile
**Category:** Trust, Safety & Security
**Market Size:** ~$5B US in commercial threat intelligence — indicator feeds, finished reporting, dark web and brand monitoring, and adversary tracking — from Recorded Future, Mandiant, Flashpoint, Intel 471, ReliaQuest and the intelligence arms of the large endpoint vendors
**Tech Maturity:** Substantial collection, unmeasured product. These vendors run genuine collection operations — underground forum access, malware analysis, infrastructure tracking, incident response telemetry — and deliver indicators and finished reporting at volume. Whether any of it changed a customer's outcome is not measured by the vendor, the customer or anyone else, because the counterfactual is an incident that did not happen.
**Workforce:** Intelligence analysts and researchers, collection and source operations staff, malware and infrastructure analysts, customer-facing intelligence advisors, platform and data engineers

## Key Pain Themes
The product's value is structurally unverifiable. An indicator blocked, a report read, a warning heeded — none of these produce an observable outcome, because the success case is an attack that did not occur against a target that may never have been selected. So the category is sold on collection breadth, analyst credentials and the plausibility of the reporting, and renewed on whether the customer feels informed.

The second theme is relevance. A feed containing millions of indicators is mostly irrelevant to any particular customer, whose actual exposure depends on their technology stack, their sector, their geography and their attack surface. Vendors ship volume with coarse tagging, and the filtering work falls to a customer whose security team is already the constraint.

The third is decay and precision. Indicators age quickly — infrastructure is reassigned, domains are sinkholed, addresses are reallocated to unrelated parties — and a stale indicator produces a false positive that costs analyst time and, occasionally, blocks something legitimate. Feed precision is rarely published and is difficult for a customer to measure independently.

## Current Tech Landscape
Recorded Future and Mandiant lead the finished-intelligence tier; Intel 471 and Flashpoint specialise in underground collection; endpoint vendors bundle intelligence with telemetry from their own installed base, which is a genuine structural advantage. Structured formats — STIX and TAXII — enable exchange and are adopted unevenly. Threat intelligence platforms from Anomali, ThreatConnect and others aggregate and deduplicate feeds. Open-source and community feeds plus sector ISACs provide substantial free coverage. Adversary frameworks such as MITRE ATT&CK provide a shared vocabulary that has genuinely improved the field.

## Problems
- [[problems/threat-intelligence-vendors/high-impact|🔴 High Impact: Selling Intelligence Whose Value Cannot Be Checked]]
- [[problems/threat-intelligence-vendors/low-impact-1|🟡 Low Impact: Relevance Against the Customer's Actual Estate]]
- [[problems/threat-intelligence-vendors/low-impact-2|🟡 Low Impact: Indicator Decay and Feed Precision]]
- [[problems/threat-intelligence-vendors/worker-life-1|🟢 Worker Life: The Analyst Writing Reports Nobody Reads]]
- [[problems/threat-intelligence-vendors/worker-life-2|🟢 Worker Life: The Defender Whose Alert Queue Is Someone Else's Feed]]
- [[problems/threat-intelligence-vendors/ml-opportunity|🧠 ML Opportunities]]
- [[problems/threat-intelligence-vendors/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Threat intelligence is an assurance product with an unobservable outcome, which places it in the same structural position as penetration testing, bug bounties and compliance certification — and with the same consequence, that the market competes on volume and reputation because quality cannot be demonstrated. What distinguishes this category is that two measurable proxies are available and unused: whether an indicator ever matched anything in a customer's telemetry, and whether it matched something that turned out to be real. Vendors bundled with endpoint telemetry can compute both across a large installed base, and the resulting statement — this feed's indicators match at this rate with this precision for organisations like yours — is the closest thing to a product measurement the field can have and is published by nobody.
