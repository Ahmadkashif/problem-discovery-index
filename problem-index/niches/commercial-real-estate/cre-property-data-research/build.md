# Verification Effort Allocated by Decay, Not by Calendar

**Niche:** [[niches/commercial-real-estate/cre-property-data-research/profile|Commercial Property Data & Research Platforms]]
**Industry:** [[industries/commercial-real-estate|Commercial Real Estate]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Hundreds of researchers re-verify facts on a rotation, so a building where nothing has happened in six years gets called as often as one where three tenants just moved out.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #change-point-detection #confidence-intervals #optimization-fundamentals #data-integration #revenue-impact

## The Problem
The product is a database of facts that decay at wildly different rates. A building's floor plate does not change; its rent roll changes constantly; its ownership changes rarely but consequentially. Verification capacity — a large workforce making calls — is allocated largely by rotation and by market priority, which treats decay as uniform when it is anything but. The consequence is systematic: high-churn assets in active submarkets go stale between visits while stable assets are re-confirmed repeatedly, and the staleness concentrates exactly where subscribers are most likely to be relying on the data for a live transaction. Meanwhile the company holds, in its own change history, a detailed record of how fast every field on every property type actually moves.

## Why Nobody Has Built This
Verification has always been organized as a coverage obligation — every property in the coverage universe touched on a cycle — because that is what the sales promise implies and what is easy to manage against. Reallocating on predicted decay means accepting that some properties are deliberately left longer, which reads as a coverage reduction unless the reasoning is visible. The prediction itself is also non-trivial: change events are sparse per property, so decay has to be modelled hierarchically across property types, submarkets, and tenant profiles rather than per asset. And field research is managed operationally, with no analytics function positioned to own the allocation question.

## What to Build
A decay model over the change history that estimates, per property and per field, the probability the current record is already wrong. Change events the company records anyway — tenant moves, ownership transfers, rent adjustments, construction and permit activity, listing appearances — become the training signal, and external activity indicators supply leading information the internal record cannot: a permit filed, a listing posted, a loan recorded. Verification capacity is then allocated by expected error reduction per call rather than by rotation, with the constraint that no property exceeds a maximum age regardless of predicted stability, which preserves the coverage promise. The same model directly produces the staleness signal subscribers most need, since a property flagged as likely to have changed is exactly the one a broker should confirm before relying on it. Allocation runs continuously and is measured against verification outcomes, so the model learns which of its predictions were right — a feedback loop that exists naturally here and almost nowhere else in this sweep.

## Target Customer
Chief research officers and heads of data operations at property data platforms running 500-2,000 researchers, and the subscribers whose transaction decisions currently rest on records of unknown age.

## Impact If Built
Improves accuracy without adding headcount, in the largest cost centre the business has. It also converts coverage from a promise into a measured property — a platform that can state expected accuracy by field and property type is making a claim no competitor with the same rotation model can match, and it is the claim subscribers actually care about when a number is going into an underwriting.
