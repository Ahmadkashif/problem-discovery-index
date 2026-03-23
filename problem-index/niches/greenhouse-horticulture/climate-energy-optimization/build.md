# RL-Based Climate Setpoint Optimizer for Commercial Greenhouses

**Niche:** [[niches/greenhouse-horticulture/climate-energy-optimization/profile|Climate & Energy Optimization]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No commercial product uses reinforcement learning to continuously optimize greenhouse climate setpoints — adjusting heating, ventilation, shading, lighting, and CO2 injection to minimize energy cost while maximizing crop quality — despite academic proof that RL agents outperform experienced growers by 15-25% on energy efficiency.
**Tags:** #reinforcement-learning #time-series-forecasting #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
An experienced head grower adjusts greenhouse climate setpoints throughout the day based on a mental model of how weather conditions, energy costs, and crop requirements interact. This model is deeply tacit: the grower who "feels" that tonight's heating setpoint should drop 2°F because tomorrow's forecast is sunny (the morning sun will warm the greenhouse before the crop experiences cold stress) is performing an optimization that accounts for thermal mass, energy cost, and crop growth response — but cannot articulate the calculation. The grower's optimization is local (one setpoint at a time) and conservative (erring toward crop safety over energy savings because a crop loss costs far more than extra heating). An RL agent operating within grower-defined safety bounds can explore the global optimization space 100x faster, discovering energy savings the grower would never test because the risk of manual experimentation on a $2M crop is too high.

## Why Nobody Has Built This
Three barriers: (1) sim-to-real transfer — the RL agent must be trained in simulation first, but greenhouse dynamics vary significantly by structure type, climate zone, crop, and equipment, making generic simulators unreliable; (2) grower trust — no head grower will hand over climate control to a black-box algorithm, so the system must operate as a recommender initially, with the grower approving setpoint changes until trust is established; (3) integration — the optimizer must connect to existing climate computers (Priva, Ridder, Argus) via their APIs, which are proprietary and inconsistently documented. The Wageningen research demonstrating RL superiority used purpose-built research greenhouses with full API access — commercial deployment requires solving the integration problem at each facility.

## What to Build
A software layer connecting to the grower's existing climate computer via API (Priva REST API, Ridder Modbus/TCP, Argus OPC-UA). The system ingests real-time sensor data, weather forecasts, energy price signals, and crop growth measurements. Phase 1 (months 1-6): observational mode — learns the facility's dynamics and the grower's current patterns, identifies the largest energy waste opportunities, and presents them as recommendations ("last Tuesday you heated to 68°F overnight, but the crop only needed 64°F based on the morning forecast — estimated savings: $340"). Phase 2 (months 6-12): constrained optimization — proposes setpoint adjustments within grower-defined bounds, grower approves or rejects, model learns from both. Phase 3 (month 12+): autonomous optimization within expanding bounds as trust grows.

## Target Customer
Head growers and facility managers at commercial greenhouses spending $200K+/year on energy (typically 3+ acres). Approximately 2,000-3,000 US operations at this scale. Price model: shared savings — the system charges 20-30% of documented energy cost reduction.

## Impact If Built
15-25% energy cost reduction, translating to $45K-$200K annually per facility. Crop quality maintained or improved through more precise environmental control. Head grower's climate management time reduced by 30-50%, freeing bandwidth for crop quality and staff management. Across the US greenhouse industry, total addressable energy savings exceed $2B annually.
