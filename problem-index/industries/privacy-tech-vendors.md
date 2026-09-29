# Privacy Tech Vendors

## Profile
**Category:** Trust, Safety & Security
**Market Size:** ~$7B US in privacy management software — consent management, data subject request automation, data discovery and mapping, assessments and third-party risk — led by OneTrust, TrustArc, Securiti, BigID, Transcend, DataGrail, Didomi and Usercentrics
**Tech Maturity:** Mature workflow tooling resting on artefacts that are inaccurate by construction. These platforms run consent collection at internet scale, automate request fulfilment and generate the records regulators ask for. The foundational input — where personal data actually is, where it flows and who it reaches — is compiled by asking people, and it is out of date the week it is finished.
**Workforce:** Privacy engineers and platform staff, privacy counsel and programme managers on the customer side, consent and web integration specialists, data discovery and classification engineers, assessment and vendor risk analysts

## Key Pain Themes
Consent is the category's most visible product and its least examined. Banners are measured on acceptance rate, optimised toward it, and regulators across several jurisdictions have repeatedly found that the resulting designs do not obtain valid consent — decisions on interface patterns, on the prominence of reject options and on pre-ticked and bundled choices have been consistent enough to constitute a body of law. The vendors supply the configurable banner and the customer chooses the configuration, which distributes responsibility usefully and leaves the underlying question unmeasured: whether the person understood what they agreed to.

The second theme is that the data map is a survey artefact. Records of processing, data flow diagrams and system inventories are assembled by interviewing teams, and they diverge from reality immediately because systems are created, connected and retired continuously. Every downstream obligation — fulfilling a deletion request, assessing a transfer, responding to an incident — rests on that map.

The third is that fulfilment runs into systems that cannot do what is being asked. Deletion requires deletion capability, and a great deal of enterprise infrastructure — backups, analytics warehouses, logs, third-party processors — was not designed with it, so the workflow tool orchestrates a request that ends in an engineer writing a script.

## Current Tech Landscape
OneTrust and TrustArc hold the broad enterprise privacy management estate; Didomi, Usercentrics and Osano focus on consent; Transcend and DataGrail on request fulfilment and integrations; BigID and Securiti on discovery and classification. Consent frameworks from the advertising industry structure the adtech side and have themselves been the subject of regulatory findings. Data discovery uses pattern matching and classification across databases and object stores with varying depth. Assessment workflows are questionnaire-driven. Regulatory enforcement has been the main driver of adoption throughout.

## Problems
- [[problems/privacy-tech-vendors/high-impact|🔴 High Impact: Consent Measured on Acceptance, Never on Understanding]]
- [[problems/privacy-tech-vendors/low-impact-1|🟡 Low Impact: The Data Map Is a Survey]]
- [[problems/privacy-tech-vendors/low-impact-2|🟡 Low Impact: Knowing What Actually Leaves]]
- [[problems/privacy-tech-vendors/worker-life-1|🟢 Worker Life: The Privacy Officer Maintaining a Record That Is Wrong]]
- [[problems/privacy-tech-vendors/worker-life-2|🟢 Worker Life: The Engineer Asked to Delete From Systems That Cannot Delete]]
- [[problems/privacy-tech-vendors/ml-opportunity|🧠 ML Opportunities]]
- [[problems/privacy-tech-vendors/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
This category was built to produce the artefacts a regulator asks for, and it is very good at that. The gap is between the artefact and the reality: a consent record that satisfies an audit and may not reflect an informed choice, a processing record assembled by interview that diverges from the systems, a deletion confirmation that covers the systems someone remembered. Every one of those gaps is measurable with data the vendors could obtain — banner interaction telemetry, actual data flows observed rather than described, deletion verified rather than requested — and measuring them would replace a compliance artefact with evidence. It would also, in each case, reveal that the current artefact overstates the position, which is why the measurement has not been built.
