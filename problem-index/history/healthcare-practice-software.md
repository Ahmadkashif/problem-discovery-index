# History: Healthcare Practice Software

**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Primary Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**Secondary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Origin Parent:** [[origins/hospital-systems/profile|Hospital Systems]]
**Episode Tier:** 1
**Transferable Pattern:** A subsidy that pays for a certified capability, rather than a used one, buys adoption at the pace of the deadline and usability at the pace of nothing at all — because the vendor is graded, and paid, against the certificate.

## Before the Deadline

Ambulatory medicine — the doctor's office, not the hospital — ran on paper for longer than most of this vault's industries, and for an ordinary reason: a solo or small-group practice had neither the capital nor the IT staff a hospital could deploy. Where hospital systems had begun computerising billing and some clinical functions from the 1960s onward, the independent practice kept a paper chart in a folder, a superbill the front desk coded by hand, and a claim mailed or faxed to a payer. Athenahealth's own founding is a clean marker of this era's shape: it began in 1997 not as a software company but as **Athena Women's Health, a physical birthing centre in San Diego**, founded by Jonathan Bush and Todd Park. The company only became a claims-and-billing software business in 2000, when **athenaCollector** launched as a cloud-based revenue-cycle service — because the founders had lived the paper billing problem themselves, running an actual clinic, before they tried to sell the fix to others.

This is the industry's real starting condition: fragmented, undercapitalised, and — critically for what follows — **legally distinct from the hospital track that shares its origin.**

## The Origin Event

**HITECH, enacted February 2009 within the American Recovery and Reinvestment Act**, is this industry's origin event, and it is the same statute that built [[origins/hospital-systems/profile|Hospital Systems]] — but it ran two separate incentive tracks, and this industry's whole shape follows from which track its buyers qualified for. Hospitals had their own incentive formula, scaled to discharge volume. **Ambulatory practices claimed through the "eligible professional" track**, worth up to **$44,000 per eligible professional over five years through Medicare, or up to $63,750 through Medicaid** — real money for a solo physician, and enough to make switching off paper, or off a legacy system, a financially rational decision inside a fixed window.

