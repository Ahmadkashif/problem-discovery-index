# Provider Network Management and Credentialing

**Industry:** [[insurance-tpa|Insurance Third-Party Administrators (TPAs)]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Credentialing verification platforms exist for health systems, but TPAs managing workers' comp and group health need to maintain preferred provider directories that factor in cost-effectiveness, treatment outcomes, return-to-work speed, and geographic coverage — not just license status and malpractice history.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #cross-validation #descriptive-statistics #bias-variance-tradeoff #expectation-variance-covariance

## The Problem
TPAs that manage workers' compensation and group health claims maintain provider networks — directories of physicians, specialists, physical therapists, and facilities that claimants are directed to. Network quality directly impacts claim costs: a workers' comp claimant directed to a high-quality occupational medicine provider returns to work 2-3 weeks faster than one who sees a general practitioner unfamiliar with occupational injury protocols. But TPAs evaluate providers on credentialing status (license valid, malpractice coverage adequate) rather than performance (treatment outcomes, cost per episode, return-to-work timelines, claim duration). Credentialing is a compliance checkbox; performance evaluation is what actually controls claim costs.

## What Already Exists
Credentialing platforms (Cactus, Modio) handle license verification, malpractice checks, and NPDB queries. CAQH ProView standardizes provider data collection. These systems verify that a provider is legally authorized to practice — they don't evaluate whether the provider delivers cost-effective care that produces good outcomes. Provider performance evaluation requires claims outcome data that credentialing platforms don't have.

## The Customisation Gap
A TPA-specific network management system needs to: (1) maintain standard credentialing verification (license, malpractice, sanctions), (2) score provider performance based on claims outcome data — average claim duration by diagnosis, cost per episode vs. benchmark, return-to-work timelines for workers' comp, patient satisfaction where available, (3) identify network gaps by geography and specialty, (4) recommend network additions and removals based on performance scoring, (5) generate provider report cards that TPAs can share with carrier clients to demonstrate network quality, and (6) flag providers whose billing patterns or treatment durations suggest over-utilization.

## Impact If Solved
Reduces average workers' comp claim duration by 1-2 weeks through better provider steering — worth $2,000-$5,000 per claim in reduced indemnity and medical costs. Identifies over-utilizing providers before they generate significant excess costs. Provides carrier clients with data-driven network quality reporting that differentiates the TPA competitively. For a TPA managing 10,000 workers' comp claims annually, improved network management could reduce total claim costs by $5-10M.
