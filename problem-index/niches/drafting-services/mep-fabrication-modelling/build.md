# Automatic Spooling That Learns the Installer's Breakpoints

**Niche:** [[niches/drafting-services/mep-fabrication-modelling/profile|MEP Fabrication & Spool Modelling]]
**Industry:** [[industries/drafting-services|Drafting Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Where to break a pipe run into spools depends on the shop's capacity, the truck, the lift and how the installing foreman likes to hang it, and the modeller learns that by having spools rejected.
**Tags:** #gradient-boosting #graph-neural-networks #feature-engineering #tacit-knowledge-ml #automation
**Contested on:** Every serious competitor in this niche is fighting to turn the coordinated MEP model into spool, duct and hanger packages that the prefabrication shop can build and the installer can hang without field modification, and whoever cuts model-to-spool hours while holding first-time fit takes the mechanical contractor.

## The Problem
Spooling tools break runs by length and fitting rules. Experienced modellers adjust for things the rules do not capture: spool weight for the lift available, shipping dimensions, access through a particular door, where a foreman prefers a field joint, and which shop cell will build it. New modellers, especially offshore ones who never see the site, get these wrong and the spools are reworked.

## Why Nobody Has Built This
The preferences are tacit and site-specific, and the feedback (a spool modified in the field) rarely returns to the modeller.

## What to Build
A spooling assistant that learns breakpoint choices from accepted and modified spools on past projects — weight, length, access, installer and shop — and proposes breakpoints for a new run with reasons, which the modeller accepts or adjusts.

## Target Customer
Prefabrication managers at mechanical and plumbing contractors, and the bureaus that model for them.

## Impact If Built
Fewer reworked spools, faster spooling, and offshore modellers producing spools a foreman accepts.
