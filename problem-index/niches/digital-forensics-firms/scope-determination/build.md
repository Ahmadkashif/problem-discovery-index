# Build: Bounds, Not Narrative

**Niche:** Scope Determination
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An inference layer that states, from a given evidence set, what is established, what is bounded and what cannot be addressed — with the bounds calibrated against the firm's own history of comparable investigations.
**Tags:** #bayesian-inference #evaluation-metrics #confidence-intervals #hypothesis-testing #graph-theory #probability-distributions #compliance #tacit-knowledge-ml
**Contested on:** Whether "what did the attacker access" is answered with calibrated bounds from the evidence that exists, or with a narrative.

## The Problem

A responder reaches a conclusion. The attacker had domain administrator credentials for eleven days. They accessed a file server containing three million customer records. There is no evidence of large-scale exfiltration — no unusual egress volume in the netflow that was retained, no staging archives found, no exfiltration tooling on the systems examined.

What does that support? Access was possible to three million records. Whether any were read is unknown, because file access auditing was not enabled. Whether any left is unknown for the period before netflow retention began, which covers the first six days.

The report says: no evidence of exfiltration was identified. The client's counsel reads that as a finding that nothing was taken. The board hears it as a finding. The regulator receives a notification decision built on it. And the qualification the responder actually meant — that absence of evidence here is weak evidence of absence, because the evidence that would have shown it did not exist — travels no further than the bridge call.

The responder knows exactly how weak the inference is. There is no artefact in which to say so, and saying it plainly forces the client into a conservative and enormously expensive notification.

## Why Nobody Has Built This

**Bounds are commercially unwelcome.** A client paying for an answer receives a range and a set of unanswerable questions. Firms that deliver certainty are easier to work with, and the market notices.

**Calibration requires the firm's own history.** Stating how often "no evidence of exfiltration" has later proved wrong given comparable evidence requires tracking outcomes across investigations — and outcomes frequently never arrive, since most breaches are never conclusively resolved.

**Legal privilege fragments the corpus.** Investigations are conducted under privilege, which is a substantial obstacle to building any cross-engagement dataset even within one firm.

**The narrative form is entrenched.** Forensic reporting is a written tradition serving litigation, and a probabilistic bound is harder to put in front of a jury than a clear finding.

**Every incident feels unique.** The profession's self-image is that each investigation is bespoke expert work, which resists the idea that inference from evidence classes can be systematised.

**Nobody is measured on calibration.** A firm whose scope conclusions are systematically narrow faces no consequence unless a specific case goes badly, which is rare and attributable to circumstances.

## What to Build

**Model the evidence-to-inference relationship explicitly.** For each question — was data accessed, was it exfiltrated, which records — state which evidence sources would answer it, which of those exist in this engagement, and what the surviving evidence supports. This is a structured representation of what every good responder does in their head.

**Produce three categories, always.** Established by evidence. Bounded — cannot exceed this, cannot be ruled below that. Unaddressable — no evidence exists and none will. The third category is the one that currently disappears, and naming it explicitly is most of the value.

**Calibrate the bounds from the firm's own corpus.** Across investigations with comparable evidence profiles, how often did a later development contradict the conclusion. Where outcomes are available — a subsequent leak, a later disclosure, an attacker's own claims — they are the calibration data, and no firm collects them.

**Base data-at-risk on access, not inventory.** The current default is to treat everything in a compromised system as at risk, which is defensible and frequently enormously over-inclusive. Modelling what the credentials used could actually reach, and what the observed activity pattern is consistent with, narrows scope defensibly.

**Make the unanswerable list a deliverable.** The specific evidence that would have answered each open question and was not retained. This serves the client's remediation directly and is the bridge to [[niches/digital-forensics-firms/evidence-readiness/profile|🎯 Pre-Incident Evidence Readiness]].

**Structure it for the notification decision.** Counsel needs to know the maximum defensible scope, the minimum established scope and the basis for each. Delivering exactly that, rather than a narrative they must interpret, is what makes the artefact usable at the moment it matters.

**Write for the reader downstream.** The report will be read by people who were not on the bridge call. The qualifications must survive extraction into a board slide, which means they belong in the finding rather than in a caveats section.

## Target Customer

Forensics firms with a quality position to defend, for whom calibrated bounds are a credibility claim rather than a commercial weakness — particularly those doing expert witness work where overstatement is professionally dangerous.

General counsel and breach coach law firms, who are the actual consumers of the scope conclusion and currently receive a narrative they must interpret under time pressure.

Cyber insurers, who fund most of this work and whose exposure depends directly on scope — and who are well placed to require bounded reporting as a panel condition.

## Impact If Built

The industry's central conclusion stops being stated more confidently than the evidence supports, which is a professional exposure the whole field carries.

Naming the unanswerable category explicitly is the change with the largest effect, because it is currently the information that disappears between the bridge call and the board.

And calibrating bounds against the firm's own history would let a firm say how often a conclusion of this kind has held — which is the closest this profession could come to demonstrating that its judgement is worth what it costs.
