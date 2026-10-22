# Setting GLP Doses Before the Range-Finder Ends

**Niche:** [[niches/biotech-research-firms/small-molecule-ind-packages/profile|Small-Molecule IND Packages]]
**Industry:** [[industries/biotech-research-firms|Biotech Research Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The GLP repeat-dose study cannot be designed until the dose-range finder is read out, and that serial handoff is the longest avoidable wait in a small-molecule package.
**Tags:** #bayesian-inference #gaussian-processes #transfer-learning #probability-distributions #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to compress the small-molecule IND-enabling package — dose-range finding, GLP repeat-dose studies in two species, safety pharmacology and genetic toxicology — into the fewest calendar months from candidate nomination, and whoever plans the disciplines as one critical path rather than as separate study quotes takes the account.

## The Problem
Toxicologists set GLP doses from the range-finder's tolerability and toxicokinetics: a high dose that produces toxicity without excessive mortality, a low dose near the expected no-effect level. The GLP study's protocol, animal order and room booking wait for that readout, often six to ten weeks after the range-finder starts (estimate). Each week of waiting moves the IND.

## Why Nobody Has Built This
Dose selection is a toxicologist's judgement made one compound at a time. The historical data that could inform it — exposure and tolerability across hundreds of compounds and species — is split across sponsors and owned by each, and CROs have never productised what they have seen.

## What to Build
A dose-projection model that predicts tolerability and exposure in the GLP species from early in vitro and in vivo pharmacokinetic data, the range-finder's first days, and a prior learned from the CRO's own historical studies where its contracts allow. It produces a provisional dose set with uncertainty, allowing protocol drafting and animal ordering to start in parallel and confirming doses when the range-finder completes.

## Target Customer
Integrated preclinical CROs competing on package speed; sponsor toxicology leads on compressed financing timelines.

## Impact If Built
Overlapping the range-finder and GLP preparation could remove several weeks from the critical path (estimate), the most direct lever on the contest in this niche.
