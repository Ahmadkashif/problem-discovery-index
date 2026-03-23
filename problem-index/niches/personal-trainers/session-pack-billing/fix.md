# Revenue Leakage from Expired Unused Sessions

**Niche:** [[niches/personal-trainers/session-pack-billing/profile|Session Pack Billing & Scheduling]]
**Industry:** [[industries/personal-trainers|Personal Trainers]]
**Type:** Fix (Pain Point)
**One-liner:** Session packs have expiration dates (60-90 days), but trainers don't track them — clients show up months later expecting to use remaining sessions, and the trainer either extends for free (losing revenue) or refuses (losing the client).
**Tags:** #automation #revenue-impact #quick-win

## The Problem
Session pack expiration is a significant revenue lever: a 10-session pack sold for $750 with a 90-day expiration that expires with 3 sessions unused represents $225 in recognized revenue with no delivery cost. But most trainers don't track expiration dates systematically. When a client resurfaces 4 months later saying "I have 3 sessions left," the trainer has two bad options: honor the expired sessions (losing $225 and setting a precedent that expiration doesn't matter) or enforce expiration (losing the client relationship and potential future revenue). Both outcomes are worse than proactive management: alerting the client at 30 and 14 days before expiration that sessions will expire, which motivates usage and prevents the conflict.

## Why It's Still Broken
Trainers set expiration policies when they sell packs but don't have systems to track them. Pack purchase dates live in Venmo transaction history, expiration dates are calculated mentally, and nobody sends proactive alerts. The trainer discovers expiration status only when the client contacts them. Building an expiration tracking system requires connecting pack purchase dates to calendar tracking — a simple feature that no consumer scheduling or payment tool provides. Studio platforms handle this natively, but solo trainers don't use them.

## What a Fix Looks Like
An automated expiration management system that: (1) calculates expiration dates from pack purchase date + pack term, (2) sends automated client alerts at 30 days, 14 days, and 3 days before expiration ("You have 4 sessions remaining — your pack expires March 15. Book now!"), (3) provides the trainer a dashboard showing upcoming expirations across all clients, (4) handles expired packs per the trainer's policy (auto-archive, offer extension at a fee, or convert remaining sessions to a partial-credit on next pack), and (5) tracks expired-session revenue for financial reporting.

## Who Feels the Pain
Trainers who repeatedly face the awkward choice between honoring expired sessions (losing money) and enforcing expiration (losing clients), and who have no data on how much revenue is affected by their inconsistent enforcement.

## Impact If Fixed
Proactive expiration alerts increase session utilization by 15-25% (motivating clients to use sessions before expiration), while consistent enforcement and transparent tracking prevent the $3K-6K/year in revenue lost to post-hoc session extensions.