*(No single authoritative dollar figure exists for HITECH's total cost — $19.2B, $27B, $30B and $35B all circulate depending on whether the count is authorized or disbursed funds, and whether it includes the whole HITECH title or only the CMS incentive programmes. This file does not pick one.)*

The mechanism that turned a subsidy into a market is the one [[origins/hospital-systems/the-mechanism|hospital systems' own mechanism file]] documents: **the incentive did not pay for adoption. It paid for annual attestation against numeric thresholds** — a minimum percentage of e-prescriptions, a minimum percentage of patients with an electronic problem list, a minimum percentage of qualifying encounters using a system running **ONC-Certified EHR Technology (CEHRT).** For an ambulatory vendor, this changed the product from something built to be used well into something built to be certifiable, provably, on schedule, for an audit that might come years later.

## The Binding Constraint

**Certification, not clinical usefulness, is what actually shaped what this industry's software had to do — and this is the episode.**

CEHRT criteria specify, in detail, which functions a product must contain and which data it must structure correctly to pass ONC testing: standardised problem lists, standardised medication lists, e-prescribing, the ability to generate a summary-of-care document in a specific machine-readable format. None of these criteria specify how many clicks a physician needs to document a visit, whether the interface fits a specialty's actual workflow, or whether the resulting note is legible to the next clinician who reads it. **A vendor that clears certification has satisfied the number the subsidy pays against. It has not been asked, by that same process, whether a doctor can use the product without frustration** — and the well-documented rise in physician-side documentation burden and burnout following EHR mandates, tracked in the AMA and JAMA Internal Medicine literature this vault's origin file already cites, is the visible cost of that gap.

This vault's own hub note for this industry describes the consequence without needing to know its statutory cause: *"Every vendor ships a claims engine, a scheduler and a note editor; almost none can tell a practice why its claims are being denied."* The claims engine is the certified function. Explaining a denial is not — CEHRT never asked for it, and a decade of incentive-driven build priority went to what was measured.

## The Contest — Fragmented, Because the Prize Was Fragmented

Where [[origins/hospital-systems/the-fight|Epic and Cerner]] fought a two-horse race for hospital systems large enough to run a multi-year, multi-million-dollar implementation, the ambulatory eligible-professional market never consolidated the same way, because the buyer was a different size and the sales motion was different: thousands of individually-decisioned small practices rather than a few thousand large institutions with a capital-committee process. **athenahealth, eClinicalWorks (founded 1999), Allscripts, NextGen, DrChrono, and the practice-management tier now known as Tebra (formed from a 2021 merger of Kareo and PatientPop)** all compete for the same eligible-professional dollar, none with anything like Epic's share of its own market tier.

The clearest documented cost of competing hard for that subsidy dollar, rather than for clinical trust, is **athenahealth's $18.25 million settlement with the Department of Justice, announced 28 January 2021**, resolving allegations that the company paid **illegal kickbacks to generate sales of its EHR product, athenaClinicals** — a False Claims Act case about how the certified product got sold, not about what it did clinically. *(I encountered widely repeated public reporting of a separate, larger 2017 DOJ settlement involving a different ambulatory EHR vendor over alleged certification-testing fraud, but could not independently verify the company, date or amount through a working source in this session — WebFetch returned no retrievable content from the DOJ and OIG press-release URLs I tried. Flagging this as unverified rather than citing it.)*

**Read together, even with one leg unverified, the pattern is legible: this tier's competitive pressure ran through compliance and distribution, not through the clinical usability the incentive was nominally meant to produce.**

## The Exclusion That Sharpens This — Dentistry

This industry's episode is best understood beside its opposite, and the vault has already written the opposite case. [[history/dental-practices|Dental Practices]] records that dentistry was **substantially excluded from HITECH** — eligible only through a narrow Medicaid track, largely for paediatric dentists able to clear a Medicaid patient-volume threshold, running 2011–2021 — and that its clinical record layer is correspondingly underdeveloped today: *"cone beam CTs, intraoral scans, and panoramic X-rays each have their own software, and none feeds cleanly into the treatment planning module."*

Hold the two side by side and the mechanism is exposed cleanly. **Physician practices got the money and the Medicare penalty; dental practices got neither.** Same decade, same federal government, a difference of exactly one thing — inclusion in the eligible-professional definition — and the outcome, ten to fifteen years later, is a physician-side EHR market with near-universal structured data and well-documented burnout, against a dental-side market with unresolved data silos and no comparable adoption curve. **Neither outcome is a story about which profession wanted technology more.** Both are downstream of a subsidy's eligibility list.

## What It Broke, and Why There Is No Clean Graveyard

Nothing here died the way Wirecard did or the way the Hadoop distributions did. Every vendor named above is still operating, still selling, still competing for the ambulatory eligible-professional dollar or its Medicaid equivalent. What broke instead is quieter and more durable: **the clean-claim rate and time-to-document — the two numbers this vault's own hub note says the category "lives or dies on" — are downstream of the same certified, structured-but-unexplained claims pipeline HITECH funded**, and no vendor in this tier has been asked, by any incentive as forceful as HITECH's, to solve the interpretability of a payer's own denial logic. Ambient documentation vendors (Abridge, Nuance DAX, Suki) are now taking the note-writing half of the burden out of the incumbents' hands entirely, which the incumbents have mostly answered by reselling rather than rebuilding — a live, ongoing instance of the same competitive posture this file has already described.

## What's Still Open

- [[problems/healthcare-practice-software/high-impact|🔴 Claim Denial Prediction & Clean-Claim Rate]] — the number CEHRT never asked a vendor to explain
- [[problems/healthcare-practice-software/low-impact-1|🟡 Payer Rule Engine Maintenance]]
- [[problems/healthcare-practice-software/low-impact-2|🟡 Specialty-Specific Patient Intake]]
- [[problems/healthcare-practice-software/worker-life-1|🟢 The Implementation Consultant's Migration Grind]] — a decade of somebody else's database, hand-mapped
- [[problems/healthcare-practice-software/worker-life-2|🟢 The Support Engineer's Repeat-Ticket Treadmill]]
- [[niches/healthcare-practice-software/ehr-data-migration-services/profile|EHR Data Migration Services]]
- [[niches/healthcare-practice-software/payer-rule-content-vendors/profile|Payer Rule Content Vendors]]
- [[niches/healthcare-practice-software/specialty-ehr-platforms/profile|Specialty EHR Platforms]]
- [[niches/healthcare-practice-software/solo-practice-software/profile|Solo Practice Software]] — the eligible-professional buyer HITECH was actually written for
- [[niches/healthcare-practice-software/fqhc-health-center-software/profile|FQHC Health Center Software]]
- [[niches/healthcare-practice-software/behavioral-health-ehr/profile|Behavioral Health EHR]] — this vault's origin legacy file names this segment's adoption lag as a direct, traceable consequence of HITECH's eligible-professional definition excluding psychologists and LCSWs

## The Transferable Pattern

> **Before building for an industry shaped by a subsidy, read the eligibility list, not the press release. What the money paid for is what got built. What the money excluded is what stayed broken, and it will look — to everyone building near it later — like an unrelated technical gap rather than the traceable consequence of a definition written once, in 2009, by people optimising for something other than the thing you now need.**

An FDE meeting an EHR-adjacent business should ask two separate questions that this industry's history shows are not the same question: *what does this software do*, and *what was this software paid to prove it does.* The gap between them is where the actual product opportunity has been sitting, unaddressed, since the incentive window that built the market in the first place closed.

**Sources:** HITECH Act, Title XIII of ARRA (enacted Feb 2009); CMS and ONC, *Meaningful Use* Stage 1/2/3 final rules and CEHRT certification criteria; this vault's `origins/hospital-systems/profile.md`, `origins/hospital-systems/the-mechanism.md`, `origins/hospital-systems/the-fight.md`, and `origins/hospital-systems/legacy.md`; athenahealth corporate history and DOJ press release, *Athenahealth to Pay $18.25 Million to Resolve Alleged False Claims Act Liability* (28 Jan 2021); eClinicalWorks corporate "About Us" page (founded 1999); this vault's `history/dental-practices.md`; this vault's `industries/healthcare-practice-software.md`. A widely-circulated 2017 DOJ settlement involving a different ambulatory EHR vendor over alleged certification-testing misconduct could not be independently verified through a working source in this session and is not cited as fact.
