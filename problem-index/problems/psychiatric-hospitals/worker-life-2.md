# The Psychiatrist Writing Hold Extensions for Court

**Industry:** [[psychiatric-hospitals|Psychiatric Hospitals]]
**Type:** Worker Life Changing
**One-liner:** An inpatient psychiatrist spends hours each week turning clinical judgement into the legal paperwork of involuntary holds, certifications and court testimony on state clocks, and gets back time with patients and the confidence that no hold will lapse on a missed form.
**Tags:** #large-language-models #transformers #workflow-orchestration #worker-facing #compliance #automation #evaluation-metrics

## The Problem
Many patients on an acute psychiatric unit are there involuntarily. A police officer, a crisis worker or an emergency physician starts an emergency hold, commonly 72 hours (estimate; California's section 5150 is the best-known). If the patient still meets the legal standard of danger to self, danger to others or grave disability when it expires and will not stay voluntarily, the hospital must certify a longer hold or petition a court. The patient has a right to a hearing, often held on the unit or by video within days, and a separate petition is needed to give antipsychotic medication over objection (rules differ by state; estimate).

The attending psychiatrist does most of this. On a 20-patient caseload with a third on holds (estimate), she writes certifications and petitions whose facts must match the chart, tracks each hold's expiry by hand or on a whiteboard, prepares for hearings, and testifies, sometimes several times a week. At Acadia, psychiatrists are generally independent contractors rather than employees (10-K), so the hours are often unpaid add-ons to rounding. A petition with the wrong date, a missing notice of rights, or facts the patient's lawyer can show are stale can end the hold. Then a patient the psychiatrist believes is dangerous walks out, or a patient is held without legal authority, which is the conduct described in the 2024 press reporting and investigations of the largest chain (search summary; 10-K).

## Why It Matters to the Worker
She trained to diagnose and treat, and a growing share of her week is drafting legal documents in a format she was never taught, against deadlines that are not clinical. The hearing is adversarial. The patient's public defender, whose side is mapped at [[niches/public-defenders/mental-health-court/profile|🟣 Mental Health Court Defense]], cross-examines her on the record, sometimes in front of the patient she is treating. Losing a hearing on a technicality damages the therapeutic relationship and her standing with the court. And the fear of a lapsed hold, or of holding someone a day too long, follows her home.

## What a Solution Looks Like
A legal-hold assistant built into the unit's record. It keeps every hold's legal clock, from initiation through certification, hearing and expiry, with the state's rules encoded. It drafts the certification or petition from the chart, citing the note and date behind each fact and flagging facts older than the statute allows. It assembles the hearing packet and a one-page summary of the clinical course for testimony, and records the outcome. The psychiatrist reviews, edits and signs; nothing is filed without her. A demonstration runs on synthetic charts and a single state's published forms.

## Impact If Solved
If drafting a certification or petition falls from ~45 minutes to ~15 (estimate), a psychiatrist writing eight a week gets back ~4 hours. Across a 100-bed hospital with five attendings that is ~20 physician hours a week, worth ~$5,000 at ~$250 an hour (estimate), with fewer holds released on procedural defects.
