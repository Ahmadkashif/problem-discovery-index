# Continued-Stay Reviews Argued From Scattered Notes

**Industry:** [[psychiatric-hospitals|Psychiatric Hospitals]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every one to three days a psychiatric hospital's utilization review coordinator reads a patient's notes, finds the evidence that the stay is still necessary, and argues it to a payer reviewer by phone, and the case-management tools built for medical admissions do not know what psychiatric necessity looks like.
**Tags:** #large-language-models #transformers #feature-engineering #evaluation-metrics #automation #quick-win #revenue-impact

## The Problem
A utilization review coordinator, usually a nurse or a master's-level clinician, carries ~25–40 open stays (estimate). For each managed-care patient she has a review due every one to three days (estimate). Before each call she reads the psychiatrist's progress note, the nursing notes, the medication record, the observation sheets and the social worker's discharge note, and pulls out what the payer's criteria ask for. Is the patient still a danger to self or others? Is the patient still unable to care for themselves? Have less restrictive settings been tried and failed? Is a medication still being adjusted? Is there a safe discharge plan? Then she reads it to a reviewer at the plan, who approves more days, approves fewer, or sends it to a physician for a peer-to-peer. A missed detail, such as the 2 a.m. restraint that was in the nursing note but not the psychiatrist's, can cost the hospital the days.

Medicare works differently. It does not review each stay as it happens, but a physician must recertify the need by day 12 and at least every 30 days after, and the record must show active treatment against an individual treatment plan, with progress notes at least weekly (42 CFR 424.14 and 482.61). Those records are what an auditor or a prosecutor later reads.

## What Already Exists
Hospital case-management and utilization review software (Epic's utilization management module, XSOLIS for admission status, payer portals), licensed InterQual and MCG behavioral health criteria, and the payers' own level-of-care guidelines. Revenue cycle AI vendors (AKASA, Candid Health, Trellis AI) automate prior authorization, coding and appeals for acute care. Payer-side concurrent review is mapped at [[niches/health-insurance-carriers/inpatient-post-acute-review/profile|🎯 Inpatient & Post-Acute Concurrent Review]], and the acute hospital's denial contest at [[niches/general-hospitals/clinical-denials-status-appeals/profile|🎯 Clinical Denials & Inpatient Status Appeals]].

## The Customisation Gap
The generic tools are built for medical admissions, where necessity is read from vital signs, labs and procedures. Psychiatric necessity is read from behaviour described in prose. The psychiatric layer that needs adding is:
- evidence extraction from nursing, technician and physician notes for each criterion: dangerousness, grave disability, failed lower levels of care and medication changes;
- mapping to each payer's own behavioral criteria, and to LOCUS or ASAM where states require them;
- the hold's legal status and court dates, which payers weigh;
- a packet that cites the note and line behind each statement, so the coordinator can read it aloud and defend it;
- the Medicare recertification and active-treatment documentation in the same record.

The two-week MVP is a packet drafter that runs on synthetic progress, nursing and observation notes written to a published criteria outline. It produces a cited continued-stay summary and flags criteria with no supporting evidence (ml entry 2).

## Impact If Solved
If drafting a review falls from ~30 minutes to ~10 (estimate), a coordinator doing ~12 reviews a day gets back ~4 hours a day, about half her shift. A 100-bed hospital at 85% occupancy with ~60% of days under managed care has ~19,000 reviewed days a year; if better-cited reviews keep 1–2% more of them paid at ~$1,000 a day, that is ~$190,000–$380,000 a year (estimate).
