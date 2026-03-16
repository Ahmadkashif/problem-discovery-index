# Injectable and Consumable Inventory Management

**Industry:** [[med-spas|Med Spas]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic inventory management can track stock levels, but it doesn't know that a reconstituted Botox vial expires in 24 hours, that half-used Juvederm syringes must be tracked per patient for their next visit, that Sculptra requires 72-hour advance reconstitution, or that a single expired vial of Radiesse represents $350 in waste.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml

## The Problem
Med spa inventory management is uniquely complex because of three factors that generic inventory systems don't address. First, time-sensitivity: Botox and Dysport must be reconstituted before use and expire within 24 hours (Botox) or 4 hours (Dysport) — so reconstitution must be precisely timed to patient schedules, and any last-minute cancellation after reconstitution means waste. Second, partial-use tracking: dermal filler syringes are partially used during treatment, and the remaining product is stored labeled for the specific patient's next visit (FDA and state regulations govern this practice) — creating a secondary inventory of patient-specific partial products. Third, high unit costs: a single vial of Sculptra costs $400+, Juvederm Voluma is $500+ per syringe, and even Botox at $600-$800 per 100-unit vial means every waste event is significant.

## What Already Exists
Aesthetic Record and PatientNow track treatment product usage per patient. Generic inventory systems (Lightspeed, Square for Retail) handle purchase orders and stock levels. Allergan's Allé and Galderma's ASPIRE loyalty programs track units purchased and administered. No system combines demand forecasting (how many units will be needed next week based on the appointment schedule), reconstitution timing optimization (when to reconstitute Botox based on tomorrow's schedule and cancellation probability), partial-use tracking (which patients have stored product and when they're due back), and expiration management (which products expire soonest and need to be prioritized for use).

## The Customisation Gap
A med spa inventory system needs to: (1) forecast weekly demand by product based on upcoming appointments, provider preferences, and historical usage patterns, (2) optimize reconstitution timing — recommending when to prepare Botox/Dysport based on the next day's schedule and no-show probability, (3) track patient-specific stored product with return-visit scheduling to ensure stored filler is used before expiration, (4) manage manufacturer loyalty programs and rebate tracking (Allé, ASPIRE, Evolus rewards) to optimize purchasing timing, and (5) alert when products approach expiration with recommendations to schedule appropriate patients or adjust ordering.

## Impact If Solved
Reduces product waste from 8-12% to 2-4% of total inventory cost, saving $15K-$40K annually for a mid-size practice. Eliminates the $200-$500 per-event waste from reconstituting Botox before a patient cancels. Improves stored-product utilization by ensuring patients with remaining filler are contacted and scheduled before product expires. Optimizes manufacturer rebate capture by aligning purchase timing with rebate thresholds.
