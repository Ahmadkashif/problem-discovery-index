# AI Agents & Platform Opportunities — Optometry Practices

**Industry:** [[optometry-practices|Optometry Practices]]

---

## 1. Vision and Medical Benefits Agent
#ai-agent #large-language-models #transformers #gradient-boosting #automation #data-integration #revenue-impact

**Concept:** An agent that works the payer side of every visit. Overnight it checks each scheduled patient's vision and medical coverage across plan portals and electronic eligibility, and writes one standard benefits card per patient. At checkout it reads the exam and recommends the routine-versus-medical split, codes, refraction charge and Medicare notice. It submits the claims, reads the remittances and learns which splits each plan pays, flagging the rare visit a human should decide.
**Inputs:** The schedule, insurance cards, plan portals and eligibility responses, exam notes and codes, plan rules from provider manuals, and claims and remittances.
**Outputs / Actions:** Benefits cards and authorization numbers before the visit; payer-split recommendations with codes; submitted claims; denial and recoupment alerts; a monthly report of medical revenue recovered.
**Why now:** LLMs can read each plan's benefit wording and a free-text note well enough to standardise them. Browser agents can work portals that have no API. Scribing is now free inside the EHRs (RevolutionEHR's AI Scribe since April 2026), so structured notes are available at checkout.
**Market:** Independent practices and multi-OD groups, plus rollups that integrate hundreds of offices. MyEyeDr.'s CEO describes "a scalable practice management platform that simplifies the insurance process" as a reason sellers choose it. VSP Vision, which owns Eyefinity, was hiring a Director, AI Platforms & Engineering (remote US) on 25 October 2026, and is both the largest plan and the largest EHR and claims vendor in the space. Anagram sells multi-plan eligibility and claims but had no open roles on its Ashby board. The medical half's analytics vendors are profiled under [[medical-billing|Medical Billing]]. A two-week MVP is a payer-split recommender over synthetic optometry encounters and public Medicare rules, scored against a coder's splits.

---

## 2. Diabetic Eye Exam Gap-Closure Agent
#ai-agent #large-language-models #bert #logistic-regression #data-integration #compliance #revenue-impact

**Concept:** An agent that closes the loop between optometry practices, primary care and health plans on diabetic eye exams. It reads each plan's gap list and the practice's schedule, invites unexamined members, and books them. After the exam it reads the findings, assigns CPT II result codes, writes the PCP letter, and builds the plan's supplemental-data submission. It reconciles gaps the plan still shows against exams already done.
**Inputs:** Plan gap lists and member rosters, the practice schedule and recall list, exam findings by eye, prior-year results, PCP directories, and plan submission specifications.
**Outputs / Actions:** Outreach and booked exams; CPT II codes on claims; PCP letters sent by Direct or fax; supplemental-data files; a gap-reconciliation report per plan.
**Why now:** The Eye Exam for Patients With Diabetes measure is administrative-only from 2025 (search summary), so plans depend on codes from eye practices rather than chart review. Only 66.0% of adults with diabetes reported an annual exam in 2023 (Healthy People 2030), and Medicare's rate was 54.1% in 2017 (CDC). Autonomous screening at the PCP (CPT 92229) is putting pressure on optometry's share of these exams.
**Market:** Medicare Advantage and Medicaid plans' quality teams pay for gap closure today. Optometry groups and rollups would pay for the credit and referrals. The plan-side work is [[health-insurance-carriers|Health Insurance Carriers]]. AEYE Health, whose AI bills CPT 92229 in primary care, listed a Senior DevOps Engineer, a Full Stack Developer and an AI (Vision) Researcher in Tel Aviv, Israel (undated), and US sales and implementation roles. Digital Diagnostics listed only a general application, and Eyenuk listed no openings.

---

## 3. Contact Lens Prescription and Replenishment Agent
#ai-agent #large-language-models #transformers #survival-analysis #compliance #automation

**Concept:** An agent that owns the contact lens wearer's year. It sends each prescription to the patient at the end of the fitting and records the confirmation the FTC Contact Lens Rule requires. It answers seller verification requests inside eight business hours, and offers the practice's own annual supply or subscription, with manufacturer rebates and vision-plan allowances applied. It predicts when each wearer will run out and triggers the reorder or recall before they buy elsewhere.
**Inputs:** Contact lens prescriptions and fitting notes, release confirmations, verification requests by fax, email and robocall, vision-plan contact lens allowances, manufacturer rebate programmes and order history.
**Outputs / Actions:** Prescription releases with three-year confirmation records; verification responses; annual-supply quotes and orders; run-out predictions and reorder prompts.
**Why now:** FTC staff sent 37 warning letters to prescribers in June 2025, with penalties up to $53,088 per violation. Speech-to-text now handles robocalls, and manufacturers' direct-ship programmes make practice-branded subscriptions possible.
**Market:** Practices and groups that want to keep contact lens revenue. The other side of the transaction is hiring: 1-800 Contacts, the best-known online seller, had a Frontend Engineer, AI Prototyping, a Full Stack Engineer (Python) and two Senior Software Engineers open in Draper, Utah. Contact lens distributors (ABB Optical) belong to the queued medical supply distributors industry, and online sellers to optical retail.

---

## 4. Glaucoma and Retina Co-Management Platform
#ai-platform #cnns #transfer-learning #survival-analysis #tacit-knowledge-ml #worker-facing #revenue-impact

**Concept:** A platform for multi-OD groups and rollups that reads every OCT, field and retinal image from any device. It checks usability for technicians and flags artefacts and myopic false positives. It keeps a suspect ledger for each eye and shows the OD a progression risk during the exam. When an eye needs a specialist, it drafts the referral and co-management letter and tracks it to the ophthalmologist's finding. Group clinical directors see referral, treatment and progression patterns across all their doctors.
**Inputs:** DICOM and vendor exports from Zeiss, Topcon, Heidelberg, Optos and iCare devices, visual field series, pressures, notes, referral outcomes and treatment records.
**Outputs / Actions:** Usability checks; progression risk with highlighted evidence; referral letters and tracking; doctor-level dashboards for clinical directors; suspect and glaucoma recall lists.
**Why now:** Rollups now own thousands of optometrists' imaging archives. MyEyeDr.'s purchase of EyeCare Partners' 300-plus offices, announced 29 September 2026, cites investment in clinical research and centres of excellence for common eye diseases. Pretrained retinal foundation models make fine-tuning on a group's own archive feasible.
**Market:** Rollups and large groups first, through device and EHR vendors second. Optos was hiring a Senior Software Engineer in Dunfermline, United Kingdom. Topcon Healthcare's eight open roles included no engineering, and Altris AI (an OCT biomarker platform and 2026 VSP Innovation Challenge finalist) had no careers page found. Device image-to-code work is already covered under [[healthcare-practice-software|Healthcare Practice Software]]. Weave, which sells patient messaging to optometry offices among others, was hiring machine-learning engineers for voice and speech (remote US and India) and could carry the recall side. A two-week MVP is a progression-risk scorer on the public University of Washington visual field dataset with a fundus-photo artefact check, shown as a one-screen exam card.
