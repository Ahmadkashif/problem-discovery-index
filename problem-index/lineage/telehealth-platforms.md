# Lineage: Telehealth Platforms

**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Wave:** [[series/eras/wave-11-covid-dislocation|11 — The COVID Dislocation]]
**The tool:** the Notification of Enforcement Discretion for Telehealth Remote Communications — HHS Office for Civil Rights' promise, effective 17 March 2020, not to penalise HIPAA violations arising from good-faith telehealth over non-public-facing consumer video apps such as FaceTime, Zoom and Skype
**Builder:** HHS Office for Civil Rights
**Builder in vault:** **ABSENT**
**Verification:** verified — issuer, dates and named apps checked against the Federal Register texts

## The Problem That Came First

In March 2020 the video call was not the bottleneck. Teladoc had been running one since the mid-2000s. The bottleneck was that most clinicians did not have a compliant one.

HIPAA's Security Rule applies to the transmission of patient information, and a vendor carrying that information for a covered provider is ordinarily a business associate that must sign a business associate agreement. Consumer video apps did not come with one. **So the thing every clinician and patient already had on their phone was, for clinical purposes, the one thing a practice could not safely use** — and procuring, contracting and rolling out a dedicated telehealth platform took weeks that a closed clinic did not have.

## What Got Built

A notice, not a rule. It said four specific things.

- **What was allowed:** "Apple FaceTime, Facebook Messenger video chat, Google Hangouts video, Zoom, or Skype."
- **What was not:** "Facebook Live, Twitch, TikTok, and similar video communication applications are public facing, and should not be used."
- **Scope:** telehealth "provided for any reason, regardless of whether the telehealth service is related to the diagnosis and treatment of health conditions related to COVID-19" — sprains, dental consultations and psychological evaluations included.
- **The BAA:** OCR "will not impose penalties" for the lack of one with a video vendor. For providers wanting more, it listed around a dozen vendors that said they would sign one — Microsoft Teams, Zoom for Healthcare, Cisco Webex and G Suite Hangouts Meet among them — while disclaiming endorsement.

It took effect on 17 March 2020, the same fortnight as CMS's Section 1135 waiver and the CARES Act, and was later published in the Federal Register as document 2020-08416.

## Who Built It, And Why Them

OCR enforces the HIPAA Privacy, Security and Breach Notification Rules. That is the whole reason it and not CMS, Congress or a vendor built this — **the obstacle was an enforcement risk, and only the enforcer could remove it.**

The instrument's shape follows from what OCR could do in days. Changing the Security Rule means notice-and-comment rulemaking. Declining to penalise is within an enforcer's discretion and needs no rulemaking at all. So the fix took the form of a promise about behaviour rather than a change to the law — which is exactly why the notice names apps rather than defining a standard, and why it came with no permanence. It ran "until the Secretary of HHS declares that the public health emergency no longer exists."

The public-facing line is the one piece of design judgement in it: OCR drew the boundary not at security features but at audience, excluding anything that broadcasts.

## What It Cost

It expired on schedule. OCR's expiration notice (2023-07824) ended the discretion at 11:59 p.m. on 11 May 2023, with a 90-day transition to 11:59 p.m. on 9 August 2023.

That left a split the industry still carries. Providers who had spent three years seeing patients over FaceTime had to move to a platform with a BAA; platforms that had always signed BAAs found their differentiator restored. And the notice fixed only the *channel*. Licensure, Medicare payment and controlled-substance prescribing were suspended by other agencies under other instruments, on other clocks — so the video call became legal nationally while the clinician could still see only patients in the states where they were licensed.

## What You Still Touch

The "HIPAA-compliant video" line on every telehealth vendor's pricing page is the boundary this notice suspended and then restored.

- [[problems/telehealth-platforms/low-impact-1|🟡 Licensure, Scheduling and Clinician Supply Matching]] — the constraint the notice left in place
- [[problems/telehealth-platforms/worker-life-2|🟢 The Care Coordinator Between Systems That Do Not Talk]]
- [[problems/telehealth-platforms/high-impact|🔴 The Visit Closes and Nobody Measures Whether the Patient Got Better]]
- [[niches/telehealth-platforms/licensure-and-capacity/profile|Licensure, Credentialing & Capacity Matching]]
- [[niches/telehealth-platforms/continuity-and-the-record/profile|Continuity & the Fragmented Record]] — what a consumer video call never wrote back to

**Sources:** HHS Office for Civil Rights, *Notification of Enforcement Discretion for Telehealth Remote Communications During the COVID-19 Nationwide Public Health Emergency*, Federal Register doc. 2020-08416 (21 Apr 2020), read via govinfo.gov HTML (issuer, 17 Mar 2020 effective date, named permitted and excluded apps, any-reason scope, BAA penalty waiver, vendor list with non-endorsement); OCR, *Notifications of Enforcement Discretion Expire at 11:59 p.m. on May 11, 2023*, Federal Register doc. 2023-07824 (13 Apr 2023), via govinfo.gov (expiration, transition to 9 Aug 2023); this vault's `history/telehealth-platforms.md` for the surrounding CMS 1135 waiver, CARES Act and licensure context and the Teladoc dating (vault material, not independent corroboration). The federalregister.gov page redirected to a bot check and was not read directly. WebSearch was unavailable this session (cap reached). ⚠️ **Not established:** the date the notice was first posted on hhs.gov as distinct from its effective date; who inside OCR drafted it.
