# Buy: Fraud and Bot Detection Adapted to a Workforce That Looks Suspicious

**Niche:** [[niches/crowdsourcing-platforms/verification-and-fraud/profile|Worker Verification & Fraud Control]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Bot detection and fraud scoring are built to protect a business from anonymous attackers; here the flagged party is a worker whose income the flag removes.
**Tags:** #graph-theory #gradient-boosting #evaluation-metrics #confidence-intervals #compliance #large-language-models #automation #hypothesis-testing
**Contested on:** Whether fraud tooling tuned to protect a business can be tuned for a population it also serves.

## The Problem

Fraud and bot detection is a strong commercial category. Device fingerprinting, behavioural biometrics, proxy and VPN detection, velocity rules, identity graphs and risk scoring are all mature and available as APIs, and platforms here use them.

Every product is calibrated for a context where a false positive costs a declined transaction and a false negative costs money. Here a false positive removes a person's access to income, permanently and usually without explanation, and the flagged population includes large numbers of honest workers whose circumstances — shared devices, institutional networks, privacy VPNs, second-language writing — produce the same signals as the adversary.

## What Already Exists

The fraud scoring platforms — Sift, Sardine, Arkose, and the bot-detection vendors. Device and browser fingerprinting. Proxy and VPN detection services. Identity verification. Behavioural biometrics. Generative text detection tools, which are new and whose accuracy claims deserve scrutiny.

## The Customization Gap

**The error asymmetry is different and the defaults encode the wrong one.** Vendor thresholds are tuned for transaction fraud. Here the false positive cost is a livelihood and the false negative cost is some polluted data in one batch. Retuning requires an explicit cost model the platform must construct, and the vendor defaults are actively wrong for this use.

**The flagged population's normal behaviour resembles the adversary's.** Shared computers in multi-person households, institutional and mobile-carrier NAT, privacy VPNs, and fast completion by skilled workers are all ordinary here and all trigger vendor signals. Base rates by population and geography have to be established locally; the vendor's global priors do not describe this workforce.

**Generative text detection is the new problem and the tooling is weak.** Detectors have documented accuracy limits and systematically higher error rates on non-native English writing, which is most of this workforce. Using one as a decision rule would produce discriminatory exclusion at scale, and the policy constraining it is the platform's to write.

**The action space is binary and should not be.** Fraud platforms approve or decline. Additional verification, restriction from certain study types, reduced concurrency and review periods are the proportionate responses here and have no representation in the products.

**Appeals are a due process requirement, not a quality loop.** Fraud platforms sample for model improvement. Here the appeal is the only recourse against losing income, and it needs a defined route, a human, a timeline and restoration — a workflow the vendors do not ship.

## Target Customer

Platform trust and safety teams deploying fraud tooling and finding it excludes honest workers at a rate nobody measured. Also the research-participant platforms, where the requesters are institutions with research-ethics obligations that extend to how participants are treated.

## Impact If Solved

The fingerprinting, graph analysis and risk scoring infrastructure gets used with thresholds set from this context's cost model, and the local base rates, generative-detection policy, graduated actions and appeal workflow get built. Concretely: fraud controls that protect requester data without quietly removing the honest workers who happen to share a computer.
