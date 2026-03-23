# Internal Referral Tracking Between Co-Located Practitioners

**Niche:** [[niches/acupuncture-practices/integrative-medicine-groups/profile|Integrative Medicine Group Practices]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Fix (Pain Point)
**One-liner:** Internal referrals between co-located acupuncturists, chiropractors, and massage therapists are verbal or scribbled — 30-40% of referred patients never schedule with the second provider.
**Tags:** #logistic-regression #binary-classification #tabular-ml #workflow-orchestration #revenue-impact

## The Problem
When an acupuncturist determines a patient would benefit from chiropractic care available in the same clinic, the "referral" is typically a verbal suggestion to the patient and maybe a mention to the chiropractor in the hallway. There is no tracking of whether the patient books, follows through, or what the outcome was. Practices estimate that 30-40% of internal referrals result in no appointment, representing lost revenue and suboptimal patient care.

## Why It's Still Broken
Internal referrals don't go through formal referral systems because the providers are in the same practice — there's no insurance referral requirement and no external coordination needed. Existing EHRs model referrals as inter-practice events with fax/portal workflows that are overkill for "walk the patient down the hall." The result is that the simplest referral type has the least tracking infrastructure.

## What a Fix Looks Like
A lightweight in-app referral system where a practitioner flags "recommend chiropractic" on a patient record, the front desk sees it in the scheduling queue, the patient gets an automated text offering to book, and the referring practitioner gets notified of the outcome. Closed-loop tracking with conversion metrics visible to the practice director.

## Who Feels the Pain
Practice directors who know cross-modality patients have 2-3x higher lifetime value but cannot systematically drive cross-referrals, and front desk staff who lack visibility into which patients need follow-up scheduling.

## Impact If Fixed
Converting even half of dropped internal referrals would add $50,000-120,000/year in revenue for a mid-size integrative practice, while improving patient outcomes through coordinated multi-modality care.
