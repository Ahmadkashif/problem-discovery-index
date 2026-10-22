# Catching Package Errors Before the Courier Leaves

**Industry:** [[notary-signing-services|Notary & Signing Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Document AI can already find empty signature boxes on a scanned page; nobody has tuned it to a loan signing package, where a missed initial on page 87 or a notarial certificate dated wrong costs a redraw and sometimes the rate lock.
**Tags:** #object-detection #cnns #transformers #evaluation-metrics #feature-engineering #automation #quick-win #worker-facing

## The Problem
A purchase or refinance package runs to ~100-150 pages (estimate): the note, the deed of trust with riders, the closing disclosure, the lender's affidavits and the title company's own forms. Each borrower signs, initials and dates in dozens of places, and the notary completes several acknowledgment and jurat certificates with the venue, date, names and seal. At the end of the appointment the agent flips through the package page by page looking for blanks, then scans the pages the lender wants back. Practitioners report that a single missed initial on a deed can force a full re-sign with new documents, that some lenders will not fund until clean scanbacks arrive, and that the signing service will call it "notary error" whoever caused it.

## What Already Exists
General document AI — Azure Document Intelligence, Google Document AI, AWS Textract — detects signature regions and checkboxes, and e-signature platforms enforce completion on electronic documents. Closing platforms such as Snapdocs flag missing items when the package is digital. Signing agents use phone scanner apps and the NNA's checklists.

## The Customisation Gap
A wet-ink loan package needs logic the generic tools do not carry: which pages each lender and title company requires signed, initialled or dated, and by whom (borrower, non-borrowing spouse, trustee); rider and addendum conventions that vary by lender; date rules (the signing date versus the printed date, and the rescission dates that follow it on a refinance); and notarial certificate checks under the notary's state — venue, the signer's name exactly as signed, the commission expiry, a legible seal, and whether a certificate can be corrected after the fact, which many states do not allow. It also has to run on a phone, at the table, on a crumpled page photographed under kitchen lighting, before the signer leaves.

## Impact If Solved
A pre-departure check that reads every page against the package's own requirements would catch most redraw-causing errors while the borrower is still at the table, saving the agent an unpaid return trip and the title company a funding delay. For a signing service doing thousands of orders a month, a cut in the redraw rate is the difference between keeping and losing a title company's order flow.
