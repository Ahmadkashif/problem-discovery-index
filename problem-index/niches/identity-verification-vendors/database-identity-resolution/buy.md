# Record Linkage From Official Statistics

**Niche:** [[niches/identity-verification-vendors/database-identity-resolution/profile|Database Identity Resolution]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Statistical agencies developed probabilistic record linkage with coverage evaluation and undercount measurement, and commercial identity resolution returns a match or nothing.
**Tags:** #bayesian-inference #confidence-intervals #evaluation-metrics #hypothesis-testing #data-integration #graph-theory #descriptive-statistics #expectation-maximization
**Contested on:** Every serious competitor in this niche is fighting to confirm that a claimed identity exists and belongs to this person from records that were never built for the purpose — and whoever resolves thin-file and frequently-moving populations best serves the people everyone else cannot see.

## The Problem
Census and statistical agencies have done probabilistic record linkage for decades, and — crucially — they measure who they miss. Undercount estimation, coverage evaluation surveys and differential undercount analysis by population group are standard practice, precisely because the agencies know that linkage quality varies systematically and that the people missed are not random. Commercial identity resolution uses similar linkage techniques and does none of the coverage measurement.

## What Already Exists
Probabilistic record linkage frameworks with match weights; coverage evaluation and undercount estimation; differential coverage analysis by population; name and address standardisation practice; and linkage quality reporting standards.

## The Customization Gap
The adaptation is to a real-time individual decision. It requires: (1) a decision about one person in seconds rather than an aggregate linkage over a file, so match weights must be expressed as an actionable confidence — this is the operational difference; (2) coverage evaluation without a survey, since the agency method depends on an independent enumeration that commercial resolution cannot run, making retry and alternative-path outcomes the substitute; (3) an adversary presenting deliberately false identities, which statistical linkage never contemplates; (4) commercial sources with unknown and varying coverage rather than an administrative frame; and (5) consequences for an individual rather than for a statistic, which raises the bar on both errors.

## Target Customer
Data and policy leadership, institutions with inclusion obligations, statistical and academic researchers, and identity data suppliers.

## Impact If Solved
Statistical agencies measure who their linkage misses because they know the misses are not random. Importing differential coverage measurement is the adaptation, and it is the discipline commercial resolution most conspicuously lacks.
