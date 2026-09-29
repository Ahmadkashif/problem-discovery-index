# Worker Verification & Fraud Control

**Parent Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Category:** Highly Automatable
**Contested on:** Whether fraud controls catch automated and duplicate submissions without excluding the honest workers who resemble them.

## Profile
**Market Size:** ~$150M — 5% of the US microtask and research-participant market
**Share of Parent Industry:** ~5%
**Digital Adoption:** Moderate — automated, adversarial and prone to false positives
**Target Buyer:** Platform trust & safety; requesters; academic research integrity
**Automation Potential:** Very high, and the adversary automates too

## What Makes This a Distinct Niche

Fraud is real here. Automated submission, duplicate accounts taking the same study repeatedly, VPN-masked location misrepresentation and, increasingly, generative text passed off as human free-text responses all damage requester data — and in the academic segment they damage published research.

The controls are consequently aggressive: device and network fingerprinting, VPN detection, duplicate-account graphs, attention checks, response-pattern analysis and blanket exclusion of flagged accounts. They also catch honest workers routinely. A shared household computer, a corporate or university network, a legitimate VPN used for privacy, a fast reader, a worker whose second language produces terse responses — all resemble the fraud signature closely enough to trigger exclusion, usually with no explanation and no appeal.

The niche is distinct because the error asymmetry is misjudged: platforms treat a false negative as damaging to the requester and a false positive as costless, when a false positive removes a person's access to income.

## Current Tools & Gaps

Device and browser fingerprinting. VPN and proxy detection. IP geolocation. Duplicate account detection via identifier overlap and behavioural similarity. Attention checks and response-pattern analysis. Identity verification on some platforms, particularly in the research-participant segment.

The gaps are calibration, appeal and the new adversary. Nobody measures the false positive rate, because an excluded worker who does not appeal produces no signal. Appeal routes are weak or absent. And generative text detection — the fastest-growing problem, particularly for free-text research responses — is being addressed with tools whose accuracy is poor and whose errors fall hardest on non-native English speakers.

## Problems
- [[niches/crowdsourcing-platforms/verification-and-fraud/build|🔨 Build: Calibrated Fraud Detection With a Measured False Positive Rate]]
- [[niches/crowdsourcing-platforms/verification-and-fraud/buy|🛒 Buy: Fraud and Bot Detection Adapted to a Workforce That Looks Suspicious]]
- [[niches/crowdsourcing-platforms/verification-and-fraud/fix|🔧 Fix: Excluded for Sharing a Household Computer]]
