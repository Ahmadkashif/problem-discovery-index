# Automated State Nexus and Income Allocation Engine

**Niche:** [[niches/tax-prep-firms/multi-state-remote-filers/profile|Multi-State Remote Filer Specialists]]
**Industry:** [[industries/tax-prep-firms|Tax Prep Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product takes a client's work location history, employer information, and income sources and determines which states require filing, how income should be allocated, and what credits apply — preparers research this manually for every multi-state return.
**Tags:** #bayesian-network #multiclass-classification #tabular-ml #compliance #automation

## The Problem
A preparer receives a client who worked remotely from three states during the year. The preparer must answer: Does each state impose income tax? Does the client meet the nexus threshold in each state (some states have day-count thresholds, others use any-presence rules)? How does each state require income allocation (days-based, source-based, domicile-based)? Is there a reciprocity agreement between any of the states? How do credits for taxes paid to other states interact? Each answer requires consulting state tax authority websites, tax research databases (RIA, CCH), and sometimes calling state revenue departments. For a 3-state return, this research takes 30-60 minutes.

## Why Nobody Has Built This
State nexus and allocation rules are (a) different across all 50 states, (b) changing rapidly as states respond to remote work, (c) context-dependent (a state may have different nexus rules for W-2 workers, self-employed individuals, and business owners), and (d) subject to ongoing litigation that creates uncertainty. Encoding these rules requires continuous legal monitoring and updates. Tax software vendors have focused on calculation (given an allocation, compute the tax) rather than determination (should you file, and how should you allocate?).

## What to Build
A nexus determination and income allocation engine that takes the client's profile (domicile state, employer state, days worked in each state, income sources, business activities) and outputs: (1) a list of states requiring filing with legal citations; (2) the recommended income allocation method for each state; (3) applicable reciprocity agreements; (4) credit-for-taxes-paid calculations. The engine is updated quarterly as state rules change and includes confidence levels for ambiguous situations (e.g., "New Hampshire does not tax earned income but is currently litigating its right to tax remote workers of MA employers").

## Target Customer
Senior preparers handling 50+ multi-state returns per season who spend 25-50 hours on state nexus research that is highly repetitive across similar client profiles.

## Impact If Built
Reduces per-return state research time from 30-60 minutes to under 10 minutes. Prevents filing errors (missed state filings, incorrect allocations) that trigger state notices and client penalty exposure. Enables the firm to take on multi-state clients confidently rather than declining complexity.
