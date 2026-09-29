# Editorial Judgment Is the Asset and It Is Recorded as a Field Value

**Niche:** [[niches/pharmacy-independents/drug-compendia-pricing-publishers/profile|Drug Compendia & Pricing Content Publishers]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Fix (Pain Point)
**One-liner:** A pharmacist editor weighs contradictory evidence for two days and the output is one severity grade with no record of the reasoning.
**Tags:** #tacit-knowledge-ml #large-language-models #evaluation-metrics #compliance #worker-facing

## The Problem
The value in a drug knowledge base is not the facts. It is the judgments: whether the evidence for an interaction is strong enough to grade it as major, whether a case-report signal warrants an assertion at all, which of two conflicting sources to follow, and how to represent a nuance the schema does not have a field for.

Those judgments are made by experienced clinical editors, often after substantial work, and the artefact that survives is a value in a field. The reasoning — the evidence considered, the sources discounted and why, the precedent applied from a structurally similar case decided three years ago — is not stored anywhere.

This causes three problems at once. Consistency: two editors handling comparable evidence in different therapeutic areas can grade differently, and nothing surfaces the divergence because there is no record of the basis. Defensibility: when a customer or a plaintiff's expert asks why a pair is graded as it is, the answer must be reconstructed. And succession: the editors carrying twenty years of accumulated house judgment are the product, and they are retiring out of a profession with a thin specialist pipeline.

It also blocks everything above. A model that proposes content changes needs training labels of the form "this evidence, this decision, this reasoning". The decisions exist; the reasoning does not.

## Why It's Still Broken
The schema was designed to serve dispensing systems, and a dispensing system needs a severity code, not an argument. Every downstream consumer is satisfied by the field value, so nothing in the pipeline creates pressure to record more.

Editorial productivity is measured in throughput. Time spent documenting reasoning is time not spent clearing the queue, and the queue is visible while the missing rationale is not.

And there is genuine caution about writing down internal deliberation in a product with real liability exposure. A recorded discussion of whether an interaction is serious enough to warn about is a document that can be read back in a courtroom. This is a real concern and it has been allowed to settle the question by default.

## What a Fix Looks Like
**Capture the decision at the moment it is made.** A short structured record attached to each graded assertion: evidence relied on, evidence rejected, the specific reason, and what new evidence would change the grade. Minutes per decision, inside a workflow the editor is already in.

**Store precedent as a first-class object.** Editors reason by analogy to previous decisions constantly. Making prior decisions retrievable by evidence pattern rather than by drug name is what turns individual memory into an institutional asset — and it is immediately useful, which is what determines whether people use the system.

**Report inter-editor consistency.** Periodically route the same evidence package to several editors and compare. This is uncomfortable and it is the only way to know whether the house standard is a standard or a collection of individual habits.

**Feed it upward.** The decision record is the training corpus for automated change proposal. Nothing else in the organisation produces labelled examples of how the house standard applies to ambiguous evidence.

**Settle the privilege question first.** Decide with counsel what is recorded, in what form, and under what retention posture. The current position — record nothing, so nothing is discoverable — also means the publisher cannot demonstrate a rigorous, consistent process, which is its own exposure.

## Who Feels the Pain
The senior clinical editors, who are the standard and cannot scale; the junior editors, who learn the house judgment by apprenticeship the organisation can no longer supply; and the customers, who receive a severity grade with no visible basis and no way to distinguish a well-evidenced assertion from a conservative default.

## Impact If Fixed
The publisher's most valuable and least durable asset — twenty years of accumulated editorial judgment about what the evidence supports — becomes an institutional record rather than a set of careers. Consistency becomes measurable, defensibility becomes demonstrable, and the labelled corpus that any automation of this work requires comes into existence as a by-product of the work itself.
