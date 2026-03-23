# Indirect Lending Turn Time Bottleneck

**Niche:** [[niches/credit-unions/auto-lending-cus/profile|Auto Lending CUs]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Fix (Pain Point)
**One-liner:** Dealers route auto loan applications to the lender that responds fastest — and CUs that take 45 minutes to make a decision lose deals to captive finance companies that approve in 5 minutes.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #automation #revenue-impact

## The Problem
In indirect auto lending, a dealer submits the same application to 3-5 lenders simultaneously through platforms like RouteOne or CUDL. The lender that approves first at a competitive rate wins the deal. Captive finance companies (Toyota Financial, Ally) auto-approve within 5-10 minutes. Many CUs still require manual loan officer review for applications outside narrow auto-approval parameters — adding 30-90 minutes to the decision. By the time the CU approves, the dealer has already booked the loan with a faster lender. CU lending staff report losing 20-30% of indirect deals to turn time, not rate.

## Why It's Still Broken
CU credit policies are written as static rule matrices that capture straightforward cases (FICO > 700, DTI < 40%, LTV < 100% = auto-approve) but require manual review for any exception. The exception population is large — 40-60% of applications fall outside auto-approval bounds on at least one dimension. Loan officers must review these manually, checking for compensating factors that justify approval despite one dimension being outside policy. This review step is where CU relationship lending adds value, but it also adds 30-90 minutes that costs competitive position at the dealer.

## What a Fix Looks Like
An intelligent auto-decisioning layer that handles the 40-60% of applications currently requiring manual review by evaluating compensating factors automatically: a FICO of 680 (below 700 policy minimum) with a 10-year CU member tenure and stable deposit history should auto-approve with a rate adjustment, not queue for manual review. The system encodes compensating factor logic from the CU's actual approval patterns — learning which exception combinations the loan officers consistently approve. Manual review is reserved for genuinely ambiguous cases (10-15% of applications), not routine policy exceptions. Target: reduce median decision time from 45 minutes to under 10 minutes for 80%+ of applications.

## Who Feels the Pain
Indirect lending staff who process 30-50 applications daily, manually reviewing applications they know they'll approve but must document policy compliance for, and the CU's lending revenue line that loses $500K-$2M annually in deals lost to faster competitors.

## Impact If Fixed
Recovers 20-30% of indirect deals currently lost to turn time, worth $500K-$2M in annual origination volume for a mid-size CU. Reduces loan officer manual review workload by 50-60%, freeing capacity for member relationship development. Achieves sub-10-minute decision times competitive with captive finance lenders while maintaining CU-specific credit standards.
