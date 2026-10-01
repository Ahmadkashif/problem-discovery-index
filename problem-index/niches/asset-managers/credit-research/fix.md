# Surveillance by Rotation

**Niche:** [[niches/asset-managers/credit-research/profile|Credit Research]]
**Industry:** [[industries/asset-managers|Asset Managers]]
**Type:** Fix (Pain Point)
**One-liner:** Credit analysts review issuers on a fixed calendar because nothing tells them which of their hundred names deserves attention this week.
**Tags:** #change-point-detection #gradient-boosting #time-series-forecasting #evaluation-metrics #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to read covenant and offering documents across hundreds of issuers per analyst and catch credit deterioration before the rating agencies do — and whoever does that avoids the downgrade and default losses that decide a fixed income manager's ranking.

## The Problem
The analyst's week is set by earnings dates and review cycles. A stable utility gets the same attention as a levered retailer whose revolver availability is shrinking. The analyst knows which names worry her, but the coverage universe is too large to hold in mind, and the names that surprise are the ones nobody was watching.

## Why It's Still Broken
Monitoring tools show prices and news but do not rank issuers by change in risk against the firm's own internal view, and internal ratings are rarely stored as a time series that a ranking could use.

## What a Fix Looks Like
A weekly ranked list per analyst: issuers where spreads, filings, rating outlooks or liquidity measures have moved materially relative to the firm's internal rating and recorded thesis, with the specific evidence linked. Analysts mark each as reviewed, unchanged or rating-changed, which builds the internal rating history and the label set at the same time.

## Who Feels the Pain
Credit analysts carrying large coverage lists; PMs who discover deterioration from the price.

## Impact If Fixed
Attention is allocated by risk rather than calendar, and the firm accumulates the internal-rating history it needs to evaluate its own credit research.
