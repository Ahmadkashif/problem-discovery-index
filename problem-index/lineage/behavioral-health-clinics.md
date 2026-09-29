# Lineage: Behavioral Health Clinics

**Industry:** [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
**Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**The tool:** the PHQ-9 — the nine-item Patient Health Questionnaire depression scale, each item scored 0–3 against a DSM-IV criterion, total 0–27 with cut-points at 5, 10, 15 and 20
**Builder:** Pfizer
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Diagnosing depression cost a structured interview, and the doctor who saw most depressed people did not have the time to give one.

Structured diagnostic interviews were built for psychiatrists. Primary care physicians — the people actually seeing the patient with fatigue, insomnia and back pain — had a few minutes per visit and no training in them. Depression was common in primary care and routinely missed there.

So the binding cost was **clinician minutes per positive finding**: an instrument needing a trained interviewer could not be used on everyone.

## What Got Built

A one-page form the patient fills in themselves.

It came in two steps. First **PRIME-MD** (Primary Care Evaluation of Mental Disorders), a clinician-administered screen, published in *JAMA* on 14 December 1994 as the PRIME-MD 1000 Study. It was still too long for routine use, so the same team turned it into a **self-report questionnaire, the PHQ**, validated in *JAMA* in 1999.

The **PHQ-9** is the depression module of that questionnaire standing on its own. Nine items, one for each DSM-IV criterion for major depression, each scored 0 ("not at all") to 3 ("nearly every day") over the last two weeks. The 2001 validation in the *Journal of General Internal Medicine* — 6,000 patients across eight primary care and seven obstetrics-gynaecology clinics — set the cut-points of **5, 10, 15 and 20** for mild, moderate, moderately severe and severe, and reported that a score of 10 or more had 88% sensitivity and 88% specificity for major depression against a mental-health professional's interview.

That design choice — patient-completed, summed, banded — is what turned a diagnosis into a number that can be repeated every visit.

## Who Built It, And Why Them

The people were Robert Spitzer, Janet Williams and Kurt Kroenke. Spitzer, a Columbia psychiatrist, had chaired the American Psychiatric Association's DSM-III task force from 1974; Williams was his long-time collaborator; Kroenke was a general internist. That pairing is the design: DSM criteria, cut down to fit a primary care visit.

**The money and the ownership were Pfizer's.** The 2001 paper states that "the development of the PHQ-9 was underwritten by an educational grant from Pfizer US Pharmaceuticals," and that PRIME-MD is a Pfizer trademark with copyright held by Pfizer. Pfizer still owns the copyright and lets anyone use the PHQ-9 for free.

Why a drug company, and not a medical society or the NIH? Pfizer's antidepressant sertraline (Zoloft) was approved by the FDA in 1991. The obvious commercial logic is that a drug for depression sells only as far as depression is diagnosed, and most of it was going undiagnosed in the primary care offices where most prescribing happens. A free, fast screening tool widens that funnel. **That motive is inferred from the timing and ownership; I did not find a Pfizer document stating it**, and it should be read as an interpretation.

Giving it away was the rational move: a free screen becomes the default.

## What It Cost

**The PHQ-9 measures symptoms, not what caused them or what to do about them.** It was built to find depression in a medical clinic, and it answers "how many DSM criteria, how often." It says nothing about trauma, substance use, or the social situation behind a score — which is why clinics stack the GAD-7, PCL-5 and others on top of it, each its own form.

The second cost: a score falling from 18 to 9 reads as progress to anyone looking at a chart, including a payer, whether or not the therapist agrees.

## What You Still Touch

Behavioral health clinics now give this primary-care screen to patients already in specialist treatment, as an outcome measure — a job it was not designed for, still administered largely by hand.

- [[problems/behavioral-health-clinics/low-impact-1|🟡 Automated Outcome Measurement Administration]] — PHQ-9, GAD-7 and PCL-5 on a clipboard
- [[problems/behavioral-health-clinics/high-impact|🔴 Unified Behavioral Health Record Fragmentation]] — the score sits in one place, the medication list in another
- [[niches/behavioral-health-clinics/psychological-assessment-publishers/profile|Psychological Assessment Publishers]]
- [[niches/behavioral-health-clinics/behavioral-ehr-content-teams/profile|Behavioral Health EHR Clinical Content Teams]]
- [[niches/behavioral-health-clinics/dsm-guideline-publishing/profile|Diagnostic Nomenclature & Practice Guideline Publishing]]

**Sources:** Kroenke K, Spitzer RL, Williams JBW, "The PHQ-9: validity of a brief depression severity measure," *J Gen Intern Med* 16(9), September 2001 (PMC1495268) — source of the sample, cut-points, sensitivity/specificity, the three-minute figure, the Pfizer grant statement and the trademark/copyright note; Wikipedia, *PHQ-9* (PRIME-MD 1000 Study in *JAMA*, 14 December 1994; PHQ-9 developed 1999 with a Pfizer grant; Pfizer holds copyright and allows free use), *Patient Health Questionnaire* (1999 *JAMA* PHQ validation), *Sertraline* (FDA approval 1991, developed by Pfizer), *Robert Spitzer (psychiatrist)* (DSM-III task force chair from 1974; Columbia). ⚠️ **WebSearch was unavailable** (session cap reached); research was by WebFetch of known URLs only. PubMed pages for the 1999 *JAMA* paper returned a captcha, so its exact date and sample were not checked. **Not established:** any Pfizer statement of why it funded PRIME-MD/PHQ — the Zoloft link above is inference from timing and ownership. The Joint Commission's 2018 behavioral-health outcome-measurement standard was not checked (its report returned HTTP 403), so the note does not claim any accreditor or payer requires the PHQ-9.
