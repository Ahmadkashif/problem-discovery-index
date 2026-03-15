# Automated Document Assembly from Structured Client Intake

**Industry:** [[estate-planning|Estate Planning Law Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Document assembly tools like HotDocs and Wealth Counsel generate standard estate planning documents from templates, but the intake process that feeds them — gathering asset information, family structure, and planning objectives — is still a manual conversation requiring the attorney to translate unstructured client input into structured form fields.
**Tags:** #llm #seq2seq #nlp #automation #workflow-orchestration

## The Problem
Before documents can be assembled, the attorney must gather the client's full estate planning picture: marital status, children and their ages, current asset inventory (real property, financial accounts, retirement accounts, business interests, life insurance), named beneficiaries on non-probate assets, healthcare preferences, current incapacity concerns, and charitable intentions. This intake conversation takes 60-90 minutes and generates handwritten notes or recorded discussion that a paralegal then transcribes into the document assembly software's intake fields. The transcription step adds time, introduces transcription errors, and the intake fields often don't map cleanly to the nuanced information gathered in conversation.

## What Already Exists
Wealth Counsel, WealthDocx, and HotDocs all have questionnaire-driven document assembly engines — the attorney or paralegal fills in structured fields and the software assembles the appropriate documents. Online client questionnaires exist but are rarely used because clients find them overwhelming without attorney guidance. The gap is in the middle: a structured intake tool that guides the client through the relevant information in a conversation-like format and produces clean structured data for the document assembly engine.

## The Customisation Gap
A conversational intake tool for estate planning must handle the complexity of real family situations: blended families with children from multiple relationships, clients with business interests that may need to flow into the trust differently than personal assets, clients with out-of-state real property requiring ancillary documents, and clients with international assets or beneficiaries. The conditional logic (if the client has a business interest, ask about buy-sell agreement status; if minor children, ask about special needs concerns; if age 65+, ask about Medicaid planning awareness) is estate planning-specific and requires legal domain expertise to implement correctly. Standard form-builder tools can't encode this logic.

## Impact If Solved
Reduces intake-to-draft time from 3-5 days (intake appointment + transcription + assembly review) to same-day or next-day draft delivery. Improves intake completeness — fewer follow-up calls to gather missing information. Allows attorney to focus the intake consultation on strategy and relationship-building rather than information gathering.
