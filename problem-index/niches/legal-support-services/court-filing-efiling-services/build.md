# Rejection Prediction Before the Envelope Is Sent

**Niche:** [[niches/legal-support-services/court-filing-efiling-services/profile|Court Filing & E-Filing Services]]
**Industry:** [[industries/legal-support-services|Legal Support Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** E-filing providers hold years of envelopes and the clerks' reasons for rejecting them, and use none of it to stop the next rejection.
**Tags:** #gradient-boosting #logistic-regression #large-language-models #feature-engineering #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to get a filing accepted by the clerk on the first submission, before the deadline, and whoever predicts and prevents clerk rejections best takes the account.

## The Problem
Clerks reject filings for reasons that repeat: a filing code that this county does not accept with that case type, a proposed order uploaded as the lead document, a missing fee waiver attachment. The filer learns hours later, sometimes after the deadline.

## Why Nobody Has Built This
Rejection reasons are free text written by thousands of clerks; providers compete on price per envelope and integration, not on acceptance rates; and the courts own the rules but do not publish them as data.

## What to Build
A model trained on each provider's envelope history and parsed rejection notices that scores every envelope for rejection risk by court, case type and filing code, names the likely reason, and suggests the fix before submission. Acceptance rate by court becomes a reported service metric.

## Target Customer
E-filing service providers and attorney-service companies; large litigation support teams that file directly.

## Impact If Built
Fewer last-day rejections, an estimated reduction of a third or more in avoidable rejections (estimate), and a provider able to sell measured acceptance rather than access.
