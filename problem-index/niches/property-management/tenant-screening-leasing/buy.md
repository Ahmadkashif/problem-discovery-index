# TransUnion/Experian with Decision Logic Layer

**Niche:** [[niches/property-management/tenant-screening-leasing/profile|Tenant Screening & Leasing]]
**Industry:** [[industries/property-management|Property Management]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** TransUnion SmartMove and Experian RentBureau pull screening data (credit, criminal, eviction) but deliver raw reports that the PM must interpret — adding a configurable decision logic layer that applies the PM's criteria consistently and generates compliant adverse action notices would transform screening from a data product into a decision support product.
**Tags:** #gradient-boosting #compliance #data-integration #automation #quick-win #logistic-regression

## The Problem
A TransUnion SmartMove report returns: FICO score, derogatory accounts with details, criminal records with conviction types and dates, eviction filings and judgments, and an income-to-rent ratio estimate. The PM receives this data and makes a decision. But TransUnion doesn't tell the PM what the data means in context: a 610 FICO with only medical collections is very different from a 610 with a recent eviction judgment. A 7-year-old misdemeanor marijuana possession (in a state that has since legalized) is different from a 2-year-old felony property crime. PMs without deep screening expertise often make binary decisions based on FICO alone ("above 650 = approved, below = denied"), ignoring the nuanced data that would produce better outcomes.

## What Already Exists
TransUnion SmartMove and Experian RentBureau deliver comprehensive screening data with professional formatting. They provide recommendation indicators (ResidentScore from TransUnion) but these are generic risk scores, not decisions aligned with the PM's specific criteria and local legal requirements.

## The Customization Gap
A decision logic layer that: (1) lets the PM configure their screening criteria once — credit score threshold, income ratio requirement, criminal lookback period by conviction category (aligning with their state's ban-the-box or fair chance housing laws), eviction lookback period; (2) applies these criteria automatically to every screening report, producing a recommendation (approve/conditional/deny) with the specific criteria triggered; (3) accounts for local legal requirements — in Seattle, landlords must use first-in-time processing; in Illinois, criminal history can only be considered after a conditional offer; in Oregon, there are specific limits on criminal history consideration; (4) generates FCRA-compliant adverse action notices pre-populated with the specific criteria that triggered the denial; and (5) maintains a decision audit trail showing that the same criteria were applied to every applicant.

## Target Customer
TransUnion SmartMove and Experian RentBureau users (hundreds of thousands of PMs and landlords) who want consistent decision-making on top of the screening data they already pull. TransUnion/Experian as platforms seeking to move from data providers to decision support providers.

## Impact If Solved
Transforms screening from a raw data product into a decision support product, increasing the value of each screening transaction by $5-10. Reduces fair housing liability for PMs by ensuring consistent criteria application and providing documentation. Enables PMs to comply with the growing patchwork of state and local fair chance housing laws without researching each jurisdiction's requirements individually.
