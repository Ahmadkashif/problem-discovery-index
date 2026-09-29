# Vendor Performance Measured Instead of Remembered

**Niche:** [[niches/proptech-platforms/maintenance-turn-operations/profile|Maintenance & Turn Operations]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A property operator sends millions of dollars of work to vendors chosen on relationships, holds every work order, invoice and reopen that would rank them, and evaluates them by asking regional managers who they like.
**Tags:** #gradient-boosting #survival-analysis #hypothesis-testing #confidence-intervals #evaluation-metrics #descriptive-statistics #revenue-impact #tacit-knowledge-ml
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A regional manager uses three plumbers. One is expensive and always fixes it; one is cheap and comes back twice; one is fine except on anything involving a water heater. She knows this and her colleague two regions over does not, and neither of them can prove any of it. Vendor rosters are managed by relationship and by whoever answers the phone at seven on a Saturday. When a vendor's quality declines, it is noticed slowly and anecdotally. The operator's own records contain first-visit resolution, reopen rate, cost relative to peers for the same work type, and time to complete, for every vendor, at every property.

## Why Nobody Has Built This
The measurement requires knowing what work a job actually was, and work orders are categorised by whoever created them — frequently from a resident's description — so the categories are unreliable and comparing vendors within them is comparing across noise. Reopens are not linked, as the fix note below describes, so the most important quality signal is not computed. And there is an organisational reluctance: publishing a vendor ranking creates conversations with vendors who have long relationships with named people, and in some operators the vendor relationship is not entirely arm's length, which is a reason the measurement is unwelcome rather than a reason it is wrong.

## What to Build
A vendor scorecard computed from the operator's own records, normalised for what the work actually was. Work type is inferred from the work order text, the parts and labour on the invoice and the resolution, rather than taken from a category field. Within a work type, vendors are compared on first-visit resolution, reopen rate within a window, cost relative to the operator's own distribution, and time to complete, each with volume-appropriate uncertainty so a vendor with eleven jobs is not ranked against one with four hundred. Dispatch then uses the scorecard: for this work type at this property, these vendors resolve it first time at this cost. The scorecard is shared with vendors, which is what turns it from a procurement weapon into a performance system and is how the good vendors become advocates for it.

## Target Customer
Multifamily and single-family rental operators at portfolio scale, vendor marketplaces whose value proposition is supply quality, and the platform vendors holding the data.

## Impact If Built
Maintenance is one of the largest controllable operating expenses in rental housing and vendor quality varies enormously within it, so routing work by measured performance rather than by relationship moves both cost and resident satisfaction. The normalisation by inferred work type is what makes the comparison fair and is the part that has kept this unbuilt.
