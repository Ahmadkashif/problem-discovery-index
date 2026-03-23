# Multi-Component Signage Estimator

**Niche:** [[niches/printing-shops/wide-format-signage-shops/profile|Wide-Format & Signage Shops]]
**Industry:** [[industries/printing-shops|Printing Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No estimating tool handles multi-component signage projects (print + fabrication + electrical + installation + permits) — forcing shop owners to spend 45-90 minutes per estimate manually calculating material, labor, and subcontractor costs across 5-10 components for a single sign package.
**Tags:** #automation #revenue-impact #tacit-knowledge-ml

## The Problem
A building signage package quote might include: channel letters (fabrication + LED modules + wiring + transformer + installation), a monument sign (concrete base + aluminum cabinet + routed acrylic face + LED illumination + installation), window graphics (measurement + print + lamination + installation), and directional wayfinding signs (print on aluminum composite + post mounting). Each component has its own material cost, fabrication time, and installation labor. The shop owner estimates each component separately, accounts for subcontractor costs (electrician, concrete), adds permit fees, and calculates the total. This process takes 45-90 minutes for a complex project and depends on the estimator's experience with actual fabrication and installation times — a skill that takes 5-10 years to develop.

## Why Nobody Has Built This
Sign shop estimating is more complex than commercial print estimating because it combines printing (substrate + ink cost), fabrication (metal, acrylic, wood — each with different manufacturing processes), electrical (LED, neon, transformers), structural (mounting, wind load, permitting), and installation labor (crew size, equipment, travel time). No single estimating model covers all these domains. ShopVOX and signVOX provide basic estimating templates, but they require the estimator to manually enter times and costs for each component — they do not predict costs from job specifications.

## What to Build
An estimating engine that accepts a sign project specification (sign types, dimensions, materials, illumination, location, installation method) and generates a detailed estimate by pulling material costs from the shop's price book, predicting fabrication and installation labor from historical job data (similar projects' actual times), calculating subcontractor costs from rate tables, and adding permit fees from a jurisdiction database. The system learns from actual-versus-estimated variance on completed jobs, improving accuracy over time. Multi-location programs (same sign package at 50 locations) are handled with per-location adjustments.

## Target Customer
Owners and estimators at full-service sign shops producing fabricated and installed signage. Approximately 5,000-8,000 US sign shops with fabrication capability. Average contract value: $8-15K/year.

## Impact If Built
Estimate time drops from 45-90 minutes to 10-20 minutes per project. Estimating accuracy improves by 5-10% of total project cost. Quote volume doubles without adding estimating staff, capturing revenue from inquiries that currently expire before being quoted.
