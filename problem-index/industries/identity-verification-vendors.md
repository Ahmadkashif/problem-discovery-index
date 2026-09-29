# Identity Verification Vendors

## Profile
**Category:** Fintech
**Market Size:** ~$6B US revenue across document verification, biometric matching, database identity resolution and orchestration
**Tech Maturity:** Strong matching, weak accounting — Socure, Jumio, Onfido, Persona, Incode, Alloy, ID.me and Prove run document classification, face matching, liveness detection and database resolution at high accuracy on the populations they measure, and publish pass rates rather than the distribution of who fails.
**Workforce:** Computer vision and identity data scientists, manual document reviewers, solutions and integration engineers, fraud and policy analysts, support staff for rejected applicants where the vendor operates one

## Key Pain Themes
The industry's defining asymmetry is that failure is silent. A person whose identity cannot be verified abandons the application and disappears. The vendor's dashboard shows a pass rate; the customer's dashboard shows a conversion rate; neither shows who was turned away or whether they were who they said they were. Because rejected applicants generate no outcome data, the false reject rate — the thing most consequential to the people on the other side of the product — is estimated rather than measured.

That would be a technical point except that the failures are not uniformly distributed. NIST's face recognition evaluations have documented demographic differentials in error rates across algorithms for years. Document verification adds its own: passports and modern licences read better than older or less standard documents, newer phones capture better images, and stable address histories resolve more reliably in database checks than the histories of people who move frequently, share housing, or have thin files. The population most likely to fail automated verification overlaps substantially with the population least able to absorb being denied a bank account.

Around it sit document and geography coverage, orchestration across multiple vendors, and a manual review function making identity judgements from photographs in under a minute.

## Current Tech Landscape
Document verification combines classification, field extraction, security feature checks and tamper detection. Face matching compares a selfie to the document portrait with liveness detection to defeat presentation and injection attacks. Database verification resolves name, address, date of birth, SSN and phone against credit header, telco and public record sources. Orchestration layers (Alloy, Persona, Sardine) route across vendors and escalate through step-up flows. Deepfake and injection attacks have moved fast enough to reshape liveness requirements. Regulatory pressure comes from BSA customer identification requirements on one side and from state biometric privacy statutes — Illinois' BIPA in particular — on the other.

## Problems
- [[problems/identity-verification-vendors/high-impact|🔴 High Impact: The False Rejects Nobody Counts]]
- [[problems/identity-verification-vendors/low-impact-1|🟡 Low Impact: Document and Geography Coverage]]
- [[problems/identity-verification-vendors/low-impact-2|🟡 Low Impact: Orchestration and Step-Up Routing]]
- [[problems/identity-verification-vendors/worker-life-1|🟢 Worker Life: The Document Reviewer Judging a Photograph]]
- [[problems/identity-verification-vendors/worker-life-2|🟢 Worker Life: The Solutions Engineer Explaining the Rejection]]
- [[problems/identity-verification-vendors/ml-opportunity|🧠 ML Opportunities]]
- [[problems/identity-verification-vendors/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These vendors are the gate to the financial system. Passing verification is a precondition for a bank account, a payment app, a loan, a marketplace listing and increasingly for a government benefit, and the decision is made in seconds by a model whose error distribution across populations is not published by anyone in the industry. The data required to publish it exists — every vendor holds document images, match scores, outcomes and retry behaviour at enormous volume — and the measurement is technically routine. What is missing is the willingness to produce a number that will be uncomfortable, and the recognition that a vendor which produces it first defines the standard everyone else is then measured against.
