# A Consortium Loss Database for Police and Civil Rights Claims

**Niche:** [[niches/self-insured-benefit-pools/public-entity-liability-pools/profile|Public Entity Liability Pools]]
**Industry:** [[industries/self-insured-benefit-pools|Self-Insured Benefit & Risk Pools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every pool prices police liability from its own handful of large claims, while the evidence it needs is scattered across hundreds of pools that never pool their data.
**Tags:** #gradient-boosting #survival-analysis #large-language-models #feature-engineering #evaluation-metrics #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to keep a public entity's liability programme affordable through the police-verdict cycle, but that is two contests with different winners: closing police and civil rights claims at the lowest ultimate cost, which claims managers and defence panels win, and pricing each member close enough to its own risk that low-loss members stay, which underwriters and actuaries win. Decomposed into contested sub-niches below.

## The Problem
A state municipal pool might see two or three police claims above $1M in a decade (estimate). That is too few to estimate frequency, severity or the effect of a new state law, so actuaries load the rate by judgement and reinsurers load it again. Meanwhile, the same pattern repeats elsewhere: a new statute, a run of settlements, reinsurers withdrawing.

## Why Nobody Has Built This
Pools are state-bounded, board-governed public bodies with no tradition of sharing claim data across state lines. Their association, AGRiP, lists a staff of seven. Claims are coded by line and cause, not by allegation, video or officer history, so even willing pools cannot combine them without recoding.

## What to Build
A member-governed, de-identified closed-claim database for law enforcement, jail and employment liability. Claims are recoded by allegation, injury, evidence and venue using LLM extraction from the pools' own files, joined to state law changes and public verdicts. On top: severity curves by state and allegation type, time-to-close models, and the effect of statutes such as Colorado's S.B. 20-217 on frequency and severity.

## Target Customer
Pool executive directors and finance directors, their actuaries, and the reinsurers who now price police exposure blind.

## Impact If Built
Pools could set retentions and police loads on evidence, and negotiate with reinsurers holding data the reinsurers do not have.
