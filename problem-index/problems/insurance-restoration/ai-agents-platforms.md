# AI Agents & Platform Opportunities — Insurance Restoration

**Industry:** [[insurance-restoration|Insurance Restoration]]

---

## 1. Damage Assessment and Scope Agent
#ai-agent #cnns #transfer-learning #feature-engineering #gradient-boosting #loss-functions #evaluation-metrics #backpropagation #revenue-impact

**Concept:** An AI agent that accompanies the project manager on the initial site inspection via mobile app. As the PM photographs damage and records moisture readings, the agent analyzes visible damage patterns, cross-references property records (build year, construction type, square footage), and generates a predicted moisture migration map with recommended probe points. Once the PM confirms affected areas, the agent auto-generates an Xactimate estimate with carrier-specific line-item formatting, reducing initial scope creation from 2-3 hours to 30-45 minutes while improving accuracy by incorporating construction-type-specific moisture migration predictions.

**Inputs:** Damage photos (geotagged with room location), moisture meter readings (input via Bluetooth or manual grid entry), property data (build year, construction type, floor plan if available), loss details (water source, category, elapsed time), carrier identity and program requirements
**Outputs / Actions:** Moisture migration probability map overlaid on floor plan, recommended probe points for verification, auto-generated Xactimate estimate with carrier-specific formatting, scope risk assessment (probability of supplement needs), equipment deployment recommendation
**Why now:** Multi-modal vision models can analyze water damage patterns from photos. Property data APIs (Zillow, county records) provide construction details. Xactimate API enables programmatic estimate generation. The $5K-$15K per-job cost of scope inaccuracy makes the ROI compelling.
**Market:** 25,000+ restoration companies in the US. Per-job pricing ($25-$75 per scope) or monthly subscription ($200-$500/month). Primary buyers are mid-size companies (50-200 jobs/month) where estimating consistency across multiple PMs is a constant challenge.

---

## 2. Emergency Triage and Dispatch Agent
#ai-agent #large-language-models #transformers #gradient-boosting #feature-engineering #evaluation-metrics #automation #worker-facing

**Concept:** An AI agent that handles incoming emergency calls and web submissions 24/7. The agent conducts structured intake via phone (speech-to-text) or web form, classifying loss severity (immediate dispatch vs. morning response vs. self-service guidance), identifying the appropriate crew based on loss type, proximity, certifications, and current workload, and initiating dispatch with equipment recommendations. For routine losses, the agent dispatches autonomously with PM notification. For complex or large losses, the agent prepares a complete triage brief for PM review and approval.

**Inputs:** Incoming calls (speech transcription), web form submissions, caller/property information, crew availability and location, equipment inventory and deployment status, carrier program SLA requirements, weather and storm event data (for surge capacity planning)
**Outputs / Actions:** Structured loss intake report, severity classification, crew dispatch with equipment manifest, PM notification with triage summary, customer confirmation with ETA, carrier notification where required by program rules
**Why now:** Speech-to-text accuracy enables phone-based intake. LLMs handle the conversational nature of distressed homeowner calls. GPS-based crew tracking enables proximity-based dispatch. The PM burnout crisis (40%+ annual turnover) makes after-hours automation an urgent retention tool.
**Market:** Every restoration company with carrier program obligations (requiring 24/7 response). $150-$300/month per location. The value proposition is PM retention — replacing one PM costs $15K-$25K in recruiting and training.

---

## 3. Equipment Deployment and Monitoring Agent
#ai-agent #gradient-boosting #optimization-fundamentals #time-series-forecasting #feature-engineering #evaluation-metrics #workflow-orchestration

**Concept:** An AI agent that manages equipment allocation across all active jobs. The agent tracks equipment location (GPS/Bluetooth), monitors drying progress through connected moisture sensors or manual readings, predicts when each job will reach clearance dryness, and recommends equipment redeployment as new jobs arrive. When a new water loss is dispatched, the agent automatically identifies the optimal equipment package — pulling units from jobs nearest to drying completion and scheduling delivery from warehouse stock — producing a dispatch manifest with delivery routing.

**Inputs:** Equipment inventory (type, capacity, location, runtime hours, maintenance status), drying progress per job (moisture readings, trend lines, predicted completion), new job requirements (loss type, estimated affected area, equipment needs), crew schedules and routing, warehouse stock levels, equipment maintenance schedules
**Outputs / Actions:** Equipment redeployment recommendations with routing, drying completion predictions with clearance testing scheduling, equipment pull alerts (when a unit has been running past diminishing returns), warehouse restocking alerts, equipment maintenance scheduling, per-job equipment cost tracking for invoicing
**Why now:** IoT sensors on drying equipment are becoming standard (Dri-Eaz's InjectiDry has connectivity, Phoenix offers data logging). GPS asset tracking costs have dropped below $5/month per device. The optimization problem is well-defined once data feeds are in place.
**Market:** Mid-size and large restoration companies with 100+ pieces of equipment. $100-$250/month plus per-device sensor costs. The equipment efficiency gains (15-20% capacity increase without capital expenditure) translate to $50K-$200K annual value for a company with $2M-$10M in equipment assets.
