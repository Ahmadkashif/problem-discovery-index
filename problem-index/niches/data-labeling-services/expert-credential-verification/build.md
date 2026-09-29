# Four Hundred Chemists Next Week

**Niche:** [[niches/data-labeling-services/expert-credential-verification/profile|Expert Credential Verification]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Identity verification and background screening are commodity services, and none of them can tell you whether this person can actually do organic chemistry — which is the only question that matters when a contract requires four hundred chemists next week.
**Tags:** #bayesian-inference #gradient-boosting #evaluation-metrics #confidence-intervals #cross-validation #hypothesis-testing #compliance #revenue-impact
**Contested on:** Every serious competitor here is fighting to establish that a contributor can actually do the work, at the speed a contract demands — and whoever does that takes the expert tier, because identity verification is commodity and capability verification is the constraint.

## The Problem
A contract requires four hundred contributors with graduate-level chemistry capability, starting in eight days. Sourcing produces two thousand applicants with plausible credentials. Verification confirms that they exist, that their degrees are real, and that their employment histories check out — which takes two days and tells the vendor almost nothing about whether they can assess a reaction mechanism. A twenty-minute test is written by a project lead over a weekend. Four hundred pass. Three weeks later, reviewer data shows that a substantial minority produce assessments that experts reject, and the project is behind.

## Why Nobody Has Built This
The screening industry built what was buildable — identity, criminal history, credential confirmation — and capability assessment is a different discipline that this industry has not hired for. Tests are built per project because each domain differs and there is no library, and they are built under time pressure by the person who understands the task rather than by somebody who understands assessment. Validation would require knowing which test takers turned out to be good, which is knowable retrospectively from the delivery data and is never fed back. And an expert verified for one project is re-screened for the next because nothing accumulates.

## What to Build
Assess capability directly and accumulate the result. Build the assessment from the work itself: a small set of real tasks from the domain, scored against how strong assessors handled the same items, which measures what the project actually needs rather than adjacent knowledge — and is constructible from the project's own pilot data. Validate the assessment against outcomes retrospectively, since the delivery data shows which test takers produced accepted work and that is the validation every per-project test lacks; even a few projects of history produces a usable instrument. Maintain a capability record across projects, so a contributor demonstrated to be strong at clinical reasoning is not re-screened for the next clinical project — which compounds and is the asset. Assess at the sub-domain level, since chemistry capability is not one thing and a contributor excellent at synthesis may be poor at spectroscopy, and the current screening treats the domain as atomic. Use a short adaptive assessment rather than a fixed test, which gets more information per minute of an expert's time and is what professional assessment does. Handle the leaked-test problem structurally, which the fix note addresses. And report the assessment's own predictive validity to the customer, since a vendor claiming verified experts should be able to say what the verification predicts.

## Target Customer
Expert workforce marketplaces and delivery organisations, the laboratories specifying expert requirements, and the screening vendors for whom capability is the adjacent product they do not offer.

## Impact If Built
Credential verification is commodity and answers a different question from the one that determines delivery. Building the assessment from real tasks and validating it against delivery outcomes is what turns an unvalidated weekend test into an instrument, and a persistent capability record compounds across projects where nothing currently does.
