# Build: The Inference Map

**Niche:** Evidence-Bounded Inference
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A structured map from evidence sources to answerable questions, applied to each engagement, producing what is established, what is bounded and what cannot be addressed — computed rather than recalled.
**Tags:** #bayesian-inference #graph-theory #evaluation-metrics #confidence-intervals #hypothesis-testing #probability-distributions #tacit-knowledge-ml #compliance
**Contested on:** Whether, mid-incident, a firm can state what the surviving evidence supports as a calibrated bound rather than as a narrative.

## The Problem

On day three of an incident, a senior responder holds a mental model of extraordinary complexity: which questions the engagement must answer, which evidence sources would answer each, which of those exist here, what their retention windows cover, what the gaps permit, and what the observed activity is consistent with.

That model is entirely in their head. It is reconstructed from scratch on every engagement. It is the most valuable thing the firm owns and it exists only while that person is on the case.

The consequences are practical. A junior responder cannot assemble it, so the most senior people are required in the first days of every incident, which is the direct cause of the working pattern in [[niches/digital-forensics-firms/the-responder/profile|🟣 The Responder]]. The model is not written down, so the reasoning cannot be reviewed, challenged or improved. And when the conclusion is questioned months later in litigation, the basis for it must be reconstructed from memory.

The model is also more structured than it feels. The relationship between evidence sources and questions is largely stable across incidents. What file access auditing would have shown, what netflow retention covers, what a credential's scope implies, what a process execution record permits — these are general facts about evidence, applied to a specific case.

## Why Nobody Has Built This

**The profession regards it as irreducible expertise.** The prevailing view is that investigation is judgement that cannot be systematised, which is partly true and is used to justify not attempting the part that can.

**Every incident feels unique.** The specifics differ enormously, which obscures how stable the underlying evidence-to-question relationships are.

**Privilege fragments everything.** Investigations run under legal privilege, which discourages building any cross-engagement structure even inside one firm.

**Building it exposes the gaps.** A map showing that a third of the required questions are unanswerable from the available evidence is an accurate and uncomfortable artefact for a client mid-crisis.

**No time to build during an incident and no incentive between them.** The knowledge is generated under conditions that preclude recording it, and between engagements the practitioners are recovering or on the next one.

**Senior practitioners have limited enthusiasm.** Codifying the model reduces the dependence on the individuals who hold it, which is a real consideration in a labour market this tight.

**Calibration needs outcomes that rarely arrive.** Most incidents are never conclusively resolved, so the data that would calibrate the bounds is sparse.

## What to Build

**Encode the evidence-to-question relationship as a reusable structure.** For each question a breach investigation must answer, the evidence sources that would answer it, what each source establishes, and what its absence permits. This is a knowledge base, built once, refined continuously, and it is the product.

**Instantiate it per engagement.** Inventory which sources exist, with retention windows, and compute which questions are answerable, which are bounded and which are not. On day one rather than day nine.

**Compute the bounds.** Maximum and minimum defensible scope given credential reach, observed activity, retention coverage and the data inventory — rather than asserting a figure in prose.

**Bound by access, not by inventory.** What the compromised credentials could actually reach, intersected with what the observed activity is consistent with, is frequently far narrower than everything in the affected system and is defensible in a way inventory-based scope is not.

**Record the reasoning as it is made.** The inferences and their basis captured during the engagement, so the conclusion is reviewable, defensible in later litigation, and available for calibration if an outcome ever arrives.

**Surface the unanswerable list early.** Knowing on day two which questions will never be answerable changes how the engagement is run and what the client is told, and today it emerges on day nine.

**Calibrate opportunistically.** Where an outcome does arrive — a leak site posting, a regulatory finding, a later disclosure — score the earlier conclusion. Sparse calibration data accumulated over years is far better than none.

## Target Customer

Forensics firms, sold on capacity rather than on quality: a structure that lets a mid-level responder assemble the inference map frees the senior practitioners who are the binding constraint on every engagement.

Breach coach law firms, who direct these investigations and need the answerable-question map to advise their client on timing and exposure.

Cyber insurers, who fund the work and whose reserving depends on the bounds — and who could require structured scope reporting across a panel.

## Impact If Built

The most valuable tacit knowledge in the field becomes transferable, which addresses the labour constraint that shapes everything else in this industry.

Producing the answerable-question map on day one rather than day nine changes how the engagement is planned and what the client can be told while the statutory clock still has room in it.

And bounding scope by what the access could actually reach, rather than by what was in the system, would narrow notification defensibly in a large share of incidents — which is worth an enormous amount to clients and is currently left on the table because the inventory default is easier to defend.
