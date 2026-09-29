# History: Dental Practices

**Industry:** [[industries/dental-practices|Dental Practices]]
**Primary Wave:** [[series/eras/wave-02-departmental-item-level|2 — Departmental & Item-Level]]
**Secondary Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**Origin Parent:** [[origins/insurance-carriers/profile|Insurance Carriers]] · [[origins/hospital-systems/profile|Hospital Systems]] *(by exclusion — see below)*
**Episode Tier:** 1
**Transferable Pattern:** When an industry's binding constraint is a number nobody has revisited, no amount of software moves it — and the software that gets built instead is software for coping.

> **Template note.** This industry has **no competitive fight and no graveyard.** Technology arrived as a cost of doing business, not as a weapon. Rather than manufacture drama, those sections are replaced by what is actually there. This is the most important finding of the H3 pilot — see `series/_bookmark.md`.

## Before

A dental practice kept three separate paper records, and they were functionally and legally distinct: **financial ledger cards** (one per patient, for billing), a **paper appointment book**, and **paper clinical charts**.

Note the separation, because it survived computerisation and is still the shape of the problem. Money, time and clinical fact lived in three different objects that a human being reconciled by carrying paper between them.

## The Origin Event — there isn't one

There is no moment here. No SABRE, no 8:01am in Troy Ohio. What there is instead is a slow, entirely unglamorous accumulation:

| Year | What arrived |
|---|---|
| **1985** | **Dentrix** founded by Larry M. Gibson in American Fork, Utah. Becomes the first dental practice-management system for Windows in **1989**. |
| **Sept 1985** | **CEREC** — first chairside CAD/CAM restoration placed, by Werner Mörmann and Marco Brandestini at the University of Zurich. *(Commercialised via Siemens; "Sirona" did not exist as a company until it spun out in 1997 — a common misattribution.)* |
| **1987** | **RadioVisioGraphy** — the first digital dental radiography, on a CCD sensor. |
| **early 1990s → 1994** | **Eaglesoft**, built by Scott Kabbes in Effingham, Illinois; launches as Windows software 1994. |
| **1996 → ~2001** | **Cone beam CT** — QR NewTom 9000 to the European market, US dental market around 2001. |
| **1997** | Henry Schein acquires Dentrix; Patterson acquires Eaglesoft — then ~25 employees and ~1,000 customers. **The distributors bought the software.** |
| **Aug 17 2000** | **CDT codes** named a mandatory HIPAA standard code set. The ADA maintains them and updates them annually. |
| **2003** | **Open Dental**, founded by Dr Jordan Sparks in Salem, Oregon, run initially out of the back of his own practice. First paying customer **July 22 2003**. |

**Nothing here was a competitive move.** Early practice-management software emulated the front-office ledger and the appointment book — the billing problem — and clinical charting was bolted on through the 1990s and 2000s. The paper separation was digitised, not dissolved.

> **A genuine gap, recorded as one:** no clean industry-wide adoption curve for dental computerisation exists in the sources checked. Do not assert one. Even digital radiography, introduced in 1987, was still described in 2014 as not having reached expected utilisation nearly 25 years on. Diffusion here is slow and undramatic, and saying so is more useful than inventing a hockey stick.

## What Became Cheap

**Submitting a claim.** That is very nearly the whole list, and it is the tell.

Electronic claims turn around in 7–14 days against 30+ for paper. CDT standardisation made the claim machine-readable. The rest of dental computing is downstream of getting paid faster — which is why the distributors, not software companies, ended up owning the category. Henry Schein and Patterson sell gloves, chairs and burs. The software was an attachment to the supply relationship.

## Why There Is No Fight

Dentistry is the control case for this whole series, and it is worth being precise about why.

Every origin industry in `origins/` had a contested decision where whoever solved it best took the account. **Dentistry does not.** A practice competes on location, chairside manner, insurance participation and hours. It does not compete on having better software, and no patient has ever selected a dentist on the basis of their practice-management system.

So technology arrived as **cost of doing business**: adopted to stop losing money, to satisfy a payer requirement, or because film processing became inconvenient. The closest thing to a weapon is CEREC — same-day crowns as a patient-acquisition pitch, 45 to 90 minutes of chair time instead of two visits and a temporary — and even that diffused over decades as a minority-practice capital investment rather than an arms race.

**Two real contests do exist, and both are recent, and neither is the dentist's.** PE-backed DSOs compete with each other to acquire practices. And payers are beginning to use AI against claims. More on both below.

## The Actual Constraint — and this is the episode

Dental insurance has an **annual maximum**: the most the plan will pay in a year. It is typically **$1,000–$1,500**.

That figure traces to somewhere between the early **1950s and 1970s** *(sources differ on the decade)*. It is **still the modal figure today** — roughly **32.8% of in-network PPO plans sat in that band in 2025/2026**.

**$1,500 in the early 1970s is on the order of $9,000–$10,000 in today's money.**

Everything the vault records as dental practice pain is a consequence of that one un-indexed number:

- Why the front desk spends **10–15 minutes per patient** verifying benefits — because what remains of a small, hard cap determines whether treatment is affordable *today*.
- Why treatment-plan acceptance sits near **50%** — because the plan routinely exceeds the maximum and the patient must decide what to pay for themselves.
- Why financial presentation is the industry's hardest problem — the practice must tell the patient, accurately, what *they* will owe, and that requires knowing exactly how much of a cap set fifty years ago is left.

> **No software fixes this.** A better verification tool makes the constraint faster to discover. It does not make the coverage larger. **The binding constraint is a number, and the number is a policy artefact nobody has revisited.**

This is the same shape as batch settlement in [[origins/retail-banking/the-mechanism|retail banking]] — an architecture chosen under conditions that no longer exist, outliving its reason, mistaken for a law of nature. The difference is that batch was at least a *decision*. The annual maximum appears to be something closer to an accident that nobody had standing to correct.

