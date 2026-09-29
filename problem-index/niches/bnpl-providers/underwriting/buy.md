# Credit Scoring Practice

**Niche:** [[niches/bnpl-providers/underwriting/profile|Underwriting]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Consumer credit has a century of scoring practice, model governance and affordability assessment, and instalment providers built a fast stack on a thin file.
**Tags:** #logistic-regression #gradient-boosting #survival-analysis #compliance #evaluation-metrics #confidence-intervals #hypothesis-testing #causal-inference
**Contested on:** This niche is not terminal — inferring capacity from a thin file and seeing what a consumer owes elsewhere are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
Consumer credit scoring is old, heavily studied and heavily regulated. Scorecards are built to documented standards, validated independently, monitored for drift, tested for disparate impact, and governed under model risk frameworks. Affordability assessment has its own developed methodology. Reject inference — estimating how declined applicants would have performed — is a standard technique for the exact problem of learning from a censored population. Instalment providers face all of these questions and frequently approach them as engineering rather than as credit.

## What Already Exists
Scorecard development methodology; reject inference for censored outcomes; affordability assessment frameworks; model validation and monitoring under governance; and disparate impact testing.

## The Customization Gap
The adaptation is to a decision made in a checkout on a thin file with a six-week horizon. It requires: (1) a decision budget measured in milliseconds inside a purchase flow, where scorecard practice assumes an application process — the latency constraint shapes what evidence can be gathered and is the practical difference; (2) applicants with no bureau file, which makes the traditional scorecard's primary input absent for a large share and forces alternative evidence the practice has little to say about; (3) a six-week outcome horizon, which makes continuous validation feasible in a way conventional credit's multi-year horizon never allows — an advantage the sector does not exploit; (4) obligations invisible to the assessor, which breaks the affordability calculation at its foundation and is the accumulation problem; and (5) a regulatory position that is developing rather than settled, so practice should anticipate rather than comply.

## Target Customer
Credit risk leadership at instalment providers, the bureaus adapting to short-term obligations, and credit scoring practitioners for whom the thin-file instalment population is new ground.

## Impact If Solved
A century of practice exists and the sector approached the questions as engineering. The six-week horizon makes continuous validation feasible where conventional credit never could, and invisible obligations break the affordability calculation at its foundation.
