# Approval-Weighted Lender Recommendation Engine

**Niche:** [[niches/mortgage-brokers/lender-submission-routing/profile|Lender Submission & Routing]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool combines wholesale rate pricing, lender overlay compliance, historical approval probability, and current turn times into a single lender recommendation ranked by expected borrower outcome — not just best rate, but best rate you'll actually get approved for.
**Tags:** #gradient-boosting #ranking #tabular-ml #tacit-knowledge-ml #revenue-impact #ai-agent

## The Problem
Rate comparison tools show the best rate, but the best rate is meaningless if the lender denies the file or takes 45 days to close. An experienced broker's value is knowing that Lender A quotes 6.25% but has a 680-credit overlay on investment properties (the borrower has 670), while Lender B at 6.375% will approve this file in 18 days with no issues. This overlay-aware, approval-probability-weighted ranking is the core tacit knowledge in mortgage brokerage — it's what separates a 5-year veteran from a new loan officer, and it's never been systematized.

## Why Nobody Has Built This
Three data problems converge: (1) rate sheets are semi-structured PDFs/emails that change daily and must be parsed continuously, (2) lender overlays are scattered across guideline documents, bulletins, and verbal communications and must be extracted and maintained, (3) approval outcome data is locked inside individual brokerages' LOS systems and lenders don't share aggregate approval rates by scenario. Building this requires solving all three data problems simultaneously and then training a model on outcome data that no single entity has comprehensively.

## What to Build
A recommendation engine that ingests the borrower scenario (credit, DTI, LTV, property type, loan amount, documentation type), queries parsed rate sheets for pricing, filters by overlay compliance, layers historical approval data from the brokerage's own submissions (and optionally aggregated data across an opt-in network), and outputs a ranked list of lenders scored by expected outcome: (rate x approval probability x expected turn time). The ranking adapts as the brokerage submits more loans and outcomes are recorded.

## Target Customer
Brokerages with 5+ loan officers and 15+ wholesale lender relationships where lender selection is currently centralized in 1-2 senior loan officers — the bottleneck that limits growth. Mid-size brokerages (200-500 loans/year) where a 15bps pricing improvement or 5% approval rate improvement has measurable P&L impact.

## Impact If Built
Reduces lender selection errors by 40-60%, cutting re-submission rates from an estimated 12-18% to 5-8%. Improves average borrower rate by 5-15bps through overlay-aware routing to the true best-fit lender. Enables junior loan officers to make lender selections at near-senior quality, removing the scaling bottleneck. At $3,500 average commission and 300 loans/year, a 10% improvement in pull-through rate adds $105K in annual revenue.
