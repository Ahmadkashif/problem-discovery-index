# Insurance Eligibility Pre-Verification for Recurring Orders

**Niche:** [[niches/medical-supply-retail/recurring-supply-fulfillment/profile|Recurring Supply Fulfillment]]
**Industry:** [[industries/medical-supply-retail|Medical Supply Retail]]
**Type:** Fix (Pain Point)
**One-liner:** Suppliers call patients for resupply orders only to discover during order processing that the patient's insurance has changed, lapsed, or no longer covers the product — wasting the outreach call and disappointing the patient.
**Tags:** #automation #data-integration #compliance #revenue-impact #quick-win

## The Problem
A customer service rep calls a CPAP patient for resupply, confirms the order, and enters it into Brightree. During order processing (1-3 days later), the billing team discovers: the patient's insurance changed from UnitedHealthcare to Aetna (different coverage rules, different authorization requirements), or the patient's Medicare Part B is inactive (they didn't pay premiums), or the product requires a new prior authorization under the current plan. The order is put on hold, the patient is called back to provide new insurance information, and the process restarts — wasting the original outreach call and creating a 1-2 week delay. This happens on 8-12% of recurring orders.

## Why It's Still Broken
Insurance eligibility verification (EDI 270/271 transactions) is technically automatable, but most suppliers run eligibility checks at order entry — after the patient has already been called and confirmed the order. Running eligibility checks before outreach (to identify patients with coverage issues before calling them) would prevent wasted calls, but the outreach system and the billing system are disconnected: the outreach list is generated from order history dates, not from real-time eligibility data.

## What a Fix Looks Like
An automated pre-outreach eligibility check that runs 24-48 hours before the patient appears on the outreach list: pull eligibility via EDI 270 for each patient's insurer, flag any changes (plan change, inactive coverage, benefit exhaustion), and route flagged patients to a separate workflow (resolve coverage issue before calling for resupply). Clean patients proceed to outreach with confirmed eligibility. The system also detects patients who have switched to an insurer that requires new prior authorization, triggering the auth process before the resupply call so authorization is in place by the time the patient orders.

## Who Feels the Pain
Customer service reps who complete an outreach call and order entry only to have the order rejected for coverage issues, requiring a second call to the patient. Billing specialists who process orders that fail eligibility and must be reworked. Patients who confirm an order and then receive a call back days later saying it can't be processed.

## Impact If Fixed
Eliminates 8-12% of wasted outreach calls by identifying coverage issues before calling. Saves 15-20 minutes per affected order in re-contact and rework time. Reduces patient frustration from order rejections after confirmation — a key driver of patient churn to online DME competitors. On 500 monthly outreach calls, preventing 50 eligibility failures saves 12-15 hours of staff time and retains 5-10 patients who would have churned from frustration.
