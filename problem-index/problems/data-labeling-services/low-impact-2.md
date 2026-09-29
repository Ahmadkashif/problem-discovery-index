# Expert Credential Verification at Speed

**Industry:** [[data-labeling-services|Data Labeling Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Identity verification and background screening are commodity services, and none of them can tell you whether this person can actually do organic chemistry — which is the only question that matters when a contract requires four hundred chemists next week.
**Tags:** #logistic-regression #gradient-boosting #evaluation-metrics #confidence-intervals #hypothesis-testing #feature-engineering #compliance

## The Problem
The economics of the industry have inverted. Commodity annotation is being absorbed by models, and what remains is work requiring genuine expertise: practising physicians, quantitative finance professionals, working software engineers, licensed attorneys, research scientists.

A contract arrives requiring several hundred such people, starting soon. The vendor must find them, verify they are what they claim, and confirm they can actually perform the specific task — which is not the same as holding the credential.

Verification is the bottleneck and it is genuinely hard. A claimed medical licence can be checked against a state board. A claimed PhD can sometimes be checked. But a large share of applicants for high-paying expert annotation work overstate their qualifications, and some fabricate them outright, because the pay is good and the barrier is a form. Meanwhile a self-taught practitioner may outperform a credentialed one on the actual task.

The current mechanism is a screening test, authored by a subject matter expert, plus a document check. The test takes days to build, gets shared between contributors within weeks, and measures whatever the author happened to think of.

## What Already Exists
Identity verification services (Persona, Jumio, Onfido) are mature and reliable. Background screening and credential verification services check licences, degrees and employment against primary sources. Professional licence registries are publicly queryable in most regulated fields. Technical assessment platforms (HackerRank, CodeSignal) are established for software roles. Freelance marketplaces have reputation systems.

## The Customisation Gap
Credential verification confirms a document; it does not predict task performance. The vendor's actual question is narrower and more answerable: will this person produce reliable annotations on this specific task type, which is a prediction about behaviour rather than a fact about history.

The vendor holds the data to answer it. Across hundreds of thousands of contributors and thousands of projects, it observes claimed credentials, screening test results, and subsequent measured annotation quality. Which signals actually predict performance — and which credentials predict nothing — is directly estimable and is not estimated. Screening tests are authored on intuition and never validated against the outcome they exist to predict.

Test item compromise is the second gap. Items leak, and leakage is detectable statistically: an item whose difficulty drops sharply across cohorts, or on which response times collapse, has been shared. Adaptive item generation and rotation from a large pool is standard practice in professional testing and absent here.

The third gap is fairness, and it deserves saying plainly. A screening pipeline that filters on proxies rather than demonstrated ability excludes competent people, disproportionately those without conventional credentials, and it is exactly the population this work could serve well.

## Impact If Solved
Expert workforce assembly is now the binding constraint on the industry's most valuable contracts, and it is gated by tests authored on intuition and credentials that predict less than assumed. Validating the screening signal against measured outcomes uses data the vendor already holds and is the difference between staffing a contract in a week and a month.
