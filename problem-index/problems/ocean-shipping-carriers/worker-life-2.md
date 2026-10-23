# The Service Desk When the Ship Skips a Port

**Industry:** [[ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Worker Life Changing
**One-liner:** When a sailing is blanked, a port is omitted or a whole trade re-routes, customer service agents absorb thousands of angry emails one at a time, and could get back the ability to tell each customer what happens to their box before they ask.
**Tags:** #large-language-models #transformers #time-series-forecasting #gradient-boosting #worker-facing #automation #workflow-orchestration

## The Problem
A carrier announces that next week's sailing is cancelled, that a ship will omit a port to recover schedule, or, as in late 2026, that a trade is moving back from the Cape of Good Hope to the Red Sea. Every affected booking now needs a new plan: which sailing it moves to, whether it transships somewhere new, what the new arrival date is, whether free time changes, whether cut-offs move. The operations centre makes the network decision in hours. Customer service agents, many in shared-service centres working in English on Asian or European night shifts (estimate), then face the consequences booking by booking. They answer "where is my container" emails, re-book cargo, explain charges, and chase colleagues for answers the system does not give them. Schedule reliability of 49.9% in August 2026, with late ships averaging 6.81 days behind (Sea-Intelligence), means this is not an occasional surge. It is the normal week.

## Why It Matters to the Worker
Agents carry the customer's anger for decisions they did not make and cannot explain, often without a reliable new arrival date to give. Volume spikes after every network change and every port congestion episode, and response-time targets do not move with it. The work is repetitive (the same question asked by hundreds of customers about the same ship) and the useful part, helping a customer whose cargo is genuinely at risk, gets buried under the routine. Burnout and turnover in these roles are high (estimate).

## What a Solution Looks Like
When the network changes, generate the consequences for every booking at once: the proposed new sailing and arrival estimate with an honest range, the changes to cut-offs and free time, and a drafted customer message per booking or per account. Agents approve and send in bulk, and the system answers the routine "where is my box" questions from the same plan. Bookings where the change creates real risk are ranked to the top for a person: perishable or high-value cargo, a missed connection, a customer with a contractual service guarantee. The agent's day shifts from retyping the same apology to resolving the cases that need judgement.

## Impact If Solved
A port omission on a 20,000 TEU ship can touch ~2,000–5,000 bookings (estimate). At ~5 minutes per routine reply that is ~170–420 agent hours per disruption (estimate), most of which bulk-approved notices remove. Agents' skill goes to the shipments that most need it, and better arrival estimates cut the demurrage and detention disputes that follow when customers plan around unrealistic dates.
