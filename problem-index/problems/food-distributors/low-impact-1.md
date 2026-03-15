# Route Optimization for Multi-Temperature Delivery

**Industry:** [[food-distributors|Food Distributors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic route optimization treats every stop as identical cargo — food distributors need routing that understands multi-temperature compartments, product handling constraints, and dock-time variability.
**Tags:** #reinforcement-learning #regression #tabular-ml #workflow-orchestration

## The Problem
A food distributor running 40-120 trucks daily must plan routes that satisfy customer delivery windows (restaurants need product by 5:30 AM, hospitals by 7 AM, schools by 6 AM), respect multi-temperature compartment capacity (each truck has frozen, chill, and dry sections with fixed cubic footage), enforce product-specific stacking rules (no heavy cases on soft fruit, dairy upright only), and account for highly variable dock times (a restaurant back-alley delivery takes 8 minutes; a hospital receiving dock with security check-in takes 35 minutes). Current routing tools like Roadnet or Descartes optimize for distance and time but treat cargo as homogeneous and use static stop-time estimates.

## What Already Exists
Roadnet (Omnitracs), Descartes Route Planner, and OptimoRoute all provide strong general-purpose vehicle routing with time windows. They handle basic capacity constraints (weight, cube) and can optimize for fuel cost or total drive time. Some support multi-compartment vehicles as a configuration option, but the compartment logic is static — it does not dynamically reassign compartment splits based on the day's order mix.

## The Customisation Gap
Food distribution routing needs three layers the generic tools lack. First, dynamic compartment allocation: on a heavy frozen day, the divider wall in the truck shifts to give frozen 60% of space instead of the usual 40%, which changes which stops can share a truck. Second, product-handling constraint propagation: if stop #3 adds 12 cases of eggs, the solver must ensure no subsequent heavy-case stop is loaded on top — a packing constraint that interacts with route sequence. Third, learned dock-time models: instead of static 15-minute estimates, the system should predict dock time per customer based on historical actuals (day-of-week, order size, receiving staff availability), which shifts optimal route sequencing significantly for routes with 15-25 stops.

## Impact If Solved
A 10-15% reduction in total route miles and a 20-minute average improvement in driver return time per route, translating to $1.5M-$3M in annual fuel and labor savings for a 60-truck fleet. Tighter delivery windows also reduce late-delivery penalties and customer complaints.
