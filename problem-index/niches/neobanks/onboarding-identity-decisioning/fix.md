# The Thin File Who Is Not a Fraudster

**Niche:** [[niches/neobanks/onboarding-identity-decisioning/profile|Onboarding & Identity Decisioning]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Fix (Pain Point)
**One-liner:** A recently arrived worker with no credit history, a prepaid phone and a shared address looks statistically identical to a synthetic identity, and is refused a bank account with no explanation and no route back.
**Tags:** #compliance #evaluation-metrics #confidence-intervals #descriptive-statistics #hypothesis-testing #quick-win #worker-facing #logistic-regression
**Contested on:** Every serious competitor in this niche is fighting to judge a stranger from third-party data and a document against an organised adversary — and whoever does that well decides who can open a bank account at all.

## The Problem
The applicant is real. They arrived in the country eighteen months ago, have no credit file, use a prepaid mobile, live at an address shared with several other people, and have a foreign document. Every one of those attributes is also a characteristic of synthetic identity fraud. The model refuses them. They receive a message saying the application could not be approved, with no reason and no appeal. They are precisely the population these institutions were founded to serve, and the risk system treats the absence of a conventional record as evidence against them.

## Why It's Still Broken
Thin-file applicants are statistically similar to synthetic identities on the available features, and the available features are the conventional financial record — the model is not wrong about the correlation, it is being asked the wrong question with the wrong evidence. A false decline produces no complaint the institution measures. Manual review costs money and refusal is free. And nobody counts how many real people are being refused.

## What a Fix Looks Like
Build a path rather than a cut-off. Offer a graduated route — limited functionality, lower limits, additional verification — instead of a binary refusal, which is the fix and converts a refused applicant into a customer the institution can observe and learn about. Use evidence the conventional record does not contain, such as employment documentation, remittance history, mobile tenure or utility records, which is where real thin-file applicants can demonstrate themselves. Measure the false decline rate on this population specifically, since the harm is concentrated and an aggregate rate hides it entirely. Give a reason and an appeal route, which is both fairer and generates the feedback the institution currently lacks. Distinguish thin from suspicious, because absence of record and presence of contradictory signals are different findings and are currently scored the same way. Track outcomes for applicants admitted on a graduated path, which builds the evidence that the population is bankable and is the commercial argument. Analyse decline rates by demographic, since the disparate impact here is foreseeable and is increasingly a regulatory exposure. Escalate the ambiguous cases to a person with the right evidence in front of them, connecting to the analyst niche. Report the size of the refused-but-real population, which is a number no institution has and which is directly relevant to its stated mission. And measure the lifetime value of graduated-path customers, because if it is positive the whole trade-off should move.

## Who Feels the Pain
People refused a bank account for having lived a life the conventional record does not describe; institutions refusing their own target market; and regulators observing a foreseeable disparate impact.

## Impact If Fixed
The model is not wrong about the correlation, it is being asked the wrong question with the conventional record as evidence. A graduated path converts a refused applicant into a customer the institution can observe, which is both the fairer outcome and the only way to build the evidence.
