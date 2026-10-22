# AI Agents & Platform Opportunities — Libraries & Archives

**Industry:** [[libraries-and-archives|Libraries & Archives]]

---

## 1. Collection Decision Ledger
#ai-platform #tacit-knowledge-ml #gradient-boosting #survival-analysis #large-language-models #evaluation-metrics

**Concept:** A platform that records every collection decision — buy, quantity, licence, renewal, withdrawal — as a short structured record drafted from the vendor cart and confirmed by the selector in one click, then grades each record against copy-adjusted circulation, holds and licence use. It keeps the selector's track record by subject, format and branch, suggests quantities and renewals with that record attached, and produces a policy-based rationale for any title on demand, which doubles as the starting point for a reconsideration packet.
**Inputs:** Wholesaler and OverDrive cart exports and order histories, ILS circulation and holds at title-branch level, licence terms and expiries, weeding lists, the library's collection development policy, professional review sources.
**Outputs / Actions:** Decision records with reason codes; quantity and renewal suggestions inside the cart; selector and budget-line scorecards for the collection manager; weeding lists ranked by expected future use; title rationales for boards and challenges.
**Why now:** LLMs can draft a decision record from cart and review data cheaply enough that capture no longer depends on the selector's discipline, and the 2023–2025 wave of challenges has made a documented, policy-based rationale something directors want rather than resist.
**Market:** Public library systems with dedicated selectors (an estimated few hundred in the US) and consortia or state libraries buying centrally for small libraries. The ILS vendors and OverDrive are the natural distribution partners and the natural competitors.

---

## 2. E-Resource Renewal Agent
#ai-agent #causal-inference #time-series-forecasting #large-language-models #data-integration #automation

**Concept:** An agent that tracks every licence's renewal date and, a set number of weeks before each, harvests COUNTER usage through SUSHI, reconciles titles against KBART lists and perpetual-access entitlements, checks open-access availability, pulls interlibrary loan history, models cancellation scenarios, extracts the licence's material terms (price cap, text-and-data-mining and AI-use clauses, walk-away rights), and drafts the renew/cancel/renegotiate memo for the collections committee and the consortium.
**Inputs:** Licence documents and invoices, COUNTER and SUSHI credentials, KBART files, ILL data, OA availability services, faculty publication data, consortium deadlines.
**Outputs / Actions:** Renewal calendar with alerts; cost-per-use and post-cancellation demand estimates with ranges; extracted licence terms; draft memo and negotiation brief; updated ERM records.
**Why now:** Licence text extraction and multi-source reconciliation are now accurate enough to automate, and funder open-access mandates (NIH's no-embargo policy from July 2025) are changing the cost of cancellation faster than annual spreadsheets can track.
**Market:** Academic and research libraries and their consortia; competes with ERM modules in Alma and FOLIO and with usage-analysis tools, and differentiates by producing the decision rather than the data.

---

## 3. Archival Processing Agent
#ai-agent #transformers #bert #cnns #compliance #workflow-orchestration

**Concept:** An agent that takes a scanned or born-digital collection and produces a draft processing package: box and folder inventory, date ranges, creators and subjects, a draft finding aid in the archive's own DACS and EAD conventions, sensitive-content flags by page with proposed restrictions and lapse dates, and a digitisation priority list. The archivist reviews and approves at folder level.
**Inputs:** Page images or files, accession records and donor agreements, existing finding aids for house style, restriction policies.
**Outputs / Actions:** Draft finding aid loaded into ArchivesSpace; restriction recommendations with evidence; screening report for publication; processing time estimate per collection.
**Why now:** Handwriting recognition and multimodal models can now read mixed archival material well enough to draft description and flag personal data, which removes the reading bottleneck that has kept about half of archival collections offline.
**Market:** University special collections, government archives working to M-23-07's electronic-records requirement, and historical societies; funded largely through grants and digitisation budgets. Archival software vendors (Lyrasis for ArchivesSpace, Preservica) are the obvious partners.

---

## 4. Cataloguing Copilot
#ai-agent #large-language-models #transformers #k-nearest-neighbors #worker-facing #automation

**Concept:** An assistant inside the cataloguing editor that drafts full records for items with no shared record, proposes subjects, classification and name authorities with evidence, detects duplicate and wrong-edition records before they are created, and checks vendor batch loads for missing or wrong fields before they reach the public catalogue.
**Inputs:** Title-page and contents images, digital text, the library's catalogue, shared catalogue records the library has rights to use, authority files, vendor MARC files.
**Outputs / Actions:** Draft MARC or linked-data records with per-field confidence; duplicate alerts; batch-load quality reports; backlog dashboards by language and format.
**Why now:** Multimodal models can read a title page in any script and propose controlled-vocabulary headings, and the retirement of language-skilled cataloguers has turned backlogs into a staffing crisis rather than a workflow inconvenience.
**Market:** Technical services departments at academic and large public libraries, and cataloguing outsourcers. OCLC and Clarivate are building similar features into their platforms, so an independent product must win on the hard tail — non-Roman scripts, special collections, local materials — or sell through them.
