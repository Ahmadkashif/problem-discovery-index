# AI Agents & Platform Opportunities — Plumbing & HVAC Distributors

**Industry:** [[plumbing-and-hvac-distributors|Plumbing & HVAC Distributors]]

---

## 1. Plan-and-Spec Selection and Submittal Agent
#ai-agent #large-language-models #transformers #k-nearest-neighbors #cnns #tacit-knowledge-ml #revenue-impact

**Concept:** An agent that reads a commercial bid package — drawings, Division 22 and 23 specs and the engineer's equipment and fixture schedules — extracts every line with its performance requirements, re-selects each in the distributor's own brands at the schedule's design conditions, adds the accessories the drawings imply, prices the package and assembles the comparison sheets and submittal set. It records every selection the specialist accepts or changes, so the desk's approval history becomes its training data.
**Inputs:** Bid PDFs and addenda, manufacturers' performance data and selection-tool outputs, fixture catalogues, the house's price files and project pricing, past submittal responses by engineer.
**Outputs / Actions:** A priced re-selection per schedule line with margin against each requirement; flagged accessories and submittal risks; comparison sheets and submittal packages; a bid-day summary for the specialist to release.
**Why now:** Vision-language models read schedules and drawings well enough to extract structured lines, and the A2L catalogue turnover has made every selection table new at once.
**Market:** Commercial desks at plumbing and HVAC distributors, and the manufacturers' reps who quote applied equipment. Rebar (New York, $14M Series A in March 2026, 40 clients) sells computer-vision HVAC quoting to commercial suppliers and plans plumbing next; on 2026-10-24 it had Software Engineer roles open in New York in Applied AI, ML Infrastructure, Data Platform, Platform Infrastructure and Product, plus HVAC-experienced implementation managers. Straight-resale schedule lines already matched to SKUs belong to the cross-distribution field profiled at [[niches/industrial-distributors/rfq-and-order-intake-automation/profile|RFQ & Order Intake Automation]], where Avent (founding FDE $100K–$130K and founding engineer $120K–$150K, San Francisco), Mercura (FDE, Staff, AI/LLM and Fullstack engineers, Munich only) and Comena (FDE and Fullstack Engineer at €80K–€150K, Munich only) were hiring on their YC pages.

---

## 2. Counter and Text-Order Agent
#ai-agent #cnns #contrastive-learning #large-language-models #worker-facing #workflow-orchestration

**Concept:** An agent that sits on the branch's text line, phone queue and counter screen, reads technicians' nameplate photos and messages, identifies the exact OEM or universal part, checks stock across branches, reserves it for will-call or a runner, confirms refrigerant sales against Section 608 certification, and writes the sale into the ERP for one-tap release. Each confirmation or correction becomes a labelled identification.
**Inputs:** Texts, photos and calls from technicians; model and serial numbers; parts lists and cross-references; multi-branch inventory; customer accounts and certification records.
**Outputs / Actions:** Identified parts with confidence; reservations and will-call tickets; substitution suggestions; escalation to a named counter veteran when confidence is low; ERP sales orders.
**Why now:** Multimodal models read worn nameplates, model-number databases now cover hundreds of manufacturers (Bluon's PartsConnect cites 30M+ model numbers from 240+ OEMs), and texting platforms such as Prokeep have already moved much counter traffic onto phones.
**Market:** HVAC and plumbing branches, sold per branch; Watsco builds its own (HVAC Pro+ apps, ~300 technologists). Augment's Augie, live in Eclipse at Johnstone Supply Heartland Group, starts from sales order entry and is part of the RFQ field; its six openings on 2026-10-24 were go-to-market roles, including a Pre-Sales Engineer and a Deployment Strategist, with no engineering roles. Canals (senior software engineers in San Francisco, Toronto, Santiago, Mexico City, São Paulo, Buenos Aires and Bogotá; an ML engineer in Bogotá) and Proton.ai (engineers in Europe and Latin America) sell adjacent order-entry and sales tools. No vendor yet sells counter identification as its own product to distributors.

---

## 3. Warranty and Returns Agent
#ai-agent #large-language-models #gradient-boosting #logistic-regression #automation #revenue-impact

**Concept:** An agent that turns every warranty replacement at the counter into a claim each manufacturer will pay: it decodes the serial, checks registration and coverage, matches the replacement invoice line, attaches the nameplate and failed-part photos, pre-checks the claim against that manufacturer's rejection history, files it through the portal, tracks the credit and manages the failed-part return or scrap instruction.
**Inputs:** Counter transactions, photos, serial and registration data, manufacturers' warranty terms and portal fields, rejection histories, return authorisations.
**Outputs / Actions:** Filed claims with evidence; flagged high-risk claims for the clerk; credit tracking and ageing; return and scrap tasks; a monthly recovered-versus-abandoned report.
**Why now:** Document and image models extract claim data from photos and texts reliably, and browser agents can file through portals that offer no API; the A2L launch multiplied model numbers and warranty rules at once.
**Market:** Distributor controllers and warranty managers at HVAC, water-heater and boiler distributors; adjacent to manufacturers' own warranty portals and the extended-warranty administrators profiled at [[niches/hvac-contractors/extended-service-contract-administrators/profile|Extended Service Contract Administrators]]. Recovery-share pricing fits because the value is credited dollars. No vendor found selling this to distributors.

---

## 4. Seasonal Allocation and Transition Agent
#ai-agent #time-series-forecasting #temporal-fusion-transformers #monte-carlo-methods #data-integration #revenue-impact

**Concept:** An agent that plans and re-plans branch inventory for heat waves, cold snaps and regulatory cutoffs: it forecasts demand by branch from weather and installed base, buys matched systems as sets on manufacturers' pre-season programmes, moves stock between branches ahead of forecast heat, and runs sell-down plans for products a rule may strand, re-running them when the rule changes.
**Inputs:** Sales, inventory and lost-sales signals; weather forecasts; AHRI match tables; regulatory dates and scenarios; manufacturers' allocations and terms; transfer costs.
**Outputs / Actions:** Recommended buys, transfers and markdowns; alerts when a branch's peak-week coverage falls below target; scenario reports when a regulation moves, as EPA's R-410A installation deadline did in May 2026.
**Why now:** Probabilistic forecasting with weather covariates is cheap to run at branch level, and the 2025–2026 transition showed how much inventory a regulatory date can strand or rescue.
**Market:** Purchasing and inventory directors at regional HVAC and plumbing distributors; adjacent to Netstock, GAINS, Blue Ridge and ERP replenishment modules, none of which plan matched systems against weather and regulation. Ferguson was hiring an IT Manager for AI Platform Engineering & Data Science (remote) on 2026-10-24, a sign that the largest operators build this in-house.
