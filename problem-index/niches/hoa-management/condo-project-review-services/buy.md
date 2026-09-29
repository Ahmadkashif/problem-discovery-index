# Document Extraction Adapted to Association Financials

**Niche:** [[niches/hoa-management/condo-project-review-services/profile|Condominium Project Review Services]]
**Industry:** [[industries/hoa-management|HOA Management]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Association budgets are prepared by whoever the board hired, in no standard format, and the whole review depends on reading them correctly.
**Tags:** #ocr #large-language-models #named-entity-recognition #data-integration #workflow-orchestration

## The Problem
A project review runs on documents the reviewer did not design and cannot demand a format for: an operating budget, a reserve study, a balance sheet, an insurance certificate, meeting minutes, and a questionnaire. They arrive as scans, as spreadsheets exported to PDF, as photographs of paper. A 400-unit association in Florida and a 30-unit association in Illinois produce documents with nothing structurally in common.

Everything the determination depends on is buried in them. Reserve balance and annual contribution, delinquency over thirty days, owner-occupancy, single-entity ownership concentration, special assessments current and planned, deferred maintenance disclosed in minutes. Reviewers read for those numbers by hand, on a closing clock, hundreds of times a week.

## What Already Exists
Intelligent document processing is a mature market — Instabase, Hyperscience, Google Document AI, Azure Document Intelligence — and the mortgage industry is one of its largest users. Extraction from tax returns, pay stubs, and bank statements is a solved commercial problem with high accuracy.

## The Customization Gap
Mortgage document extraction was built for borrower documents, and every property that makes those tractable is absent here.

**No issuer standardization.** A W-2 has a fixed layout because one authority defines it. An association budget is whatever the management company's accountant produced, and there are thousands of them. Layout-based extraction has nothing to anchor on; the extraction has to be semantic — find the reserve contribution wherever and however it is expressed.

**The vocabulary is unsettled.** "Reserves" may mean the fund balance, the annual contribution, or the funded percentage, and different preparers use it for different things in the same document. Getting this wrong is not a formatting error; it changes the determination.

**The answer is often a derivation.** Reserve adequacy is a relationship between the study's recommendation and the budget's contribution — two documents, computed. Delinquency percentage may require deriving a denominator. Generic extraction returns fields; this needs fields plus the arithmetic that connects them, with the derivation shown.

**Minutes are unstructured and decisive.** Deferred maintenance and pending litigation frequently appear only in board meeting minutes, in prose, mentioned once. That is a reading comprehension problem over long documents, not a field extraction problem, and it is exactly the material the post-Surfside criteria made disqualifying.

**Confidence has to gate the workflow.** In borrower processing, a low-confidence extraction is reviewed. Here a wrong number produces a wrong eligibility determination on a loan that gets sold, so the system must be explicit about what it is unsure of and route those to a human — which means calibrated confidence, not a score.

## Target Customer
Head of Operations at a project review firm, or the condo review function inside a large originator. Throughput per reviewer is the entire cost structure, and document reading is where the hours go.

## Impact If Solved
Reviewer time moves from finding numbers to judging them. Turnaround improves on a product whose deadline is somebody's closing. And structured extraction is the precondition for everything else worth doing with the corpus — no longitudinal project history exists until the documents behind it are fields rather than scans.
