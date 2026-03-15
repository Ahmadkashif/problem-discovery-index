# Greenhouse Horticulture

## Profile
**Category:** Agriculture & Food
**Market Size:** ~$20B annually in US greenhouse/nursery production; includes ornamental plants, vegetables, herbs, cannabis
**Tech Maturity:** Medium — climate control computers (Priva, Ridder, Argus) are standard in commercial greenhouses, but data analytics and ML are nearly absent; most grower decisions are still experience-driven
**Workforce:** Head growers, assistant growers, greenhouse workers, IPM scouts, shipping/logistics coordinators

## Key Pain Themes
Energy cost is the dominant financial pressure — heating, cooling, and supplemental lighting consume 20-30% of production cost, and experienced growers adjust setpoints based on intuition about crop response that they cannot articulate to junior staff. Crop scheduling across multi-zone greenhouses is managed with whiteboards and spreadsheets, leading to dead bench space between crop cycles that directly erodes revenue per square foot. IPM (Integrated Pest Management) scouts walk greenhouse ranges for 4-6 hours daily checking plants one by one for thrips, whitefly, botrytis, and powdery mildew — a task that depends on visual pattern recognition built over years of experience. Wholesale ornamental growers struggle to match live inventory at varying growth stages to buyer orders weeks in advance, because bloom timing and plant sizing are biological processes that generic inventory software cannot model.

## Current Tech Landscape
Climate control computers from Priva, Ridder/HortiMaX, and Argus Controls handle basic setpoint-driven HVAC and shade curtain automation, but none offer predictive optimization or crop-response-aware control. ERP systems like BloomMaster and Picas handle order management for ornamental growers but lack growth-stage inventory tracking. Scouting is done on paper or basic tablet apps (e.g., Bioline's ScoutPro) with no image recognition. Substrate sensor platforms (Grodan GroSens, Meter Group TEROS) collect data but leave interpretation to the grower.

## Problems
- [[problems/greenhouse-horticulture/high-impact|🔴 High Impact: Climate Control Optimization for Energy and Crop Quality]]
- [[problems/greenhouse-horticulture/low-impact-1|🟡 Low Impact: Crop Scheduling and Space Planning for Multi-Crop Greenhouses]]
- [[problems/greenhouse-horticulture/low-impact-2|🟡 Low Impact: Wholesale Order and Inventory Matching for Ornamental Growers]]
- [[problems/greenhouse-horticulture/worker-life-1|🟢 Worker Life: Repetitive Manual Crop Scouting for Pest and Disease]]
- [[problems/greenhouse-horticulture/worker-life-2|🟢 Worker Life: Irrigation System Monitoring and Adjustment]]
- [[problems/greenhouse-horticulture/ml-opportunity|🔵 ML Opportunities]]
- [[problems/greenhouse-horticulture/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Greenhouse horticulture sits at an unusual intersection: the physical infrastructure is already sensor-rich (climate computers log temperature, humidity, CO2, PAR light every minute) but the decision layer is almost entirely human intuition. This creates a massive opportunity for ML systems that can learn from the data streams already being collected. The tacit knowledge problem is moderate — experienced growers and IPM scouts carry pattern recognition skills that take years to develop, particularly around pest/disease identification and climate-crop interaction. Energy optimization via reinforcement learning has the highest dollar-per-greenhouse impact, while computer vision for scouting has the highest labor-hour impact.
