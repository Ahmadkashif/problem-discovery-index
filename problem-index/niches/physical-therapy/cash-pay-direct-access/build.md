# Cash-Pay PT Practice Operating System

**Niche:** [[niches/physical-therapy/cash-pay-direct-access/profile|Cash-Pay / Direct-Access PT]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Cash-pay PT practices get a unified platform handling subscription pricing, session packages, superbill generation, direct-to-consumer marketing attribution, and clinical documentation — replacing the 4-5 disconnected tools they currently duct-tape together.
**Tags:** #feature-engineering #decision-trees #evaluation-metrics #data-integration #revenue-impact #workflow-orchestration

## The Problem
Cash-pay PT is a fundamentally different business model from insurance-based PT, yet no purpose-built software exists for it. A cash-pay practice needs: subscription and package management (10-visit packages, monthly memberships, single-session pricing), automated billing with recurring charges, superbill generation for patients who want to self-submit to insurance for out-of-network reimbursement, direct-to-consumer marketing ROI tracking (which Google Ad campaign brought this $3,000 package purchase?), patient acquisition cost analytics, clinical documentation that prioritizes patient-facing outcome reporting over payer compliance, and scheduling that accommodates 45-60 minute sessions rather than the 20-minute insurance slots. Currently, cash-pay PTs cobble together Calendly for scheduling, Square or Stripe for payments, Google Sheets for package tracking, a generic EMR for documentation, and Mailchimp for marketing — spending hours weekly on manual data reconciliation.

## Why Nobody Has Built This
The cash-pay PT segment is relatively new and still small compared to insurance-based PT. EMR vendors target the larger insurance-billed market because that's where the revenue is — they earn from claim submission volume, which cash-pay practices don't generate. The cash-pay PT business model also varies significantly between practices: some are subscription-based, some sell packages, some charge per session, some offer hybrid models. Building a platform flexible enough to handle all variants while remaining simple enough for a solo PT to operate is a non-trivial product challenge. The market is also geographically fragmented — cash-pay practices cluster in affluent urban and suburban areas but are sparse nationally.

## What to Build
An all-in-one practice platform for cash-pay PT: (1) flexible pricing engine supporting per-session, packages (5/10/20 visits), monthly subscriptions, and hybrid models with automated billing and payment tracking, (2) superbill generator that creates insurance-submission-ready receipts with correct CPT codes and diagnosis codes, (3) patient acquisition tracking connecting marketing spend (Google Ads, Instagram, referral programs) to patient sign-ups and lifetime value, (4) lightweight clinical documentation with outcome measure tracking and patient-facing progress dashboards, (5) scheduling with support for longer session blocks, recurring appointments, and waitlist management, and (6) patient communication tools (appointment reminders, exercise program delivery, re-engagement campaigns for lapsed patients). Single login, single data model, no manual reconciliation.

## Target Customer
Solo and small-group (2-5 PT) cash-pay practices that have opted out of insurance billing entirely and are currently managing operations across multiple disconnected tools.

## Impact If Built
Eliminates 5-8 hours per week of manual tool juggling and data reconciliation for the practice owner. Reduces patient churn by providing visibility into package utilization and automated re-engagement when packages near completion. Enables data-driven marketing decisions by connecting patient acquisition cost to treatment revenue — a capability no cash-pay PT currently has.
