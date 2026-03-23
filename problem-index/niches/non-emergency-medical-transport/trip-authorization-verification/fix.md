# Post-Schedule Authorization Changes

**Niche:** [[niches/non-emergency-medical-transport/trip-authorization-verification/profile|Trip Authorization Verification]]
**Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Fix (Pain Point)
**One-liner:** Brokers modify or cancel trip authorizations after the NEMT provider has already scheduled and routed the trip, but providers have no way to detect these changes until the claim is denied.
**Tags:** #automation #data-integration #compliance #revenue-impact

## The Problem
A scheduler verifies an authorization on Monday for a Wednesday trip. On Tuesday evening, the broker cancels the authorization (patient's Medicaid eligibility lapsed, the healthcare provider cancelled the appointment, the broker reassigned the trip to a different provider). No notification reaches the NEMT provider. On Wednesday morning, the driver is dispatched, completes the trip, and the provider submits a claim — which is denied because the authorization was cancelled before the trip occurred. The provider has no recourse: the trip was completed in good faith, but the authorization was invalid at the time of service. This post-schedule authorization change problem affects 3-5% of all trips and represents pure revenue loss.

## Why It's Still Broken
Brokers update authorization status in their own systems but have no obligation or mechanism to push change notifications to providers. Provider dispatch systems store authorization data as a static snapshot at the time of scheduling — they do not poll for updates. The only way a provider can detect a post-schedule change is by re-verifying every scheduled trip immediately before dispatch, which is impractical for a fleet departing simultaneously at 7am. Even providers who re-verify find that broker portals are slow and unreliable during early morning peak hours.

## What a Fix Looks Like
A real-time authorization monitoring service that maintains a watch list of all scheduled trip authorizations and polls broker systems for status changes at regular intervals (every 4 hours and at 5am pre-dispatch). When an authorization is modified or cancelled after scheduling, the system immediately alerts the scheduler and dispatcher, preventing the trip from being dispatched. If the cancellation occurs after dispatch but before service, the driver is notified to abort. The system logs the authorization change timeline for use in disputing denials where the provider can demonstrate the authorization was valid at the time of scheduling.

## Who Feels the Pain
NEMT providers who complete 3-5% of their trips against unknowingly cancelled authorizations, billing staff who discover the denials 30-45 days later with no recourse, and drivers who unknowingly complete unbillable trips.

## Impact If Fixed
Prevents 3-5% of trips from being completed against cancelled authorizations, recovering $25K-$75K annually per provider in otherwise unrecoverable revenue. Provides documentation for disputing denials where authorization changes were not communicated, potentially recovering an additional 30-50% of post-schedule-change denials.
