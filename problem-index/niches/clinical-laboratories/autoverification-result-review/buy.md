# Instrument Middleware Given a Learned Review Layer

**Niche:** [[niches/clinical-laboratories/autoverification-result-review/profile|Autoverification & Result Review]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Labs already own middleware that applies rules to every result; it applies only the rules a person wrote, and never learns which of them work.
**Tags:** #gradient-boosting #evaluation-metrics #data-integration #automation #compliance
**Contested on:** Every serious competitor in this niche is fighting to take routine result review off technologists' hands, and whoever cuts technologist review minutes per thousand results with no rise in corrected reports takes the account.

## The Problem
Rule sets in middleware grow by accretion: each incident adds a rule, few are removed, and nobody measures their hit rates. Labs hold more results than necessary and still miss subtle errors.

## What Already Exists
Data Innovations Instrument Manager and the instrument makers' middleware (Roche, Beckman Coulter, Siemens Healthineers, Abbott), with autoverification rule builders and delta checks.

## The Customization Gap
The adaptation needs rule analytics (hit rate, share of holds released unchanged, corrected reports after release), a learned score exposed as a field rules can use, and simulation of a proposed rule change against last month's results before go-live. Change documentation has to satisfy CLIA validation and accreditor checklists.

## Target Customer
Labs standardised on one middleware platform, and the middleware vendors as channel.

## Impact If Solved
Rule sets shrink and sharpen inside software the lab already validated. Retiring rules that hold real results unchanged often frees a meaningful share of review time, ~20–30% of holds (estimate).
