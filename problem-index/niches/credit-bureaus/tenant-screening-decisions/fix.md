# Voucher Income Scored as if It Were Wages

**Niche:** [[niches/credit-bureaus/tenant-screening-decisions/profile|Tenant Screening Reports & Decisions]]
**Industry:** [[industries/credit-bureaus|Credit Bureaus]]
**Type:** Fix (Pain Point)
**One-liner:** Income-to-rent rules and credit-based scores treat a housing voucher holder as if they paid the whole rent, and decline people whose rent is mostly paid by the government.
**Tags:** #decision-trees #causal-inference #evaluation-metrics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to return a screening decision in minutes that is matched to the right applicant and holds up under FCRA accuracy rules and fair-housing law, and whoever gives landlords instant decisions with the fewest wrong-person and disparate-impact findings takes the account.

## The Problem
A common rule requires income of a multiple of the monthly rent. For a Housing Choice Voucher holder the tenant's share is a fraction of the rent, but many screening configurations apply the rule to the full rent, and credit-based scores were never validated on how voucher holders pay their share. The SafeRent settlement barred scores and recommendations for voucher applicants for five years.

## Why It's Still Broken
Screening criteria are set by each property and copied from templates; the voucher amount is often not captured on the application.

## What a Fix Looks Like
Capture voucher status and tenant share on the application, apply income rules to the tenant's portion, suppress score-based recommendations for voucher applicants where required, and report outcomes by voucher status so the rule's effect is visible.

## Who Feels the Pain
Voucher holders declined for income they do not need; property managers exposed under source-of-income ordinances and fair-housing law.

## Impact If Fixed
Voucher applicants judged on the rent they actually pay, and a known source of disparate-impact claims removed.
