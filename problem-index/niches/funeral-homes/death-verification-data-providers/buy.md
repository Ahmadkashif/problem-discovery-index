# Record Matching Adapted to Asymmetric Error Cost

**Niche:** [[niches/funeral-homes/death-verification-data-providers/profile|Death Verification Data Providers]]
**Industry:** [[industries/funeral-homes|Funeral Homes]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Matching engines optimize overall accuracy; here a false match stops a living person's pension and a missed match keeps paying a dead one, and no customer weighs those two errors the same way.
**Tags:** #probability-distributions #confidence-intervals #logistic-regression #random-forests #contrastive-learning #evaluation-metrics #hypothesis-testing #bayesian-inference #compliance #data-integration

## The Problem
Matching a customer's record against a death file is done on name, date of birth, and partial identifiers of varying quality, across populations where names repeat and data entry is imperfect. Both error directions are expensive and they are expensive to different people: a false positive terminates benefits to a living person, generates a complaint and sometimes a regulatory finding, and is discovered only when that person notices; a false negative continues an improper payment that may run for years. Matching thresholds are set once, largely uniformly, and applied to customers whose loss functions differ enormously — a small insurer's tolerance is nothing like a federal benefit programme's.

## What Already Exists
Record linkage is a mature field with strong tooling. Probabilistic matching engines, the commercial identity resolution platforms, and the established statistical linkage frameworks all handle name and date matching with blocking, scoring, and review queues, and several are widely used in exactly this application.

## The Customization Gap
Those tools produce a match score and a threshold. What the domain needs is a calibrated probability plus an explicit cost model, so that the threshold is derived from the customer's own consequences rather than set globally. That requires calibration — a score of eighty must mean an eighty percent chance of being the same person, which off-the-shelf scores generally do not — and it requires the provider to hold enough adjudicated matches to calibrate against, which is a data problem rather than an algorithm problem. The adaptation is calibrated matching with per-customer decision thresholds, review routing driven by expected cost rather than by score alone, and — the piece nobody offers — a stated expected error rate in both directions at the chosen threshold, so a customer can document why their threshold is reasonable when a regulator asks about a wrongly terminated benefit.

## Target Customer
Heads of identity science and product at death data providers, and the benefit administrators who currently accept a vendor's default threshold and absorb both error types without measuring either.

## Impact If Solved
Lets the same underlying data serve customers with opposite risk postures correctly, which is a product capability rather than an accuracy improvement. Stated bidirectional error rates are also the documentation a customer needs when a wrongful termination is challenged, and no competitor provides it.
