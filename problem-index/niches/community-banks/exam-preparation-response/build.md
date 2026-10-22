# An Evidence Library Mapped to the Request Letter

**Niche:** [[niches/community-banks/exam-preparation-response/profile|Examination Preparation & Response]]
**Industry:** [[industries/community-banks|Community Banks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The documents an examiner asks for already exist inside the bank; nobody has indexed them against the request letter, so every exam starts with a search.
**Tags:** #large-language-models #transformers #word-embeddings #compliance #workflow-orchestration #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to have a bank's evidence for every request-letter item located, current and mapped before the letter arrives, and whoever turns the examination from a document hunt into a retrieval most completely takes the account.

## The Problem
The request letter asks for the board-approved loan policy with its approval date, the last two quarters of allowance support, the interest rate risk model validation, the vendor risk assessment for the core processor, minutes of every ALCO and loan committee since the last exam, and a hundred other items. Each was produced on schedule; finding the right version, confirming it is current and uploading it in the regulator's format takes the CFO and compliance officer most of a month.

## Why Nobody Has Built This
Request letters differ by regulator, exam type and examiner-in-charge, and are written in free text. Compliance software vendors built around risk assessments and control libraries rather than the letter. Document management tools store files without knowing what an examiner will ask for.

## What to Build
A continuously maintained library that ingests documents as they are produced (board and committee packages, policies, reports, model outputs, audit and loan review reports), classifies each against a taxonomy of exam request categories, records approval and review dates, and links each open finding to its remediation evidence. When a letter arrives, an LLM maps each item to candidate documents, flags gaps and stale versions, and assembles a numbered response package for review.

## Target Customer
CFOs, compliance officers and CEOs at community banks under $3B, where no one's full-time job is exam management.

## Impact If Built
Exam preparation drops from weeks to days, missing-document findings disappear, and the same library serves the external audit and loan review.
