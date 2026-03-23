# Multilingual Energy Audit Report Generator

**Niche:** [[niches/energy-auditors/non-english-homeowner-audits/profile|Non-English Homeowner Audits]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool generates energy audit reports and retrofit proposals in the homeowner's preferred language with technically accurate building science terminology.
**Tags:** #llm #text-generation #nlp #automation #worker-facing

## The Problem
An energy auditor completes an audit of a Spanish-speaking homeowner's 1965 ranch house and generates the standard English report: "The blower door test measured 3,200 CFM50, indicating significant air infiltration. Recommended measures: attic air sealing to reduce ACH50 from 12 to 7, R-38 blown cellulose insulation over existing R-11 batts, and duct sealing with mastic to reduce leakage to <10% of system airflow." The homeowner, who speaks conversational English but not technical English, receives this report and cannot evaluate the recommendations. The auditor tries to explain verbally but lacks the Spanish building science vocabulary. The homeowner declines the recommended $8,000 in improvements — not because they do not want them, but because they do not understand what they are agreeing to.

## Why Nobody Has Built This
Technical building science translation requires domain-specific vocabulary that generic translation services handle poorly. "Blower door" is not a standard dictionary term in any language. "R-value" has no direct equivalent in many languages. "Air changes per hour" requires explanatory context, not just literal translation. Creating accurate multilingual audit reports requires building a domain-specific translation layer with validated technical terminology in each target language — a specialized NLP challenge. The market for multilingual energy audits is significant but fragmented across dozens of languages and dialects.

## What to Build
A report generation module that takes standard English audit data (blower door results, insulation levels, equipment specs, recommended measures, savings projections) and produces a homeowner-facing report in the homeowner's preferred language. The module uses LLM translation with a domain-specific glossary of building science terms validated by bilingual energy professionals in each target language. Reports include visual diagrams, annotated photos, and plain-language explanations alongside technical data. Initial language support: Spanish, Mandarin, Vietnamese, Korean, and Tagalog (the top 5 LEP languages in US households).

## Target Customer
Energy auditors serving communities with 20%+ LEP populations, utility program equity officers seeking to improve LEP household participation rates, and community-based organizations bridging language gaps in energy programs.

## Impact If Built
Increases LEP household retrofit authorization rates from an estimated 30-40% to 60-70% by providing comprehensible audit findings. For utility programs with equity mandates, this directly addresses the participation gap for LEP households and helps meet regulatory requirements for equitable program delivery.
