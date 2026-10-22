# Line-of-Sight Qualification Learned From Every Install

**Niche:** [[niches/wireless-carriers/wisp-address-qualification/profile|WISP Address Qualification & Installs]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every WISP install is a free, same-day label of whether the coverage prediction was right, and almost no one trains on it.
**Tags:** #cnns #gradient-boosting #gaussian-processes #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche (coverage-prediction tools, LiDAR heat-map vendors and radio makers' planning software) is fighting to tell, before the truck rolls, whether a specific roofline can hold the advertised speed from a specific sector, and whoever qualifies addresses most accurately takes the account.

## The Problem
Coverage tools compute a path profile from terrain and LiDAR and give a predicted signal level. Installers then find that a tree line, a barn or a ridge the data missed blocks the path, or that a marginal prediction works fine. The outcome is recorded in the install ticket and never returned to the model.

## Why Nobody Has Built This
Each WISP's install history is small, and coverage vendors sell per-query predictions rather than models trained on customer outcomes. Install results are recorded inconsistently, often as free text.

## What to Build
A qualification model that starts from physics-based path profiles and learns corrections from the operator's installs: imagery-derived tree height and density, building footprints, season of the LiDAR capture, sector load, and installer notes. It outputs a probability of meeting each plan tier and a recommended mounting height. Pooled learning across many WISPs, with consent, handles small operators.

## Target Customer
WISP owners and sales managers, and coverage-tool vendors wanting a calibrated product.

## Impact If Built
Fewer failed installs and early cancellations, more sales at addresses the conservative tool rejected, and installers who spend their days installing.
