# A Pooled Underwriting Model for PEOs Too Small to Have One

**Niche:** [[niches/professional-employer-organizations/small-regional-peos/profile|Small & Regional PEOs]]
**Industry:** [[industries/professional-employer-organizations|Professional Employer Organizations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A PEO with 3,000 worksite employees writes too few groups to learn which ones go bad, so it underwrites on rules of thumb while the large PEOs learn from tens of thousands.
**Tags:** #gradient-boosting #bayesian-inference #transfer-learning #evaluation-metrics #compliance #ai-platform #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to give a PEO with a few thousand worksite employees a health plan and a workers' comp programme it can sell against ADP TotalSource, Insperity and TriNet without an actuarial department of its own, and whoever keeps that PEO's carriers renewing its programmes on workable terms takes the account.

## The Problem
A small PEO quotes a few hundred prospects a year and admits a fraction. Its outcome history is too thin for any statistical learning, and its underwriting is one or two people plus a consultant. When the carrier backing its health or comp programme sees a bad year, the carrier reprices or exits, and the PEO has no evidence that its selection is sound.

## Why Nobody Has Built This
Each PEO treats its client book as a competitive secret. Health data is protected health information, so pooling needs business associate agreements and de-identification. Consultants hold cross-PEO experience, as the PrestigePEO deck shows with studies across 10,726 subscriber worksites, but sell it as advice, not as a model a PEO can run at quote time.

## What to Build
A consortium underwriting model. Participating small PEOs contribute de-identified quote files and client-level outcomes under a common data standard. The model learns group-level risk patterns across the pool, then adapts to each PEO's own appetite and market with partial pooling. Each member gets quote-time scoring, comparables and an annual selection report it can show its carriers, while no member sees another's clients.

## Target Customer
CEOs of PEOs with 1,000-20,000 worksite employees, many of them PrismHR customers, and the carriers and programme administrators backing them, who would value the selection evidence.

## Impact If Built
Small PEOs underwrite with evidence instead of instinct and can show carriers why their programme deserves renewal, narrowing the advantage that scale gives the largest PEOs.
