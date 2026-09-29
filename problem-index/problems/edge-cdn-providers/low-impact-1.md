# Bot Classification Under Adaptation

**Industry:** [[edge-cdn-providers|Edge & CDN Providers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every provider sells bot management built on signatures, fingerprints and behavioural heuristics, and every one of them is in a race against adversaries who adapt within days of a rule shipping.
**Tags:** #gradient-boosting #graph-neural-networks #dbscan #change-point-detection #confidence-intervals #feature-engineering #evaluation-metrics #compliance

## The Problem
A meaningful share of web traffic is automated, and the automation ranges from benign — search crawlers, monitoring, feed readers — through commercially unwelcome — price scraping, inventory hoarding, content harvesting — to outright hostile: credential stuffing, card testing, fraud.

Providers classify this and act: allow, challenge, rate limit, block. The classification runs on browser and TLS fingerprints, request patterns, IP reputation, header consistency and behavioural signals.

Every one of those is adaptable. Fingerprints can be spoofed. Residential proxy networks defeat IP reputation. Headless browsers driving real browser engines produce genuine fingerprints. Timing can be randomised. Sophisticated operators test against the major providers before deploying, so a new detection technique has a short useful life.

The error costs are severely asymmetric and pull in opposite directions. A false positive blocks a paying customer, who experiences it as the site being broken and frequently does not report it. A false negative allows credential stuffing or lets a scraper take inventory. Customers tune conservatively, which means the sophisticated adversary passes and the unsophisticated one is caught, which is close to the opposite of what is wanted.

## What Already Exists
Bot management products are mature at every provider, with reputation feeds, fingerprinting libraries, behavioural scoring and challenge mechanisms. JavaScript challenges and proof-of-work alternatives are widely deployed. Device attestation is emerging. Verified bot programmes allow legitimate crawlers to identify themselves. Shared threat intelligence exists across the industry.

## The Customisation Gap
Detection is largely per-request while the phenomenon is a campaign. An operation running against a customer is a coordinated set of requests sharing infrastructure, timing and behavioural characteristics, and modelling it relationally rather than individually is what survives the adaptation of any single signal.

Cross-customer campaign propagation is the provider's structural advantage. An operation seen against one customer is directly relevant to the next, frequently minutes later, and turning that into automatic protection rather than into an eventual rule update is where the vantage point actually pays.

Adaptation itself is a detectable event. When a campaign's characteristics shift, that is a change point in a monitored population, and detecting it as it happens is far more useful than discovering it through a rise in successful attempts.

False positive measurement is the gap that most damages customers. Blocked legitimate users do not complain, they leave, so the error is invisible in every metric — and it is estimable from downstream behaviour: challenged sessions that were abandoned, blocked clients that had a long legitimate history.

## Impact If Solved
Bot management is an adversarial problem addressed with per-request rules that adversaries out-adapt, tuned conservatively because false positives are invisible. Campaign-level modelling with cross-customer propagation is the version that uses the provider's actual advantage, and measuring false positives is what would let customers stop tuning against the wrong error.
