# Authorized Units That Don't Match Billed Units

**Niche:** [[niches/physician-practices/medical-benefit-drug-access/profile|Medical-Benefit Drug Access (Buy-and-Bill & Infusions)]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Fix (Pain Point)
**One-liner:** Drugs are authorized in doses or vials and billed in J-code units; weight-based dosing, wastage and dose changes make the two drift until a claim denies for exceeding the authorization.
**Tags:** #data-integration #descriptive-statistics #compliance #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to get each infused or injected drug approved, funded and paid before the first dose, and whoever starts the most patients on therapy with no denied or unfunded doses takes the account.

## The Problem
An authorization approves a drug at a dose for a number of administrations. The claim bills HCPCS units (for example, per 10 mg), plus discarded drug with the JW modifier, or JZ when none is wasted. A weight change, a dose escalation or a different vial size moves billed units above what was authorized, and the payer denies the excess.

## Why It's Still Broken
The authorization is in a portal, the dose in the infusion record, and the units are calculated at charge entry. Nobody recalculates authorized units when the dose changes, and the denial arrives weeks after the drug was given.

## What a Fix Looks Like
A unit ledger per patient and drug: authorized units and dates, units given per administration from the infusion record, wastage documented, and remaining authorized units. It flags any planned dose that would exceed the authorization and triggers an update request before the patient's chair time.

## Who Feels the Pain
Infusion nurses and pharmacists; reimbursement staff appealing unit denials; practices that wrote a cheque for the drug months earlier.

## Impact If Fixed
Preventing unit-overage denials could recover ~0.5%–1% of drug revenue now lost or delayed (estimate). For a practice billing ~$20M a year in drugs (estimate), that is $100,000–$200,000.
