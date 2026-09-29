# Lineage: Medical Supply Retail

**Industry:** [[industries/medical-supply-retail|Medical Supply Retail]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**The tool:** HCPCS Level II — the letter-plus-four-digit code set (E-codes for durable medical equipment) that names every wheelchair, CPAP and oxygen concentrator on a Medicare claim
**Builder:** Health Care Financing Administration
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Medicare paid for things, and physician codes described only acts.

A doctor's claim describes something a clinician *did*. A home medical equipment supplier's claim describes an *object* — a hospital bed, a walker, a month of oxygen — often rented, by someone who is not a clinician. The physicians' procedure vocabulary had no words for that.

What filled the gap was local. The later record shows code sets "developed by state Medicaid agencies, Medicare contractors, and private insurers for use in specific programs and jurisdictions." **The same wheelchair could carry a different code, or none, depending on which contractor processed the claim.** The payer could not compare prices across regions.

## What Got Built

A national code list for the things CPT did not cover.

HCPCS — first the *HCFA Common Procedure Coding System* — was established in **1978** "to provide a standardized coding system for describing the specific items and services provided in the delivery of health care." According to AAPC's history, in **1983** HCFA folded its own procedure coding into the AMA's CPT, which became Level I. At the same time it built a second national list for everything else, and that list became Level II.

Level II codes are one letter from A to V followed by four digits. **E-codes are durable medical equipment.** K-codes were created as temporary codes for the regional DME contractors. The locally invented codes survived as "Level III" until they were **discontinued on December 31, 2003**.

Use was voluntary at first. On **August 17, 2000**, the HIPAA code-set rule (45 CFR 162.1002) named HCPCS Level II a required standard. After that, a DME claim to any covered payer, not just Medicare, speaks this vocabulary.

## Who Built It, And Why Them

The Health Care Financing Administration, the agency that ran Medicare and Medicaid until it was renamed the Centers for Medicare & Medicaid Services in 2001.

**Why them:** the payer is the party that needs a unit to price. A fee schedule, a rental cap or a regional comparison cannot exist until "a standard manual wheelchair" is one string that means the same thing on every claim. Physicians had the AMA, which owned CPT and had a reason to maintain it. Suppliers of equipment had no body that could impose a vocabulary on a national payer. The payer imposed one on them.

That is why Level II looks the way it does. It is shaped for claims adjudication, not for choosing products. CMS still makes every addition, revision and deletion, on a twice-yearly cycle for non-drug items. I could not find a named designer, or any internal HCFA account of why 1978 or 1983 in particular.

## What It Cost

**A code names a category, not a product, and not a right to be paid.** CMS says so directly: HCPCS Level II "isn't a methodology or system for making coverage or payment determinations, and the existence of a code doesn't, of itself, determine coverage."

So the supplier's work splits into three translations that the code does not do. First, from a physician's order to a code, which is often ambiguous. Then from the code to the specific products in stock — the vault's own estimate is 5,000–20,000 SKUs mapped to hundreds of codes. Then from the code to whether *this* payer covers it for *this* diagnosis. A separate contractor had to be created just to rule which products belong under which code.

The vocabulary gave the payer comparability. It left the supplier's link from patient to product to payment undone.

## What You Still Touch

Every DME order is still a hunt for the right five characters:

- [[problems/medical-supply-retail/low-impact-1|🟡 Product Catalog Search by Clinical Need and Payer Coverage]] — the three-way match between need, code and coverage
- [[problems/medical-supply-retail/high-impact|🔴 Insurance Eligibility Verification and Prior Authorization for DME]] — the coverage question the code does not answer
- [[niches/medical-supply-retail/dme-coding-pricing-contractor/profile|DME Coding & Pricing Determination]] — the institution that rules on product-to-code mapping
- [[niches/medical-supply-retail/mobility-wheelchair-dealers/fix|Complex Equipment Documentation for Prior Authorization]] — HCPCS codes and modifiers as one line in a much longer packet

**Sources:** CMS, *HCPCS Level II Coding Procedures* (cms.gov, fetched) for the August 17 2000 HIPAA designation under 45 CFR 162.1002, CMS's maintenance role, the January/July cycle and the "isn't a methodology … for making coverage" quotation; Wikipedia, *Healthcare Common Procedure Coding System* (fetched) for 1978, the "standardized coding system" quotation, the HCFA name and the Level III definition and December 31 2003 end; Wikipedia, *HCPCS Level 2* (fetched) for the letter-plus-four-digits format and the E- and K-code descriptions; AAPC, *What is HCPCS* (search summary, **not read at source**) for the 1983 merger with CPT and the June 14 2001 renaming. This vault's medical-supply-retail problem and niche notes for the SKU-to-code figures and the PDAC role (vault material, not independent corroboration). ⚠️ **Not established:** the named people at HCFA who designed Level II; whether E-codes existed in the first 1983 release or came later; the 1993 creation of regional DME contractors, which is widely cited but was not checked this session and is left out; any primary HCFA document from 1978 or 1983.
