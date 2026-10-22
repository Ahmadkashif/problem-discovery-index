# Coverage Heat Maps Calibrated to the Operator's Own Installs

**Niche:** [[niches/wireless-carriers/wisp-address-qualification/profile|WISP Address Qualification & Installs]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** WISPs already pay for LiDAR-based heat maps, which predict signal from physics alone and are never adjusted to how installs in that operator's terrain actually turn out.
**Tags:** #gaussian-processes #regularization #feature-engineering #evaluation-metrics #quick-win
**Contested on:** Every serious competitor in this niche (coverage-prediction tools, LiDAR heat-map vendors and radio makers' planning software) is fighting to tell, before the truck rolls, whether a specific roofline can hold the advertised speed from a specific sector, and whoever qualifies addresses most accurately takes the account.

## The Problem
A heat map that is right on average can still be systematically wrong for one operator's forested valleys or one tower's height. Sales teams learn to distrust it and fall back on site surveys.

## What Already Exists
TowerCoverage, Cambium cnHeat and similar tools that compute coverage from terrain, LiDAR and radio parameters.

## The Customization Gap
The adaptation needs an import of install outcomes and measured signal levels; a per-operator residual correction by clutter type and tower; seasonal adjustment; confidence shown per address rather than a single colour; and a feedback loop that updates after each batch of installs.

## Target Customer
WISPs already licensing a heat-map tool.

## Impact If Solved
The existing tool becomes trustworthy enough to qualify addresses at the point of sale without a survey visit.
