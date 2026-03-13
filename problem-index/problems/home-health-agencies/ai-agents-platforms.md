# AI Agents & Platforms — Home Health Agencies

**Industry:** [[home-health-agencies|Home Health Agencies]]
**Derived from:** [[problems/home-health-agencies/high-impact|High Impact]], [[problems/home-health-agencies/low-impact-1|Low Impact 1]], [[problems/home-health-agencies/low-impact-2|Low Impact 2]], [[problems/home-health-agencies/worker-life-1|Worker Life 1]], [[problems/home-health-agencies/worker-life-2|Worker Life 2]]

---

## 1. Scheduling & Dispatch Agent
#ai-agent #ml-optimization #revenue-impact

**What it does:** An autonomous scheduling agent that builds daily visit schedules overnight, then actively manages the day in real-time. When a patient cancels at 9am, the agent re-routes affected clinicians, offers the open slot to waitlisted patients, and notifies all parties via SMS. When a clinician calls out, it redistributes their visits across remaining staff by acuity priority, flagging any visits that cannot be safely reassigned.

**Who uses it:** Scheduling coordinators (as supervisors), field clinicians (receive optimized routes on their phones)
**Decisions it makes/augments:** Initial schedule assignment (automates), real-time re-routing on disruption (automates with coordinator override), visit prioritization on constrained days (augments — coordinator approves triage of low-acuity deferrals)
**Why an agent:** Scheduling is a continuous decision loop, not a one-time optimization. The agent must sense disruptions, re-plan, communicate, and learn from outcomes. It's managing a fleet of knowledge workers across a geography — classic autonomous agent territory.
**Compounding value:** The agent learns visit duration patterns per patient (Mrs. Johnson's wound care always runs 15 minutes over), clinician travel preferences, and cancellation patterns (Monday mornings have 2x the cancellation rate).

---

## 2. OASIS Co-Pilot Agent
#ai-agent #worker-facing #ml-nlp

**What it does:** A bedside documentation agent that assists clinicians during OASIS assessments. It pre-populates fields from prior data, guides the clinician through only the questions needing fresh observation, validates internal consistency in real-time ("you marked M1800 as 'independent with ADLs' but M1810 indicates 'requires assistance with bathing' — please reconcile"), and checks scoring against CMS guidelines before submission.

**Who uses it:** Field clinicians (RNs, PTs, OTs, SLPs)
**Decisions it makes/augments:** Field pre-population (automates), consistency checking (automates), CMS guideline validation (automates), clinical scoring judgment (augments — clinician makes final call)
**Why an agent:** OASIS completion is a multi-step reasoning process with interdependencies between fields. The agent needs to maintain context across 100+ questions, apply CMS logic, and interact conversationally when inconsistencies arise. This is reasoning + interaction, not just form-filling.
**Compounding value:** As the agent processes more assessments for a patient, it builds a longitudinal functional trajectory that informs future pre-population and flags unexpected declines.

---

## 3. Referral Intake & Onboarding Platform
#ai-platform #data-integration #workflow-orchestration

**What it does:** A platform that receives hospital discharge referrals (via fax, e-fax, HIE, or portal), extracts structured data from the referral documents, auto-generates the plan of care from hospital orders, checks insurance eligibility and home health benefit status, pre-schedules the start-of-care visit, and routes incomplete referrals back to the discharge planner with specific missing-information requests.

**Who uses it:** Intake coordinators, hospital discharge planners (as referral submitters), scheduling coordinators
**Decisions it makes/augments:** Data extraction from referral docs (automates), eligibility verification (automates), plan of care generation (automates draft — clinical review required), first-visit scheduling (automates with coordinator override), missing-info identification (automates)
**Why a platform:** Referral intake connects two organizations (hospital and agency) and spans multiple workflows (document processing → eligibility → care planning → scheduling). A platform creates a shared surface between the hospital and agency, reduces phone tag, and builds institutional knowledge about referral patterns.
**Network effects:** Multi-hospital integration builds referral volume intelligence — which hospitals send complete referrals, which send patients the agency is equipped to serve, and which referral patterns predict high-acuity cases.

---

## 4. Clinical Peer Support & Knowledge Platform
#ai-platform #worker-facing #quick-win

**What it does:** A mobile-first platform where field clinicians post clinical questions (text, photos of wounds, medication questions), receive AI-assisted initial guidance with citations to clinical guidelines, and get peer responses from colleagues and clinical supervisors. The platform builds a searchable knowledge base of resolved clinical Q&A specific to the agency's patient population.

**Who uses it:** Field clinicians (all disciplines), clinical supervisors, quality/education directors
**Decisions it makes/augments:** Initial clinical guidance (augments — surfaces relevant guidelines and similar past cases), question routing to appropriate specialists (automates), knowledge base curation (automates indexing, tags, and search)
**Why a platform:** Clinical knowledge in home health is trapped in individual clinicians' experience. A platform externalizes it, making the collective expertise available to every clinician, especially new hires. The knowledge base compounds with every question asked and answered.
**Network effects:** Cross-agency deployment creates a community of practice. A wound care question from a nurse in Ohio gets answered by the wound care specialist who saw the same presentation in Florida last month.

---

## 5. EVV-Payroll-Clinical Reconciliation Agent
#ai-agent #automation #compliance

**What it does:** An agent that continuously monitors the three records of every visit (EVV check-in/out, clinical note, payroll entry), classifies discrepancies, auto-resolves routine variances, and escalates true exceptions with a pre-written explanation of the discrepancy and recommended resolution. It learns from each reconciliation decision to reduce future exceptions.

**Who uses it:** Billing coordinators, payroll administrators
**Decisions it makes/augments:** Discrepancy classification (automates), routine variance resolution (automates), exception escalation with recommendation (augments — coordinator approves)
**Why an agent:** Reconciliation is ongoing (new visit data arrives daily), requires judgment (is a 20-minute gap between EVV checkout and note signature normal?), and benefits from memory (this clinician always documents in their car — that's a known pattern, not an exception).
**Compounding value:** The agent's auto-resolution rate increases over time as it learns agency-specific patterns, clinician-specific habits, and payer-specific tolerance rules.
