# Harms That Arrive Before the Labels

**Industry:** [[trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A new abuse pattern appears, classifiers trained on historical labels miss it for weeks, and those weeks are when it does most of its damage.
**Tags:** #transfer-learning #contrastive-learning #dbscan #change-point-detection #large-language-models #bert #evaluation-metrics #confidence-intervals

## The Problem
Harm is adversarial and generative. Coordinated campaigns invent terminology to evade detection; scam formats mutate weekly; new platforms and formats create new abuse surfaces; and a real-world event produces a wave of content types that did not exist the week before.

Supervised classifiers trained on historical labelled data are structurally behind. Detecting a new pattern requires examples, examples require labels, labelling requires a definition, and a definition requires someone to have recognised the pattern — a chain that takes weeks at best. The harm does its damage during that period, and for fast-moving campaigns the entire lifecycle can complete before a classifier is updated.

Evasion is the deliberate version. Actors who know they are being classified test the boundary, adopt terminology that evades, and share what works. Every classifier deployed publicly is subject to this, and static models degrade continuously against it.

The cold start problem is the same shape for new customers. A platform deploying a vendor's tooling for the first time has its own content distribution, its own communities and its own emergent slang, and the classifier was fitted on someone else's.

## What Already Exists
Vendors retrain regularly and maintain research teams tracking emerging harms. Hash matching handles known content — the established child safety infrastructure being the clearest success, where a known-content mechanism works extremely well. Behavioural and coordination signals detect campaign structure independently of content. Large language models have improved few-shot performance on described categories substantially, which is a genuine shift in this problem's tractability. Threat intelligence sharing between platforms exists in specific areas and is limited elsewhere.

## The Customisation Gap
Few-shot adaptation from a description is the capability that has changed and is unevenly exploited. A policy team that can describe a newly-observed harm in words and get a usable detector in hours rather than weeks changes the response time fundamentally, and that is now closer to achievable than it was — with the caveat that a detector built from a description needs careful evaluation before deployment, because a fluent model will confidently classify against a description in ways that surprise its author.

Novelty detection is the complementary half. Surfacing content that does not fit any existing category, clustered so a policy person sees a pattern rather than individual items, is how a new harm gets recognised at all — and it is an unsupervised problem that does not wait for labels.

Coordination signals are the most robust detector of campaigns and are underused relative to content classification. Accounts acting together, content propagating in unnatural patterns and timing correlations identify a campaign regardless of what its content says, which makes them resistant to the terminology evasion that defeats content models.

And per-customer adaptation should be routine rather than a professional services engagement. A platform's own content, communities and slang differ, and light adaptation on a customer's own labelled examples is the difference between a generic classifier and a usable one.

## Impact If Solved
The period between a harm appearing and a classifier detecting it is when the harm does its damage, and the supervised pipeline structurally guarantees that period is weeks. Description-based few-shot detection with careful evaluation, unsupervised novelty clustering that surfaces patterns before anyone has named them, and coordination signals that resist terminology evasion would compress that window — which is the single most consequential improvement available in this category.
