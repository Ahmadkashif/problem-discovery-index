# Buy: Outbreak Detection From Public Health

**Niche:** Novel Harm Response
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Public health built syndromic surveillance to detect an outbreak before the pathogen is identified, which is precisely the problem of detecting a harm before the label exists.
**Tags:** #change-point-detection #time-series-forecasting #evaluation-metrics #confidence-intervals #graph-theory #k-means-clustering #automation
**Contested on:** Whether a new abuse pattern can be detected in the weeks when it does most of its damage.

## The Problem

Detecting that something new and harmful is happening, before you know what it is, is the outbreak detection problem, and public health has built a substantial apparatus for it.

Syndromic surveillance monitors symptom patterns rather than confirmed diagnoses, because symptoms appear before a pathogen is identified. Aberration detection algorithms flag unusual clusters in time and space. Event-based surveillance monitors informal sources — news, social media, clinician reports — for signals of an emerging event. Clinician alerts are treated as a formal signal, because a doctor noticing an unusual presentation is frequently the earliest indication. And the whole system is designed around the premise that the confirmed case definition arrives late.

Trust and safety has exactly this structure — a novel harm appears, the definition arrives weeks later, and the damage happens in between — and monitors only confirmed categories.

The parallel is close enough that the methods transfer with modest adaptation.

## What Already Exists

Syndromic surveillance: monitoring pre-diagnostic indicators to detect outbreaks early, with established algorithms and operational systems in most health systems.

Aberration detection: statistical methods for identifying unusual clusters in time, space and population, developed specifically for surveillance.

Event-based surveillance: monitoring informal and unstructured sources for early signals, including the systems that scan news and online sources for disease events.

Clinician reporting: formal channels treating a practitioner's observation of something unusual as a surveillance signal.

Trust and safety: category-based classification and periodic retraining.

## The Customization Gap

**Reviewers are the clinicians and are not treated as a signal.** A moderator seeing something they cannot categorise is the exact analogue of a clinician seeing an unusual presentation, and public health treats that as a formal surveillance input where trust and safety treats it as a case to escalate.

**Syndromic monitoring has a direct equivalent.** Monitoring pre-label indicators — clustering, coordination, escalation rates, report text — is syndromic surveillance applied to content, and nobody does it.

**The adversary adapts, which public health's pathogens do not.** An abuse pattern responds to detection deliberately, which means the surveillance itself must change and the source discipline has no equivalent pressure.

**Speed requirements are higher.** Outbreak detection operates over days to weeks. A coordinated campaign runs in hours to days, which compresses everything.

**Event-based surveillance across sources transfers well.** The systems that scan informal sources for disease signals are directly analogous to monitoring for a harm pattern appearing on other platforms or in reporting.

**The sharing infrastructure exists there and not here.** Public health has international reporting obligations and established sharing. Trust and safety shares only in the most severe categories, which is the structural gap.

## Target Customer

Platform trust and safety operations, for whom the surveillance framing reorganises a problem they currently handle as a sequence of escalations.

Vendors, for whom syndromic-style monitoring is a product capability that fits alongside classification rather than competing with it.

Cross-platform trust and safety bodies, for whom the public health sharing model — including its obligations and its governance — is the most relevant precedent for extending signal sharing beyond the severe categories.

## Impact If Solved

A discipline built specifically to detect something harmful before it can be named applies directly to a field that monitors only what it has already named.

Treating reviewer escalations as a formal surveillance signal is the closest transfer and the cheapest — it uses humans who have already noticed and routes their observation to a monitor rather than to a queue.

And the cross-platform sharing model from public health is the precedent for extending signal sharing beyond the few categories where it currently exists, which is where the earliest detection of a novel pattern almost always sits.
