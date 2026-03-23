# Charity Care Screening Gap Before Collection Attempts

**Niche:** [[niches/collections-agencies/medical-debt-collectors/profile|Medical Debt Collectors]]
**Industry:** [[industries/collections-agencies|Collections Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** Agencies attempt to collect on medical debts from patients who qualify for the provider's charity care program because no automated income screening occurs before accounts enter the work queue.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #compliance #worker-facing

## The Problem
Most hospitals and health systems have charity care programs that write off balances for patients below certain income thresholds (typically 200-400% of the federal poverty level). When unpaid balances are placed with a collection agency, the provider's charity care eligibility is rarely pre-screened. Agents call patients who are both unable to pay and eligible for charity care — calls that are unproductive, emotionally damaging to both parties, and increasingly a regulatory and reputational risk as states pass laws requiring charity care screening before third-party collection.

## Why It's Still Broken
Charity care eligibility depends on the patient's income, which is not included in the placement file. Estimating income from available data (zip code demographics, credit header attributes, employment indicators) is imprecise but feasible — no collection platform does it. Additionally, each provider has a different charity care policy (different income thresholds, different coverage percentages), and these policies are not standardized or digitized. The agency has no systematic way to match a patient's estimated income against the originating provider's specific charity care criteria.

## What a Fix Looks Like
A screening layer that runs on every new medical debt placement: estimate the patient's household income using available data (credit bureau attributes, census tract income data, employment indicators from skip trace feeds), compare against the originating provider's charity care threshold, and flag accounts where the patient is likely charity care-eligible. Flagged accounts are routed to a verification queue where the agency contacts the patient about charity care application rather than payment demands.

## Who Feels the Pain
Collection agents who spend time calling patients who cannot pay and should qualify for charity care — calls that are emotionally difficult and unproductive — and compliance officers who face increasing regulatory scrutiny over medical debt collection practices.

## Impact If Fixed
Diverts an estimated 8-15% of medical debt accounts to charity care screening before collection, improving agent productivity, reducing complaints and regulatory exposure, and generating goodwill with provider clients who face reputational risk from aggressive collection of charity-eligible patients.
