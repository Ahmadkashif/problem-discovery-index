# Verdict and Settlement Databases Adapted to the Firm's Own Venue

**Niche:** [[niches/legal-practice-software/pi-intake-and-case-value/profile|Personal Injury — Intake Selection & Case Value]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Verdict and settlement reporters are an established purchasable product that every PI firm consults and nobody models with, because the reported cases are a biased sample of tried outcomes and the firm's business is untried ones.
**Tags:** #bayesian-inference #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #dimensionality-reduction #data-integration #revenue-impact
**Contested on:** Every serious competitor in personal injury firm software is fighting to tell a firm which of this week's intakes to sign and what each is worth against this venue and this carrier — and whoever predicts that best takes the account.

## The Problem
A lawyer valuing a case pulls comparable verdicts from a reporter, finds three similar cases in the county with awards between $180K and $1.1M, and forms a judgment. The reported cases are the ones that went to verdict, which is a small and unrepresentative slice — cases tried are systematically those where the parties could not agree, which means they are the disputed liability cases and the outlier damages cases. Using them as a reference for a case that will settle is a known error that every practitioner half-knows and nobody corrects, because the alternative reference — what cases like this actually settle for in this venue — is not published by anyone.

## What Already Exists
Jury Verdict Research, VerdictSearch, Trellis and Lex Machina supply verdict and docket data with real coverage, and the docket analytics vendors have made judge- and venue-level litigation statistics ordinary. Carriers maintain far better settlement data internally and publish none of it. Firms maintain their own settlement history in their case management system and do not treat it as data. The purchasable half of the picture is the tried half.

## The Customization Gap
The adaptation is to combine the purchased tried-case data with the firm's own settled-case data while being explicit about what each one is evidence for. It requires: (1) treating verdicts as a censored, selected sample and correcting for that selection rather than averaging over it, which is a well-understood statistical problem and an unusual one in this industry; (2) using the firm's own settlements — and pooled settlements across firms on a platform, where permitted — as the primary evidence for settlement value, with verdicts informing the tail; (3) building venue, judge and carrier effects as structured factors rather than as filters, so a thin cell borrows strength from similar cells instead of returning three cases; (4) exposing uncertainty honestly, since a lawyer given a point estimate will anchor on it and a lawyer given an interval will negotiate with it; and (5) tracking every valuation against what the case ultimately resolved for, which is the feedback loop the reporters can never provide and the platform can.

## Target Customer
PI firms that subscribe to a verdict reporter and use it for valuation, and the case management vendors who could bundle a defensible valuation rather than a link to a search.

## Impact If Solved
Correcting the tried-case bias typically moves valuations materially, and in a consistent direction, which changes both what a firm demands and what it accepts. The firm's own settlement history is the highest-value asset in this adaptation and costs nothing to acquire — it is already in the system, unmodelled.
