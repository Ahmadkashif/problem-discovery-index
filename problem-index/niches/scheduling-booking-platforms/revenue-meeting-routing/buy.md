# Entity Resolution and Real-Time Decisioning

**Niche:** [[niches/scheduling-booking-platforms/revenue-meeting-routing/profile|Revenue Meeting Routing]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Real-time decisioning at low latency is routine in advertising and payments, and entity resolution is a settled discipline, and inbound routing runs on a rules form somebody filled in eighteen months ago.
**Tags:** #gradient-boosting #logistic-regression #graph-theory #k-nearest-neighbors #evaluation-metrics #confidence-intervals #cross-validation #data-integration
**Contested on:** Every serious competitor here is fighting to get an inbound prospect onto the right seller's calendar in the seconds after they raise their hand — and whoever holds both the correctness and the latency takes the revenue operations account, because both halves are required and each vendor currently has one.

## The Problem
Making a scored decision in tens of milliseconds against a live profile is what advertising exchanges and payment fraud systems do millions of times a second. Deciding that two records describe the same company is entity resolution, with decades of method and mature tooling. Inbound lead routing needs both, at a volume that is trivial by comparison, and runs on a static rules form maintained by whoever is in revenue operations this year.

## What Already Exists
Entity resolution and record linkage frameworks, including probabilistic matching and blocking; company identity graphs from commercial data providers; real-time feature stores and decisioning platforms; propensity scoring with mature libraries; and rules engines with versioning and testing. Every one of these is available and none is at the edge of anything.

## The Customization Gap
The adaptation is to a business-to-business account graph and a scheduling action. It requires: (1) company-level rather than person-level resolution, including corporate structure, acquisitions, subsidiaries and the free-email-domain case, since the routing decision attaches to an account and this is where it fails; (2) resolution against the customer's own messy customer relationship data rather than against a clean reference, because the ownership answer must come from their system with its duplicates and its stale records, which is harder than matching to a reference graph; (3) availability as a live input to the decision, which decisioning platforms have no analogue for and which is what distinguishes a correct routing from a deliverable one; (4) a rules layer that revenue operations can read, edit and test, since this decision is politically owned and a learned model nobody can inspect will be rejected regardless of its accuracy; and (5) latency budgets that accommodate a customer relationship system lookup, which is usually the slow step and needs caching rather than heroics.

## Target Customer
Scheduling and routing vendors, revenue operations platforms, customer relationship vendors, and the data providers supplying company identity.

## Impact If Solved
The techniques are mature and the volumes are small, so the difficulty is entirely in the messy account graph and the seam between products. Account-level resolution against the customer's own data is the hard part and the one that determines whether anything downstream is correct.
