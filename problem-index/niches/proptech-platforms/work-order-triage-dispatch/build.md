# Diagnosis, Urgency and Trade Inferred From the Resident's Own Words

**Niche:** [[niches/proptech-platforms/work-order-triage-dispatch/profile|Work Order Triage & Vendor Dispatch]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Millions of resident complaints have already been followed by a known diagnosis, trade, parts list and outcome, and the next complaint is triaged by a site manager reading a sentence between two other tasks.
**Tags:** #bert #large-language-models #transformers #gradient-boosting #confidence-intervals #evaluation-metrics #automation #revenue-impact
**Contested on:** Every serious competitor in maintenance triage is fighting to turn a resident's free-text complaint into the right trade, the right urgency and the right vendor without a site manager reading it — and whoever triages most accurately takes the account.

## The Problem
"Water on the kitchen floor, not sure where from." A site manager reads it, guesses plumbing, marks it routine because the resident did not sound alarmed, and assigns the general maintenance technician. It turns out to be a failed supply line behind the dishwasher that has been wetting the subfloor for a week, which becomes a floor replacement and a mould remediation. The same sentence appears hundreds of times a year across the operator's portfolio with known outcomes attached, and the distribution of what it actually turns out to be is recoverable from the record.

## Why Nobody Has Built This
The labels are imperfect — the recorded category is what the intake person chose rather than what it was, and the true diagnosis lives in the technician's closing note or in the invoice line items. Deriving reliable labels means reading the resolution side of the record, which is unglamorous data work that has to be done before any modelling starts. Platform vendors have also been reluctant to automate a decision with a safety dimension: a triage that downgrades an active leak has a consequence, and the product has to be designed around that asymmetry rather than around average accuracy.

## What to Build
A triage model over the operator's own corpus that returns, from the resident's text plus unit and property context: a ranked set of likely diagnoses, a recommended trade, an urgency with the reasoning, and a predicted parts list. Labels are derived from the resolution side — closing notes, invoice lines, parts used — rather than from the intake category. Urgency is the asymmetric part and is designed that way: the model is tuned to over-call rather than under-call on the conditions where delay causes escalating damage, because the cost of sending someone unnecessarily is an hour and the cost of missing an active leak is a floor. Predictions are shown with confidence and the site manager can override in one tap, which supplies continuous labels. Vendor selection then uses the inferred work type against the performance scorecard from the parent niche, which is where the two capabilities compound.

## Target Customer
Property operators at portfolio scale, vendor marketplaces whose dispatch quality is their product, and the platform vendors holding the corpus.

## Impact If Built
Accurate triage puts the right trade with the right parts at the door the first time, which is the largest single determinant of maintenance cost and of resident satisfaction in rental housing. The urgency component is where the damage-cost asymmetry lives, and a small improvement in catching escalating conditions early pays for the whole capability.
