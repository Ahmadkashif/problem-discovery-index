# Recommendations Graded on Evidence Quality and Never on Whether Anyone Followed Them

**Niche:** [[niches/urgent-care/clinical-reference-decision-support/profile|Clinical Reference & Decision Support Content Publishers]]
**Industry:** [[industries/urgent-care|Urgent Care]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The publisher's recommendations are consulted millions of times a day at the point of care, and it never learns which ones a clinician acted on.
**Tags:** #transformers #large-language-models #evaluation-metrics #causal-inference #gradient-boosting

## The Problem
The product is a graded recommendation. A clinician facing an undifferentiated presentation opens a topic, reads what the evidence supports, and decides. The grading system describes the strength of the evidence and the strength of the recommendation — a scale about the literature.

There is a second scale nobody maintains: whether the recommendation is followed, and what happens when it is not. That is not a literature question, it is an empirical one, and the publisher is structurally blind to it. Content is licensed to health systems and clinicians; the consultation happens inside their environment; the decision that follows is recorded in their record system; nothing returns.

Two things are lost. The first is the obvious feedback loop — which recommendations change behaviour, which are consulted and ignored, and which topics clinicians open repeatedly because the answer was not usable. The second is subtler and more valuable: the publisher does not know what question the clinician was actually trying to answer. It sees a topic opened. It does not see that the clinician was three minutes into an encounter with a presentation that did not match any topic cleanly, which is the ordinary condition of urgent care.

Meanwhile the competitive ground has shifted underneath. General language models answer clinical questions fluently, and their failure mode is fabrication — a recommendation that sounds right, a citation that does not exist, a guideline superseded two years ago. The publishers hold the exact corrective: a curated, dated, graded, citation-backed body of synthesis maintained by physicians. They deploy it as a searchable encyclopedia.

## Why Nobody Has Built This
The licensing chain puts a wall exactly where the feedback would flow, in the same shape as the drug compendia problem: publisher to health system to clinician, with usage data belonging to the middle party and clinical outcomes to the third.

Liability makes the institutional posture conservative. A reference work that describes what the evidence supports occupies a very different legal position from a system that recommends an action for a specific patient, and every step toward the latter is examined carefully. That caution is reasonable and has been allowed to settle the strategic question by default.

And the editorial model is built around topics, because that is how a reference work is organised and how physician authors write. Presentations do not arrive as topics.

## What to Build
Reasoning over the synthesis corpus, with the presentation rather than the topic as the entry point.

**Ground generation in the curated corpus, by construction.** Every generated statement should resolve to a specific graded recommendation in a specific dated topic with its citations. This turns the publisher's asset into the thing that makes generative clinical answering safe, and it is the only defensible product any of these companies can build against a general model.

**Make the entry point a presentation.** A clinician has a set of findings, not a diagnosis. Mapping unstructured presentation descriptions to the differential and to the relevant recommendations is a retrieval and reasoning problem over content the publisher already owns, and it is what the topic-based structure prevents today.

**Model currency risk.** Not every topic needs review at the same rate. Given publication volume in an area, guideline activity, and time since last review, predict which topics are most likely to be out of date. Editorial capacity is finite and is currently allocated by schedule.

**Negotiate for usage telemetry.** De-identified consultation events — what was searched, what was opened, what was abandoned, what was followed — do not require patient data and would be the first behavioural feedback this industry has ever had. It is a commercial negotiation, not a technical obstacle.

**Report the currency and the grounding.** Time since last evidence review, per topic, exposed to the reader; and a stated proportion of generated content traceable to a graded recommendation. In a market about to be flooded with fluent, ungrounded clinical answers, a measured claim of that kind is the whole differentiation.

## Target Customer
Chief Medical Officer or VP of Clinical Content at a clinical reference publisher. The argument is stark: the fluent-answer layer of this product is being commoditised by general models, and the curated, dated, graded synthesis underneath it is the only part that cannot be.

## Impact If Built
Point-of-care reference is consulted millions of times a day and is doing a substantial share of the diagnostic reasoning in settings like urgent care, where presentations are undifferentiated and encounters are minutes long. Making that reasoning presentation-first and verifiably grounded is both a clinical safety improvement and the only durable position the publishers have.
