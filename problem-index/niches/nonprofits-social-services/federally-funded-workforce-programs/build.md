# Outcome-Risk Early Warning System

**Niche:** [[niches/nonprofits-social-services/federally-funded-workforce-programs/profile|Federally Funded Workforce Programs]]
**Industry:** [[industries/nonprofits-social-services|Nonprofits Social Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool today can predict which enrolled participants are at risk of not achieving WIOA performance outcomes (employment, credential, measurable skill gain) early enough for case managers to intervene.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
WIOA programs are funded based on performance outcomes — if a program falls below negotiated targets for entered employment rate, median earnings, credential attainment, or measurable skill gains, it faces sanctions and funding reductions. Case managers develop intuition over years about which participants are at risk: the ones who miss two consecutive training sessions, the ones whose transportation situation just changed, the ones who enrolled in a credential program above their reading level. But this intuition isn't systematized, and by the time poor outcomes show up in quarterly reports, it's too late to intervene.

## Why Nobody Has Built This
Outcome prediction for workforce programs requires combining structured data (demographics, enrollment data, attendance) with unstructured signals (case notes, engagement patterns, life events). The data lives across 3-4 disconnected systems, and no single vendor has access to all of it. Additionally, workforce development boards are cautious about predictive models that could introduce bias — any system must be transparent about its risk factors and avoid reinforcing demographic disparities.

## What to Build
A risk-scoring engine that ingests participant data from case management systems, attendance tracking, and state workforce databases, identifies early-warning signals correlated with poor outcomes (attendance drop-off, missed milestones, enrollment in mismatched training), and surfaces at-risk participants to case managers with specific recommended interventions. The model is trained on historical outcome data and updated monthly as new outcomes are recorded.

## Target Customer
Workforce Development Board directors managing $5M-$50M in WIOA funding who face sanctions for missing performance targets. There are 550 WDBs in the US.

## Impact If Built
Enables targeted intervention 60-90 days earlier in the participant journey, improving WIOA performance outcomes by 8-12% and preventing the $500K-$2M funding reductions that follow missed performance targets.
