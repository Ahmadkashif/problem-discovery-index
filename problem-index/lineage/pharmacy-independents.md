# Lineage: Independent Pharmacies

**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Wave:** [[series/eras/wave-02-departmental-item-level|2 — Departmental & Item-Level]]
**The tool:** the NCPDP Telecommunication Standard — the real-time pharmacy claim message, Version 1.0 published September 1988, built on NCPDP's paper Universal Claim Form
**Builder:** NCPDP
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

In the 1970s, by the standards body's own account, an insured patient paid cash for a prescription and mailed the receipt to a health plan. Plans faced "thousands of claims each week to manually process," paying or rejecting them "inaccurately and with limited consistency."

Plans then contracted with pharmacies to collect a copayment and file the claim themselves — and "each health plan designed their own claim form and submission process." The pharmacy inherited every plan's paperwork and a receivable measured in weeks.

Some of those plans were built by pharmacists. PAID Prescriptions was founded in 1965 and by 1968 was setting its own reimbursement rates for pharmacies wanting into its network. Pharmaceutical Card System was formed in 1969 "to process claims, funded by nominal charges on each claim." Pharmacy trade organisations complained about the recordkeeping, the variable coverage and the rates.

## What Got Built

**First a form, then a message.**

The form was the Universal Claim Form: one paper claim every plan would accept. NCPDP credits it, together with the National Drug Code and a standard pharmacy identifier, with saving $1.05 — 85% — on each paper claim printed from a store system rather than filled in by hand on a plan's own form.

The message was **Telecommunication Standard Version 1.0, published in September 1988**: a fixed format in which a dispensing system sends the patient, the prescriber and the drug, and the processor answers while the patient waits — eligible or not, the copayment, the amount the pharmacy will be paid — and, as the standard grew, clinical alerts such as allergies and interactions. By 2009, NCPDP reported, 99% of pharmacy claims ran this way, the whole cycle taking under five seconds.

## Who Built It, And Why Them

NCPDP was incorporated in **1977** as an extension of a Drug Ad Hoc Committee that had made recommendations for the National Drug Code. Its members come in three classes: pharmacies and other providers, payers and processors, and software vendors.

**That membership is the reason.** A claim format has to be accepted on both sides of the counter. Processors such as PCS lived on a charge per claim, so a cheaper claim was their margin. Pharmacies, in NCPDP's words, were "overwhelmed" by receivables as cash business turned into third-party business. The vendors wrote the dispensing software that would have to speak the format. NCPDP's account of 1988 names all three: "pharmacies, payers and technology vendors collaborated."

The business case set the shape. The standard was designed around the moment of dispensing — the answer arrives before the bottle is handed over — because the pharmacy's problem was not knowing what it would be paid, and the payer's was processing paper by hand.

## What It Cost

In its 2009 white paper NCPDP listed among the standard's benefits: "Pharmacies knew instantly how much they would be paid for the claim."

For many pharmacies that stopped being true. Price concessions known as DIR — direct and indirect remuneration — were assessed after the fact, clawing back part of a payment the real-time answer had already confirmed. The instant number became provisional.

The regulator's correction went through the same channel. A CMS final rule issued on April 29 2022 required that, from **January 1 2024**, all pharmacy price concessions in Medicare Part D be applied at the point of sale, redefining the negotiated price as "the lowest amount a pharmacy could receive as reimbursement." The fix made the real-time number the worst case. It covers Part D only, and incentive payments may still arrive later.

The same channel delivers every clinical alert, claim by claim, to the pharmacist at the counter.

## What You Still Touch

The copayment a technician reads off the screen before bagging a prescription is a response to a 1988 message format.

- [[problems/pharmacy-independents/high-impact|🔴 DIR Fee Exposure Prediction and PBM Contract Optimization]] — forecasting the clawback the instant answer omitted
- [[problems/pharmacy-independents/worker-life-1|🟢 Drug Interaction Alert Prioritization and Alert Fatigue Reduction]] — alerts delivered claim by claim
- [[niches/pharmacy-independents/dir-fee-pbm-optimization/profile|DIR Fee & PBM Optimization]]
- [[niches/pharmacy-independents/psao-contract-analytics/profile|Pharmacy Services Administrative Organizations]] — collective bargaining over what the message will say

**Sources:** NCPDP, *Pharmacy: A Prescription for Improving the Healthcare System* (executive summary, October 2009), for the 1970s workflow quotes, "each health plan designed their own claim form", the Universal Claim Form as NCPDP's genesis, "overwhelmed", the three-party collaboration, Version 1.0 in September 1988, the listed benefits including "knew instantly how much they would be paid", 99% real-time and under five seconds, and the $1.05 (85%) paper-claim saving. NCPDP, *History and Impact* page, for "1977 — NCPDP Incorporated" and "1988 — Telecom Standard". Wikipedia, *National Council for Prescription Drug Programs*, for the Drug Ad Hoc Committee and NDC and the three membership classes. Mattingly, Hyman and Bai, "Pharmacy Benefit Managers: History, Business Practices, Economics, and Policy", *JAMA Health Forum* 4(11), November 3 2023, for PAID (1965, rates from 1968), PCS (1969, "nominal charges on each claim") and the trade organisations' complaints. CMS-4192-F via Epstein Becker Green, Ropes & Gray and a CMS reminder notice (search summaries) for the April 29 2022 rule, the January 1 2024 effective date, the redefinition and the incentive-payment exception. ⚠️ **Not established:** the Universal Claim Form's adoption year — secondary sources say 1978, but no NCPDP primary text read gives it, so the body gives no year; the name and dates of the Drug Ad Hoc Committee; who drafted Version 1.0; and whether the 1988 message had any mechanism for later adjustments. This vault's `history/pharmacy-independents.md` dates the first PCS card to 1968; the JAMA paper dates PCS's formation to 1969 — the discrepancy is unresolved and the history note is not relied on here.
