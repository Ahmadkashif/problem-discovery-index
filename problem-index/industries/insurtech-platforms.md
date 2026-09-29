# Insurtech Platforms

## Profile
**Category:** Vertical SaaS
**Market Size:** ~$16B US insurance core systems, agency management and distribution technology
**Tech Maturity:** High investment, slow change — Guidewire and Duck Creek run policy, billing and claims for most US carriers; Applied Systems and Vertafore run the independent agency channel; Socotra, EIS and a wave of MGA platforms compete on speed of product launch. Core replacement programmes run for years and the submission process sitting on top of them still arrives as email attachments.
**Workforce:** Implementation consultants, rate filing and product configuration analysts, integration engineers, data conversion specialists, underwriting operations staff, agency support teams

## Key Pain Themes
Commercial insurance distribution runs on unstructured submissions. A broker emails a carrier a loss run, an ACORD form, a schedule of vehicles or property in a spreadsheet, and a narrative — and an underwriting assistant retypes all of it into the policy system before an underwriter can look at it. Carriers receive far more submissions than they can quote, decline most of them, and cannot triage well because the triage requires reading. Beneath that sits the rate filing burden: every rating change must be filed and approved state by state, and translating a filed rate into working configuration is a permanent, specialised, error-prone job. Certificates of insurance consume an astonishing amount of agency labour for a document that conveys no coverage. And the two roles carrying it all — the agency service representative doing renewal remarketing, and the underwriting assistant doing intake — spend their days on transcription.

## Current Tech Landscape
Guidewire and Duck Creek dominate carrier core systems with long, expensive implementations; Socotra and EIS position on configurability. Applied Epic and Vertafore AMS360 are the agency systems of record. ACORD forms are the interchange standard and are honoured inconsistently. Submission ingestion has become a distinct product category with real traction. Rating engines are mature; the filing translation around them is not. Comparative raters serve personal lines well and commercial lines poorly. Data enrichment vendors supply property, vehicle and business attributes at quote.

## Problems
- [[problems/insurtech-platforms/high-impact|🔴 High Impact: Commercial Submission Ingestion and Triage]]
- [[problems/insurtech-platforms/low-impact-1|🟡 Low Impact: Rate Filing to Configuration Translation]]
- [[problems/insurtech-platforms/low-impact-2|🟡 Low Impact: Certificate of Insurance Issuance]]
- [[problems/insurtech-platforms/worker-life-1|🟢 Worker Life: Agency Service Rep Renewal Remarketing]]
- [[problems/insurtech-platforms/worker-life-2|🟢 Worker Life: Underwriting Assistant Transcription]]
- [[problems/insurtech-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/insurtech-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
The platform vendors sit at the junction where the industry's information actually flows and capture almost none of it as data. A carrier core system holds every submission that arrived, every one that was declined and why, every quote that was issued and whether it was bound, and every policy's subsequent loss experience. That chain — submission to decline reason to quote to bind to loss — is the empirical basis for every question underwriting leadership guesses at. It exists inside systems that were designed to administer policies and never to answer questions about them.
