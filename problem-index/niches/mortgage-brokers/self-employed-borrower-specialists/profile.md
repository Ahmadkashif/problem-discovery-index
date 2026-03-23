# Self-Employed Borrower Specialists

**Parent Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Category:** Low Digitized

## Profile
**Market Size:** $60-90B in annual origination volume
**Share of Parent Industry:** ~12-18% of broker-originated volume
**Digital Adoption:** Low — income calculation for self-employed borrowers (Schedule C, K-1, 1120-S analysis) is almost entirely manual, with processors hand-calculating qualified income from 2-3 years of tax returns
**Target Buyer:** Senior loan officer / processor specializing in self-employed files
**Automation Potential:** High — tax return income analysis follows deterministic rules that vary by lender but are fully codifiable

## What Makes This a Distinct Niche
Self-employed borrowers represent the most documentation-intensive segment of mortgage origination. A W-2 borrower's income verification takes minutes; a self-employed borrower's requires analyzing 40-80 pages of tax returns across multiple schedules, entity types, and fiscal years to calculate "qualifying income" — which differs from actual income and varies by lender. Brokers who specialize in this segment develop deep expertise in add-back calculations, depreciation treatment, and entity structure interpretation that generalist brokers lack. The result is a sub-industry where experienced processors are irreplaceable bottlenecks and file turn times are 2-3x longer than conventional loans.

## Current Tools & Gaps
LOS platforms like Encompass store the data but don't calculate self-employed qualifying income — processors use spreadsheets or Fannie Mae's 1084/1088 worksheets manually. Tools like LoanBeam and Ocrolus offer some OCR-based tax return parsing, but they extract fields rather than performing the multi-step income calculation logic that varies across 30+ wholesale lenders' guidelines. No tool today maps a self-employed borrower's tax return data to lender-specific qualifying income rules automatically.

## Problems
- [[niches/mortgage-brokers/self-employed-borrower-specialists/build|🔨 Build: Automated Self-Employed Income Calculator with Lender-Specific Rules]]
- [[niches/mortgage-brokers/self-employed-borrower-specialists/buy|🛒 Buy: Tax Return OCR Adapted for Mortgage Qualifying Income]]
- [[niches/mortgage-brokers/self-employed-borrower-specialists/fix|🔧 Fix: Add-Back & Depreciation Inconsistency Across Processors]]
