# Tenant Retention Prediction and Proactive Renewal Outreach

**Industry:** [[property-management|Property Management]]
**Type:** High Impact
**One-liner:** Property managers who rely on tenant renewal decisions made at the lease expiration date — with no early warning of which tenants are at risk of non-renewal — get a 90-day renewal probability score for every upcoming lease expiration, enabling proactive engagement that reduces vacancy turnover costs.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact

## The Problem

Tenant turnover is the most expensive event in residential property management: cleaning, repainting, appliance repair, leasing agent commission, and vacancy days combine to a cost of $1,500-$4,000 per unit turnover. Property managers currently have no visibility into which tenants are likely to not renew until they receive the official non-renewal notice — typically 30-60 days before lease expiration, too late to do much about it.

The signals of non-renewal risk exist in the property management system months before the decision: maintenance request frequency and types (a tenant who stops requesting maintenance may be disengaging or preparing to move), rent payment timing (late payments in the final months of tenancy predict non-renewal), lease inquiry patterns (a tenant who requests a copy of their lease may be reviewing exit rights), and engagement with communication from the property manager.

## Why It's High Impact

For a property manager with 200 units at $1,200 average monthly rent and 35% annual turnover rate (70 turnovers/year), the turnover cost is $105,000-$280,000 annually. Reducing the turnover rate from 35% to 30% through proactive retention outreach saves $7,500-$20,000 annually. At 1,000 units under management, the impact is $37,500-$100,000 annually in avoided turnover cost.

The intervention is simple: contact at-risk tenants 90-120 days before lease expiration with a renewal offer, address maintenance concerns proactively, and offer a lease renewal incentive (1 month at reduced rent, appliance upgrade). This outreach regularly converts non-renewing tenants to renewers — but only when done early enough, and only if the property manager knows who to contact.

## What a Solution Looks Like

A renewal risk score per tenant in AppFolio or Buildium, updated monthly, that surfaces: (1) tenants with upcoming lease expirations and low renewal probability; (2) the primary signals driving the low score; (3) a recommended outreach action per tenant (proactive maintenance resolution, renewal incentive offer, direct call from property manager). The property manager works through the at-risk list each month, making outreach calls with context from the model.

## Implementation Path

AppFolio or Buildium data is the training foundation. Any property management firm with 3+ years of tenant history (payment records, maintenance requests, renewal/non-renewal outcomes) has training data. Gradient boosting on tenant features: 4-6 week modeling project. AppFolio has the scale and integration path to make this a platform feature.
