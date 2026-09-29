# The Mechanism: What a Credit Score Actually Models

**Origin:** [[origins/credit-bureaus/profile|Credit Bureaus]]
**Tags:** #logistic-regression #probability-distributions #evaluation-metrics #feature-engineering #hypothesis-testing #causal-inference #compliance #tacit-knowledge-ml

## The Question a Score Answers

A FICO-style score is not a measure of a person's worth, morality, or likely life trajectory — the character-file system this origin replaced tried, badly, to answer questions like that. **It answers one specific, narrow, statistical question: what is the probability that this individual will become 90-plus days delinquent on some obligation within roughly the next 24 months?**

## The Inputs, Deliberately Chosen

The published FICO factor weights are approximate but consistently ordered: payment history (the single largest factor — has this person paid on time before), amounts owed and utilisation (how much of available credit is in use), length of credit history, new credit (recent applications), and credit mix (variety of account types). **What is explicitly excluded is at least as important as what is included**: no occupation, no address or neighbourhood, no race, sex, or the subjective character assessments that defined the pre-1970 system. The Equal Credit Opportunity Act made several of these exclusions a legal requirement, not merely a design choice.

## The Statistical Shape

This is a **scorecard problem**: predict a binary outcome (default within the window, or not) from a fixed set of features, calibrated so the output can be read as a probability and compared against a threshold a lender sets for its own risk appetite. The mechanics are the textbook logistic-regression case — weighted, summed inputs pushed through a function that outputs a bounded probability — though production scorecards from this era were frequently built and validated as much through segmentation and business rules as through a single fitted model, because the disputability requirements FCRA imposed favoured a model whose reasoning could be explained to a regulator and to the consumer who challenged it.

## The Trade-Off Nobody Fully Resolved

**What statistical scoring gave up, deliberately, was context** — the same trade airline yield management made when it gave up price fairness for revenue. A scorecard cannot tell the difference between someone who missed a payment because they are unreliable and someone who missed it because a hospital bill arrived the same week; it counts the same event the same way for both. The **thin-file** or **credit-invisible** population — people with too little credit history to score reliably — is a direct byproduct of a system that requires history as its raw material; this vault's own `bnpl-providers` note describes an entire industry built substantially to serve exactly this population.

## The Contested Question — Presented as Open, Not Resolved

**Whether replacing character judgement with statistical scoring reduced discrimination in lending is a genuinely unsettled question, and this file will not resolve it.** One line of argument, made by the Federal Reserve and much of the lending industry, holds that a model using only payment behaviour and excluding protected characteristics by construction removes the opportunity for a human gatekeeper's individual prejudice to operate. The competing line, made by consumer advocates and a body of legal scholarship, holds that the inputs themselves — credit history, neighbourhood-correlated utility and rental patterns, generational wealth reflected in existing credit access — encode the effects of historical redlining and discrimination, so a "neutral" model reproduces disparate outcomes without anyone needing to intend them. **Both positions are held by serious, credentialed people citing real data, and the honest position is that this is unresolved, not that one side is obviously correct.**

## The Transferable Pattern

> **A model that removes an input to remove a bias only succeeds if nothing else in the remaining inputs is correlated with the thing you removed.** Address, spending category, even the device used to apply, can each silently reconstruct what a scorecard was explicitly built to exclude — a lesson that generalises to almost any "fairness through exclusion" design in this vault's ML-opportunity notes, and one worth treating with real suspicion rather than as a solved problem.

**Sources:** myFICO, *The History of the FICO Score*; Federal Reserve, *Report to the Congress on Credit Scoring and Its Effects on the Availability and Affordability of Credit* (2007); Wikipedia, *Equal Credit Opportunity Act*, *Credit score in the United States*; this vault's `industries/bnpl-providers.md`.
