# History: Telehealth Platforms

**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Primary Wave:** [[series/eras/wave-11-covid-dislocation|11 — The COVID Dislocation]]
**Secondary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Origin Parent:** [[origins/hospital-systems/profile|Hospital Systems]]
**Episode Tier:** 1
**Transferable Pattern:** When an emergency suspends a rule rather than repealing it, price the business as though the suspension will end — because eventually, on a schedule nobody controls, it does.

## Before

Video-call telemedicine was not a new technology in March 2020. **Teladoc was founded in 2002** in Dallas by Byron Brooks and Michael Gorton, launched nationally in 2005, and by **November 2016 already had 15 million members and roughly 75% US market share** — built almost entirely on employer-sponsored benefit plans marketed as a convenience, not a substitute for a doctor's visit. The infrastructure worked. What did not exist was a reason for most patients, and almost no reason for Medicare patients, to use it.

**Medicare telehealth utilisation sat under 1% of visits before March 2020.** Three legal facts, not one technical one, held it there: Medicare would not pay parity rates for a video visit except at a narrow set of rural "originating sites"; a clinician licensed in one state could not treat a patient physically located in another; and the **Ryan Haight Act (2008)** required a prior in-person examination before a clinician could prescribe a controlled substance by telemedicine. A member of a corporate telehealth plan could see a doctor for a rash. A Medicare patient, or anyone needing a controlled-substance prescription, mostly could not — by rule, not by bandwidth.

## The Origin Event

In roughly two weeks in March 2020, all three rules were suspended at once, not by a single act but by a cluster of emergency actions: **CMS issued its Section 1135 blanket waiver on March 13 2020** (retroactive to March 6), lifting the originating-site restriction; **Medicare telehealth payment parity took effect March 1 2020** and was formalised in the **CARES Act on March 27 2020**; **OCR's HIPAA enforcement discretion for telehealth took effect March 17 2020**, permitting ordinary consumer video tools; and the **DEA suspended the Ryan Haight in-person-exam requirement from around March 2020** under its public-health-emergency authority.

The demand response was immediate and enormous. Medicare telehealth visits went from under 1% to **over 43% by April 2020**. Zoom's daily meeting participants went from roughly 10 million in December 2019 to roughly 200 million in March 2020 and 300 million in April 2020 — a scale-up the industry's existing video infrastructure absorbed without needing to be reinvented, because Teladoc, Amwell and others had already spent fifteen years building it for a market that had simply never been allowed to use it at this size.

## What Became Cheap

**The regulatory permission to have the visit at all.** Nothing about the clinical encounter itself changed — the video call, the questionnaire, the e-prescription over Surescripts, all of it pre-dated 2020. What became cheap, overnight, was legal risk: a clinician could see an out-of-state Medicare patient on a consumer app and prescribe a controlled substance without an in-person exam, and none of the three pre-existing constraints applied for the duration of the emergency.

## The Contest — a race to monetise a suspension

The suspension created a commercial opportunity that a wave of direct-to-consumer platforms moved on immediately, several of them founded specifically to exploit it. **Cerebral Inc. was founded in 2020** by Kyle Robertson and Ho Anh as a subscription mental-health platform combining a short online assessment with prescribing. **Done Global Inc. was founded in 2019** by Ruthia He, a former Facebook product designer with no medical background, purpose-built around 30-minute ADHD consultations ending in a stimulant prescription.

Both grew on volume, and volume for ADHD stimulants under a suspended in-person-exam requirement is precisely where the contest turned adversarial. In 2022 the Department of Justice opened a Controlled Substances Act investigation into Cerebral's prescribing practices; Cerebral halted most controlled-substance prescribing in response and, in **November 2024, agreed to pay $3.65 million to resolve the investigation.** Done Global went further and did not survive it as a going concern in any recognisable form: the DOJ charged CEO Ruthia He and Clinical President David Brody in **June 2024** with illegally distributing controlled substances by telemedicine and conspiring to commit healthcare fraud, alleging the company had distributed **over 40 million Adderall pills for more than $100 million in revenue**. On **18 November 2025, a federal jury convicted both**, with He also convicted of conspiring to obstruct justice; both face up to 20 years.

This is a genuine corpse, and it is worth being precise about what killed it. Not competition. Not a funding cycle. **A federal prosecution, brought against the exact business model the 2020 suspension made possible**, once regulators concluded the suspension was being used to manufacture demand for a controlled substance rather than to preserve care continuity during an emergency.

## The Binding Constraint

