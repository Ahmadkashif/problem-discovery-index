# Fix: Confidence Describes the Collection, Not the Indicator

**Niche:** Indicator Feeds
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** An indicator's confidence score reflects how the vendor obtained it, and the customer reads it as a prediction of whether acting on it will be right.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #worker-facing #hypothesis-testing #descriptive-statistics
**Contested on:** Whether a feed delivers what a particular customer should act on, or everything the vendor collected with the filtering left to the buyer.

## The Problem

Indicators arrive with a confidence score. High confidence typically means the vendor's analysts observed it directly — in malware configuration, in incident response, in monitored infrastructure. Lower confidence means it came from a less direct source.

The customer reads it differently. To them, high confidence means acting on this will probably be right — safe to block, worth alerting on, unlikely to be a false positive.

Those are different claims. An indicator can be collected with complete certainty — the vendor watched the malware connect to it — and still produce false positives, because the address was reallocated three weeks later, or because it is a shared hosting provider where malicious and legitimate services coexist, or because the domain was sinkholed and now points at a researcher.

So the score describes the provenance and is used as a prediction of the outcome, and the two diverge in exactly the cases that produce the most analyst time and the most damaging blocks.

No vendor calibrates the score against observed precision, so nobody knows how badly they diverge — including the vendors, who have never checked whether their high-confidence indicators actually perform better.

## Why It's Still Broken

**Collection confidence is what the vendor can know.** A vendor without telemetry genuinely cannot assess how an indicator will perform, only how reliably they observed it. The score is honest about what it measures and silent about what it is used for.

**Calibration needs the precision data.** Checking whether high-confidence indicators perform better requires adjudicated outcomes, which is the hard half of the measurement problem.

**The ambiguity is convenient.** A score that customers read as a performance prediction is more valuable commercially than one labelled as a provenance descriptor.

**Scoring schemes vary per vendor.** Each has its own scale and semantics, which makes the meaning ambiguous even before the provenance-versus-performance confusion.

**Infrastructure reuse is the underlying cause and is nobody's fault.** Addresses are reallocated, hosting is shared, domains are sinkholed. A correctly collected indicator becomes wrong through the ordinary operation of the internet, which is the lifecycle problem in [[niches/threat-intelligence-vendors/indicator-lifecycle/profile|⚡ Indicator Lifecycle & Decay]].

**Customers do not ask what the score means.** The field is named confidence and it is taken at face value.

## What a Fix Looks Like

**Label the score for what it is.** Rename it collection confidence, or ship it alongside a separate field, so a customer cannot mistake a provenance descriptor for a performance prediction. This costs a field name and removes the central confusion.

**Add an infrastructure-type flag.** Shared hosting, cloud provider range, content delivery network, dynamic residential address, sinkhole. Each of these makes an indicator dramatically more likely to produce false positives regardless of how well it was collected, and every one is determinable from public data. This is the single most useful addition available.

**Ship first-seen and last-seen dates prominently.** Age is the strongest available predictor of an indicator having gone stale, and it is frequently buried or absent.

**Calibrate collection confidence against observed precision.** Where a vendor has telemetry, check whether high-confidence indicators actually produce better outcomes. If they do, that is a strong claim worth making; if they do not, the score needs rethinking. Nobody has looked.

**State the intended use per indicator.** Block, alert, hunt or context. This does more than any confidence score, because it communicates the precision the vendor believes the indicator supports.

**Let customers score for themselves.** Publish enough metadata — collection method, infrastructure type, age, observation count — that a customer can build their own scoring appropriate to their risk posture, rather than accepting one number.

**Agree a common vocabulary.** Vendor-specific confidence scales make multi-feed operation harder than it needs to be, and a shared semantic would benefit everyone except the vendor whose score currently looks highest.

## Who Feels the Pain

The SOC analyst, working alerts from high-confidence indicators that turn out to be shared hosting, and learning to discount the score.

The detection engineer, deciding what to block, with a score that does not tell them what they need to know about false positive risk.

The organisation that blocked a legitimate service because a high-confidence indicator pointed at a reallocated address.

And the vendors with genuinely well-performing indicators, whose confidence scores are indistinguishable from everyone else's because nobody has calibrated any of them.

## Impact If Fixed

Relabelling the score and adding an infrastructure-type flag are both small changes that address the central confusion and the largest driver of false positives, using information that is publicly determinable.

Stating the intended use per indicator communicates more about appropriate precision than any score, and is a field rather than a model.

And calibrating confidence against observed precision would test an assertion attached to every indicator in every feed — which is a question nobody in this industry has asked about their own product.
