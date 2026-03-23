# Conviction-Aware Resource Matching

**Niche:** [[niches/nonprofits-social-services/reentry-services-providers/profile|Reentry Services Providers]]
**Industry:** [[industries/nonprofits-social-services|Nonprofits Social Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No resource directory today can filter housing, employment, and services by conviction type — a person with a sex offense has fundamentally different resource options than someone with a drug conviction, but all reentry clients are treated identically by existing tools.
**Tags:** #recommendation #data-integration #tabular-ml #automation #compliance

## The Problem
A reentry case manager's first task is matching the client to available resources — housing, employment, treatment, and education. But eligibility for each resource depends heavily on conviction type, time since release, supervision level, and state-specific laws. A client with a sex offense cannot live within 1,000 feet of a school, eliminating 60% of available housing. A client with a felony drug conviction may be ineligible for SNAP in some states. An employer willing to hire someone with a theft conviction may refuse someone with a violent offense. Case managers carry this eligibility knowledge in their heads, and when they leave, the knowledge walks out the door.

## Why Nobody Has Built This
Building a conviction-aware resource directory requires ongoing maintenance of legal restrictions that vary by state, county, and municipality — and change frequently. No resource directory vendor wants to take on the liability of telling a case manager "this housing is available for sex offenders" and being wrong. Additionally, the data about which employers and landlords accept which conviction types is not publicly available — it lives in case managers' personal networks and informal databases.

## What to Build
A resource matching engine where case managers input client profile (conviction type, supervision requirements, geographic restrictions, benefit eligibility) and receive filtered resource options ranked by fit. The system maintains a community-contributed database of employer and landlord policies regarding conviction types, updated by case managers as they learn from each placement attempt. Over time, the system learns which resources successfully place which client profiles.

## Target Customer
Reentry program managers overseeing 5-15 case managers who collectively serve 200-1,000 returning citizens per year. There are 2,000+ reentry programs nationwide.

## Impact If Built
Reduces resource search from 4 hours to 30 minutes per client, increases successful placement rate by 25% by eliminating mis-referrals to conviction-ineligible resources, and preserves institutional knowledge when case managers turn over.
