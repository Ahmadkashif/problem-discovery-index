# Photo-Based Dent Count and Pricing Tool for PDR Operators

**Niche:** [[niches/auto-body-shops/paintless-dent-repair/profile|Paintless Dent Repair Operators]]
**Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool uses photos to count, size, and price dents automatically — PDR operators manually count dents panel-by-panel and calculate prices from memory or a spreadsheet.
**Tags:** #cnn #object-detection #computer-vision #tacit-knowledge-ml #revenue-impact

## The Problem
PDR pricing requires counting every dent on a vehicle, categorizing each by size (dime, nickel, quarter, half-dollar, silver dollar), depth (shallow, medium, deep), and panel location (roof costs more than door due to access difficulty). An experienced PDR tech walks around a hail-damaged vehicle and estimates 45 dents in 3 minutes — a junior tech takes 15 minutes and misses 10 dents, underpricing the job by $300-$500. This visual assessment skill is pure tacit knowledge: the experienced tech's eyes scan across reflections in the paint surface to detect dents invisible to untrained observers.

## Why Nobody Has Built This
Dent detection in photos requires detecting subtle surface deformations that may be only 1-2mm deep — visible to the trained eye as light reflection irregularities but extremely difficult for standard object detection models. The training data challenge is significant: you need thousands of labeled photos of dented panels with precise dent counts, sizes, and locations annotated by experienced PDR technicians. No dataset like this exists publicly.

## What to Build
A smartphone camera tool that uses controlled lighting conditions (the PDR tech already uses a specialized light board for dent detection) to photograph each panel, automatically detect and count dents, categorize them by size and depth, and calculate the price using the operator's rate matrix. The output is a panel-by-panel dent map with pricing that becomes the customer-facing estimate and the basis for the invoice. It learns from technician corrections to improve accuracy.

## Target Customer
PDR operators (solo and small teams) who price 5-20 vehicles per week and want consistent, fast, defensible pricing that doesn't depend on the individual technician's experience level.

## Impact If Built
Reduces vehicle assessment time from 10-15 minutes to 3-5 minutes per vehicle. Eliminates 15-25% underpricing by junior technicians. For a PDR operator doing $200K/year in revenue, capturing the 15% currently left on the table through undercount represents $30K in additional annual income.