The suspensions that made this contest possible did not become permanent, and the honest accounting matters more than the popular one. As of this writing:

| Suspended rule | Status |
|---|---|
| HIPAA enforcement discretion | **Expired.** Ended with the public health emergency at 11:59pm on 11 May 2023; the 90-day grace period ran out 9 August 2023. |
| Interstate licensure waivers | **Mostly expired.** By May 2023 only New York and Texas still had active waivers; the Interstate Medical Licensure Compact is a standing multi-state fast-track for licensure applications, not a wholesale waiver, and it existed before 2020. |
| Medicare payment parity | **Alive only by repeated short-term patch.** It lapsed 30 September 2025, was restored by the continuing resolution that ended the 2025 shutdown through 30 January 2026, and was extended again through **31 December 2027** in FY2026 appropriations. It is re-litigated almost annually. |
| DEA controlled-substance flexibility | **Never lapsed, never made permanent.** Extended four times; currently through 31 December 2026. |

Utilisation settled where that half-permanence would predict: **roughly 13–17% of visits by 2022–23**, around 55% below the April 2020 peak but still 10–20 times the pre-pandemic baseline. This vault's own `niches/telehealth-platforms/_overview.md` records the platforms' own tell: they build point-of-care clinical decision support readily, because clinicians want it and nobody in the business opposes it, and defer prescribing-pattern accountability — measuring which clinicians and which presentations are generating prescriptions at rates the evidence does not support — "until a regulator asks." After Done Global, the regulator has asked. **No amount of engineering moves a reimbursement rule with an expiry date, and no amount of clinical UX absolves a business model built on a suspended exam requirement once the suspension is understood, by a prosecutor, as the product.**

## What's Still Open

- [[problems/telehealth-platforms/high-impact|🔴 The Visit Closes and Nobody Measures Whether the Patient Got Better]]
- [[problems/telehealth-platforms/low-impact-1|🟡 Licensure, Scheduling and Clinician Supply Matching]]
- [[problems/telehealth-platforms/worker-life-1|🟢 The Clinician on a Visit Quota]]
- [[niches/telehealth-platforms/prescribing-accountability/profile|🎯 Prescribing Pattern Accountability]] — the half of the niche the Done Global case shows platforms cannot keep deferring
- [[niches/telehealth-platforms/point-of-care-decision-support/profile|🎯 Point-of-Care Decision Support]]
- [[niches/telehealth-platforms/clinical-outcome-measurement/profile|🟠 Clinical Outcome Measurement]]
- [[niches/telehealth-platforms/licensure-and-capacity/profile|⚡ Licensure, Credentialing & Capacity Matching]]

## The Transferable Pattern

**Suspended is not repealed, and the gap between the two is where an entire cohort of businesses can be built, funded, and — as Done Global shows — prosecuted.** An FDE evaluating a telehealth business built in this window should ask a single diagnostic question before anything else: does the revenue model survive the reversion of each suspended rule to its pre-2020 form? Teladoc's pre-pandemic business survived because it was built for a world where those rules held; Done Global's did not, because the suspension was not incidental to the business, it *was* the business. The distinction between "technology unlocked by a temporary rule" and "a business whose product is the exploitation of a temporary rule" looks identical from the outside for about a year. It stops looking identical exactly when the rule is enforced again.

**Sources:** CMS, Medicare Telemedicine Fact Sheet and Section 1135 waiver (issued 13 Mar 2020, retroactive 6 Mar); AHA advisory (17 Mar 2020); Federal Register 2020-08416 (OCR enforcement discretion) and 2023-07824 (expiration, effective 11 May 2023 + 90-day grace to 9 Aug 2023); Federal Register 2025-24123 and DEA release (Dec 2025, fourth extension to 31 Dec 2026); Alliance for Connected Care licensure dashboard; McKinsey, *Telehealth: a quarter-trillion-dollar post-COVID-19 reality*; Wikipedia, *Teladoc Health* (founding 2002, 2016 membership/market-share figures, 2020–21 growth); Wikipedia, *Cerebral (company)* (founding 2020, 2022 DOJ investigation, Nov 2024 $3.65M settlement); Wikipedia/DOJ press materials, *Done Global* (founding 2019, June 2024 charges, 18 Nov 2025 jury conviction of Ruthia He and David Brody, ~40M pills / $100M+ revenue alleged); this vault's `series/eras/wave-11-covid-dislocation.md`, `industries/telehealth-platforms.md`, `niches/telehealth-platforms/_overview.md`.
