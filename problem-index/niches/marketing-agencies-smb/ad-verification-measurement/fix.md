# Fraud Analysts Recognize a Scheme and File a Signature

**Niche:** [[niches/marketing-agencies-smb/ad-verification-measurement/profile|Ad Verification & Measurement]]
**Industry:** [[industries/marketing-agencies-smb|SMB Marketing Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** Analysts spend days reconstructing how a fraud operation works, and the system keeps the detection rule and discards the reconstruction.
**Tags:** #tacit-knowledge-ml #graph-ml #anomaly-detection #worker-facing #large-language-models

## The Problem
When a new invalid traffic scheme appears, an analyst investigates: tracing infrastructure, correlating behaviour across publishers, working out how the operation monetizes and what it is imitating. That takes days of skilled work and produces an understanding of a scheme — its economics, its infrastructure pattern, its behavioural fingerprint, how it will likely evolve when blocked.

What the system stores is a signature: a rule that matches the traffic. The reasoning behind it, the alternatives considered, the parts the analyst could not confirm, and the prediction about how the operation would adapt are not recorded in any structured form.

So when the scheme reappears in modified form — which is the normal outcome, since blocking a signature is a cost to the operator rather than an end to them — the next analyst starts over. And the accumulated understanding of how fraud operations behave, which is the team's real expertise, lives in a small number of investigators in a field where they are heavily recruited.

## Why It's Still Broken
The detection pipeline is the product, and its unit is a rule. Signatures are what production consumes, so signatures are what the workflow produces, and everything upstream of the rule is treated as working notes.

Speed pressure reinforces it. A live scheme is costing advertisers money now, and writing up the investigation after shipping the block is time that stops nothing.

And there is a security instinct: detailed documentation of how detection works is exactly what an adversary would want, so the culture defaults to keeping method knowledge thin and personal. That protects against one risk and creates a larger one, which is that the knowledge is not held anywhere durable.

## What a Fix Looks Like
Model schemes as entities, not rules as artefacts.

**Scheme records.** The operation's inferred structure, monetization, infrastructure, and behavioural fingerprint, with the evidence for each and confidence levels. Linked to the signatures derived from it, so a rule always points back to what it is a rule about.

**Evolution tracking.** When a variant appears, link it to its predecessor. Over time this is a genealogy of fraud operations, and it is the single most useful artefact for predicting what a blocked operator does next.

**Record the analyst's prediction.** What the investigator expects the operation to do when blocked, recorded at the time. Checking those against what happened is how the team learns which instincts are reliable, and it costs a sentence.

**Retrieval during investigation.** An analyst seeing unfamiliar traffic should find structurally similar past schemes — by infrastructure pattern, by behavioural shape — rather than by remembering. This is what compresses a multi-day investigation.

**Feed the scheme layer into detection.** Once schemes are entities with fingerprints, detection can match at the scheme level rather than the signature level, which is exactly the shift from reactive to structural that the build note in this niche depends on.

## Who Feels the Pain
Fraud analysts, re-investigating variants of operations the team already understood. New analysts, who take a long time to become effective because the knowledge is oral. Leadership, whose detection capability is a handful of heavily recruited people. And advertisers, whose protection depends on whether the analyst who understood a scheme is still employed.

## Impact If Fixed
Detection quality is the product, and it currently resets partially whenever an investigator leaves. Capturing scheme-level understanding turns a reactive signature library into an accumulating model of how fraud operations behave — which is both a better detector and the only asset in this business that a competitor cannot rebuild by hiring.
