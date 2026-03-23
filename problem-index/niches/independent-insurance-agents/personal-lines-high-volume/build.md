# Rate-Change Detection and Auto-Reshop Engine

**Niche:** [[niches/independent-insurance-agents/personal-lines-high-volume/profile|Personal Lines High-Volume Shops]]
**Industry:** [[industries/independent-insurance-agents|Independent Insurance Agents]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool proactively detects when a client's carrier has filed a rate increase and automatically re-shops the policy across appointed carriers before the renewal date.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #automation #revenue-impact

## The Problem
Personal lines agencies discover a client's rate increase only when the renewal declaration page arrives — typically 30-45 days before expiration. At that point, the CSR must manually pull the current policy details, run comparative quotes, prepare options for the client, and process any carrier change. For agencies with 2,000+ policies, this reactive workflow means many renewals go un-shopped, and clients discover the increase on their credit card statement — often triggering a call to a competitor.

## Why Nobody Has Built This
Carrier rate filings are public data (state DOI records), but no product connects filed rate changes to individual policies in an agency's book of business and triggers automated re-quoting. Building this requires mapping policy-level data (carrier, coverage type, territory, tier) to rate filing impacts, which varies by state and carrier. The comparative rater vendors (EZLynx, TurboRater) have the quoting infrastructure but lack the rate-filing intelligence layer.

## What to Build
A monitoring engine that tracks carrier rate filings across all states and appointed carriers, identifies which policies in the agency's AMS will be affected, estimates the premium impact, and triggers automated re-quoting through the comparative rater. The producer receives a daily dashboard: "47 policies renewing in the next 60 days are affected by rate increases averaging 12% — 23 have competitive alternatives."

## Target Customer
Operations managers at personal lines agencies with 2,000+ active policies who currently rely on CSRs to manually check each renewal.

## Impact If Built
Proactive reshop increases client retention by 5-10% and captures 15-20% of policies that would otherwise lapse to direct carriers. For a 3,000-policy agency, that is 150-300 retained policies worth $75K-$150K in annual commission revenue.
