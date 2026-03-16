# AI Agents & Platform Opportunities — Moving Companies

**Industry:** [[moving-companies|Moving Companies]]

---

## 1. Virtual Move Survey Agent
#ai-agent #llm #computer-vision #automation

**Concept:** An AI agent that conducts the entire pre-move survey asynchronously via the customer's smartphone. The customer walks through their home guided by voice prompts ("Now show me the bedroom closet... can you open the garage door?"), and the agent identifies, counts, and classifies items in real-time, asks clarifying questions ("Is that piano a baby grand or upright?"), flags access challenges ("I see a narrow spiral staircase — is that the only way to the second floor?"), and generates a complete cube sheet with photos, inventory, and access notes. The estimator reviews the agent's output and adjusts rather than conducting the survey from scratch.

**Inputs:** Smartphone video stream (customer-guided walkthrough), voice responses to agent questions, structured move details (origin address, destination address, move date).
**Outputs / Actions:** Complete inventory list with item categories and estimated volumes, access condition report (stairs, elevator, walk distance, parking), photo documentation linked to each room, draft cube sheet ready for estimator review, auto-generated binding or not-to-exceed quote using company pricing rules.
**Why now:** Vision-language models (GPT-4V, Gemini) can identify household items and spatial layouts from video with sufficient accuracy for initial classification. LLM-powered voice agents can conduct natural conversations that adapt to what the camera sees. Edge inference on modern smartphones eliminates the need for cloud round-trips during the walkthrough.
**Market:** 15,000+ independent moving companies in the US, plus van line agents. Each estimator conducts 5-15 surveys per week; replacing even half with virtual surveys saves 10-30 hours per estimator weekly. Priced as SaaS at $200-500/month per estimator seat, the addressable market is $50-150M annually.

---

## 2. Crew Dispatch and Schedule Optimization Agent
#ai-agent #ai-platform #workflow-orchestration #automation

**Concept:** An autonomous dispatch agent that takes the daily or weekly move manifest and produces optimized crew-truck-route assignments, then manages the schedule in real-time throughout the day. When a morning move runs long (crew texts "need 2 more hours"), the agent automatically recalculates downstream assignments, notifies affected customers with updated windows, reassigns available backup crew if needed, and alerts the dispatcher only when human judgment is required (e.g., a customer threatens cancellation). It replaces the dispatcher's whiteboard with a living plan that adapts continuously.

**Inputs:** Move bookings with estimated scope, crew availability and skill profiles, truck fleet status (location, capacity, maintenance), real-time updates from crews (check-in/check-out, delay reports), customer communication preferences, traffic and weather data.
**Outputs / Actions:** Optimal daily crew-truck-move assignments, automated customer notifications (ETAs, schedule changes), crew dispatch messages with route and loading instructions, escalation alerts to human dispatcher for exceptions, end-of-day performance reports (on-time rate, utilization, overtime).
**Why now:** LLM agents can handle the natural-language communication layer (customer texts, crew updates) while constraint-optimization engines handle the mathematical scheduling. The combination was not practical before 2024 because the communication and reasoning layers required human dispatchers. Modern fleet telematics (Samsara, KeepTruckin) provide the real-time location and HOS data feeds the agent needs.
**Market:** Any moving company running 5+ trucks daily faces dispatch complexity that grows combinatorially. Mid-size movers (10-50 trucks) spend $150,000-400,000 annually on dispatch staff. Priced at $500-2,000/month based on fleet size, targeting the 3,000+ US movers with 5+ trucks — a $50-100M addressable market.

---

## 3. Claims Processing and Settlement Agent
#ai-agent #computer-vision #compliance #automation

**Concept:** An end-to-end claims agent that handles damage claims from initial customer report through settlement offer. When a customer submits a damage claim (via photo upload and description), the agent matches destination photos against origin photos using image comparison models, assesses whether damage is consistent with transit (vs. pre-existing or normal wear), calculates liability based on the customer's selected valuation tier and the item's declared value, drafts a settlement offer letter that complies with FMCSA timelines (30-day acknowledgment, 120-day resolution), and presents the complete case to a claims manager for approval. For straightforward cases (clear transit damage, full-value coverage, item value under $500), the agent processes the claim autonomously.

**Inputs:** Customer-submitted damage photos and description, pre-move inventory photos from the survey or crew documentation, move contract (valuation tier, declared values, special items list), FMCSA regulatory rules and company settlement policies, historical claims data for similar items and damage types.
**Outputs / Actions:** Damage assessment report with photo comparison evidence, liability calculation with regulatory citation, draft settlement offer letter, automated acknowledgment email to customer within 24 hours, case file ready for manager review, payment processing trigger for approved settlements.
**Why now:** CNN-based image comparison can reliably detect new scratches, dents, and breaks when given before/after photos of the same item. LLMs can generate compliant correspondence that references specific regulatory requirements. The combination allows a claims workflow that previously required a trained adjuster to handle the straightforward 60-70% of cases autonomously.
**Market:** Long-distance movers process 50-500 claims annually, each consuming 4-8 hours of staff time. The 2,000+ FMCSA-registered household goods carriers represent the primary market. Priced per-claim ($25-75) or as a monthly subscription ($300-1,000), the addressable market is $20-50M annually.
