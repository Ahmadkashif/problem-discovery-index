# Damage-to-Estimate Draft Generator

**Niche:** [[niches/public-adjusters/xactimate-automation/profile|Xactimate Estimate Automation]]
**Industry:** [[industries/public-adjusters|Public Adjusters]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product takes a PA's inspection notes and photos and generates a draft Xactimate estimate with appropriate line items, quantities, and pricing pre-populated for the specific damage type and property.
**Tags:** #llm #cnn #multimodal #automation #revenue-impact

## The Problem
An experienced PA inspects a property, takes 150 photos, makes notes ("3-tab shingles, 28 squares, 6/12 pitch, 3 pipe jacks, step flashing at chimney, interior water damage in master bedroom ceiling and wall, laminate flooring buckled in kitchen"), and then spends 4-8 hours manually entering this information into Xactimate line by line. The estimate creation process is mostly mechanical translation of inspection findings into Xactimate line items — the PA already knows what needs to be in the estimate from the inspection. The bottleneck is data entry, not judgment.

## Why Nobody Has Built This
Xactimate has a proprietary file format (ESX) and API access is limited. Building a draft generator requires (1) mapping natural language damage descriptions to Xactimate selector codes (thousands of codes organized in a hierarchical tree), (2) extracting measurements from photos and notes, (3) applying local pricing and market conditions, and (4) outputting an ESX file that Xactimate can import. Verisk (Xactimate's parent) has no incentive to build this — faster estimate creation means less time spent in their software.

## What to Build
A multimodal estimate generator that accepts inspection photos, voice/text notes, and aerial measurements, then produces an importable Xactimate draft. The PA's input: "Wind damage, 3-tab shingles, 28 squares, 6/12 pitch" triggers automatic population of all related line items (tear-off, felt, drip edge, shingles, ridge cap, pipe jacks, waste factor, steep charge, O&P). Interior damage notes generate corresponding interior line items. The PA reviews and refines the draft in Xactimate rather than building from zero.

## Target Customer
PAs writing 3-8 Xactimate estimates per week who currently spend 20-40 hours per week on estimate creation.

## Impact If Built
Reduces estimate creation time by 60-75% (from 6 hours to 1.5-2 hours per estimate). For a PA writing 5 estimates per week, reclaims 20-25 hours per week — enough to handle 40% more claims or improve work-life balance dramatically.
