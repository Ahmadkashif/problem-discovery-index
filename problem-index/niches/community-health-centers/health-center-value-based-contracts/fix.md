# Quality Incentives Paid on Lists the Center Cannot Reconcile

**Niche:** [[niches/community-health-centers/health-center-value-based-contracts/profile|Health Center Value-Based Contracts & FQHC-Led ACOs]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Fix (Pain Point)
**One-liner:** Each Medicaid plan pays a health center's quality incentive on its own HEDIS-style list, computed from claims, while the center works its UDS measures from the EHR, and the two disagree about the same patients.
**Tags:** #data-integration #feature-engineering #descriptive-statistics #compliance #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to earn quality and shared-savings payments for a health center's attributed Medicaid and Medicare patients on top of the PPS floor, and whoever books the most value-based revenue per attributed patient takes the account.

## The Problem
A plan says a patient is missing a diabetic eye exam that the center's records show was done at a mobile retinal camera event. Another plan counts the patient as attributed to a different clinic. The center's quality team works four plan lists and its own UDS measures, all slightly different.

## Why It's Still Broken
Each plan computes measures on its claims and its attribution. Supplemental data submissions exist but differ by plan, deadline and format. The HEDIS chart-review work belongs to plans and vendors, as in [[niches/health-insurance-carriers/hedis-hybrid-chart-review/profile|⚡ HEDIS Hybrid Chart Review & Stars Measurement]].

## What a Fix Looks Like
A reconciliation that matches each plan's gap list to the center's evidence and sends supplemental data in each plan's format before its deadline. It shows the dollars at stake per gap.

## Who Feels the Pain
Quality coordinators, medical assistants rooming patients, and CFOs who book incentive revenue that arrives smaller than expected.

## Impact If Fixed
Closing ~15% more gaps through supplemental data (estimate) can lift incentive payments by ~$20,000–$60,000 per plan per year for a mid-sized center (estimate).
