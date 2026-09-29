# Feature Store Consistency Guarantees

**Industry:** [[mlops-platforms|MLOps Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Feature stores exist specifically to guarantee that training and serving see the same values, and they deliver that guarantee only for features defined inside them — which is a minority of the features any real model uses.
**Tags:** #feature-engineering #hypothesis-testing #confidence-intervals #evaluation-metrics #change-point-detection #data-integration #workflow-orchestration

## The Problem
The feature store was invented to solve training-serving skew. Define a feature once, materialise it to an offline store for training and an online store for serving, and both paths read the same definition.

It works for the features that live in it. In practice a model's feature vector is assembled from several sources: some from the feature store, some computed inline in the serving code because they depend on the request itself, some passed in by the calling service, some looked up from a database the feature store does not front. The guarantee covers one subset and the skew lives in the others.

Point-in-time correctness is the second recurring failure. Training data must reflect what was knowable at prediction time, and constructing that requires joining feature values as of the historical moment rather than as of now. Feature stores support point-in-time joins and the support is easy to bypass, and a leaked future value produces an evaluation score that looks excellent and a production model that does not work.

Freshness is the third. A feature materialised hourly is stale by up to an hour at serving and was computed exactly at event time in training. Nobody quantifies what that costs.

## What Already Exists
Feast provides an open standard for feature definitions with offline and online stores. Tecton, Databricks Feature Store, SageMaker Feature Store and Vertex Feature Store are mature commercial implementations. Point-in-time join support is standard. Materialisation scheduling and monitoring are provided. Feature lineage and discovery interfaces exist.

## The Customisation Gap
Coverage is the gap, and it is architectural rather than a missing feature. Request-time features cannot be pre-materialised, features owned by other services will not be migrated, and the store therefore guarantees consistency for part of the vector while the model consumes all of it. Nothing measures what fraction of a given model's features are actually covered, which would be the first useful number.

Point-in-time correctness verification is absent. Whether a training set actually respects temporal ordering is checkable — by comparing feature timestamps against label timestamps systematically — and is checked by convention rather than by the platform. Leakage detection should be a gate on training rather than a discovery made after deployment.

Freshness impact is unmeasured. The cost of an hourly materialisation versus a five-minute one, expressed in model performance rather than in latency, is estimable by evaluating against features at both staleness levels and is not something any platform reports, so materialisation frequency is chosen by intuition and budget.

## Impact If Solved
The feature store's entire justification is a consistency guarantee, and it currently covers an unmeasured fraction of the surface where inconsistency occurs. Measuring coverage, verifying point-in-time correctness as a gate, and quantifying freshness cost turns a partial guarantee into a stated one.
