# Sequenced Multi-Benefit Application Strategy Engine

**Niche:** [[niches/nonprofits-social-services/benefits-eligibility-screeners/profile|Benefits Eligibility Screeners]]
**Industry:** [[industries/nonprofits-social-services|Nonprofits Social Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool today can assess a household's eligibility across 20+ benefit programs simultaneously and output an optimal application sequence that maximizes total benefits by leveraging categorical eligibility chains.
**Tags:** #bayesian-network #recommendation #tabular-ml #tacit-knowledge-ml #automation

## The Problem
Experienced benefits navigators know that application order matters: if a family applies for Medicaid first and gets approved, they become categorically eligible for SNAP (no separate income test), which then makes them eligible for free school meals. Apply in the wrong order and the family goes through 3 separate income verifications instead of 1. This sequencing knowledge is tacit — navigators develop it over years of experience with 20+ programs and their interactions. New navigators screen programs independently, missing categorical eligibility chains and costing families $2,000-$5,000/year in unclaimed benefits.

## Why Nobody Has Built This
Modeling cross-program eligibility interactions requires encoding the rules of 20+ programs across 50 states, including the categorical eligibility linkages between them. This is a massive rule engine maintenance problem — states update income thresholds annually, add/remove categorical eligibility provisions, and create state-specific programs. No technology company has invested in this because the paying customer (community nonprofits) has tiny budgets, and the actual beneficiaries (low-income households) can't pay at all.

## What to Build
An eligibility strategy engine that takes household demographics (composition, income, assets, immigration status, disability status) and state of residence, evaluates eligibility across all applicable federal and state programs simultaneously, identifies categorical eligibility chains, and outputs a sequenced application plan: "Apply for Medicaid first (approval in 30 days), then SNAP (categorical approval in 7 days), then request free school meals (automatic with SNAP)." The system estimates total annual benefit value and generates pre-filled applications for each program.

## Target Customer
Benefits navigators at community health centers, FQHCs, community action agencies, and 211 call centers who screen 50-200 households per month. There are 15,000+ organizations doing benefits screening nationally.

## Impact If Built
Increases per-household benefit enrollment from an average of 2.1 programs to 3.4 programs, unlocking $3,000-$8,000/year in additional benefits per family, while reducing screening time from 45 minutes to 10 minutes per household.
