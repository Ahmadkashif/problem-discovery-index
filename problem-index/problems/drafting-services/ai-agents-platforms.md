# AI Agents & Platform Opportunities — Drafting Services

**Industry:** [[drafting-services|Drafting Services]]

---

## 1. Checker's Copilot for Shop Drawings
#ai-platform #cnns #object-detection #graph-neural-networks #tacit-knowledge-ml #revenue-impact

**Concept:** A platform that sits in the checker's review, captures every markup with its model object and category, and ranks each new sheet's regions and objects by the probability that they hold an error, drawing on the bureau's own past markups and downstream outcomes. It combines codified rules (bolt clearances, edge distances, lap lengths, client standards) with a learned model of where this bureau's senior checkers look, and builds a sheet-level error record over time.
**Inputs:** Shop-drawing and drawing-set PDFs, Tekla, SDS2, Revit or rebar models, checker markups from Bluebeam or the model, engineer review comments, fabricator queries, field-fix and back-charge reports.
**Outputs / Actions:** Ranked review list per sheet with the nearest precedent markups; categorised markup capture; error-escape reports by detailer, client and error type; evidence of checking for fabricators and quality programmes such as NISD's.
**Why now:** Vision models now read engineering drawings well enough to localise symbols and dimensions, model APIs expose object graphs, and early AI checkers such as ClearHandoff show bureaus will pay per sheet; none yet learns the bureau's own checker or joins downstream outcomes.
**Market:** Steel, rebar and MEP detailing bureaus, fabricators with in-house detailing departments and large offshore enterprises; priced per sheet or per ton checked. No existing buyer category beyond checklist tools.

---

## 2. Overnight Markup Desk Agent
#ai-agent #transformers #large-language-models #object-detection #workflow-orchestration #worker-facing

**Concept:** An agent that receives a client's marked-up set before the US day ends, reads every cloud and note, links each to its sheet and element, proposes the implied changes on unmarked sheets, and sends the client a short packet of specific questions while they are still at their desk. The offshore drafter starts the shift with a structured task list, answers attached, and the agent checks the returned set against the list before it goes back.
**Inputs:** Marked-up PDFs, clean sheets and sheet index, prior markups and issued sets for the project, client contact and response history.
**Outputs / Actions:** Task list per sheet; question packet emailed to the client; drafter assignments; a completeness check of the outgoing set against every task.
**Why now:** Vision-language models can read handwriting on drawings and reason about sheet references, which turns the most error-prone handoff in offshore delivery into a checkable step.
**Market:** Offshore drafting enterprises and US bureaus using offshore teams; architects and engineers who send overflow work. Competes with Bluebeam's markup list and email; differentiates by turning markups into verified tasks.

---

## 3. Bureau Bid and Revision Desk
#ai-agent #gradient-boosting #feature-engineering #large-language-models #revenue-impact #automation

**Concept:** An agent that reads a bid set, extracts the drivers of drafting effort, prices the job from the bureau's own history in its chosen unit (per sheet, per ton or hourly) with a stated revision allowance, and drafts the proposal. Once the job is live it tracks every incoming revision against the quoted rounds, classifies each as client-caused or bureau-caused, and drafts change requests for out-of-scope work before the hours are spent.
**Inputs:** Bid and design drawings, client history, past quotes and timesheets, incoming revisions and markups, contract terms.
**Outputs / Actions:** Quote with a confidence range; proposal draft; revision-round ledger; draft change requests; job margin forecast.
**Why now:** Document parsing of drawing sets is now cheap enough to run on every bid, and per-sheet bureaus under offshore and AI price pressure cannot afford unpriced revisions.
**Market:** The ~2,956 US bureaus and the offshore enterprises; small firms are poor buyers individually, so it fits as a module inside a practice-management or marketplace product. Adjacent to construction estimating software, which counts materials, not drafting hours.

---

## 4. Fabricator Detailing Control Tower
#ai-platform #semantic-segmentation #graph-neural-networks #data-integration #workflow-orchestration #compliance

**Concept:** A platform for the buyer of detailing — the steel or rebar fabricator, or the MEP subcontractor — that tracks every package across all its detailing vendors: submittal status against the AISC 303 14-day approval clock or the pour schedule, design revisions received and their affected pieces, engineer comments, shop queries, field fixes and back-charges. It grades vendors on error escapes per ton and turnaround, and flags packages at risk before they reach the shop.
**Inputs:** Detailer transmittals and models, submittal register, design revisions, engineer comments, fabrication and erection schedules, shop queries, field-fix and back-charge records.
**Outputs / Actions:** Package status board with clock alerts; revision impact lists routed to the right detailer; vendor scorecards; back-charge documentation with the originating revision attached.
**Why now:** Model-based detailing and cloud submittal platforms have put all the inputs in digital form, and fabricators spreading work across onshore and offshore bureaus need a way to compare them on more than price.
**Market:** AISC-member fabricators, rebar fabricators and mechanical contractors with prefabrication shops. Adjacent to Tekla PowerFab and Procore, neither of which grades detailing vendors.
