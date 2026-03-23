# Weekly Lender Guideline Change Tracking

**Niche:** [[niches/mortgage-brokers/non-qm-specialty-brokers/profile|Non-QM & Specialty Lending Brokers]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Non-QM lender guidelines change weekly — a product that was available last week may have been suspended, a credit score minimum may have shifted, or a new property type restriction may have been added — and brokers discover the change only when their submission is denied.
**Tags:** #nlp #text-classification #automation #compliance

## The Problem
Non-QM wholesale lenders issue guideline bulletins weekly — sometimes daily — via email. A broker working with 15 non-QM lenders receives 30-50 guideline update emails per week. Each email may contain minor pricing adjustments or major program changes (a lender suspends DSCR loans under $150K, or changes the minimum credit score for bank statement programs from 680 to 700). The broker can't read every update in real time. They submit a loan based on last week's guidelines and get a denial because the lender changed a critical overlay on Tuesday. The submission, denial, and re-submission cycle costs 2-3 weeks and may kill the deal.

## Why It's Still Broken
Guideline changes are communicated as unstructured text in emails — sometimes as PDF attachments, sometimes as inline text, sometimes buried in a weekly digest with 20 other items. No tool parses these communications, extracts the specific parameter changes, and updates a structured guideline database. Brokers who maintain personal cheat sheets of lender guidelines can't keep them current across 15-20 lenders with weekly changes. The lenders themselves don't provide structured, machine-readable guideline feeds — they email PDFs.

## What a Fix Looks Like
A guideline change monitoring system that: (1) ingests lender guideline update emails (automatically forwarded from the broker's inbox or pulled from lender portals); (2) uses NLP to extract specific parameter changes (credit score minimum changed, LTV limit adjusted, program suspended, new property type restriction); (3) displays a change log showing what changed, when, and for which lender; (4) alerts the broker when a change affects a loan currently in their pipeline ("Lender X increased minimum FICO for bank statement programs to 700 — your file #2341 has a 695 FICO and is pending submission to this lender"); (5) maintains a current-state guideline comparison table across all lenders.

## Who Feels the Pain
Non-QM loan officers who submit loans to lenders based on outdated guidelines and receive avoidable denials, and processors who must re-analyze files for alternative lenders when a guideline change invalidates the initial submission.

## Impact If Fixed
Eliminates 15-25% of non-QM submission denials caused by guideline changes the broker wasn't aware of. Saves 1-2 hours per week per loan officer currently spent reading lender update emails. Protects deals that would otherwise fail due to the 2-3 week delay from submission-denial-resubmission cycles triggered by undetected guideline changes.