## The Exclusion That Explains the Rest

**Dentistry was substantially excluded from HITECH.** Only the Medicaid EHR incentive track was realistically available, largely to paediatric dentists able to clear the Medicaid patient-volume threshold, and only where certified dental EHR technology existed at all. The programme ran 2011–2021.

Hold that against [[origins/hospital-systems/profile|Hospital Systems]], where federal money and penalties took basic EHR adoption from 9% in 2008 to 84% in 2015 in seven years.

**Dentistry got neither the money nor the mandate, and its clinical record layer is correspondingly underdeveloped** — which is exactly what the vault observes without knowing the cause: *"Dental imaging exists in a silo — cone beam CTs, intraoral scans, and panoramic X-rays each have their own software, and none feeds cleanly into the treatment planning module."*

That is not an engineering failure. It is the absence of a subsidy, visible thirty years later in a file format.

## What Is Actually Happening Now

**The rollup.** Aspen Dental, around 1998, is a commonly cited early DSO. PE activity accelerated from **2015**, spiked **2019–2021** at 15+ new platforms a year, and there are now roughly **130 PE-backed DSO platforms**, with dental logging 120+ add-on deals in 2024 — the most of any healthcare category. Dentistry is a textbook rollup target: fragmented, capital-light per location, mixed cash and insurance, with an ageing owner-operator base heading for retirement.

> **Contested figure — do not cite a single number.** Two incompatible penetration statistics are in circulation: *8.8% of US dentists in 2017 → 16.1% in 2024*, versus *16% in 2017 → 30%+ by 2023*. Same base year, very different trajectories, most likely different definitions of "DSO-affiliated." Unresolved.

On quality, the clearest documented harms are **Medicaid-focused paediatric chains** — Small Smiles, Kool Smiles and related entities settled False Claims Act allegations over unnecessary treatment in the 2010s. Real and DOJ-documented, but specific to that segment. Broader peer-reviewed evidence on DSO versus independent treatment intensity is thin and mixed. **Do not over-claim in either direction.**

**The AI, and who it is actually for.** Three FDA clearances matter: **Overjet "Dental Assist," cleared May 20 2021**; **Pearl "Second Opinion," cleared March 4 2022**; and **VideaHealth** (K232384, 30+ findings, ages 3+). Both Overjet and Pearl market competing "industry first" claims for different specific indications — read the press releases accordingly.

The efficacy evidence is **entirely vendor-sponsored**: Pearl cites 92% sensitivity and 89% specificity from an internal multi-site study; VideaHealth reports a 43% reduction in missed lesions. There is no independent large-scale outcomes literature. This is early-stage.

And here is the part worth an episode's closing minutes: **the same technology is being sold to payers for claims and utilisation review.** If that adoption is running ahead of clinical adoption — and the research suggests it may be — then dental AI's first real deployment is not helping a dentist find caries. It is helping an insurer decline the claim.

> **Flagged as unverified.** The payer-side adoption claim could not be confirmed with specific carriers and dates in this session. It is the most interesting thread here and **must be researched before it appears in any script.**

## What's Still Open

- [[problems/dental-practices/high-impact|🔴 Instant, accurate benefit verification]] — the 10–15 minutes, and the cap behind it
- [[problems/dental-practices/worker-life-1|🟢 The front-desk coordinator on hold]] — 2–3 hours a day
- [[problems/dental-practices/low-impact-1|🟡 Treatment plan financial presentation]]
- [[niches/dental-practices/insurance-verification/profile|Insurance Verification]]
- [[niches/dental-practices/treatment-plan-financials/profile|Treatment Plan Financials]]
- [[niches/dental-practices/dental-imaging-ai-vendors/profile|Dental Imaging AI Vendors]]
- [[niches/dental-practices/dental-payer-clinical-policy/profile|Dental Payer Clinical Policy]] — where the AI may actually be landing
- [[niches/dental-practices/dental-service-organizations/profile|Dental Service Organizations]]

## The Transferable Pattern

> **Find the number that governs the business, then find out when it was set and by whom. If nobody can tell you, you have found the constraint — and it is almost certainly not a software problem.**

For an FDE this is the more common situation than anything in the airlines or programmatic files, and it is the one nobody trains you for. Most businesses are not fighting a rival with an algorithm. Most businesses are coping with a rule.

The professional skill is telling the two apart **before** you build, because the software you would build is completely different:

- If the constraint is **information** — the practice does not know the remaining benefit — build the verification tool. Real, valuable, and the vault's high-impact note for this industry.
- If the constraint is **the cap itself**, no tool helps, and the honest answer to the customer is that their problem is with the payer, not with their software.

Both are true here simultaneously, and saying so is more useful than picking one. An FDE who can hold that distinction in front of a customer is worth considerably more than one who ships a dashboard.

**Sources:** Henry Schein and Patterson corporate histories (Dentrix 1985/1989/1997; Eaglesoft 1994/1997); Open Dental company history (2003); Wikipedia, *CEREC*, *Dentrix*, *Current Dental Terminology*; ADA (CDT maintenance; HIPAA standard code set, Aug 17 2000; ADA Dental Claim Form 2012 revision); NADP and ADA on annual maximums (2025/2026 plan-band data); ONC/CMS on HITECH eligibility and the Medicaid EHR Incentive track 2011–2021; FDA 510(k) records — Overjet K212519 (May 20 2021), Pearl Second Opinion (March 4 2022), VideaHealth K232384; DOJ False Claims Act settlements (Small Smiles, Kool Smiles); dental trade press (DrBicuspid, Dentistry Today, Off the Cusp); this vault's `industries/dental-practices.md`.
