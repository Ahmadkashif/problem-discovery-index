# Finding Prioritisation

**Parent Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to turn thousands of findings into the handful that matter for this application — and whoever does that takes the account, because the ratio between what the category reports and what is worth acting on is its central unresolved problem.

## Profile
**Market Size:** ~$780M US attributable to vulnerability prioritisation and risk scoring
**Share of Parent Industry:** ~26% of category revenue
**Digital Adoption:** Low — severity scores are used because nothing better is offered
**Target Buyer:** Application security leadership and engineering leadership
**Automation Potential:** Very High — the evidence for a real priority exists and is not assembled

## What Makes This a Distinct Niche
A scan of a typical application returns hundreds or thousands of findings. A small fraction are reachable from the application's own code, a smaller fraction are exploitable in its configuration, and a smaller fraction still are worth interrupting a release for. The tools report a severity score computed by somebody who has never seen the application, which is the honest description of what a published severity rating is, and the raw count is presented as the security posture. The consequence is entirely predictable and is the same as every other uncalibrated signal in this vault: the output is filed rather than fixed, the teams receiving it learn to ignore it, and when something genuinely urgent arrives it is in a queue nobody reads. Prioritisation is the contest because everything else in the category depends on somebody acting on the output.

## Current Tools & Gaps
Composition analysis with published severity ratings, exploit prediction scoring available and thinly used, reachability analysis offered by several vendors with varying rigour, and policy gates on severity thresholds. The gaps: severity is a property of the vulnerability and priority is a property of the situation, and the tools report the first; exploitation evidence — whether a vulnerability is being exploited in the wild — is available and under-weighted; the application's own context, including whether the vulnerable path is reachable and whether the configuration enables the attack, is the determining factor and is assessed by a human per finding; the organisation's own history of what it fixed and dismissed is a strong prior and is discarded nightly; and the raw count remains the reported metric.

## Problems
- [[niches/software-supply-chain-security/finding-prioritisation/build|🔨 Build: A Severity Score From Somebody Who Has Never Seen the Application]]
- [[niches/software-supply-chain-security/finding-prioritisation/buy|🛒 Buy: Exploit Prediction and Risk Scoring That Exist]]
- [[niches/software-supply-chain-security/finding-prioritisation/fix|🔧 Fix: The Count Reported as the Posture]]
