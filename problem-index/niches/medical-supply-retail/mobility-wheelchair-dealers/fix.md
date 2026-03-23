# Complex Equipment Documentation for Prior Authorization

**Niche:** [[niches/medical-supply-retail/mobility-wheelchair-dealers/profile|Mobility & Wheelchair Dealers]]
**Industry:** [[industries/medical-supply-retail|Medical Supply Retail]]
**Type:** Fix (Pain Point)
**One-liner:** Power wheelchair prior authorizations require 15-30 pages of clinical documentation assembled from multiple sources, and first-pass denial rates run 30-40% because the documentation rarely meets every payer-specific requirement on the first try.
**Tags:** #bert #text-classification #nlp #compliance #revenue-impact

## The Problem
A complex power wheelchair prior authorization requires: a detailed Letter of Medical Necessity (LMN) from the prescribing physician describing functional limitations, a face-to-face evaluation within the required timeframe, an ATP assessment with specific clinical findings, the equipment configuration with HCPCS codes and modifiers, the CMN (Certificate of Medical Necessity), and supporting clinical documentation (therapy evaluations, medical records). This 15-30 page package must specifically address each criterion in the applicable Local Coverage Determination (LCD). Medicare's LCD for power mobility devices has 12 specific clinical criteria that must each be addressed — miss one, and the claim is denied. Different Medicare Administrative Contractors (MACs) interpret the same LCD differently, adding regional variation.

## Why It's Still Broken
The documentation requirements are a moving target: LCDs are updated, MACs issue new interpretive guidance, and individual reviewers have inconsistent standards. An LMN that was approved by Noridian in Q1 might be denied by the same MAC in Q3 because of a new emphasis on a specific criterion. Billing staff must continuously track policy changes and audit documentation packages against current standards — a knowledge-intensive process that relies on experienced staff who take 12-18 months to train. Turnover in these roles is high, and each new hire repeats the same expensive learning curve.

## What a Fix Looks Like
A documentation assembly and audit tool that: maintains current LCD criteria by product category and MAC region, provides a structured LMN template that ensures every required criterion is addressed (with prompts for the physician: "Please document the patient's functional mobility limitation for each of the following activities..."), audits the assembled documentation package against applicable coverage criteria and flags gaps before submission ("Criterion 7: face-to-face evaluation date is more than 45 days before the order date — this will trigger a denial"), and tracks MAC-specific interpretive trends from historical submission outcomes. The goal is 90%+ first-pass approval rate, up from the current 60-70%.

## Who Feels the Pain
Billing specialists who assemble documentation packages and absorb the frustration of denials for preventable gaps, ATPs who must re-engage physicians to obtain missing documentation, and patients who wait 4-8 weeks for equipment that should have been approved in 2.

## Impact If Fixed
Increasing first-pass approval rate from 65% to 90% eliminates the resubmission cycle for 25% of orders, saving 2-4 hours of staff time per resubmission. On 200 complex wheelchair orders per year, this recovers 100-200 hours of billing staff time and reduces average patient wait time by 2-3 weeks. Prevents revenue loss from denied claims that are never successfully appealed (estimated 5-10% of total complex wheelchair revenue).
