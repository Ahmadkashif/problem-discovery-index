# Government Loan Scenario Pre-Qualification Engine

**Niche:** [[niches/mortgage-brokers/fha-va-government-brokers/profile|FHA/VA Government Lending Brokers]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool lets a broker input a borrower scenario and instantly see FHA vs. VA vs. USDA eligibility, program-specific costs (MIP, funding fee), and which wholesale lenders will accept the file — before pulling credit or submitting to AUS.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #automation #compliance #revenue-impact

## The Problem
Government loan programs have overlapping but distinct eligibility rules — a borrower might qualify for FHA but not VA (no service record), or qualify for VA but get better terms through FHA (lower funding fee due to disability status), or qualify for USDA if the property is in an eligible rural zone. Brokers currently run these comparisons mentally or by submitting to multiple AUS systems, wasting hours and hard credit pulls. For FHA manual underwriting scenarios (borrowers below 620 FICO or above 50% DTI), there's no pre-screening tool at all — the broker submits and hopes.

## Why Nobody Has Built This
FHA, VA, and USDA program rules span thousands of pages of agency handbooks, mortgagee letters, and circulars — and they change with each administration. Building a rules engine requires continuous monitoring and updating of three separate federal agencies' guidelines plus individual wholesale lenders' overlays on those guidelines. The engineering effort is substantial and the market (government lending specialist brokers) is smaller than the conventional lending market that attracts most fintech investment.

## What to Build
A scenario simulator that takes borrower inputs (credit score, income, DTI, service history, property location, purchase price) and outputs a side-by-side comparison of FHA, VA, and USDA eligibility with program-specific costs, then layers in which wholesale lenders accept that scenario and at what pricing. Includes a manual underwriting pathway analyzer for FHA that predicts approval likelihood based on compensating factors.

## Target Customer
Government lending specialist brokerages where 60%+ of volume is FHA/VA — typically 3-15 loan officers serving first-time homebuyers, veterans, and lower-income borrowers. These brokers run 5-10 scenario comparisons daily and currently do them manually.

## Impact If Built
Saves 30-60 minutes per scenario comparison, enabling brokers to pre-qualify borrowers during the first phone call instead of over 2-3 days of research. Reduces hard credit pulls from exploratory AUS submissions by an estimated 40%. Increases conversion rate from lead to application by surfacing the optimal program match immediately.
