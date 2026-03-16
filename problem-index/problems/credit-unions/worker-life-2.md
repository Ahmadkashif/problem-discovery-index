# Loan Officer Manual Underwriting Documentation for Exception Loans

**Industry:** [[credit-unions|Credit Unions]]
**Type:** Worker Life Changing
**One-liner:** Loan officers spend 45-90 minutes per exception loan writing narrative justifications that explain why a non-standard approval is sound — time reclaimed when an LLM drafts the underwriting memo from structured inputs the officer already has in their head.
**Tags:** #llm #text-generation #nlp #worker-facing #compliance

## The Problem

Credit unions approve a higher proportion of non-standard loans than commercial banks — that is the point of relationship lending. But every exception to standard underwriting criteria (debt-to-income above threshold, loan-to-value above policy limit, credit score below minimum, non-traditional income documentation) requires a written underwriting exception memo that documents the compensating factors justifying approval. At a mid-size CU, 20-35% of loan applications involve at least one exception requiring narrative documentation.

A loan officer processing an exception loan spends 45-90 minutes writing the memo: describing the exception, documenting compensating factors (strong member history, collateral equity, co-signer strength, stable employment verified through deposit history), referencing policy provisions that permit the exception, and structuring the narrative to satisfy both internal loan committee review and NCUA examination requirements. The writing itself is not the hard part — the loan officer knows why the loan is sound. The hard part is translating that judgment into the specific regulatory language and structured format that compliance and examiners expect. Experienced officers have templates and phrasings they reuse; junior officers struggle for hours to produce a memo that survives committee scrutiny.

## Why It Matters to the Worker

Loan officers at CUs typically manage 15-25 active applications simultaneously. Each exception memo that takes 45-90 minutes displaces time that could be spent on member consultations, application processing, or pipeline management. The officers most affected are the best relationship lenders — the ones who see compensating factors that justify approvals other lenders would decline — because they generate the most exceptions. The documentation burden punishes exactly the judgment that makes CU lending valuable. Officers report that memo writing is the most tedious part of their week, and several cite it as the reason they process fewer applications than their capacity allows.

## What a Solution Looks Like

An LLM-powered memo drafting tool integrated with the loan origination system (MeridianLink, CU Direct). The loan officer completes structured fields: exception type, compensating factors (selected from a checklist plus free-text elaboration), relevant member history highlights, and policy reference. The model generates a draft exception memo in the CU's standard format, using regulatory-appropriate language, with proper policy citations and compensating factor analysis. The officer reviews, edits if needed, and submits. The model is fine-tuned on the CU's historical approved exception memos to match institutional voice and examiner expectations. Output is always a draft requiring officer review — the model assists documentation, not the lending decision itself.

## Impact If Solved

Reduces exception memo writing time from 45-90 minutes to 10-20 minutes of review and editing. For a loan officer handling 5-8 exception loans per week, this reclaims 3-6 hours weekly — equivalent to processing 2-4 additional loan applications. Junior officers produce examination-ready memos from their first month rather than requiring 6-12 months to develop the documentation skill. The documentation quality floor rises institution-wide, reducing NCUA examination findings related to inadequate exception documentation.
