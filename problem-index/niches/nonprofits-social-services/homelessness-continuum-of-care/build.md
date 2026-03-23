# Real-Time Bed & Service Matching

**Niche:** [[niches/nonprofits-social-services/homelessness-continuum-of-care/profile|Homelessness Continuum of Care]]
**Industry:** [[industries/nonprofits-social-services|Nonprofits Social Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform today can match a homeless individual's specific needs (medical, behavioral health, family composition, pets, criminal history) against real-time bed availability across a 30-agency CoC network.
**Tags:** #recommendation #ranking #tabular-ml #data-integration #ai-agent

## The Problem
When a coordinated entry worker assesses someone experiencing homelessness, they must find the best available placement from across the entire CoC — emergency shelter, transitional housing, rapid rehousing, or permanent supportive housing. Each provider has different eligibility criteria (sex, age, family status, sobriety requirements, sex offender restrictions, pet policies), and bed availability changes by the hour. Workers currently call 5-10 providers to find a match, a process that takes 2-4 hours and often results in suboptimal placements because the worker didn't know about an available bed at a provider they didn't call.

## Why Nobody Has Built This
Real-time inventory requires every provider to update bed availability in a shared system continuously — a behavior change that's proven extremely difficult to enforce across independent agencies with different staffing levels and technology comfort. Additionally, matching logic must handle complex eligibility rules that vary by provider and often include subjective criteria ("we can accommodate behavioral health clients if they're medication-compliant") that resist simple rule encoding.

## What to Build
A real-time bed matching platform where providers update availability via a simple mobile app (one tap: "bed available" / "bed occupied"), and coordinated entry workers search available beds by client characteristics. The matching engine applies provider eligibility rules automatically, ranks matches by suitability (proximity, service alignment, housing first principles), and handles the referral workflow — including waitlist management when no immediate match exists.

## Target Customer
CoC lead agencies managing coordinated entry across 20+ providers, serving 5,000+ individuals annually. There are 400 CoCs in the US.

## Impact If Built
Reduces time-to-placement from 4 hours to 30 minutes, increases appropriate placement rate from 60% to 85%, and prevents 20-30% of returns to homelessness caused by mismatched initial placements.
