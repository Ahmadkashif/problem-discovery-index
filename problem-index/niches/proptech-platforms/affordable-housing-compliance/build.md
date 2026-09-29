# Income Certification Computed From the Source Documents

**Niche:** [[niches/proptech-platforms/affordable-housing-compliance/profile|Affordable Housing Compliance]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Income certification is a rule-governed calculation over documents a household has already provided, it decides whether a property keeps its tax credits, and it is performed by a scarce specialist with a calculator and a highlighter.
**Tags:** #bert #large-language-models #transformers #evaluation-metrics #confidence-intervals #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in affordable housing software is fighting to produce a tenant file that passes a compliance review without a specialist rebuilding it by hand — and whoever gets first-pass audit rate highest takes the portfolio.

## The Problem
A household provides six weeks of pay stubs for one member with variable hours, a benefit award letter for another, a self-employment ledger for a third, and a bank statement showing an asset. The specialist must annualise the variable earnings using the prescribed method, determine which benefit amounts count, compute imputed income on the asset, and arrive at a household figure that will be checked by a state agency reviewer against the same documents. The calculation is deterministic given the rules. Performing it takes forty minutes, the rules are held in a specialist's head and a binder, and a mistake risks the property's credits.

## Why Nobody Has Built This
The stakes are the obstacle rather than the difficulty. An incorrect certification is not a bad user experience; it is a potential recapture event, so vendors have been unwilling to compute a number the owner will rely on. The rules are also genuinely intricate and vary across the programmes a property may be layered with, and encoding them requires compliance expertise that software teams do not have and compliance specialists cannot write down easily. And the population that does this work is small, so the market looks small — while the consequence of a finding is enormous, which is the mismatch that has kept it unserved.

## What to Build
A calculation engine over extracted source documents, with every figure traceable to the document and passage it came from and every rule application shown. Extraction pulls the numbers from pay stubs, award letters, verification forms and self-employment records. The engine applies the programme's prescribed annualisation, inclusion and asset rules, producing a household income figure with a complete audit trail — which is the artefact a reviewer wants and which currently has to be reconstructed from a paper file. Where the rules require a judgement, the engine stops and asks the specialist, with the relevant guidance and the precedent from this portfolio's prior determinations attached, rather than guessing. Layered programmes are computed side by side with conflicts surfaced explicitly. The specialist's role becomes review and judgement rather than arithmetic and transcription, which is both a large time saving and the only way this scarce workforce scales.

## Target Customer
Affordable housing owners and management agents, compliance service providers, and the state housing finance agencies that conduct the reviews and would benefit from receiving files in this form.

## Impact If Built
Reducing a forty-minute certification to a ten-minute review multiplies the capacity of a workforce that is genuinely scarce and retiring, which is the binding constraint on affordable housing operations. A complete audit trail per figure also changes the review itself from reconstruction to verification — and the downside being avoided, credit recapture, is severe enough that even a modest reduction in error rate justifies the work.
