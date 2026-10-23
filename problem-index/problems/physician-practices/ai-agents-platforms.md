# AI Agents & Platform Opportunities — Physician Practices

**Industry:** [[physician-practices|Physician Practices]]

---

## 1. Ordering-Practice Prior Authorization Agent
#ai-agent #large-language-models #gradient-boosting #evaluation-metrics #automation #revenue-impact

**Concept:** An agent that starts when the physician signs an order. It checks whether the plan requires authorization, pulls the payer's current medical policy, matches each criterion to cited evidence in the chart, and flags what is missing while the patient is still in the room. Then it submits through the payer's FHIR API, portal or fax, tracks the 72-hour and seven-day decision clocks, books and briefs the peer-to-peer, and drafts the appeal. It learns from each outcome which evidence each payer accepts, and tracks which clinicians qualify for state gold-card exemptions.
**Inputs:** Signed orders, chart notes and reports, payer medical policies and radiology benefit manager guidelines, prior requests and outcomes, payer API endpoints, gold-card status by state and payer.
**Outputs / Actions:** Requirement checks at order entry; criterion-by-criterion evidence packets; submissions and status checks; peer-to-peer briefs; appeal drafts; payer-behaviour reports for contracting.
**Why now:** LLMs can read a 40-page policy and a chart together and cite the match. CMS-0057-F decision clocks apply from January 2026 and payer APIs from January 2027. Clinicians attest to electronic prior authorization in MIPS from 2027. A two-week MVP is a packet builder over Synthea synthetic patients (open source, FHIR output) and five payers' published policy PDFs for one order type, such as knee MRI or a biologic.
**Market:** Practice administrators and revenue cycle leaders at specialty groups and MSOs; an existing buyer category. Vendors hiring engineers on their own boards or YC job pages on 24 October 2026: Commure (Athelas) had a Forward Deployed Engineer ($130K–$190K) and a Senior FDE in Mountain View, plus Applied AI RCM, Claims Intelligence and Billing Agents engineers. Cair Health had a founding FDE on its YC job page (remote US, $110K–$130K) and lists clinics and MSOs as customers. Candid Health had a Forward Deployed Software Engineer (listed since November 2025) and an AI/ML Engineer. SuperDial had a tech lead and Infinitus a Forward Deployed Product Manager, both working payer phone calls. The payer side of the same request is [[health-insurance-carriers|Health Insurance Carriers]], and hospitals' scheduled-service authorization is in [[general-hospitals|General Hospitals]].

---

## 2. Front-Desk Voice and Scheduling Agent
#ai-agent #large-language-models #transformers #gradient-boosting #worker-facing #automation

**Concept:** An agent that answers the practice's phones and texts. It books, reschedules and cancels against the real template rules (visit types, new-patient holds, referral requirements, procedure prep), answers referral-status and billing questions, takes refill requests into a structured queue and verifies insurance before the visit. It hands upset, clinical or unusual calls to a person with a summary, and fills late cancellations from a waitlist ranked by no-show risk.
**Inputs:** PM schedules and template rules, patient records, payer eligibility responses, call audio and texts, waitlists, no-show predictions.
**Outputs / Actions:** Booked and rescheduled appointments; resolved routine calls; warm transfers with summaries; refill and message tickets; eligibility flags before arrival; filled cancellations.
**Why now:** Real-time voice models now hold safe, scripted conversations, and EHR scheduling APIs are open enough to write to. Receptionists earn a mean $18.20 an hour (BLS) and turn over quickly.
**Market:** Practice administrators, specialty groups and MSOs. Assort Health, which began with specialty scheduling, had a Forward Deployed Engineer ($155K–$210K), a Senior FDE ($190K–$240K) and a Head of Forward Deployed Engineering open in San Francisco, and says it raised a $120M Series C at a $1.2B valuation. Hello Patient was hiring Software Engineers II in Austin and New York ($120K–$160K). Hippocratic AI had FDE roles in Menlo Park and remote US, though it sells mainly to health systems and payers. Overflow and after-hours answering for practices is a separate buyer, profiled in [[answering-services|Telephone Answering Services]].

---

## 3. Referral Intake and Closure Agent
#ai-agent #large-language-models #graph-neural-networks #survival-analysis #data-integration #revenue-impact

**Concept:** For a specialty practice, an agent that reads every inbound faxed or e-faxed referral packet. It extracts the patient, the reason, insurance and urgency, checks the referral and authorization requirements, asks the sending office for anything missing, and books the first visit. For a primary care group it works the other side: it tracks every outbound referral to a kept visit, chases the specialist for the consult note, and flags urgent referrals that have lapsed.
**Inputs:** Fax and e-fax streams, Direct messages, referral orders, payer referral rules, specialist schedules, consult notes, claims for out-of-network completions.
**Outputs / Actions:** Structured referral records; requests for missing documents; scheduled first visits; lapsed-referral alerts; closed-loop consult notes filed to the PCP chart; leakage reports by destination.
**Why now:** Document models now read messy multi-page faxes reliably enough to act on. Value-based contracts pay for keeping referrals in network and penalise lapsed ones.
**Market:** Specialty practice administrators and value-based primary care groups. Tennr, which automates referral paperwork for provider groups and health systems, had a Sr. Forward Deployed Engineer in New York ($160K–$180K plus bonus) and a Senior Backend Engineer (ML) open. Home health has its own version of the same intake work in [[home-health-agencies|Home Health Agencies]].

---

## 4. Visit-to-Claim Documentation and Value-Based Gap Platform
#ai-platform #large-language-models #bert #logistic-regression #compliance #revenue-impact

**Concept:** A platform that turns the visit conversation into a signed note. It proposes the E/M level the documentation supports and the chronic conditions assessed, each with evidence. It surfaces the open quality gaps and risk-adjustment suspects for the patient in the room, from claims and prior records, before the visit ends. It keeps an audit trail so every code and gap closure can be defended.
**Inputs:** Ambient audio and transcripts, chart history, claims and payer gap lists, quality measure specifications, coder audit outcomes.
**Outputs / Actions:** Signed notes; E/M and HCC suggestions with evidence spans; pre-visit gap summaries; MIPS and ACO quality capture; audit-risk reports by clinician.
**Why now:** Ambient scribes became mainstream, and athenahealth now bundles athenaAmbient at no extra subscription cost (HIT Consultant), so stand-alone note writing is turning into a commodity. The value moves to coding defensibility and gap closure, where the Shared Savings Program's 511 ACOs and MA risk contracts pay.
**Market:** CMIOs, medical group presidents and ACO leaders. Hiring on 24 October 2026: Ambience (Senior ML Engineer, Staff ML Engineer for Frontier AI, Clinical AI Researcher), Abridge (Member of Product Staff, Forward Deployed), Commure (Ambient AI backend and fullstack engineers), Suki (Senior AI Engineer), Healthie, an EHR and practice platform for virtual-first and specialty practices (Forward Deployed Engineer, New York), and Aledade, which runs value-based contracts for independent primary care (Staff Software Engineer for its AI platform, Data & Algorithm and Risk engineers, all remote US). The ambient vendors as a category are profiled from the vendor side in [[document-preparation-services|Document Preparation Services]].
