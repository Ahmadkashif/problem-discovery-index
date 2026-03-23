# Custom-Cut Specification Errors in Order Processing

**Niche:** [[niches/restaurant-suppliers/independent-protein-suppliers/profile|Independent Protein Suppliers]]
**Industry:** [[industries/restaurant-suppliers|Restaurant Suppliers]]
**Type:** Fix (Pain Point)
**One-liner:** Custom-cut protein orders pass through 3-4 handoffs (chef to rep via phone, rep to office via text, office to cutting room via ticket) — and each handoff degrades specification accuracy, resulting in 5-10% of custom-cut orders arriving at the restaurant wrong.
**Tags:** #nlp #text-classification #data-integration #worker-facing #automation

## The Problem
A chef calls the sales rep: "I need 20 strips at 14, 10 filets at 8, and 15 pounds of stew meat in 1-inch cubes." The rep texts the office: "Tonys - 20 NY 14oz, 10 filet 8oz, 15lb stew 1in." The office enters into the ERP: "20 x Strip Steak 14oz, 10 x Filet Mignon 8oz, 15 lb Stew Meat Cubed." The cutting room receives a ticket: "Strip 14oz x20, Filet 8oz x10, Stew cubed 15lb." At each handoff, specification detail can be lost or misinterpreted. Did the chef mean bone-in or boneless strip? Center-cut filet or tenderloin tails? The experienced office staff person who knows Tony's preferences can fill in the gaps — but when the office staff person is out sick, the substitute enters the order literally, and Tony gets bone-in strips instead of boneless.

## Why It's Still Broken
The specification information exists in three places: the chef's head (what they want), the rep's notebook (what they usually order), and the ERP's customer file (what was entered historically). No system connects these three sources. The ERP stores product codes that do not capture custom specifications at the detail level required (thickness, trim level, bone-in/out, aging, packaging). Adding specification fields to the ERP is technically possible but practically impossible — every product would need 5-10 additional specification attributes, and the office staff entering orders would need to verify each attribute on every order.

## What a Fix Looks Like
A custom-cut specification database linked to each customer account: when Tony orders "20 strips," the system auto-populates his saved specification (boneless, center-cut, 14 oz, 3/4" thick, trimmed to 1/4" fat cap, individually vacuum-sealed). The cutting room ticket includes the full specification rather than the abbreviated description. Deviations from the saved spec are flagged ("Tony usually orders 14 oz strips — this order says 16 oz. Confirm with rep?"). The specification database is built over time from order history and rep input, and the chef can view and modify their specs through the ordering portal.

## Who Feels the Pain
Chefs who receive 14 oz bone-in strips instead of 14 oz boneless strips and must send them back — disrupting prep and the dinner service. Cutting room staff who cut product to specification only to learn it was the wrong specification, wasting product worth $15-$50/lb. Office staff who take the blame for miscommunication between the rep and the cutting room.

## Impact If Fixed
Custom-cut specification errors reduced from 5-10% to under 1% of orders. Re-cut and re-delivery costs saved: $500-$2,000/week for a mid-size protein supplier. Customer satisfaction improves — getting the cut right the first time is the single most important service quality indicator in protein supply. Cutting room waste from incorrect cuts reduced by 3-5%, recovering $30K-$80K annually in wasted product.
