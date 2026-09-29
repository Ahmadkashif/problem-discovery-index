# Fix: Nobody Reads the Completed Questionnaire

**Niche:** Security Questionnaires
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Three hundred questions are answered under deal pressure and filed by a recipient who checks that the file exists, and both sides know it.
**Tags:** #evaluation-metrics #compliance #confidence-intervals #hypothesis-testing #revenue-impact #worker-facing
**Contested on:** Whether a certificate substitutes for answering three hundred questions, or whether every enterprise buyer sends their own regardless.

## The Problem

The questionnaire is completed and returned. On the receiving side, a vendor risk analyst opens it, scans for red flags, confirms the required fields are populated, records that the assessment was performed, and files it. Time spent: often under an hour, for a document that took the supplier days.

This is not laziness. The analyst may be processing hundreds of supplier assessments a year with no capacity to investigate any deeply, no way to verify a self-reported answer, and a process that measures them on assessments completed. The questionnaire's function in that process is to exist.

Both sides understand this. Suppliers know the document is mostly unread, which affects how carefully it is answered. Buyers know the answers are self-asserted and unverified, which affects how much weight they place on them. The practice continues because the process requires it, because a completed questionnaire is the artefact an auditor or a regulator will ask for, and because no party is positioned to stop.

The result is a substantial industry-wide expenditure of skilled time producing documents that primarily demonstrate that a step was performed.

## Why It's Still Broken

**The artefact satisfies the requirement.** Vendor risk programmes are assessed on whether suppliers were assessed. A completed questionnaire is the evidence, and its usefulness is not what is being measured.

**The asking side has no capacity.** An analyst covering hundreds of suppliers cannot investigate any of them properly. The questionnaire is what fits the capacity available.

**Nothing verifies self-assertion.** Answers are unverifiable without an audit the buyer will not commission, so additional scrutiny yields little and the rational effort allocation is low.

**Certificates do not answer the specific questions.** A SOC 2 report covers controls in general terms and the buyer's questionnaire asks about their specific concerns — data residency, subprocessors, a particular retention period. The certificate genuinely does not substitute, which is why it did not eliminate the practice.

**Standardised questionnaires reduce variation and not volume.** Adoption helps the supplier somewhat and buyers still add bespoke sections, and the underlying process still requires a completed document per supplier.

**Nobody measures whether any of it predicts anything.** Whether questionnaire responses correlate with supplier incidents is unstudied, so there is no evidence that would justify either abandoning or improving the practice.

## What a Fix Looks Like

**Tier the assessment by what the supplier actually touches.** A supplier with access to production customer data warrants real scrutiny; one providing a marketing tool with no data access does not warrant three hundred questions. Most programmes apply a near-uniform process regardless, and tiering would free the capacity to do the important assessments properly.

**Accept a live trust profile in place of the spreadsheet.** Where a supplier publishes a machine-readable, control-state-derived profile, consume it directly. This is better evidence than a self-answered questionnaire and takes minutes rather than days on both sides.

**Ask fewer questions and verify some.** Twenty questions with three verified against evidence is worth more than three hundred self-asserted. Buyers have never been offered this trade and most would take it.

**Measure whether responses predict anything.** A large buyer with years of supplier assessments and supplier incidents could check whether questionnaire answers correlate with outcomes. Nobody has, and the answer would determine whether the practice deserves its cost.

**Reuse assessments across buyers.** A supplier assessed thoroughly by one customer is assessed again by the next thirty. Shared assessment models exist and have thin adoption; the obstacle is trust in another buyer's assessment rather than any technical barrier.

**Say plainly what the certificate covers.** Suppliers should publish the mapping from their certificate to the questions buyers commonly ask, so a buyer can see exactly which of their concerns are already addressed and which genuinely need asking.

## Who Feels the Pain

The supplier's compliance and sales engineering team, spending days producing documents under deal pressure that they know will be scanned and filed.

The vendor risk analyst, running a process they know is weak evidence, at a volume that precludes doing it better, measured on completion.

The buying organisation, which believes its supply chain has been assessed and holds a file of self-reported answers nobody verified.

And the smaller supplier most of all, for whom questionnaire burden is a genuine barrier to selling into enterprise and is absorbed by the same one or two people who do everything else.

## Impact If Fixed

Tiering by actual data access would redirect the capacity currently spread thinly across every supplier toward the small number that genuinely matter, which is a strict improvement on both sides.

Accepting live trust profiles would collapse days of work into minutes and produce better evidence than the questionnaire it replaces, which is the rare change that is cheaper and more accurate.

And measuring whether responses predict supplier incidents is a study one large buyer could run from data they already hold, and it would settle whether this industry-wide expenditure buys anything at all.
