# Commercial Submission Intake

**Parent Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Category:** High Market Share
**Contested on:** Every serious competitor in submission intake is fighting to turn a broker's email attachments into a structured, triaged submission and rank it by the probability it will be quoted and bound — and whoever raises quote-to-submission ratio most takes the account.

## Profile
**Market Size:** ~$2.4B US submission ingestion, underwriting workbench and distribution technology
**Share of Parent Industry:** ~15% of insurtech revenue and the category's most active area
**Digital Adoption:** Medium — the product category is real and adoption is partial
**Target Buyer:** Underwriting operations and distribution leaders at carriers, MGAs and wholesale brokers
**Automation Potential:** Very High — extraction and triage are both well-posed on abundant labelled data

## What Makes This a Distinct Niche
Commercial insurance submissions arrive as email. A broker attaches an ACORD application, a loss run from the expiring carrier in whatever format that carrier produces, a schedule of vehicles or locations in a spreadsheet, sometimes a supplemental questionnaire, and writes a paragraph explaining the account. An underwriting assistant reads all of it and retypes it into the policy system. Only then can an underwriter look, and by then the carrier has already spent real money on an account it will probably decline — carriers receive far more submissions than they can quote and decline most of them. The two capabilities that matter are therefore extraction, which removes the transcription, and triage, which decides where the underwriting attention goes. The second is worth more and is much less built.

## Current Tools & Gaps
Submission ingestion is a genuine product category now with real traction, handling extraction from ACORD forms, loss runs and schedules with improving accuracy. Underwriting workbenches organise the resulting submission. Data enrichment vendors supply property, vehicle and business attributes. The gaps are downstream of extraction: triage is generally rules-based on class code and premium size rather than modelled on the carrier's own history of what it quotes and binds; decline reasons are recorded inconsistently or not at all, which removes the labels that would make triage learnable; broker-level behaviour — which brokers send business this carrier writes, and which send submissions that are shopped everywhere and bound nowhere — is known informally by underwriters and modelled by nobody; and the loss run, which is the single most informative document in the submission, is extracted for its numbers rather than analysed for its pattern.

## Problems
- [[niches/insurtech-platforms/commercial-submission-intake/build|🔨 Build: Triage Ranked by Probability of Quote and Bind]]
- [[niches/insurtech-platforms/commercial-submission-intake/buy|🛒 Buy: Document Extraction Extended to the Loss Run's Meaning]]
- [[niches/insurtech-platforms/commercial-submission-intake/fix|🔧 Fix: Decline Reasons Nobody Records]]
