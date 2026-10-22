# A Briefed Notary and a Record of What They Saw

**Niche:** [[niches/notary-signing-services/seller-and-deed-signings/profile|Seller & Deed Signings]]
**Industry:** [[industries/notary-signing-services|Notary & Signing Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The title office may already know a seller signing is high-risk, but the notary walks in unbriefed and walks out having recorded nothing beyond an ID number.
**Tags:** #tacit-knowledge-ml #cnns #object-detection #large-language-models #evaluation-metrics #compliance #worker-facing
**Contested on:** Every serious competitor in this sub-niche is fighting to prove that the person signing the deed is the owner of record before it records and the proceeds are wired, and whoever stops impostors without delaying genuine sellers becomes the title company's approved notary.

## The Problem
Impostors pick vacant land and the property of absentee or recently deceased owners. The title office can score that risk at order open; that file-level score is analysed under Title & Settlement Offices as [[problems/title-and-settlement-offices/low-impact-2|Seller Identity Verification Built for Title]] and its [[problems/title-and-settlement-offices/ml-opportunity|seller impersonation risk model]]. What happens at the table is the notary's work, and it is not built for. The notary gets an address and a package, not the reasons the file is flagged. Then they spend about a minute on the credential, and the journal records the ID type and number, not what they noticed: a licence issued last week, a signer who could not name the cross street, a companion who answered for them, a thumbprint taken reluctantly.

## Why Nobody Has Built This
Title offices and notaries are separate businesses joined by a fee. Nobody defines what a notary should check beyond the statute or what they should record, and title offices worry about liability if they share risk flags. Notaries are paid a flat fee and will not do extra work for nothing.

## What to Build
A notary-side app with two halves. Before the signing, a short briefing from the title office's flags tells the notary what to verify and why: owner's age and mailing address, vacant land, recent ID issue, a seller who asked for their own notary. At the table, a structured capture of about a minute:
- both sides of the credential, with the barcode read and the issue date flagged;
- the portrait matched to a live face;
- the thumbprint where the state requires one;
- four prompted observations, answered in a sentence each and turned into fields by a language model: did the seller know the property, who else was present, did anyone answer for them, did they read before signing.

The record attaches to the journal entry and returns to the title file. Graded later against outcomes, it becomes the labelled data that teaches new notaries what experienced ones notice.

## Target Customer
Approved-notary panels and signing services that handle seller signings for title offices; underwriters that set approved-notary standards.

## Impact If Built
The notary arrives knowing what to look for and leaves with evidence of what they checked. That improves the rare refusals that matter and protects honest notaries when a deed is challenged.
