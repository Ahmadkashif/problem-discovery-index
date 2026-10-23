# A Rate Estimate From a Sample Photo and the Firm's History

**Niche:** [[niches/contract-packagers/quoting-line-rate-estimating/profile|Quoting, Line-Rate Estimating & Job Costing]]
**Industry:** [[industries/contract-packagers|Contract Packagers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The estimator's best evidence is the similar jobs the firm has run before, and nobody can find them.
**Tags:** #tacit-knowledge-ml #gradient-boosting #cnns #k-nearest-neighbors #confidence-intervals #revenue-impact #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to predict what a new job will actually cost to run before the quote goes out, and whoever quotes closest to the run's actual labour per unit, changeover time and component scrap takes the account.

## The Problem
An estimator quoting a new display or club pack looks at a sample and remembers similar jobs, if they were there for them. The firm's past quotes and run records could show exactly how comparable formats ran, but they are not searchable by format, geometry or component type.

## Why Nobody Has Built This
The data has never been joined: quotes in spreadsheets, actuals on labour sheets. The judgement involved is tacit and the estimators are sceptical of tools that claim to replace them.

## What to Build
A tool that takes photos of the sample and the spec sheet, finds the most similar past jobs by structured features and image similarity, and shows their quoted and actual rates, ramps and scrap. It then gives a rate range for the new job from a model trained on the firm's graded history. The estimator sets the number, and the tool records it with its assumptions for grading later.

## Target Customer
Owners and estimators at co-packers with 20+ employees running many new jobs a year.

## Impact If Built
Fewer underquoted jobs, faster quotes, and an estimating skill that can be passed on.
