# SUD-Specific Group Therapy Documentation

**Niche:** [[niches/behavioral-health-clinics/substance-use-disorder-programs/profile|Substance Use Disorder Treatment Programs]]
**Industry:** [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** EHR group note features exist but generate identical boilerplate across patients — SUD programs need individualized per-patient documentation from shared group sessions that tracks each patient's unique treatment plan goals.
**Tags:** #large-language-models #attention-mechanisms #transformers #bert #transfer-learning #automation #compliance

## The Problem
An IOP group therapy session has 8-12 patients, lasts 90 minutes, covers a structured curriculum topic (e.g., relapse prevention skills, coping strategies, motivational enhancement), and requires individual progress notes per patient documenting their specific participation, responses, and progress toward their unique treatment plan goals. Clinicians currently spend 30-60 minutes after each group writing individual notes — often 3-4 groups per day, meaning 2-4 hours daily on group documentation alone. The alternative is using the EHR's "copy to all" group note feature, which generates near-identical notes across all patients. Payers audit these, flag them as cloned documentation, and deny claims.

## What Already Exists
Every behavioral health EHR (SimplePractice, TherapyNotes, Valant, Netsmart) has a group session note feature that allows a clinician to document a group session and apply a base note to all participants. General-purpose clinical documentation AI tools (Ambient by Nuance, DeepScribe, Abridge) transcribe and summarize individual therapy sessions. Some newer AI note tools (Upheal, Blueprint) target behavioral health but focus on individual sessions, not group therapy with multiple patients requiring distinct notes.

## The Customization Gap
SUD group documentation requires three capabilities no existing tool combines: (1) a shared session layer capturing the group topic, curriculum module, clinician interventions, and group dynamics; (2) a per-patient individualization layer that maps each patient's observed participation and responses to their unique treatment plan goals (which differ — one patient's goal is "identify three relapse triggers" while another's is "practice assertive communication with family"); and (3) SUD-specific clinical language and billing compliance for H0015 group counseling codes, including documentation that each patient received a therapeutic intervention (not just attended). The tool must also handle variable attendance — patients join and leave IOP programs on different schedules, so group composition changes daily.

## Target Customer
Group therapy facilitators and counselors at IOP/PHP programs running 3-5 groups per day with 8-12 patients each, who currently spend 2-4 hours daily on post-group documentation.

## Impact If Solved
Reduces group documentation time from 30-60 minutes per group to 10-15 minutes by generating individualized draft notes from a shared session template. Eliminates cloned-note audit risk, protecting against payer clawbacks that can reach $50K-$200K per audit finding. Frees clinician time for direct patient contact — recovering 1.5-3 clinical hours per clinician per day.
