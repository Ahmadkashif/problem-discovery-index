# AI Agents & Platforms — Physical Therapy

**Industry:** [[physical-therapy|Physical Therapy]]
**Derived from:** [[problems/physical-therapy/high-impact|High Impact]], [[problems/physical-therapy/low-impact-1|Low Impact 1]], [[problems/physical-therapy/low-impact-2|Low Impact 2]], [[problems/physical-therapy/worker-life-1|Worker Life 1]], [[problems/physical-therapy/worker-life-2|Worker Life 2]]

---

## 1. Authorization Lifecycle Agent
#gradient-boosting #feature-engineering #evaluation-metrics #ai-agent #revenue-impact #compliance

**What it does:** An agent that monitors every patient's authorization status across all payers in real-time. It tracks visits consumed vs. authorized, fires alerts 2-3 visits before expiration, pre-populates concurrent review forms with clinical data from the EMR, submits extension requests to payer portals, and blocks scheduling of unauthorized visits. When a denial comes back, it auto-generates the appeal with supporting documentation.

**Who uses it:** Front-desk/authorization coordinators, clinic directors (dashboard view)
**Decisions it makes/augments:** Authorization status monitoring (automates), extension request timing (automates), form pre-population (automates), appeal generation (automates draft — coordinator reviews), scheduling blocks (automates — prevents unauthorized visits)
**Why an agent:** Authorization management is a continuous monitoring task with time-sensitive triggers (submit too late = gap in care; submit too early = insufficient progress data). The agent must track state across 200+ patients, multiple payers with different rules, and interact with different submission portals. This is event-driven orchestration.
**Compounding value:** Learns which clinical documentation patterns lead to approvals vs. denials per payer. Over time, the pre-populated forms become increasingly optimized for each payer's review criteria.

---

## 2. Documentation Intelligence Agent
#large-language-models #transformers #attention-mechanisms #transfer-learning #ai-agent #worker-facing

**What it does:** An agent embedded in the PT's documentation workflow that takes clinical inputs (objective measurements, functional tests, interventions performed) and generates a complete visit note with payer-appropriate medical necessity language. It knows the patient's treatment plan goals, tracks progress across visits, and adjusts documentation language to match the payer's audit expectations. Flags when documentation is insufficient for continued authorization.

**Who uses it:** Physical therapists, physical therapist assistants
**Decisions it makes/augments:** Note structure and language (automates), medical necessity framing (automates), documentation sufficiency assessment (automates alert — PT decides what to add), progress-toward-goals narrative (automates from data)
**Why an agent:** PT documentation requires session-over-session context — the agent must know what was documented last time, what the goals are, how the patient is progressing, and what the payer expects. It's not generating a single note in isolation; it's maintaining a coherent treatment narrative across 15-30 visits.
**Compounding value:** Learns each PT's documentation style and vocabulary. Builds payer-specific documentation models that improve approval rates over time.

---

## 3. Outcome-Driven Care Platform
#time-series-forecasting #evaluation-metrics #descriptive-statistics #ai-platform #data-integration #compliance

**What it does:** A platform that integrates outcome measurement, HEP adherence tracking, treatment planning, and quality reporting into a unified clinical intelligence system. It auto-selects measures by diagnosis, administers them at the right intervals (via patient portal or tablet in-clinic), trends scores longitudinally, correlates outcomes with adherence data from connected HEP apps, and generates MIPS/quality reports automatically.

**Who uses it:** PTs (clinical view per patient), clinic directors (practice analytics), billing/compliance staff (quality reporting)
**Decisions it makes/augments:** Measure selection and scheduling (automates), adherence-outcome correlation (augments PT's clinical reasoning), treatment plan modification suggestions (augments — surfaces data, PT decides), quality reporting (automates)
**Why a platform:** Outcome data only becomes actionable when connected to treatment context and adherence data. The platform closes the loop: prescribe exercises → track adherence → measure outcomes → adjust plan → compare to benchmarks. No individual tool does this end-to-end.
**Network effects:** Multi-clinic deployment enables benchmarking ("your ACL rehab outcomes are in the 60th percentile — clinics using this protocol are in the 85th"). Aggregate data can support value-based reimbursement negotiations with payers.

---

## 4. HEP Adherence & Coaching Agent
#gradient-boosting #feature-engineering #time-series-forecasting #ai-agent #worker-facing #quick-win

**What it does:** A patient-facing agent that delivers home exercise programs via mobile, sends reminders, tracks completion (self-reported or motion-sensor-validated), adapts difficulty based on patient feedback, and reports adherence data back to the PT's clinical workflow before the next visit. When adherence drops, it sends motivational nudges and alerts the PT.

**Who uses it:** Patients (exercise delivery and tracking), PTs (adherence data in their workflow)
**Decisions it makes/augments:** Reminder timing and frequency (automates, adapts to patient behavior), difficulty adaptation (automates minor adjustments — PT sets parameters), adherence alerting to PT (automates), motivational messaging (automates)
**Why an agent:** Patient engagement requires adaptive, ongoing interaction — not a one-time exercise handout. The agent must sense adherence patterns, adjust its approach (more reminders? simpler exercises? different time of day?), and communicate clinically relevant adherence data back to the PT.
**Compounding value:** Learns individual patient adherence patterns. Builds population-level insights about which exercise delivery approaches maximize compliance for different patient demographics and diagnoses.

---

## 5. Supervision Compliance & Scheduling Agent
#decision-trees #feature-engineering #optimization-fundamentals #ai-agent #compliance #automation

**What it does:** An agent that monitors PTA caseloads against supervision requirements (varying by state and payer), identifies upcoming supervision gaps, and automatically adjusts the schedule to insert PT supervision visits at the right intervals. It ensures the supervising PT is on-site when required and blocks PTA appointments that would violate supervision ratios.

**Who uses it:** Clinic directors/schedulers, PTAs (compliance visibility), supervising PTs (supervision schedule)
**Decisions it makes/augments:** Supervision gap identification (automates), schedule adjustment for compliance (automates recommendation — scheduler confirms), supervision ratio monitoring (automates), scheduling blocks for violations (automates)
**Why an agent:** Supervision rules create a constraint layer on top of the clinical schedule that changes as patients move between PTAs and PTs, new patients are admitted, and state/payer rules update. The agent continuously monitors the constraint space rather than requiring manual tracking.
**Compounding value:** Learns scheduling patterns that maintain compliance with minimal disruption. Identifies systemic supervision bottlenecks (e.g., "we need another supervising PT on Tuesdays").
