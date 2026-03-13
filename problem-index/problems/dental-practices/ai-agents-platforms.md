# AI Agents & Platforms — Dental Practices

**Industry:** [[dental-practices|Dental Practices]]
**Derived from:** [[problems/dental-practices/high-impact|High Impact]], [[problems/dental-practices/low-impact-1|Low Impact 1]], [[problems/dental-practices/low-impact-2|Low Impact 2]], [[problems/dental-practices/worker-life-1|Worker Life 1]], [[problems/dental-practices/worker-life-2|Worker Life 2]]

---

## 1. Insurance Intelligence Agent
#ai-agent #revenue-impact #data-integration

**What it does:** An agent that proactively verifies insurance benefits for the next day's schedule overnight. It logs into payer portals, extracts complete benefit breakdowns (not just eligibility), tracks each patient's remaining annual maximum and frequency limitations, and presents the front desk with a verified benefit summary per patient by 7am. When it can't extract data from a portal (changed layout, login issues), it flags those patients for manual verification.

**Who uses it:** Front-desk coordinators (consume results), billing coordinators (exception handling)
**Decisions it makes/augments:** Benefit data extraction (automates), verification completeness assessment (automates), patient cost estimation (automates estimate — front desk communicates to patient)
**Why an agent:** Benefit verification requires navigating different payer portals with different layouts, login flows, and data locations. The agent must adapt to portal changes, handle authentication, manage sessions across multiple payers, and retry on failures. This is browser automation + data extraction + scheduling — a natural agent workflow.
**Compounding value:** The agent builds a persistent benefit database per patient that updates with each visit and claim. Over time, it can predict benefit utilization trajectories ("this patient will hit their annual max by October at current treatment velocity").

---

## 2. Chairside Documentation Agent
#ai-agent #worker-facing #ml-nlp

**What it does:** A voice-activated agent that listens to the dentist's verbal callouts during procedures, transcribes them, maps them to CDT codes and charting entries, tracks materials used (with lot numbers from barcode scans), and generates the complete procedure record. The dental assistant confirms the charted entry between patients with a quick review — replacing real-time transcription during the procedure.

**Who uses it:** Dental assistants (primary users), dentists (voice input)
**Decisions it makes/augments:** CDT code mapping from verbal description (automates), tooth/surface identification (automates), material tracking (automates with barcode input), procedure note generation (automates — assistant confirms)
**Why an agent:** Chairside documentation is real-time, context-dependent (the agent needs to know what procedure was planned, what tooth is being worked on, what materials are in the tray), and multi-modal (voice + barcode scan + PMS integration). The agent maintains procedure context across the visit.
**Compounding value:** Learns each dentist's verbal patterns and abbreviations. Builds a procedure-specific vocabulary per practice. Reduces assistant confirmation time from minutes to seconds as accuracy improves.

---

## 3. Case Presentation & Financial Platform
#ai-platform #revenue-impact #quick-win

**What it does:** A patient-facing platform that presents treatment plans with verified insurance coverage, precise out-of-pocket costs, multiple payment options (in-house, CareCredit, Sunbit), and calendar-year optimization recommendations. The patient sees an interactive breakdown: "Your crown costs $1,200. Insurance covers $720. Your cost: $480. If you schedule before December 31, you use this year's remaining benefits. If you wait until January, your out-of-pocket is $720 because your deductible resets."

**Who uses it:** Treatment coordinators (configure and present), patients (interactive cost explorer), office managers (track acceptance rates)
**Decisions it makes/augments:** Cost calculation with insurance rules (automates), treatment sequencing optimization (automates recommendation), financing option selection (presents options — patient decides), acceptance follow-up timing (automates reminders for undecided patients)
**Why a platform:** Case acceptance connects insurance intelligence, treatment planning, and patient financing into a single patient experience. A platform aggregates acceptance patterns across procedures, price points, and financing options — enabling the practice to optimize how they present treatment.
**Network effects:** Multi-practice deployment builds benchmarking data — what acceptance rate should you expect for a $2,000 crown with Delta Dental PPO coverage? The platform can answer this.

---

## 4. Imaging Unification & Analysis Platform
#ai-platform #data-integration #ml-computer-vision

**What it does:** A platform that aggregates all dental imaging (intraoral, periapical, bitewing, pano, CBCT) into a unified timeline per patient, mapped to tooth numbers. Includes AI-assisted pathology detection (caries, bone loss, periapical lesions) that highlights regions of interest across all modalities. Dentists see the full visual history of any tooth in one view, with AI annotations as a second-opinion layer.

**Who uses it:** Dentists (clinical use), hygienists (perio charting comparison), treatment coordinators (visual aids for case presentation)
**Decisions it makes/augments:** Image indexing by tooth and date (automates), pathology detection (augments — dentist confirms), longitudinal comparison (automates side-by-side presentation), treatment planning visual support (augments case presentation)
**Why a platform:** Imaging data grows with every visit. A platform that maintains the longitudinal visual record and applies consistent AI analysis creates a diagnostic asset that individual imaging software can't match. The tooth-level timeline is the organizing principle that no current system provides.
**Network effects:** Aggregate pathology detection across practices improves model accuracy. Cross-practice data enables population-level dental health insights.

---

## 5. Schedule & Revenue Optimization Agent
#ai-agent #revenue-impact #ml-optimization

**What it does:** An agent that optimizes the daily and weekly schedule for production (revenue) and efficiency. It balances hygiene exams (high volume, low revenue per visit) with restorative procedures (lower volume, higher revenue), identifies open slots that could accommodate treatment plan patients who haven't scheduled, and sends targeted outreach to patients whose treatment plans are aging or whose insurance benefits are about to reset.

**Who uses it:** Office managers, scheduling coordinators
**Decisions it makes/augments:** Schedule template optimization (augments — manager approves structure), open-slot patient outreach (automates outreach, patient decides), treatment plan follow-up prioritization (automates — ranks by revenue potential and insurance timing)
**Why an agent:** Schedule optimization is continuous and event-driven — cancellations create opportunities, benefit year-end creates urgency, and patient recall needs evolve. The agent monitors the schedule in real-time and takes proactive action rather than waiting for a human to notice an opportunity.
**Compounding value:** Learns the practice's production patterns, patient no-show probabilities, and seasonal demand. Revenue-per-hour improves as the agent optimizes mix over time.
