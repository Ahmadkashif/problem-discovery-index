# Self-Insured Plan Performance Intelligence Dashboard

**Niche:** [[niches/insurance-tpa/self-insured-employers/profile|Self-Insured Employer Programs]]
**Industry:** [[industries/insurance-tpa|Insurance TPA]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product gives mid-market self-insured employers real-time visibility into claims trends, stop-loss utilization, and plan design impact without requiring actuarial consulting.
**Tags:** #time-series-forecasting #gradient-boosting #tabular-ml #revenue-impact

## The Problem
Self-insured employers making $5M-$50M in annual claims decisions rely on quarterly PDF reports from their TPA. They discover adverse trends (e.g., a spike in musculoskeletal claims, a single claimant approaching the stop-loss attachment point) months after the trend began. Plan design changes happen annually during renewal, using stale data and broker intuition rather than real-time analytics. CFOs managing millions in health spend have less visibility than a $50K/month Google Ads manager.

## Why Nobody Has Built This
TPAs don't want to build it — transparent claims analytics give employers leverage to negotiate TPA fees and switch administrators. Consulting firms sell this as high-margin professional services ($50K-$200K annual engagements) and have no incentive to productize. The data exists in TPA claims systems but is locked behind proprietary formats and reporting limitations.

## What to Build
A SaaS dashboard that ingests claims data from any TPA (via data feeds, 835/837 EDI, or API) and provides employers with real-time trend analysis, stop-loss tracking, plan design scenario modeling, and peer benchmarking. Automated alerts for emerging trends (e.g., "Pharmacy spend up 15% QoQ — driven by 3 specialty drug starts"). Annual plan design recommendations based on the employer's actual claims distribution.

## Target Customer
Mid-market self-insured employers (200-2,000 employees) spending $3M-$30M annually on health claims who currently receive only basic TPA reporting.

## Impact If Built
Enables data-driven plan design decisions that reduce total health spend by 5-10%. For an employer spending $15M annually, this represents $750K-$1.5M in savings — a 10-20x ROI on a $75K-$100K annual SaaS subscription.
