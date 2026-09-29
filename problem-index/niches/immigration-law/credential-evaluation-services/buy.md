# Document Verification Against Institutions That Do Not Answer

**Niche:** [[niches/immigration-law/credential-evaluation-services/profile|Foreign Credential Evaluation Services]]
**Industry:** [[industries/immigration-law|Immigration Law Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Verification means writing to a registrar in another country and hoping, and the alternative is detecting a forgery from a scan.
**Tags:** #computer-vision #ocr #anomaly-detection #binary-classification #data-integration

## The Problem
Before an evaluation can be issued the documents have to be genuine. Transcripts and degree certificates arrive as scans and photographs from thousands of institutions in over a hundred countries, in many scripts and formats.

Primary verification means contacting the issuing institution. Some respond in days through a formal system, some respond in months by email, and some do not respond at all — because the registrar has no capacity, or the records were lost, or the institution no longer exists. Meanwhile document fraud in this space is a real and organized business, because the payoff is a work visa.

So evaluators rely heavily on analyst familiarity: knowing what this university's transcript looks like, what its seal and signature block should be, what its grading scale is, which document features have appeared in past forgeries. That knowledge sits in the analysts who have seen the most documents.

## What Already Exists
Identity document verification is a mature commercial category — Jumio, Onfido, IDEMIA and others authenticate passports and driving licences at high accuracy and scale, using template matching, security feature detection, and tamper analysis.

## The Customization Gap
Those systems work because their targets are standardized, secured documents issued by a few thousand authorities to a common design. Academic documents are the opposite.

**No templates and no security features.** A university transcript has whatever layout the registrar chose, printed on ordinary paper, with a seal and a signature. There is nothing to match against, so authenticity has to be assessed from consistency with prior genuine documents from that same institution — which requires a reference archive of them, which the evaluator has and no vendor does.

**Institution-specific normality.** The useful question is not whether this document looks like a transcript, but whether it looks like a transcript from *this* institution in *this* year — including how the grading scale is expressed, how course codes are formed, and how the seal is placed. That is an anomaly detection problem per institution, on a long-tailed distribution where most institutions appear rarely.

**Internal consistency as the strongest signal.** Credit totals that do not reconcile to the stated degree, a graduation date inconsistent with the programme duration, a grading scale that does not match the country's convention, course sequences that could not have been taken in that order. These catch fabrications that look visually perfect, and they require domain knowledge no generic verification product has.

**Multi-script, low-quality input.** Photographs of documents in scripts commercial OCR handles poorly, sometimes with a translation whose fidelity is itself in question.

**Verification routing as an economic decision.** Which institutions respond, how fast, through what channel, and at what cost is knowledge the evaluator has accumulated per institution and holds informally. Routing verification effort by expected response and by document risk is the practical improvement, and it belongs in the same system.

## Target Customer
Director of Evaluation Operations at a credential evaluation service, where verification is simultaneously the slowest step, the largest fraud exposure, and the least systematized part of the process.

## Impact If Solved
Fraudulent credentials that pass produce visas and licences that should not exist; genuine documents wrongly doubted cost real people months. Both errors currently depend on which analyst opened the file. Making institution-level document normality explicit turns the most experienced analysts' pattern recognition into something the organization owns — and routing verification by expected response time attacks the step that sets turnaround.
