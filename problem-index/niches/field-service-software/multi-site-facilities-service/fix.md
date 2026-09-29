# Quality Measured by Who Complained

**Niche:** [[niches/field-service-software/multi-site-facilities-service/profile|Multi-Site Facilities Service]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Fix (Pain Point)
**One-liner:** A facilities contractor's operating picture of its own quality is the set of complaints that reached an account manager's inbox, which measures client temperament at least as much as service, and none of it is ever recorded as data.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #bert #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in multi-site facilities software is fighting to prove that service actually happened, to the standard promised, at a site nobody supervises — and whoever makes verification credible to the client takes the contract.

## The Problem
A client emails an account manager: the third-floor washrooms were not done again. The account manager calls the supervisor, the supervisor speaks to the crew, and the matter is resolved. Nothing is recorded. The same exchange happens across forty accounts, and the contractor's understanding of its own quality is whatever survives in a few managers' heads. A quiet client with poor service looks identical to a well-served one. When a contract is lost, the post-mortem is a conversation, and the pattern that would have predicted it — a rising complaint rate at that account over six months — was never visible because it was never counted.

## Why It's Still Broken
Complaints arrive through personal channels, which is how account management works in this industry and is not going to change. Logging them feels bureaucratic and slightly disloyal — an account manager who records every complaint is creating a written record of their account's problems. And there is no obvious place to put them, since the field service system models work orders rather than client sentiment. So the single richest quality signal the contractor receives is handled entirely as correspondence.

## What a Fix Looks Like
Capture complaints as structured records with almost no effort. Email to an account address is parsed into site, area, issue type and severity automatically, which is ordinary text work, and the account manager confirms with one tap rather than filling in a form. Resolution is recorded with a cause. From that, the contractor gets the three things it lacks: complaint rate per site normalised for site size and client contact frequency, trend per account with alerting on a rising rate, and issue-type concentration, which usually points at a specific task in the specification being systematically skipped. Compare against the inspection sample, since a site with a low complaint rate and poor inspection scores is a quiet client who is about to leave, and that is the most valuable single finding this data produces.

## Who Feels the Pain
Account managers who sense an account is deteriorating and have nothing but an impression; supervisors chasing complaints one at a time with no pattern view; and crews blamed repeatedly for a specification item that was never properly scheduled.

## Impact If Fixed
Complaint data is free, already arriving, and currently discarded; structuring it takes parsing and a tap. Rising-rate alerting on an account gives a contractor months of warning before a renewal it would otherwise lose blind, and the quiet-client-with-poor-scores finding identifies the accounts most at risk, which no contractor in this segment can currently see.
