# Dealer Performance Analytics and Relationship Scoring

**Niche:** [[niches/credit-unions/auto-lending-cus/profile|Auto Lending CUs]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** CRM tools track dealer contacts but don't analyze dealer performance — which dealers send profitable loans that perform well versus which dealers cherry-pick approvals and send the CU adverse-selected paper.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact #data-integration

## The Problem
A CU with 50 dealer relationships has no systematic way to rank dealers by economic value. Dealer A sends 200 applications per year with a 2% default rate; Dealer B sends 40 applications with a 0.5% default rate and higher average loan size. Which relationship is more valuable? The answer depends on default losses, average loan margin, application quality (approval rate), and operational cost per deal. CU lending managers track these dimensions in separate reports or not at all, making dealer relationship decisions based on volume alone — rewarding dealers who send high-volume, low-quality paper.

## What Already Exists
CU Direct's CUDL platform tracks dealer submission volume and basic approval metrics. CRM tools (Salesforce, HubSpot) manage dealer contact relationships. Portfolio analytics platforms (Trellance, CU*Answers) provide aggregate loan performance reporting. None of these combine dealer-level submission patterns, approval rates, loan performance, and relationship cost into a single dealer scorecard.

## The Customization Gap
The gap is a dealer performance analytics layer that joins CUDL/LOS submission data with loan performance data from the core platform to compute dealer-level metrics: risk-adjusted profitability per deal, application quality score (approval rate + average credit quality), portfolio concentration from each dealer, delinquency and default rates by dealer cohort, and trend analysis (is this dealer's paper quality improving or deteriorating?). The tool should generate a dealer scorecard that informs relationship decisions: which dealers deserve rate concessions, which need performance improvement conversations, and which should be terminated.

## Target Customer
Indirect lending managers at CUs with 20+ dealer relationships and $50M+ in annual auto origination volume who want data-driven dealer management instead of volume-based relationship decisions.

## Impact If Solved
Identifies underperforming dealer relationships that contribute disproportionate losses — terminating the bottom 10% of dealers by risk-adjusted profitability typically reduces auto loan losses by 5-10% with minimal volume impact. Provides data for rate concession negotiations that are currently done by gut. Surfaces portfolio concentration risk from over-reliance on specific dealers.
