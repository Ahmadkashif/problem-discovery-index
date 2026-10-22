# AI Agents & Platform Opportunities — Legal Support Services

**Industry:** [[legal-support-services|Legal Support Services]]

---

## 1. Hard-Serve Planning Agent
#ai-agent #gradient-boosting #survival-analysis #tacit-knowledge-ml #worker-facing #revenue-impact

**Concept:** An agent that sits between the dispatcher and the server on every open job. It scores the address, orders the day's attempts by the windows the subject is most likely home, triggers a skip trace when the attempt pattern says the address is dead, and tells the server when the diligence record is strong enough to ask the court for substituted service. Each one-tap attempt record feeds the model and builds the diligence declaration as the job proceeds.
**Inputs:** Open jobs with deadlines from every source the server works for; attempt logs with GPS, photos and reason codes; skip-trace results; address history from prior jobs; court rules for substituted service.
**Outputs / Actions:** Ranked daily route; address-validity alerts; skip-trace orders; drafted diligence declarations and affidavits; deadline warnings to the attorney when service is unlikely inside the window.
**Why now:** Geotagged, photographed attempts are now routine (mandatory in New York City since the 2010 reforms, and standard on national networks), so the training data exists; phone-side models are cheap enough to run on every attempt.
**Market:** National service networks and multi-server firms first, then the server-software vendors (ServeManager and peers) as a channel to the long tail of one-person firms. Litigators and volume filers benefit through faster service; nobody sells this today.

---

## 2. Graded Prior-Art Search Workbench
#ai-platform #transformers #bert #contrastive-learning #evaluation-metrics #revenue-impact

**Concept:** A platform for patent search houses that keeps every search as structured data — claim elements, queries, classes visited, references with element-level passages and ratings — and grades it later against public outcomes: examiner citations, PCT search report categories, PTAB institution and final decisions. It suggests passages and references during the search from the house's own graded archive and drafts claim charts in each output format.
**Inputs:** The house's past charts and ratings, kept per client because delivered searches are client work product, and pooled only with client consent; live search sessions; full-text patent and non-patent literature; PTAB and patent office outcome data.
**Outputs / Actions:** In-session reference and passage suggestions; structured claim charts in IPR, contention and in-house formats; per-analyst and per-technology recall scorecards; alerts when a new PTAB decision relies on art the house found, or missed, on a patent it has searched.
**Why now:** Semantic patent search is now a commodity; the scarce thing is a graded record of which human calls were right, and the PTAB's shift in 2025 toward fewer institutions makes being right on the first search more valuable.
**Market:** Patent search houses in the US and India, and in-house search groups at large corporate filers; generic AI search vendors compete on retrieval, not on grading.

---

## 3. Filing and Return Packet Agent
#ai-agent #large-language-models #gradient-boosting #automation #compliance #workflow-orchestration

**Concept:** An agent that assembles everything a court or foreign authority will check before a document is submitted: the e-filing envelope with the right case-type and filing codes and fees; the return of service with the elements that court requires for that service method; or, for service abroad, the Hague request with the correct form, translations and copies for that country's Central Authority. It predicts clerk rejections before submission and fixes what it can.
**Inputs:** Draft filings and service records; court e-filing rules and historical rejection notices; state proof-of-service requirements; Hague Convention country practices.
**Outputs / Actions:** Ready-to-submit envelopes and returns; rejection-risk flags with reasons; Hague request packages; status tracking and resubmission when a clerk rejects.
**Why now:** Mandatory e-filing has spread across state courts and generates clean rejection histories; language models can read rejection notices and court rules at the scale this needs.
**Market:** Attorney-service and e-filing service companies, national service networks and litigation support teams at small firms; a fragmented buyer category that already pays per filing.

---

## 4. Guarded Self-Help Filing Assistant
#ai-agent #large-language-models #transformers #compliance #worker-facing #workflow-orchestration

**Concept:** An assistant for legal document preparers and bankruptcy petition preparers that interviews the self-represented customer, fills the court's forms, checks them against local filing requirements, and keeps a record that every step was form completion at the customer's direction, not legal advice. It stops and refers out when the conversation crosses into advice.
**Inputs:** Customer intake answers and documents; state and local court forms; the preparer's registration rules (county registration and bond for California legal document assistants, Arizona certification, 11 U.S.C. §110 for bankruptcy petition preparers); district fee caps.
**Outputs / Actions:** Completed form sets; filing checklists for the customer; an audit trail of who decided what; referral flags to legal aid or a lawyer.
**Why now:** Language models can conduct the interview, but unauthorised-practice rules make an unguarded consumer chatbot a liability; a preparer-supervised tool with an audit trail fits the regulatory line courts and bar regulators are now drawing.
**Market:** Legal document preparers, petition preparers and court self-help centres, serving the self-represented parties in about three-quarters of state civil cases; small, fragmented buyers, best reached through state associations or court partnerships.
