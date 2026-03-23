# CSBG Outcome Reporting Burden

**Niche:** [[niches/nonprofits-social-services/rural-community-action-agencies/profile|Rural Community Action Agencies]]
**Industry:** [[industries/nonprofits-social-services|Nonprofits Social Services]]
**Type:** Fix (Pain Point)
**One-liner:** CAAs spend 200-400 hours per year manually compiling CSBG Annual Report data from disconnected sources because no system maps program activities to ROMA (Results Oriented Management and Accountability) outcomes automatically.
**Tags:** #automation #compliance #data-integration #worker-facing

## The Problem
Every CAA must submit an annual CSBG report organized around ROMA outcomes — National Performance Indicators that measure changes in family self-sufficiency, community engagement, and agency capacity. Compiling this report requires pulling data from 5-10 program databases, mapping individual client activities to ROMA outcome categories, counting unduplicated clients across programs, and producing narrative descriptions of community impact. This process takes 200-400 hours annually, typically falling on one overworked staff member who manually cross-references spreadsheets.

## Why It's Still Broken
The ROMA framework uses outcome categories (e.g., "Family achieved and maintained a living wage") that don't directly correspond to how any single program tracks its data. Mapping a Head Start enrollment, a weatherization project completion, and a job placement to the correct ROMA outcome requires understanding both the program-specific data model and the ROMA taxonomy. CAP60 and some state systems support ROMA reporting, but they only capture data entered directly into those systems — not data from program-specific databases like ChildPlus or state LIHEAP systems.

## What a Fix Looks Like
A ROMA reporting engine that connects to each program database, applies configurable mapping rules (e.g., "Job placement in employment program → National Performance Indicator 1.2: Employment"), deduplicates clients across programs using a master client index, and generates a draft CSBG Annual Report with all National Performance Indicators pre-populated. The staff member reviews and validates rather than compiles from scratch.

## Who Feels the Pain
The single administrative staff member (often the executive director at small CAAs) who spends 6 weeks every spring locked in an office compiling the annual CSBG report instead of managing programs.

## Impact If Fixed
Reduces CSBG reporting from 300 hours to 40 hours annually, frees the equivalent of 7 working weeks per year for program delivery, and improves reporting accuracy by eliminating the manual cross-referencing that introduces counting errors.
