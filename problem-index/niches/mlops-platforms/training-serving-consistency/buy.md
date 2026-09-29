# Data Validation and Contract Testing

**Niche:** [[niches/mlops-platforms/training-serving-consistency/profile|Training–Serving Consistency]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software engineering solved the equivalent problem with contract testing and data engineering solved it with schema contracts, and machine learning pipelines use neither across the training–serving boundary.
**Tags:** #data-integration #hypothesis-testing #evaluation-metrics #automation #workflow-orchestration #descriptive-statistics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to prove that the feature values a model sees in production are the values it was trained on — and whoever does that takes the account, because it is the most common expensive failure in applied machine learning and nothing currently detects it.

## The Problem
Two systems that must agree on a shared interface is a solved problem with a name. Consumer-driven contract testing has services publish and verify their expectations of each other in continuous integration, catching the mismatch before deployment. Data contracts do the same for schemas and semantics between producers and consumers. Machine learning has two implementations of the same feature logic maintained by two teams and verifies neither against the other.

## What Already Exists
Consumer-driven contract testing frameworks with broker infrastructure and CI integration; data contract tooling with schema registries, compatibility checking and enforcement at the producer; data validation libraries with schema inference and distributional assertions; and property-based testing for verifying that two implementations agree across generated inputs.

## The Customization Gap
The adaptation is to a contract whose subject is a computed value rather than a schema. It requires: (1) the contract expressed as feature semantics — definition, window, aggregation, null handling, point-in-time rule — rather than as types, since the failures here pass every type check and the semantics are what diverge; (2) verification by differential execution against shared inputs rather than by static comparison, because the definitions live in different languages and only running both settles whether they agree; (3) tolerance calibration, since floating-point and ordering differences produce tiny legitimate divergences and a zero-tolerance contract will be disabled within a week; (4) the model as the consumer that publishes the contract, which is the right direction of ownership and inverts how most feature pipelines are organised today; and (5) enforcement in CI on both pipelines, so that editing either one fails the build rather than silently degrading a model — which is the property that makes this preventive.

## Target Customer
ML platform teams, the data engineering functions who own the serving pipelines, and the contract testing and data contract vendors for whom feature semantics are an unserved contract type.

## Impact If Solved
The pattern for two systems agreeing on an interface is mature and unapplied here. Differential execution against shared inputs, enforced in CI on both pipelines, converts the category's most expensive silent failure into a failed build.
