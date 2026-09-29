# Flakiness Research the Platforms Have Not Read

**Niche:** [[niches/ci-cd-platforms/flaky-tests-signal-quality/profile|Flaky Tests & Signal Quality]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Flaky test detection, categorisation and repair is an active research area with published taxonomies and tools, and commercial platforms ship a rerun-passed counter.
**Tags:** #logistic-regression #gradient-boosting #hypothesis-testing #confidence-intervals #evaluation-metrics #cross-validation #graph-theory #automation
**Contested on:** Every serious competitor in this niche is fighting to make a pipeline failure mean something again — and whoever does that takes the platform account, because once engineers learn to re-run rather than investigate, every other capability in the category is built on a signal nobody trusts.

## The Problem
Software engineering research has spent a decade on flaky tests: empirical taxonomies of their causes, detection techniques that do not rely on re-running, tools that identify order dependence by permuting execution, repair suggestions, and prediction of which new tests are likely to become flaky. The commercial platforms, which hold orders of magnitude more execution data than any study, ship a counter of tests that passed on retry.

## What Already Exists
Published flaky test taxonomies from large-scale empirical studies; detection tools including order-dependence checkers that permute test execution; prediction models from test and code features; repair pattern catalogues; and the broader test selection and prioritisation literature. Most with open implementations and public datasets.

## The Customization Gap
The adaptation is to a multi-tenant platform with enormous and heterogeneous execution data. It requires: (1) inference from natural variation rather than from deliberate experiments, since the research techniques frequently permute or repeat execution deliberately and a platform can instead exploit the fact that the same tests run millions of times across different orders, machines and loads — which is a strictly richer dataset and needs different methods; (2) cross-customer learning on the test level, where an open-source library's tests are flaky in the same way for everybody and the platform can see that while no single customer can; (3) cause attribution rather than detection, which the research supports and the products skip, and which is the entire difference between a list and an action; (4) low false positive rates, because telling a team a test is flaky when it is detecting a real intermittent bug is a serious error that will discredit the feature; and (5) actionable output tied to the remedy for the identified cause, since an engineer given a cause and a known repair pattern will fix it and one given a label will not.

## Target Customer
CI platform vendors, test tooling vendors, and large engineering organisations with a flakiness problem severe enough to fund internal work.

## Impact If Solved
An active research area addresses exactly this and the platforms holding the best data in existence have not engaged with it. Inference from natural variation is the adaptation that exploits their unique position, and cause attribution is what makes the output usable.
