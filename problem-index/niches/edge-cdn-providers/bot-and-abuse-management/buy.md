# Adversarial Learning and Drift Detection

**Niche:** [[niches/edge-cdn-providers/bot-and-abuse-management/profile|Bot & Abuse Management]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Adversarial machine learning, concept drift detection and online learning are developed fields built for exactly this situation, and bot management ships static rules on a research cycle.
**Tags:** #gradient-boosting #contrastive-learning #change-point-detection #gaussian-mixture-models #evaluation-metrics #confidence-intervals #cross-validation #compliance
**Contested on:** Every serious competitor in bot management is fighting to keep up with adversaries who adapt within days of a rule shipping — and whoever detects the adaptation as it happens across their whole customer base takes the market, because no single customer can see it.

## The Problem
Classification against an adversary who observes the classifier and adapts is adversarial machine learning, with a substantial literature on robustness, evasion and the dynamics of the resulting arms race. Detecting that a model's input distribution has shifted is concept drift detection, equally well studied. Fraud detection has run online learning against adapting adversaries for decades. Bot management ships rule updates from a research team on a weekly cadence.

## What Already Exists
Adversarial machine learning research on evasion and robustness; concept drift detection methods with mature implementations; online and incremental learning; fraud detection practice with its established handling of sparse labels and adapting adversaries; and anomaly detection over behavioural features. All published and applied at scale in adjacent security domains.

## The Customization Gap
The adaptation is to a multi-tenant network with sparse labels and asymmetric costs. It requires: (1) cross-customer drift detection as the primary signal, since the adversary's adaptation is visible as a correlated shift across many properties and this is the provider's structural advantage — no customer-scoped model can see it; (2) honest treatment of label scarcity, because confirmed bot and confirmed human labels are rare and the abundant signal is unlabelled traffic, which pushes toward semi-supervised and contrastive approaches rather than the supervised framing the problem is usually given; (3) per-customer cost asymmetry, since a blocked user costs a retailer a sale and costs a content site very little, and the same threshold cannot be right for both; (4) robustness to probing, since an adversary with access to the defence can query it, which argues for randomisation and for not exposing the decision boundary through the response; and (5) fairness measurement, because behavioural and fingerprint-based classification systematically disadvantages users on older devices, unusual browsers and assistive technology, and that exclusion is a real harm that nobody measures.

## Target Customer
Edge and security providers, fraud detection vendors, and the security research teams building these detections.

## Impact If Solved
Developed fields address precisely this adversarial setting and the category ships static rules on a human cycle. Cross-customer drift detection is the adaptation that uses the provider's unique position, and the fairness measurement is the one most likely to be skipped and most likely to matter to the people affected.
