# Statistically Faithful Nonsense

**Niche:** [[niches/synthetic-data-providers/regulated-domain-generation/profile|Regulated Domain Generation]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** General generators produce records that match every distribution and that a domain expert identifies as impossible on sight, because impossibility is not a statistical property.
**Tags:** #bayesian-inference #probability-distributions #evaluation-metrics #convex-optimization #tacit-knowledge-ml #compliance #hypothesis-testing #decision-trees
**Contested on:** Every serious competitor in this niche is fighting to produce records a domain expert cannot tell are impossible — and whoever does that takes the account, because in a regulated domain a single implausible record ends the evaluation.

## The Problem
A health system evaluates a synthetic patient cohort. The age distribution matches, the diagnosis frequencies match, the length-of-stay curve matches. A clinician reviewing twenty records finds a male patient with an obstetric procedure, a haemoglobin value that would be incompatible with the patient being alive, an antibiotic course of forty days at a paediatric dose on an adult, and a discharge that precedes the admission. Every one of those is statistically unremarkable and clinically impossible. The evaluation ends, and the vendor's fidelity report is irrelevant to why.

## Why Nobody Has Built This
The knowledge of what cannot occur is not in the data — the source contains only what did occur, and a generative model interpolating between real records produces combinations that were never observed precisely because they cannot happen. Encoding the constraints requires domain expertise the vendors do not have and regard as a services cost rather than product. The constraint sets are large, domain-specific and would have to be built per vertical, which conflicts with the general-platform positioning. And no benchmark penalises implausibility, so the incentive points elsewhere.

## What to Build
Constrain the generation with domain knowledge rather than hoping the data contains it. Encode hard impossibilities explicitly — sex-specific procedures and diagnoses, age-appropriate dosing, physiological bounds, temporal ordering of clinical events, code combinations the coding system itself forbids — and enforce them during generation rather than filtering after, since a large share of them are already formally specified and merely unused, which the buy note develops. Separate impossible from merely rare, because the whole value of synthetic data in these domains is generating the rare case and a filter that removes everything unusual removes the reason for the purchase. Build the constraint set with domain experts as a structured elicitation exercise, and treat the resulting set as a durable asset that improves across every customer in that vertical — which is the thing that compounds and the reason this is a product rather than a service. Report an expert-detectable implausibility rate as the headline metric, measured by having experts review a sample, since it is the acceptance test the buyer applies and nothing else predicts the outcome. Preserve the rare-but-real cases with their constraints intact, which is the hard and valuable version of the problem. And make the constraint set inspectable by the customer's own clinicians, because the review they will do anyway is far more productive against a stated rule set than against raw records.

## Target Customer
Health systems, payers, clinical research organisations, banks and insurers building non-production and research datasets, and the generation vendors selling into regulated verticals.

## Impact If Built
Impossibility is not in the data and a general model cannot learn it. An expert-detectable implausibility rate is the acceptance test the buyer already applies, and the domain constraint set is the asset that compounds across every customer in the vertical.
