# Wave 11 — The COVID Dislocation (2020)

**Trigger:** CMS Section 1135 blanket waiver issued **March 13 2020** (retroactive to March 6); Medicare payment parity effective **March 1 2020**, formalised in the CARES Act March 27 2020; OCR HIPAA enforcement discretion for telehealth effective **March 17 2020**; DEA suspension of the Ryan Haight in-person exam requirement from ~March 2020
**What went to ~zero:** the requirement of **physical co-presence**
**Failure class produced:** the asymmetric hold, inherited wholesale from Wave 8

> **This wave's framing had to be corrected during research, and the correction is the lesson.** The working thesis was that COVID "permanently moved a regulatory boundary." For telehealth — the headline case — **that is largely false.** What actually happened is more interesting and much better teaching material.

## What Was True The Day Before

Telehealth was legal and barely used: under 1% of Medicare visits. The constraint was never technology — video calling had worked for a decade. The constraints were **reimbursement** (Medicare paid less, or not at all, outside rural originating sites), **licensure** (a clinician licensed in one state could not treat a patient in another), and **prescribing** (the Ryan Haight Act required a prior in-person exam for controlled substances).

Three legal facts, not one technical one. This is the wave's whole argument: **the binding constraint on an industry is frequently a rule, and no amount of engineering moves a rule.**

## The Trigger

In roughly two weeks in March 2020, all three were suspended at once. Not improved — suspended.

Telehealth went from **under 1% of Medicare visits to over 43% by April 2020**, with overall office and outpatient telehealth running roughly 78× baseline at peak. Nothing was invented. A rule changed.

## What Actually Stuck — the honest accounting

This is the part the popular narrative gets wrong, and where an episode earns its keep.

| Change | Status as of Sept 2026 |
|---|---|
| **HIPAA enforcement discretion** (use consumer FaceTime/Zoom) | **Expired.** Ended 11:59pm May 11 2023 with the PHE; 90-day grace expired Aug 9 2023. Full compliance required since. |
| **Interstate licensure waivers** | **Mostly expired.** By May 2023 only NY and TX had active waivers. The Interstate Medical Licensure Compact (~43 jurisdictions) is the surviving workaround — not a wholesale waiver. |
| **Medicare payment parity** | **On life support.** Expired with the PHE, kept alive by a chain of short-term congressional patches: lapsed Sept 30 2025, restored by the CR ending the 2025 shutdown through Jan 30 2026, extended again via FY2026 appropriations through **Dec 31 2027**. Re-litigated almost annually. |
| **DEA controlled-substance flexibility** | **Never lapsed, never made permanent.** Extended four times; currently through Dec 31 2026, with a permanent rule still pending. Soft permanence without codification. |

**Utilisation settled at roughly 13–17% of visits by 2022–23** — about 55% below the Q2 2020 peak but still 10–20× the pre-pandemic baseline. The accurate framing is *"settled meaningfully above baseline, well below peak, on borrowed regulatory time"* — not *"permanently transformed."*

**The genuinely permanent shift is elsewhere.** Remote work went from ~5.7% of workers primarily at home in 2019, to ~60% of paid workdays at lockdown peak, to a stable **20–25% of paid workdays** sustained five years on — a 4–5× step up that has held. That, not telehealth, is the clean structural break.

**And the clearest durable effect is negative.** NAEP 2022 recorded 4th-grade math down 5 points and 8th-grade math down 8 points against 2019 — the largest math decline since testing began in 1990, with no state improving. Unlike the health rules, this has not reverted.

## The Competitive Fight

**Regulatory arbitrage against the clock.** Every business built in this window was betting on which suspensions would become permanent. The telehealth platforms that built for a permanent world and the ones that built for a reversible one made genuinely different architectural choices — on licensure matching, on documentation, on controlled-substance workflow. The vault's own `niches/telehealth-platforms/_overview.md` captures the consequence precisely: platforms build the clinical-support half readily and defer the prescribing-accountability half "until a regulator asks."

That deferral is now visibly a bet on the calendar.

## What It Broke

**It manufactured an industry on a temporary legal footing and then let the footing wobble annually.** Every telehealth business in this vault operates under a reimbursement rule with an expiry date that Congress renews at the last minute. That is not a technology risk and cannot be engineered away.

*(Myth to avoid: "COVID created the EOR industry." Deel and Remote were both founded in **2019**, before the pandemic; Papaya Global in 2016. COVID accelerated adoption of remote-hiring infrastructure that already existed. That is a demand shock, not an origin story — unlike telehealth, where the regulatory unlock genuinely was the creating event.)*

## Children in This Vault

**Primary:**
- [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
- [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
- [[industries/telehealth-platforms|Telehealth Platforms]]
- [[industries/virtual-assistant-services|Virtual Assistant Services]]

**Secondary:**
- [[industries/fractional-cto-services|Fractional CTO Services]]
- [[industries/corporate-training|Corporate Training]]
- [[industries/k12-private-schools|K-12 Private Schools]]
- [[industries/language-schools|Language Schools]]
- [[industries/tutoring-centers|Tutoring Centers]]
- [[industries/chiropractic-practices|Chiropractic Practices]]
- [[industries/acupuncture-practices|Acupuncture Practices]]
- [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
- [[industries/home-health-agencies|Home Health Agencies]]
- [[industries/urgent-care|Urgent Care Centers]]
- [[industries/work-collaboration-tools|Work Collaboration Tools]]
- [[industries/faith-organizations|Faith Organizations]]
- [[industries/digital-bpo-operations|Digital BPO Operations]]

**Sources:** CMS, Medicare Telemedicine Fact Sheet and Section 1135 waiver; AHA advisory (March 17 2020); Federal Register 2020-08416 (OCR enforcement discretion) and 2023-07824 (expiration); Federal Register 2025-24123 and DEA release Dec 31 2025 (fourth extension); KFF telehealth coverage explainer; Alliance for Connected Care licensure dashboard; McKinsey, *Telehealth: a quarter-trillion-dollar post-COVID-19 reality*; Stanford SIEPR / WFH Research (Bloom, Barrero, Davis); UNESCO education response data; NAGB/NAEP 2022 Nation's Report Card; Contrary Research (Deel, Papaya Global).
