# Reliability Engineering and Acceptance Sampling

**Niche:** [[niches/ai-agent-platforms/task-reliability-prediction/profile|Task Reliability Prediction]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Manufacturing built acceptance sampling and reliability demonstration testing to decide whether a batch meets a standard at a stated confidence, and this category ships on a demo.
**Tags:** #hypothesis-testing #confidence-intervals #probability-distributions #monte-carlo-methods #evaluation-metrics #descriptive-statistics #survival-analysis #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to tell a buyer, before deployment, what fraction of their tasks the agent will complete correctly and which ones it will fail — and whoever does that takes the account, because no other claim in this market is checkable.

## The Problem
Deciding whether something meets a quality standard, with a stated confidence, from a sample rather than by inspecting everything, is what acceptance sampling was built for and it has a century of practice, published plans and agreed producer and consumer risk conventions. Reliability demonstration testing does the same for failure rates. The question of how many tasks a pilot needs to establish a reliability claim has a precise answer, and this category picks a round number.

## What Already Exists
Acceptance sampling plans with defined producer and consumer risk; reliability demonstration testing with required sample sizes for a target rate at a confidence; sequential sampling for early stopping; stratified sampling methodology; failure mode and effects analysis with severity weighting; and process capability indices.

## The Customization Gap
The adaptation is to a population of tasks that is heterogeneous and whose failure costs vary enormously. It requires: (1) stratified acceptance by task type rather than one plan over a mixed population, since the aggregate rate is not the quantity anybody cares about and the classical single-plan approach hides exactly the segments that matter; (2) severity-weighted acceptance, because a wrong refund and a slightly awkward reply are both failures and treating them equally is the category's most consequential measurement error — failure mode analysis supplies the weighting discipline; (3) sample sizes computed from the target rate and confidence rather than chosen, which immediately shows that most pilots are far too small to support their conclusions; (4) sequential plans so a clearly-failing agent is rejected early and a clearly-passing one accepted without a full run, which matters when each trial costs model calls and human grading; and (5) continued sampling in production as ongoing acceptance, since the input distribution drifts and a one-time demonstration ages.

## Target Customer
Agent vendors, enterprise buyers and their risk functions, and the quality engineering profession for whom this is a fresh application of well-established method.

## Impact If Solved
A century of acceptance sampling answers exactly how many tasks a pilot needs, and the category picks a round number. Severity-weighted, type-stratified acceptance addresses the measurement error that makes an aggregate resolution rate misleading.
