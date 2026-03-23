# Non-QM Product Matrix Matching Engine

**Niche:** [[niches/mortgage-brokers/non-qm-specialty-brokers/profile|Non-QM & Specialty Lending Brokers]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system that takes a borrower's non-standard profile — 12-month bank statements, DSCR on an investment property, foreign national status — and instantly identifies which non-QM lenders will approve it, at what rate, with what conditions, across a matrix of 100+ lender-product combinations.
**Tags:** #gradient-boosting #ranking #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
A self-employed borrower with 12 months of bank statements showing $15K average monthly deposits, a 720 credit score, and 20% down payment needs a $600K purchase loan. The broker must determine which of 20+ non-QM lenders offers a bank statement program that accepts this profile at the best rate. Lender A requires 24 months of statements. Lender B accepts 12 months but caps LTV at 75%. Lender C accepts 12 months with 80% LTV but excludes deposits from transfers. Lender D has the best rate but requires a minimum 740 credit score. An experienced non-QM specialist navigates this matrix in 30 minutes from memory; a generalist loan officer spends 3-4 hours reading lender guidelines or submits to the wrong lender, triggering a denial and 2-3 week delay.

## Why Nobody Has Built This
Non-QM guidelines are distributed as unstructured PDFs that change weekly. Encoding them into a searchable, queryable database requires: (1) parsing lender guidelines from PDF to structured data; (2) maintaining weekly updates across 20+ lenders; (3) modeling the complex eligibility logic (conditional rules like "12-month statements accepted if FICO > 700 AND LTV < 80% AND property type != condo"); (4) handling rate sheet pricing that varies by multiple dimensions simultaneously (FICO tier x LTV tier x product type x documentation type). This is a significant data engineering challenge that no one has undertaken because the non-QM market was small until recently (it has tripled since 2020).

## What to Build
A non-QM product matching engine that: (1) accepts the borrower profile (FICO, LTV, income documentation type, property type, loan purpose, loan amount, citizenship status); (2) evaluates eligibility against every non-QM lender's guideline matrix in the broker's lender network; (3) returns a ranked list of eligible lender-product combinations with rate, terms, conditions, and estimated turn time; (4) highlights the trade-offs: "Lender B offers the best rate but requires 24-month statements; Lender C accepts 12-month statements at 0.25% higher rate." Guidelines are maintained through a combination of automated PDF parsing and manual curator review.

## Target Customer
Non-QM specialist loan officers and brokerage owners originating 10+ non-QM loans per month who currently navigate lender guidelines from memory or personal cheat sheets — and generalist brokers who avoid non-QM because the product complexity is overwhelming.

## Impact If Built
Reduces non-QM lender selection from 30-60 minutes (specialist) or 3-4 hours (generalist) to 5 minutes. Eliminates lender selection errors that cause 20-30% of non-QM submissions to be denied on guideline technicalities. Opens non-QM origination to generalist brokers who currently decline non-QM borrowers — expanding the addressable market by 2-3x.
