# Deletion and Suppression Across a Licensed File

**Industry:** [[directory-and-list-publishers|Directory & List Publishers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Privacy platforms handle a company's own customers; a compiler has to match deletion requests against a third-party file built from thousands of sources, keep deleted people from coming back at the next compile, and push the deletion to every licensee who holds a copy.
**Tags:** #k-nearest-neighbors #large-language-models #feature-engineering #evaluation-metrics #compliance #data-integration #automation

## The Problem
From 1 August 2026, California's Delete Act requires the state's registered data brokers — over 600 of them — to pull deletion requests from the DROP platform and delete matched, non-exempt records on a rolling 45-day basis. A list compiler sits squarely in that population. It also maintains Do Not Call flags on phone records, its own internal suppression file, opt-outs collected by industry preference services, state registry obligations in several other states, and contractual suppressions owed to customers. Since California's business-to-business exemption lapsed (recalled: January 2023), work contacts in a B2B file are personal information too.

The matching is the hard part. A DROP request identifies a person by the details they supplied; the compiler's file holds that person under a variant name, a former address, a household record, or as a contact at three employers. Under-matching leaves the record live and the compiler out of compliance; over-matching deletes a different person with a similar name and quietly shrinks a sellable count. And deletion is not a one-time event: the next compile re-ingests the same carrier listings, filings and web pages, and the deleted person reappears unless the suppression survives every source refresh.

## What Already Exists
Privacy request platforms — OneTrust, Transcend, DataGrail, Ketch — orchestrate access and deletion requests across a company's own systems. Do Not Call scrubbing services and the FTC registry handle phone suppression for telemarketers. USPS licensees run NCOALink and address standardisation. Identity resolution tools from the marketing stack match people across records.

## The Customisation Gap
The generic platforms assume the requester is the company's customer and the data sits in known systems the company controls. A compiler needs: probabilistic matching of request identifiers to compiled person and household records, with match thresholds documented for a regulator; suppression keys that persist across every rebuild, so re-ingested source records are caught before publication; separation of a person's B2B contact records from consumer records, which carry different obligations; propagation of each deletion to downstream licensees and resellers under their contract terms, with confirmation tracked; and an evidence log per request showing what was matched, what was deleted, what was exempt and why, within the 45-day window. None of the request platforms models the "zombie record" problem, because their customers do not rebuild their database from outside sources every month.

## Impact If Solved
A compiler gets defensible, on-time deletion at file scale, stops re-publishing people it has already deleted, and can show a regulator its match logic — while losing fewer legitimate records to over-matching, which protects the counts it sells.
