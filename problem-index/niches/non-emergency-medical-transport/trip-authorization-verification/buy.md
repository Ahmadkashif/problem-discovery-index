# Authorization-to-Dispatch Compliance Gate

**Niche:** [[niches/non-emergency-medical-transport/trip-authorization-verification/profile|Trip Authorization Verification]]
**Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** NEMT dispatch systems allow trips to be dispatched without verified authorizations, creating unbillable trips that the provider discovers only when the claim is denied weeks later.
**Tags:** #compliance #automation #workflow-orchestration #revenue-impact

## The Problem
Dispatchers face constant pressure to get vehicles moving on time — a 7am dispatch window leaves no room for pausing to verify authorizations on 30 vehicles. Current dispatch software allows any trip to be dispatched regardless of authorization status, relying on the assumption that the scheduler verified the authorization the previous day. In practice, 5-8% of dispatched trips lack valid authorizations: the scheduler forgot to verify, the authorization expired overnight, or the trip was added last-minute without verification. Each unauthorized trip costs $50-$150 in unbillable driver time, fuel, and vehicle wear — costs the provider discovers only 30-45 days later when the claim is denied.

## What Already Exists
Healthcare scheduling systems (Epic, Cerner) enforce authorization verification before scheduling procedures — a clinician cannot schedule a surgery without a verified prior authorization. NEMT dispatch platforms (TripMaster, CTS, RouteGenie) store authorization numbers but do not enforce verification status as a dispatch prerequisite. Compliance workflow tools (Jira, ServiceNow) gate process steps but are not built for NEMT operations.

## The Customization Gap
NEMT dispatch needs an authorization compliance gate: a trip cannot move to "dispatched" status unless its authorization status is "verified" — confirmed within the past 24 hours against the broker's system. Trips with unverified or expired authorizations are blocked from dispatch and flagged for scheduler resolution. The gate must be flexible enough to allow emergency overrides (with a compliance officer's approval and an audit log) for urgent trips where authorization verification is pending. The verification timestamp and source must be stored as part of the trip record for audit purposes.

## Target Customer
NEMT operations managers and compliance officers who know that 5-8% of dispatched trips lack valid authorizations but have no system to prevent unauthorized dispatch.

## Impact If Solved
Prevents 5-8% of trips from being dispatched without authorization, saving $30K-$100K annually per provider in unbillable trip costs. Creates an audit trail that demonstrates proactive compliance — increasingly important as Medicaid programs tighten NEMT oversight.
