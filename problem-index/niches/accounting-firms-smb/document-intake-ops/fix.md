# Document-to-Engagement Matching and Routing

**Niche:** [[niches/accounting-firms-smb/document-intake-ops/profile|Client Document Intake & Processing Operations]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Documents arrive without context — an email from an unknown address, a portal upload with a filename like "scan001.pdf" — and staff waste 5-10 minutes per document figuring out which client and engagement it belongs to.
**Tags:** #bert #text-classification #nlp #automation #worker-facing

## The Problem
Not every document arrives neatly labeled. A client's adult child forwards their parent's 1099 from their own email address. A business client's bookkeeper uploads payroll reports without identifying which entity they belong to (the client may have 3 LLCs). A scanned batch of mail contains documents for 5 different clients in a single PDF. Physical documents arrive with no cover letter identifying the sender. In each case, a staff member must open the document, identify it, determine which client it belongs to, and route it to the correct engagement. For a batch of 50 documents, this identification-and-routing step alone takes 30-60 minutes — time spent on pure administrative overhead before any substantive work begins.

## Why It's Still Broken
Document-to-client matching is a multi-signal problem: the system needs to check the sender's email against the client contact list, scan the document for identifying information (name, SSN last 4, EIN, address), match against active engagements, and handle ambiguity (a document could belong to the individual return or the business entity). Current tools treat upload and filing as the same step — if the client uploads to their portal folder, routing is implicit. But this only works for the 20-30% of documents that arrive through the portal with the client logged in. Everything else requires manual routing.

## What a Fix Looks Like
An intelligent routing engine that processes every inbound document through a matching pipeline: check sender identity (email, phone number) against client database, extract identifying text from the document (name, SSN/EIN fragments, employer name), score against active engagements, and auto-route with confidence. High-confidence matches (>95%) are auto-filed. Lower-confidence matches present the staff member with a ranked list of 2-3 likely clients for one-click routing. Documents that match no client are flagged as unknown for manual review. Each routing decision feeds back into the matching model.

## Who Feels the Pain
Administrative assistants and intake staff who are the first handlers of every document, spending 20-30% of their workday on document identification and routing rather than substantive processing.

## Impact If Fixed
Automates 70-80% of document routing decisions, saving 1-2 hours per day during tax season and eliminating misfiled documents that cause preparation errors downstream.
