# Spreading the Small Business Borrower's Tax Returns

**Industry:** [[community-banks|Community Banks]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Document extraction is a solved category, but a community bank borrower arrives as a web of S corporations, partnerships, a holding LLC and two guarantors' personal returns, and the global cash flow that ties them together is still rebuilt in Excel for every request and every annual review.
**Tags:** #large-language-models #transformers #graph-theory #feature-engineering #evaluation-metrics #automation #data-integration

## The Problem
A typical small business credit request at a community bank comes with three years of business tax returns (Form 1120-S or 1065 with every schedule), the owners' personal returns (Form 1040 with Schedules C, E and K-1s from every entity they touch), a personal financial statement, interim financials if they exist, and a rent roll if real estate is involved. A credit analyst keys the returns into a spreading tool line by line, then builds the global cash flow: each entity's cash available for debt service, the distributions that flow from one entity to the owner and back into another, the owner's personal obligations, and the combined debt service coverage ratio that the credit policy tests. A borrower with five entities and two guarantors can take most of a day, and the same work repeats at annual review when the new returns arrive. Abrigo's own lender survey found nearly half of institutions keyed credit memo data manually and nearly a third took five to seven weeks to close a commercial loan.

## What Already Exists
Spreading modules in Abrigo (Sageworks), Moody's lending tools, nCino and Baker Hill handle financial statement input and ratio calculation; several now offer OCR or AI-assisted extraction of tax return line items. General document-AI platforms read IRS forms reliably, and tax return transcript services supply verified figures from the IRS.

## The Customisation Gap
The extraction is not the hard part; the structure is. The bank-specific logic is: recognising which K-1 on the guarantor's return belongs to which entity in the request; tracing distributions and intercompany rents so cash is not counted twice in the global cash flow; applying the bank's own credit policy adjustments (which add-backs are allowed, how depreciation on a related-party building is treated, which living expense assumption applies); handling the entities that file on extension so the analyst is mixing tax years; and carrying the borrower's structure forward so next year's annual review starts from last year's map rather than a blank spread. Each bank's policy differs, and the spreading tools treat each entity as a separate statement rather than as a node in a borrower's family of companies.

## Impact If Solved
An entity-aware spread that assembles the global cash flow from the returns as filed, flags the double counts and the policy exceptions, and carries the structure into next year would turn most of an analyst's day per complex borrower into an hour of review, and would cut the five-to-seven-week close times that send small business borrowers to faster lenders.
