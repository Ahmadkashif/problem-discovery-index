# Respondent Quality as a Modelled Property of Every Interview

**Niche:** [[niches/data-analytics-consultants/survey-panel-operators/profile|Survey Research & Panel Operators]]
**Industry:** [[industries/data-analytics-consultants|Data Analytics Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Panel quality is managed by removing obvious bad actors after the fact, when the useful question is how much each completed interview should count — and the paradata to answer it is collected and thrown away.
**Tags:** #bayesian-inference #probability-distributions #hypothesis-testing #confidence-intervals #gradient-boosting #evaluation-metrics #feature-engineering #dimensionality-reduction #data-integration #revenue-impact

## The Problem
Panel research lives or dies on whether respondents are who they claim and are answering attentively, and both are under sustained attack — professional respondents, fraudulent completes, and automated submission have become an industry-wide problem. The defence is largely binary and retrospective: trap questions, speed checks, and duplicate detection remove obvious offenders, and everyone else counts equally. That is a blunt instrument for a graded problem. A respondent who is real but rushing, or real but answering outside their claimed expertise, degrades a study without triggering any check, and their responses enter the dataset weighted identically to a careful one. Meanwhile every interview generates paradata — timing per question, revision behaviour, straightlining, device and session characteristics, and the respondent's entire history across prior studies — that would support a graded quality estimate and is retained, if at all, for fraud screening alone.

## Why Nobody Has Built This
Quality is contractually framed as a screening obligation — deliver n valid completes — which makes it a pass/fail concept in every commercial conversation, so nothing in the operating model asks for a graded one. Paradata is stored per study rather than per respondent across studies, which is where the signal actually lives. And there is a commercial disincentive that is rarely said aloud: a graded quality model would show that some delivered completes are weak, in an industry where the deliverable is a count.

## What to Build
A respondent quality model producing a calibrated estimate per interview rather than a screening verdict. It is built on paradata joined across studies at the respondent level — response timing relative to question complexity, consistency with prior stated characteristics, straightlining and pattern behaviour, and attention indicators — validated against the cases where truth is knowable, such as verifiable claims and repeated measures. The output feeds weighting rather than exclusion, so a study's effective sample size reflects the quality actually obtained, which is more honest and more useful than a headline count. Cross-study respondent history is the decisive input and is currently the least used: someone who has claimed four incompatible occupations across a year is identifiable only if the panel looks across studies, and most quality systems do not. The same model directs panel investment, showing which recruitment sources produce respondents who hold up rather than merely complete.

## Target Customer
Chief research officers and heads of methodology at panel operators running 500-3,000 staff, and the insight buyers who commission studies and currently receive a completed sample with no quality gradient attached.

## Impact If Built
Attacks the credibility problem that is the industry's biggest structural threat, and does it with data already collected. Quality-weighted delivery is also a genuine product differentiator in a market where every operator promises clean data and none can evidence it — and it directs recruitment spend, the largest recurring cost, at sources that produce respondents worth having.
