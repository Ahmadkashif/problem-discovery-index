# Debtor Contactability & Payment Propensity Scoring

**Industry:** [[collections-agencies|Collections Agencies]]
**Type:** High Impact
**One-liner:** Every outbound call is prioritized by likelihood of reaching the debtor and converting the conversation into a payment arrangement, replacing static segmentation with dynamic scoring.
**Tags:** #gradient-boosting #binary-classification #ranking #tabular-ml #revenue-impact

## The Problem
Collection agencies purchase or receive debt portfolios and must work thousands of accounts with limited agent hours. Today, accounts are prioritized by balance size and days-past-due — crude proxies that ignore behavioral signals like prior contact attempts, time-of-day patterns, payment history on other accounts, and demographic indicators. The result is that agents burn through low-probability accounts at the same rate as high-probability ones, depressing recovery rates to 15-20% on purchased debt when optimal targeting could push that significantly higher.

## Why It's Unsolved
Building an effective propensity model requires joining data across collection platforms (payment history, contact attempts, disposition codes), skip tracing feeds (phone validity, address recency), and external enrichment (credit bureau attributes, employment indicators) — data that lives in 4-6 siloed systems with no common key beyond SSN. Additionally, the target variable is noisy: a "successful contact" that leads to a broken promise is coded differently across platforms, and agencies rarely have clean labeled outcomes that track from first contact through payment fulfillment. Regulatory constraints on data usage (FCRA, state privacy laws) further limit which features can legally be used in scoring.

## What a Solution Looks Like
A scoring engine ingests account-level features (balance, age, prior attempts, disposition history), contact-level features (phone type, time since last verified, number of prior owners), and enrichment data (employment status, credit attributes where permissible). It outputs a ranked queue for each agent shift — ordered by expected value (contact probability x payment probability x recoverable amount) — with recommended contact channel (call, text, letter, email) and optimal time window. The dialer consumes this queue directly, replacing static list ordering.

## Impact If Solved
A 5-10 percentage point improvement in right-party contact rate translates to $2-4M in additional annual recoveries for a mid-size agency (500 seats, $200M portfolio). Agents spend more of their shift in productive conversations, improving both revenue and job satisfaction.
