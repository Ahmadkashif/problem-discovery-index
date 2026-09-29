# The Relying Customer

**Parent Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Category:** Underserved Audience
**Contested on:** Whether the party the report exists for can extract anything from it beyond whether it is clean and current.

## Profile

**Market Size:** ~$180M
**Share of Parent Industry:** ~6%
**Digital Adoption:** Low — a PDF and a checklist
**Target Buyer:** Enterprise vendor risk teams, procurement, security leadership
**Automation Potential:** High — extraction and comparison are mechanical

## What Makes This a Distinct Niche

The report exists so that this person can decide whether to rely on a supplier. They did not commission it, did not select the auditor, could not influence the scope, and receive it as a finished document.

They process it at volume. An enterprise vendor risk function may review hundreds of reports a year, and each is fifty to a hundred pages of prose with an opinion, a system description, a control matrix, test results and exceptions. The realistic review is a scan: is it current, is it the right type, is the opinion clean, are there exceptions.

Everything that distinguishes one report from another — the scope boundary, the carve-outs, the testing depth, the complementary user entity controls the customer themselves must implement — is in prose they do not have time to extract.

So the artefact that an entire industry produces is consumed as a binary. The market's quality signal is degraded not only by the report's format but by the volume at which its reader operates, and nobody has built anything for that reader.

## Current Tools & Gaps

Vendor risk platforms that store the report as an attachment and record that it was received. Some extraction of basic fields — report type, period, auditor, opinion. Questionnaire workflow alongside. Manual review by an analyst against a checklist.

The gaps are that nothing helps the reader extract the content. Scope and exclusions are not extracted, so the analyst does not know what the report covers. Carve-outs are not surfaced. Complementary user entity controls — the things the customer must do for the supplier's controls to work — are listed in the report and almost never acted on. Exceptions are recorded without their materiality being assessed. Reports are not comparable across suppliers. And nothing tracks the same supplier's reports over time, so a narrowing scope or a new exception is invisible.

## Problems

- [[niches/soc2-audit-firms/the-relying-customer/build|🔨 Build: A Report Reader's Instrument]]
- [[niches/soc2-audit-firms/the-relying-customer/buy|🛒 Buy: Document Extraction From Contract Analysis]]
- [[niches/soc2-audit-firms/the-relying-customer/fix|🔧 Fix: Nobody Does the Complementary Controls]]
