# Manufacturer-Agnostic Treatment System Sizing Tool

**Niche:** [[niches/plumbing-contractors/water-treatment-filtration/profile|Water Treatment & Filtration]]
**Industry:** [[industries/plumbing-contractors|Plumbing Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Water treatment equipment manufacturers provide sizing calculators for their own products but no tool compares across brands or designs multi-component treatment trains — a manufacturer-agnostic sizing tool would let contractors spec the best system for the water, not the brand they happen to carry.
**Tags:** #decision-trees #feature-engineering #data-integration #quick-win #revenue-impact

## The Problem
Every water treatment equipment manufacturer — Kinetico, Culligan, Pentair, Fleck, Clack — provides a sizing calculator for their product line. Enter the water hardness and flow rate, get the recommended softener model. But these calculators are single-product, single-brand tools. A contractor deciding between a Fleck 5600SXT and a Clack WS1 must run two separate calculators and manually compare output. More critically, when the water requires a multi-component treatment train (iron filter + softener + RO), no manufacturer tool designs the full system — each handles only their component. The contractor pieces together components from different manufacturer sizing tools, hoping they're compatible in flow rate, pressure drop, and treatment sequence.

## What Already Exists
Kinetico, Pentair, and Fleck each offer web-based sizing calculators for their equipment. These tools are accurate for single-component sizing but don't address: (1) multi-brand comparison for the same application, (2) multi-component treatment trains where upstream equipment affects downstream sizing, (3) compatibility verification (will the iron filter's output flow rate meet the softener's service flow requirement?), or (4) total system cost comparison across brand combinations.

## The Customization Gap
A manufacturer-agnostic sizing tool needs: (1) a unified equipment database spanning all major manufacturers with performance specifications (flow rate, capacity, regeneration requirements, media type, physical dimensions), (2) a treatment train builder that accounts for pressure drop accumulation across components and verifies flow rate compatibility, (3) side-by-side comparison of equipment options by performance, cost, warranty, and replacement part availability, (4) system-level output showing total pressure drop, required inlet pressure, drain requirements, electrical requirements, and physical space needed, and (5) a bill of materials with all components, fittings, and accessories needed for installation. Built as a subscription tool ($49-99/month) for water treatment contractors, with revenue supplemented by equipment manufacturer referral fees for specified products.

## Target Customer
Water treatment contractors who install equipment from multiple manufacturers and currently spend 30-60 minutes per quote running separate sizing tools and manually comparing options, or contractors locked into a single brand because they only know how to size that manufacturer's equipment.

## Impact If Solved
Reduces system design time from 30-60 minutes to 10-15 minutes per quote. Enables contractors to specify the optimal equipment for each application rather than defaulting to the brand they know best. Eliminates compatibility errors in multi-component systems that cause flow restriction, pressure drop issues, and premature equipment failure — problems that currently generate $500-2,000 callbacks per incident.
