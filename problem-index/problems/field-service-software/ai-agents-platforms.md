# AI Agents & Platform Opportunities — Field Service Software

**Industry:** [[field-service-software|Field Service Software]]

---

## 1. Dispatch Agent
#ai-agent #gradient-boosting #bert #convex-optimization #evaluation-metrics #workflow-orchestration #revenue-impact #automation

**Concept:** An agent that owns the dispatch board's arithmetic and leaves the judgement with the dispatcher. It predicts the likely fault from the customer's description and the address history, derives the probable parts and duration, ranks available technicians by demonstrated outcomes on that equipment and failure class, and proposes assignments with the reasoning shown. Through the day it re-optimises on every disruption — an overrun, a call-out, a no-heat emergency — and presents the best recovery options with the cost of each, rather than requiring the dispatcher to rebuild the plan mentally. It learns the informal constraints from overrides rather than from a settings page.

**Inputs:** Incoming call text; address service history; equipment make, model and age; technician locations, skills and truck inventory; the day's committed windows; drive times; historical dispatcher overrides.

**Outputs / Actions:** Ranked assignment proposals with predicted fault, parts and duration. Automatic re-planning on disruption with costed options. Customer window-change messaging on approval. Parts pick lists per technician per day. It proposes; the dispatcher approves. It never silently reassigns a committed window.

**Why now:** The service history corpus that makes fault and duration prediction possible has been accumulating in these platforms for a decade and has never been modelled. Optimisation was always available and always rejected, because it optimised without the constraints that matter — learning those from override history is what changes the outcome.

**Market:** Residential and commercial trades running five or more technicians, which is roughly where a dedicated dispatcher appears. Sold through the platform vendors, whose own competitive position rests on first-time fix rate claims they currently cannot substantiate.

---

## 2. Technician Field Assistant
#ai-agent #large-language-models #cnns #object-detection #transformers #evaluation-metrics #automation #worker-facing

**Concept:** An agent that removes the truck paperwork. The technician photographs the data plate, the failed component and the completed work, and speaks a two-sentence summary. The agent identifies the equipment from the plate, retrieves the model's known failure modes and this address's history, recognises parts from photographs and scans, writes the visit narrative in the format the office needs, pre-fills the checklist where a photograph evidences the item, builds the priced invoice from the task and parts, and drafts the follow-up recommendation from what was observed. The technician reviews, corrects and signs.

**Inputs:** Photographs; spoken summary; parts scans; the price book; equipment history for the address; the vendor's cross-contractor failure corpus for that model; warranty status.

**Outputs / Actions:** A completed visit record with narrative, parts, photographs and checklist. A priced invoice ready to present. A drafted follow-up recommendation with the observed evidence attached. Inventory decrements from recognised parts. Warranty claim initiation where the equipment is in period. It signs nothing on the technician's behalf and flags anything it inferred rather than observed.

**Why now:** Plate reading under bad conditions, part recognition and narrative generation from a spoken summary have all crossed the threshold where reviewing is faster than typing. The economics were always overwhelming — an hour a day per technician, unpaid, in a trade that cannot recruit.

**Market:** Every field service platform, and the trades directly at scale. Retention is the sales argument rather than efficiency, which reaches the owner rather than the operations manager and is a far shorter conversation.

---

## 3. Installed Base Intelligence Platform
#ai-platform #gradient-boosting #survival-analysis #cnns #evaluation-metrics #confidence-intervals #data-integration #revenue-impact

**Concept:** A platform that turns the vendor's cross-contractor service history into a model-level reliability corpus for the installed base — what fails, on which equipment, at what age, in which climate, and what it costs to fix. No manufacturer holds this beyond its own warranty window and no contractor holds enough of it. From that corpus follow the things contractors most want: which equipment to recommend, when to advise replacement rather than repair, which service agreements are profitable at which price, and which units in their own base are approaching predictable failure.

**Inputs:** Service visit history across contractors with equipment make, model, age, failure category, parts, cost and outcome; climate by geography; install dates; replacement events; service agreement records.

**Outputs / Actions:** Survival curves per component per model. Repair-versus-replace guidance with the cost curve behind it. Proactive service targeting — which units in a contractor's base are due for a predictable failure this season. Service agreement pricing grounded in expected cost by equipment profile. A brand reliability view the contractor can use in purchasing conversations.

**Why now:** The corpus reached a size where model-level survival estimation is statistically meaningful, and nobody noticed because the data was being used to print invoices. It is also the only asset in the category a competitor cannot replicate by shipping a feature.

**Market:** Field service platform vendors as the natural owner; secondarily manufacturers, distributors and home warranty companies, all of whom would pay for cross-brand service-life data that does not otherwise exist. The contractor-facing product sells on proactive revenue rather than cost savings, which is the easier pitch.
