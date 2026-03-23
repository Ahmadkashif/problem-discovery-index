# Climate & Energy Optimization

**Parent Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Category:** Highly Automatable

## Profile
**Market Size:** $4-6B (embedded — energy represents 20-30% of greenhouse production cost)
**Share of Parent Industry:** ~25% of operating costs
**Digital Adoption:** Medium — climate computers log comprehensive environmental data, but the optimization of setpoints based on that data is entirely manual, performed by the head grower using experienced intuition
**Target Buyer:** Head Grower / Facility Manager responsible for energy cost and crop quality
**Automation Potential:** High — the combination of dense sensor data, well-understood physical models (thermodynamics), and biological crop response data creates an ideal environment for reinforcement learning and model-based optimization

## What Makes This a Distinct Niche
Greenhouse energy management is the single highest-value operational decision domain: a 5-acre commercial greenhouse spends $300K-$800K annually on natural gas, electricity, and propane. The head grower adjusts 8-12 climate setpoints (heating pipe temperature, ventilation temperature, minimum ventilation rate, shade curtain deployment, supplemental lighting thresholds, CO2 injection rate) multiple times per day based on weather forecasts, energy prices, and crop growth stage. This optimization is a multi-objective problem — minimize energy cost while maintaining crop quality, growth rate, and disease prevention — with a state space too large for any human to optimize globally. The grower satisfices: finding "good enough" setpoints through years of experience rather than optimal ones. Academic research (Wageningen University's Autonomous Greenhouse Challenge) has demonstrated that RL agents can outperform experienced growers on energy efficiency by 15-25%, but no commercial product has crossed from research to deployment.

## Current Tools & Gaps
Priva, Ridder/HortiMaX, and Argus Controls provide rule-based climate control with comprehensive data logging. These systems execute setpoints precisely but do not optimize them — the grower is the optimization layer. Energy monitoring systems (Onset HOBO, Dent Instruments) track consumption but do not connect energy use to crop outcomes. The gap: a system that continuously optimizes setpoints based on the actual energy-crop-quality tradeoff surface, learning from each facility's specific dynamics.

## Problems
- [[niches/greenhouse-horticulture/climate-energy-optimization/build|🔨 Build: RL-Based Climate Setpoint Optimizer for Commercial Greenhouses]]
- [[niches/greenhouse-horticulture/climate-energy-optimization/buy|🛒 Buy: Climate Computer Analytics Layer with Energy Benchmarking]]
- [[niches/greenhouse-horticulture/climate-energy-optimization/fix|🔧 Fix: Night Energy Waste from Conservative Heating Setpoints]]
