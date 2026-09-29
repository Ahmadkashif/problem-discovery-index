# Restaurant Tech Platforms

## Profile
**Category:** Vertical SaaS
**Market Size:** ~$12B US restaurant technology (POS, online ordering, back-of-house, labour)
**Tech Maturity:** High and fragmented — Toast and Square own the SMB point of sale, Olo and Otter aggregate digital ordering, 7shifts and Crunchtime handle labour, MarginEdge and Restaurant365 handle back office. Nearly every restaurant now runs five to nine systems that half-integrate, and the resulting data is complete and unjoined.
**Workforce:** Onboarding and menu build specialists, integration engineers, hardware support technicians, data operations staff for item and vendor catalogues, customer success managers

## Key Pain Themes
Restaurant technology has solved transaction capture and failed at prediction, in an industry where the two decisions that determine survival — how many people to schedule and how much food to prep — are both forecasts. Operators make them from last week's numbers and a gut feel about the weather. Platforms hold years of transaction history at fifteen-minute granularity for hundreds of thousands of locations and return a sales report. Underneath that sit two data-plumbing problems the category has never resolved: menu items that must be mapped consistently across the POS, three delivery marketplaces, a website and a kiosk, each with its own modifier structure; and invoice lines from distributors that never match the recipe ingredients they are supposed to cost. Support carries a burden peculiar to the vertical — when the system fails it fails during service, with a queue at the counter, and the person calling is not able to wait.

## Current Tech Landscape
Toast has become the default for independent full-service restaurants with an increasingly broad suite; Square dominates the counter-service and small-format end. Olo, Otter, Deliverect and Chowly bridge the delivery marketplaces into the POS with varying fidelity. Labour scheduling is a crowded category (7shifts, HotSchedules, Sling) where forecasting is universally claimed and rarely trusted. Back-office and inventory (MarginEdge, Restaurant365, Craftable) do invoice capture well and recipe costing partially. Kitchen display systems and prep management remain surprisingly primitive. Loyalty and CRM sit in yet another system.

## Problems
- [[problems/restaurant-tech-platforms/high-impact|🔴 High Impact: Store-Level Demand Forecasting for Labour and Prep]]
- [[problems/restaurant-tech-platforms/low-impact-1|🟡 Low Impact: Menu Item Mapping Across Channels]]
- [[problems/restaurant-tech-platforms/low-impact-2|🟡 Low Impact: Invoice Line to Recipe Ingredient Matching]]
- [[problems/restaurant-tech-platforms/worker-life-1|🟢 Worker Life: Manager Schedule Rebuild Cycle]]
- [[problems/restaurant-tech-platforms/worker-life-2|🟢 Worker Life: Support During Service Failure]]
- [[problems/restaurant-tech-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/restaurant-tech-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
The platform vendor holds the densest consumer demand dataset in the economy that nobody analyses: item-level transactions at minute resolution across hundreds of thousands of locations, joined to weather, local events, day of week, price changes and promotions. A single restaurant cannot forecast because it has one location's history and a thin sample. The vendor has the pooled version of the same question — how does demand for this kind of item, at this kind of location, in this weather, on this day, actually behave — and it is the only party who can answer it. It ships a sales dashboard.
