# Lineage: E-Signature & Document Workflow

**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** the DocuSign envelope — a server-held container of documents, recipients, signing fields and routing order, closed out by a Certificate of Completion audit trail
**Builder:** DocuSign
**Builder in vault:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Verification:** partial — see Sources

## The Problem That Came First

A signature needed the paper and the person in the same place.

A multi-party agreement — a home purchase, a loan, an employment packet — meant printing, signing, then physically moving pages between parties who were rarely together. Tom Gonser later described the process as "people running around, shoving paper into envelopes, sticking them on planes and flying them across the country for $80." Every signer added a round trip, and every round trip added days.

The law stopped being the constraint. The Uniform Law Commission promulgated the Uniform Electronic Transactions Act in 1999, and President Clinton signed the federal ESIGN Act on 30 June 2000, effective 1 October 2000. An electronic signature was now enforceable. What did not yet exist was a practical way for strangers at different companies to produce one on the same document and prove afterwards that they had.

## What Got Built

**The envelope** is DocuSign's unit of work. It holds the documents, the list of recipients, the fields each recipient must complete, the order in which they are asked, and the status of each step. When the last recipient finishes, the system generates a **Certificate of Completion** — an audit record of who signed, when, from what IP address, and the chain of custody of the document.

The architectural choice underneath is the one Gonser describes as his founding idea: "rather than moving the files around the internet, let's just keep them in a server, and have people come to the files as opposed to the other way around." Earlier digital-signature approaches passed encrypted files between parties. The envelope inverts that. The document stays in one place and each signer visits it in turn; the envelope is the paper-mail metaphor wrapped around a shared server record.

That inversion makes the audit trail cheap: every action happens on the provider's server, so the provider observes and can certify it.

## Who Built It, And Why Them

**DocuSign**, founded in 2003 by Court Lorenzini, Tom Gonser and Eric Ranft, and based at first in Seattle.

Gonser came from the transaction side. In 1998 he had founded NetUpdate, which ran online transaction management for mortgages. NetUpdate had acquired DocuTouch, a Seattle e-signature start-up that held patents on web-based digital signatures and collaboration. After the 2000 market collapse NetUpdate narrowed into mortgage origination; Lorenzini, with Gonser's support, negotiated the purchase of certain DocuTouch assets from NetUpdate and started DocuSign with them.

So the builders had seen, inside mortgage transactions, that the signature kept a digital process on paper — and held patents addressing it. Real estate was the first market because, in Gonser's words, it "has a paper problem, perhaps more so than any other industry." Sales began in 2005 when zipForm — the real-estate forms software now called zipLogix — integrated DocuSign into its virtual forms. The envelope reached agents through the forms they already used.

## What It Cost

The envelope made the signature the product, and then the billing unit. DocuSign's plans meter usage by envelopes sent. The platform is paid when an envelope is sent, whether or not it is ever completed.

It also fixed what the system observes. The envelope records status — sent, delivered, viewed, signed, completed — and nothing about why a signer stopped. It knows that step three has been waiting eleven days; it does not know that step three is on holiday, or disputes a clause. The routing order is set by the sender before sending, not negotiated afterwards.

And the envelope is agnostic about content. It carries documents without understanding them, so the terms inside every signed agreement left the system as a PDF, not as data.

## What You Still Touch

Every "please DocuSign" email is one envelope; the reminder that follows is its only response to a stall.

- [[problems/esignature-document-workflow/high-impact|🔴 Why Envelopes Stall]] — status tracked, cause unobserved
- [[problems/esignature-document-workflow/worker-life-1|🟢 Deal Desk Signature Chasing]] — a person doing what the envelope cannot
- [[problems/esignature-document-workflow/worker-life-2|🟢 Contract Administrator Metadata Entry]] — the cost of a content-agnostic container
- [[niches/esignature-document-workflow/envelope-completion-funnel/profile|Envelope Completion Funnel]]
- [[niches/esignature-document-workflow/mortgage-and-title-closing/profile|Mortgage & Title Closing]] — the first market, still the hardest closing

**Sources:** Wikipedia, *Docusign* (founding in 2003 by Lorenzini, Gonser and Ranft; NetUpdate founded 1998; DocuTouch as a Seattle e-signature start-up holding web-signature patents; Lorenzini's purchase of DocuTouch assets; first sales in 2005 via zipForm/zipLogix; Seattle-to-San Francisco headquarters move; Nasdaq IPO 27 April 2018); SaaS Mag, "Cracking Categories: Interview with Tom Gonser" (the $80 overnight-envelope quote; "keep them in a server" quote; NetUpdate's narrowing into mortgage origination after 2000); search-result summary of Gonser on real estate's "paper problem" (quote not read in its original context); Scale Venture Partners, "DocuSign: After five thousand years signing goes digital" (ESIGN in 2000; near-decade to mainstream acceptance); PandaDoc/SignWell/NCUA summaries of ESIGN (signed 30 June 2000, effective 1 October 2000) and Wikipedia, *Uniform Electronic Transactions Act* (promulgated 1999); DocuSign Support, "What is a Docusign envelope?" and eSignature REST API reference (envelope contents, routing order, Certificate of Completion). ⚠️ **Not established:** when DocuSign first used the word "envelope" for its unit, and whether envelope-based pricing dated from the 2005 launch — I found no dated source for either. The specific patents DocuTouch held were not identified.
