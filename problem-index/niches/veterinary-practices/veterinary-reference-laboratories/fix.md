# The Pathologist's Reasoning Is the Product and It Ships as a Comment

**Niche:** [[niches/veterinary-practices/veterinary-reference-laboratories/profile|Veterinary Diagnostic Reference Laboratories]]
**Industry:** [[industries/veterinary-practices|Veterinary Practices]]
**Type:** Fix (Pain Point)
**One-liner:** A clinical pathologist reads a slide, weighs it against the history and the chemistry, and writes three sentences; nothing records why, and nobody ever learns whether they were right.
**Tags:** #tacit-knowledge-ml #evaluation-metrics #large-language-models #automation #worker-facing

## The Problem
Alongside the automated results sits interpretation. A clinical pathologist reviews a blood smear, a cytology sample, a histopathology section, or an unusual chemistry pattern, and writes a comment: what this most likely represents, what else it could be, and what to do next. For the general practitioner receiving it, that comment often is the diagnosis.

It is a judgment made from the slide, the signalment, the history the practice supplied, and the pathologist's accumulated experience of thousands of similar cases. What gets stored is the comment.

Three consequences, and they are the ones this index has now recorded in a dozen expert-judgment businesses. Consistency is unmeasured: cytology interpretation has documented inter-observer variability, and no laboratory routinely measures agreement between its own pathologists on the same material. Outcomes are unlinked: the animal is treated, biopsied, referred or dies, and in a very large share of cases the laboratory itself performs the follow-up testing — so the confirmation exists in the same database as the original opinion, and nothing joins them. And the reasoning is unrecorded, so the corpus that would support any assistance to interpretation consists of conclusions without the thinking that produced them.

This matters more here than in most places because the discipline is short of people. Board-certified veterinary clinical pathologists are few, demand for interpretation is growing with corporate consolidation and diagnostic volume, and turnaround pressure falls directly on them.

## Why It's Still Broken
Volume is the pressure. Pathologists are measured on cases read per day against a turnaround commitment, and structured capture is time taken from the queue.

The report format is inherited from paper. A free-text comment is what practices expect and what every downstream system carries, so nothing requires more.

Outcome linkage is genuinely non-trivial, though not for the usual reason: there is no privacy barrier at all here. Follow-up testing may arrive months later, from a different practice, under a different patient record, and the identity resolution has simply never been built because no product required it.

And there is a mild professional discomfort about measuring agreement. Pathologists know inter-observer variation exists; a laboratory that quantified its own would be creating a number it would then have to manage.

## What a Fix Looks Like
**Capture the differential, not just the conclusion.** The considered alternatives, the feature that discriminated, and the confidence — as structured fields alongside the comment. Seconds on straightforward cases, a minute on hard ones.

**Link to confirmation, because you can.** Where the laboratory later performs a biopsy, a culture, a repeat panel or a necropsy on the same patient, join it back. This is an entity resolution project with no legal obstacle and no consent requirement — the rarest condition in clinical data anywhere — and it produces a validated accuracy record.

**Measure inter-pathologist agreement deliberately.** Route a sample of cases to several readers and compare. It is uncomfortable, it is the only way to know what a given diagnostic call actually means, and it produces the calibration set any interpretive assistance would require.

**Use the reasoning as supervision.** Assisted interpretation — flagging the likely differential from image and chemistry — is achievable in this field precisely because the data is unencumbered, and it needs labelled examples of how ambiguous material is resolved. The decision record is that corpus.

**Give the pathologists retrieval over their own archive.** Similar cases, with what they were called and what they turned out to be, is useful from the first week — which is what determines whether the capture habit survives.

## Who Feels the Pain
Clinical pathologists, whose expertise is the product, whose numbers are limited, and whose judgment is stored as prose; general practice veterinarians, who receive an interpretation with no stated confidence and no way to know the reader's accuracy; and the laboratory, whose most differentiated service has never been measured despite the confirming evidence sitting in its own database.

## Impact If Fixed
Interpretive services are where a diagnostics company competes on something other than turnaround and price, and they depend on a scarce, ageing specialty. Recording the reasoning and linking to confirmation makes accuracy measurable for the first time, creates the training corpus for assistance that could extend a limited pathologist workforce — and does it in the one clinical domain where no privacy regime stands in the way.
