# An Alternatives Map for Every Household

**Niche:** [[niches/wired-broadband-providers/residential-retention-and-migration/profile|Residential Retention & Migration]]
**Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Whether a household stays depends on what else it can buy at its address, and no operator keeps a current, address-level record of that.
**Tags:** #k-nearest-neighbors #feature-engineering #gradient-boosting #data-integration #evaluation-metrics #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor is fighting to keep a household's broadband revenue when its current connection stops being its best option, but for cable operators that is a pricing contest at promo roll-off against fixed wireless and fibre, and for telcos it is an operational contest to move households off copper before the wire center is retired. Decomposed into contested sub-niches below.

## The Problem
A cable household near a new fibre build, a copper DSL household inside a fixed wireless sector with spare capacity, and a household with no alternative at all look identical in a churn model built on tenure and bill size. Retention offers, marketing and migration plans are set without knowing which is which.

## Why Nobody Has Built This
Until the FCC's Broadband Data Collection, provider availability was published by census block and was badly overstated. Location-level availability now exists, but turning it into a living competitive map means joining it to fixed wireless eligibility, construction permits and the operator's own account base, which no billing or CRM vendor does.

## What to Build
A per-address alternatives record refreshed each map cycle: every competing provider, technology and advertised speed from the public BDC data matched to the operator's accounts through the Fabric; fixed wireless eligibility checks; fibre overbuild footprints from permits and announcements; and a model of which alternatives actually pull customers, learned from past churn. It feeds both sub-niches: save-offer targeting for cable and migration sequencing for copper.

## Target Customer
Heads of retention, pricing and market planning at cable operators and telcos.

## Impact If Built
Every retention, pricing and migration decision gets the one fact that most predicts the outcome, and spend moves to the households that actually have somewhere else to go.
