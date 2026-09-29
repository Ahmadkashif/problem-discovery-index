# AI Agents & Platform Opportunities — Construction Tech Platforms

**Industry:** [[construction-tech-platforms|Construction Tech Platforms]]

---

## 1. Schedule Risk Agent
#ai-agent #gradient-boosting #survival-analysis #time-series-forecasting #evaluation-metrics #confidence-intervals #revenue-impact #workflow-orchestration

**Concept:** An agent that continuously maps field signal onto schedule activities and maintains a live forecast of which activities will slip and why. Every morning it produces a ranked risk list for the project team with the specific driver attached — this activity is exposed because a long-lead submittal has been in review for nineteen days and the fabrication window no longer fits. It watches RFI ageing, submittal rejections, crew presence against plan, change order activity by location, and each subcontractor's historical reliability across the vendor's whole customer base. When a driver is actionable it opens the action: escalating the submittal, flagging the reviewer, proposing a resequence.

**Inputs:** Current and baseline schedule; RFI and submittal registers with status and ageing; daily reports; change orders with location; subcontractor identity and cross-project performance history; weather; reality capture progress data where available.

**Outputs / Actions:** A daily ranked activity risk list with named drivers and forecast intervals. Automatic escalation of the specific documents blocking at-risk activities. A weekly look-ahead for the coordination meeting. An owner-facing forecast where the contract permits. It proposes resequencing; it never changes the schedule of record.

**Why now:** The signals have been captured for a decade and never joined, because the schedule sat outside the platform and the activity mapping was never maintained. Inferring that mapping from text, location and timing is now tractable, and it is the only missing piece.

**Market:** Owners and developers are the honest buyer — they bear the cost of slip and are not exposed by documenting it, unlike general contractors, who face delay-claim discovery. Also sells to construction managers on cost-reimbursable work. Any project above roughly $20M carries enough liquidated damages exposure to justify it on a single avoided slip.

---

## 2. Specification Intelligence Platform
#ai-platform #large-language-models #bert #transformers #word-embeddings #workflow-orchestration #automation #compliance

**Concept:** A platform that reads the project specification the moment it is issued and produces everything downstream that is currently derived from it by hand: the submittal register with sections, types, quantities and review periods; the routing map for each item; the closeout requirements; and a diff against the previous addendum so the team sees exactly what changed. It then answers RFIs against the spec — a large share of RFIs are questions the specification already answers, and retrieving that before routing removes the item entirely.

**Inputs:** Project specifications and addenda; contract documents where they modify review periods; drawings for cross-reference; the platform's historical registers built from comparable specs; prior RFIs and their answers across projects.

**Outputs / Actions:** A drafted submittal register for engineer confirmation. Proposed routing with predicted realistic review durations from cross-project history. Addendum diffs highlighting changed requirements. Suggested answers with citations for RFIs the spec already covers, presented to the project engineer before routing. Coverage warnings where a spec section produced no register entries.

**Why now:** Specification documents are long, structured and already stored by the platform in enormous volume, paired with the registers engineers eventually built from them — a labelled corpus that was sitting there. Extraction quality on this document class is now well past the threshold where review is faster than authoring.

**Market:** General contractors and construction managers of every size; the register task is universal and identically painful at a $5M project and a $500M one. Sells into the same buyer as the core platform, which makes it a natural attach rather than a new relationship.

---

## 3. Field Reporting Agent
#ai-agent #cnns #object-detection #large-language-models #transformers #evaluation-metrics #automation #worker-facing

**Concept:** An agent that assembles the daily report during the day rather than asking for it at the end. It ingests site photographs as they are taken, recognises which trades are working in which areas, pulls crew counts from sign-in or badge data, retrieves weather for the site, collects delivery tickets and logged observations, and drafts the narrative from coordination messages. At the end of the shift the superintendent opens something that is mostly correct, corrects it, adds what only they know, and signs. Every statement in the draft is traceable to an artefact, so the resulting record is stronger evidence than the one it replaces, not weaker.

**Inputs:** Timestamped geotagged photographs; sign-in, badge or gate records; delivery tickets; weather API; project messages and safety observations; the day's planned schedule activities; the superintendent's prior reports as style reference.

**Outputs / Actions:** A drafted daily report ready for review before the shift ends. Flagged discrepancies between planned and observed trade presence, routed to the schedule risk view. A photo index organised by location and activity. It asserts nothing it cannot trace to a source artefact, and it never signs on the superintendent's behalf.

**Why now:** Site photo volume has become enormous and is almost entirely unread by any system. Trade and activity recognition on construction imagery is now good enough to draft from, and the grounding requirement — no claim without an artefact — is what makes it acceptable for a document with evidentiary weight.

**Market:** General contractors and specialty contractors; superintendent shortage is a binding industry constraint and administrative load is the most cited reason people leave the role. Sells on retention and capacity rather than on software features, which reaches a different budget.
