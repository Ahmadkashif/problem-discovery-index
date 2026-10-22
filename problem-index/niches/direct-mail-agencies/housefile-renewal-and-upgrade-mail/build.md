# Donor-Level Ask and Cadence Optimisation

**Niche:** [[niches/direct-mail-agencies/housefile-renewal-and-upgrade-mail/profile|Housefile Renewal & Upgrade Mail]]
**Industry:** [[industries/direct-mail-agencies|Direct Mail Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every donor gets the same multiplier on their last gift and the same appeal calendar, though some give more when asked for more and others lapse when mailed too often.
**Tags:** #causal-inference #gradient-boosting #survival-analysis #bayesian-optimization #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to set each existing donor's ask amount, cadence and package so renewal and upgrade rates rise without mailing donors into lapse — and whoever gets the ask right donor by donor takes the account.

## The Problem
A national charity mails its active donors roughly twelve to twenty times a year (estimate). Each reply device carries an ask string, usually anchored on the highest previous contribution. Whether a donor would give more if asked for more, or would give again sooner if mailed less, is answered for segments by occasional tests and for individuals not at all.

## Why Nobody Has Built This
Testing ask amounts per donor needs randomisation over many appeals, and a bad ask costs revenue in the moment. Lapse caused by over-mailing shows up months later and is attributed to "donor fatigue" rather than to a decision.

## What to Build
An experimentation and modelling layer over the appeal calendar: small randomised variations in ask string and mailing frequency on every appeal, estimated with uplift models of gift amount and time to lapse, and fed back into per-donor recommendations — ask ladder, number of appeals and package — that the strategist reviews before each mailing.

## Target Customer
Annual giving directors and housefile strategists at nonprofits with 50,000+ active mail donors (estimate).

## Impact If Built
Even small gains in average gift and retention across the housefile compound into the largest single lever on net fundraising revenue, without adding a piece of mail.
