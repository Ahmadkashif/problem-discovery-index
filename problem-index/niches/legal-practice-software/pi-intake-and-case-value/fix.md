# The Declined Case Nobody Follows

**Niche:** [[niches/legal-practice-software/pi-intake-and-case-value/profile|Personal Injury — Intake Selection & Case Value]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Fix (Pain Point)
**One-liner:** Firms decline or refer out most of the calls they receive and never learn what happened to any of them, which means the intake criteria that shape the entire business have never been tested against a single counterfactual.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #logistic-regression #workflow-orchestration #compliance #quick-win
**Contested on:** Every serious competitor in personal injury firm software is fighting to tell a firm which of this week's intakes to sign and what each is worth against this venue and this carrier — and whoever predicts that best takes the account.

## The Problem
A firm takes 400 calls a month and signs 60. The other 340 disappear: declined outright, referred to another firm, or simply not followed up. Of the referred ones, some settle for substantial sums and the referring firm receives a fee, which is recorded in accounting and never joined back to the intake record. Of the declined ones, nothing is known at all. The firm's qualification criteria are therefore evaluated against exactly zero evidence about what they exclude, which is the one thing that would tell the firm whether they are right.

## Why It's Still Broken
Nobody owns the question. Intake teams are measured on sign rate and speed; marketing is measured on cost per signed case; nobody is measured on what was correctly declined. The referral fee lands in a different system months later with no matter number linking it back. And there is a mild disincentive at the top: a partner who discovers the firm has been declining a profitable segment for three years has discovered an expensive mistake, and the number is easier not to compute.

## What a Fix Looks Like
Join the three records the firm already has. Referral agreements produce outcomes and fees — record the referred matter's identity at referral time so the fee, when it arrives, closes the loop against the original intake. Where cases are declined outright, docket monitoring can find a meaningful share of them filed by another firm, and the public record gives a resolution. That produces the first outcome data any PI firm has ever had about its own declines, and it is enough to test the criteria: which declined segments went on to resolve well, at what rate. Add a small deliberate exception budget — a handful of marginal cases signed each month specifically to learn — and the criteria become a thing the firm measures rather than a thing it inherited.

## Who Feels the Pain
Intake specialists judged on a sign rate whose correctness nobody knows; marketing directors optimising spend toward criteria that have never been validated; and the callers in whatever segment the firm is wrongly declining.

## Impact If Fixed
Closing the referral loop is a fortnight of integration work and produces the segment's first counterfactual data. Firms that run this typically find at least one declined segment with materially better economics than parts of what they sign, and the correction is immediate and permanent. It is also the only mechanism that keeps the build note's model from simply memorising the firm's existing filter.
