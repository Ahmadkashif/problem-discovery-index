# Lease Loss Early Warning

**Niche:** [[niches/outdoor-advertising-companies/ground-lease-retention/profile|Ground Lease Retention]]
**Industry:** [[industries/outdoor-advertising-companies|Outdoor Advertising Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Operators learn a valuable lease is at risk when the landlord's lawyer calls; the signals were in public records and their own files a year earlier.
**Tags:** #survival-analysis #gradient-boosting #large-language-models #feature-engineering #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep each ground lease at a rent the face can carry before a lease aggregator or a rival operator reaches the landowner, and whoever knows each site's true value and renewal risk first keeps the location.

## The Problem
Tens of thousands of leases expire on a rolling basis. Real estate managers prioritise by expiry date and by instinct about which landlords are restless. High-revenue sites with a landlord who has just inherited the land, listed it for sale or been approached by an aggregator sit in the same queue as a rural poster with a loyal farmer.

## Why Nobody Has Built This
Lease terms are locked in scans; ownership changes sit in county records; revenue sits in billing. The loss events are rare enough per market that no manager sees the pattern.

## What to Build
A survival model of lease loss and rent reset per site, using extracted lease terms (options, escalators, notice and sale clauses), payment history, county ownership and sale records, landlord type, face revenue relative to rent, and logged outside approaches. It ranks sites by revenue at risk and recommends the action: early renewal, land purchase, permanent easement, or nothing.

## Target Customer
VPs of real estate at operators with large leased portfolios.

## Impact If Built
The real estate team spends its time on the few hundred leases that carry most of the value at risk, and buys or extends them before an aggregator does.
