# Insurance Adjuster Behavior Pattern Database

**Niche:** [[niches/personal-injury-law/motor-vehicle-accidents/profile|Motor Vehicle Accidents]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Plaintiff attorneys get data-driven settlement intelligence — which adjusters at which carriers settle at what ranges for what injury types — leveling a playing field where the defense side has had algorithmic pricing for decades.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #cross-validation #tacit-knowledge-ml #revenue-impact #data-integration

## The Problem
Insurance carriers use Colossus, Claims Outcome Advisor, and internal ML models to algorithmically determine settlement ranges for MVA claims. The plaintiff's attorney has nothing comparable. An experienced PI attorney "just knows" that Adjuster X at State Farm in the Dallas office lowballs soft tissue cases but settles TBI cases fairly, or that GEICO's third-party vendor adjusters have less authority and require escalation. This knowledge is tacit, locked in individual attorneys' heads, and lost when they retire or move firms. New associates have no way to learn which fights to pick and which settlements to accept without years of pattern exposure.

## Why Nobody Has Built This
The data exists but is fragmented across thousands of PI firms, each holding their own settlement outcomes in case management systems with no standardized schema. No single firm has enough volume across all carriers, adjusters, injury types, and jurisdictions to build a statistically significant model. The chicken-and-egg problem is severe: you need firms to contribute their settlement data to build the model, but firms won't contribute until the model proves valuable. Additionally, settlement data is considered competitively sensitive — firms worry that sharing outcomes helps their competitors or, worse, helps the carriers recalibrate.

## What to Build
A multi-firm settlement intelligence platform where PI firms contribute anonymized case outcome data (carrier, adjuster identifier, injury type, treatment cost, demand amount, settlement amount, time to resolution, jurisdiction) and receive back benchmarking analytics. Core features: adjuster behavior profiles (average settlement-to-demand ratio by injury type), carrier-level strategy detection (which carriers are hardlining which case types this quarter), jurisdiction-level verdict and settlement distributions, and case-specific settlement range predictions given the firm's current case parameters. The model uses gradient-boosted trees on tabular features (injury severity, treatment duration, jurisdiction, carrier, adjuster history, policy limits) to predict settlement ranges and optimal demand timing.

## Target Customer
MVA-focused PI firm owners and managing partners handling 200+ active cases who want data-driven settlement strategy instead of relying on institutional memory. Secondary market: PI attorneys in new markets or new associates who lack the decades of adjuster-specific pattern recognition that veteran attorneys accumulate.

## Impact If Built
A 5-10% improvement in average settlement value through better-informed demands and negotiation timing. Across a 500-case firm with a $15K average settlement, that represents $375K-$750K in additional contingency revenue annually. Eliminates the 3-5 year "learning curve" for new associates to develop adjuster and carrier intuition.
