# Master-Policy-to-Unit-Policy Coverage Mapper

**Niche:** [[niches/public-adjusters/condo-hoa-claims/profile|Condo Association & HOA Claims]]
**Industry:** [[industries/public-adjusters|Public Adjusters]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product maps the coverage boundaries between a condo association's master policy and individual unit owner policies to determine which policy covers each damage element before estimates are written.
**Tags:** #llm #named-entity-recognition #nlp #compliance #revenue-impact

## The Problem
When a water pipe bursts on the 5th floor of a condo building, damage cascades through multiple units. The master policy may cover the pipe itself (common element), the drywall in the hallway (common element), and possibly the drywall inside units (if "all-in" coverage). The unit owner's HO-6 policy covers personal property and improvements. The line between "common element" and "unit owner responsibility" is defined by the association's governing documents (CC&Rs, bylaws) and the master policy's coverage form — which vary by association. A PA handling this claim must read the CC&Rs, the master policy, and each unit owner's HO-6 policy to allocate each damage item to the correct policy before writing estimates.

## Why Nobody Has Built This
The coverage boundary analysis requires parsing three types of legal documents (CC&Rs, master policy, HO-6 policy), cross-referencing their provisions, and applying state-specific condo insurance statutes that vary in how they define "common elements" and "unit boundaries." The combinations are nearly infinite — different CC&Rs, different master policy forms, different state laws — making a rules-based approach impractical. An LLM-based approach must handle the variability while providing legally defensible allocations.

## What to Build
A coverage mapping tool that ingests the association's CC&Rs, master policy, and a representative HO-6 policy, then for each damage category (structural, fixtures, flooring, paint, personal property, improvements), determines which policy provides coverage and flags ambiguous items for PA review. Output is a coverage allocation matrix that guides estimate writing — "pipe repair: master policy, drywall: master policy, unit flooring: HO-6, unit appliances: HO-6."

## Target Customer
PAs specializing in condo and HOA claims who handle 10-30 association-related events per year, each involving multiple units and policy layers.

## Impact If Built
Reduces coverage allocation analysis from 6-10 hours to 1-2 hours per event. Prevents misallocation errors that cause claim denials or delayed settlements — a single misallocation can delay a $500K claim by 3-6 months while policies are corrected.
