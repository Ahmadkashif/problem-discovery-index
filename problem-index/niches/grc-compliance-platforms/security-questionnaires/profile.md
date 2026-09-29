# Security Questionnaires

**Parent Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Category:** Low Digitized
**Contested on:** Whether a certificate substitutes for answering three hundred questions, or whether every enterprise buyer sends their own regardless.

## Profile

**Market Size:** ~$900M
**Share of Parent Industry:** ~10%
**Digital Adoption:** Low — answer libraries and copy-paste
**Target Buyer:** Sales engineering, compliance, security leadership
**Automation Potential:** Very high — it is retrieval over a stable answer corpus

## What Makes This a Distinct Niche

Every enterprise customer sends a security questionnaire. Three hundred questions, in the buyer's own spreadsheet, asking things the SOC 2 report already covers, in the buyer's own wording, to be answered by the vendor's compliance or sales engineering function inside a sales cycle.

The certificate was supposed to prevent this. It did not. Buyers send questionnaires anyway, because the certificate does not answer their specific questions, because their vendor risk process requires a completed questionnaire artefact, and because the person sending it is following a procedure rather than making a judgement about sufficiency.

The contest is over whether that ever changes. On the answering side, the work is real and recurring — a growing company may complete hundreds a year, each one a sales blocker with a deadline. On the asking side, the recipient of the completed questionnaire frequently does very little with it beyond filing it, which is the uncomfortable fact underneath the whole practice.

It is a distinct market because the buyer is sales engineering rather than compliance, the deadline is a deal rather than an audit, and the work is retrieval and adaptation over an answer corpus rather than evidence collection.

## Current Tools & Gaps

Answer libraries maintained in a spreadsheet or a dedicated tool. Trust centres publishing standard documentation. Questionnaire automation products that suggest answers from a library. Standardised questionnaires — CAIQ, SIG, VSA — intended to reduce variation and adopted partially. Platform trust pages that pre-answer common questions.

The gaps sit at the joins. Answers are maintained by hand and go stale, so a library confidently supplies an answer that was true last year. Nothing links an answer to the underlying control state, so the questionnaire response and the platform's own evidence can disagree. Question matching is lexical, so the same question phrased differently is not recognised. Nothing tracks which answers triggered follow-up or blocked a deal, which is the feedback that would improve the library. And on the asking side, nothing measures whether questionnaire responses predict anything at all about a supplier.

## Problems

- [[niches/grc-compliance-platforms/security-questionnaires/build|🔨 Build: Answers Bound to Control State]]
- [[niches/grc-compliance-platforms/security-questionnaires/buy|🛒 Buy: Proposal Automation for a Compliance Corpus]]
- [[niches/grc-compliance-platforms/security-questionnaires/fix|🔧 Fix: Nobody Reads the Completed Questionnaire]]
