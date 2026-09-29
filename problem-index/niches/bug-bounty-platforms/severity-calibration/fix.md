# Fix: CVSS Is Cited, Not Applied

**Niche:** Severity Calibration
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Programmes name a scoring standard and then assign the band they intended, reverse-engineering the score to match, which gives the appearance of a method without the constraint of one.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #worker-facing #descriptive-statistics
**Contested on:** Whether a finding's severity can be referenced against how comparable findings were rated across the whole market, or remains one programme's private judgement.

## The Problem

Nearly every bounty programme cites CVSS. Very few apply it.

Applying it means working through the vector — attack vector, complexity, privileges required, user interaction, scope, and the three impact metrics — and accepting the score it produces. What happens instead, routinely, is that the triager forms a view of the severity, assigns a band, and if a score is required constructs a vector that lands there. The standard supplies the vocabulary and none of the discipline.

The consequence is that severity looks methodical and is not. A researcher who disputes a rating is told it is CVSS medium, with no vector shown, and has nothing to argue with. If the vector were published, the disagreement would become specific — we differ on whether privileges are required — which is a resolvable conversation rather than a contest of opinions.

There is a legitimate critique underneath this. CVSS genuinely is a poor fit for bounty work: it was designed for published vulnerabilities in distributed software, it handles business impact badly, and its base score ignores the context that matters most here. The problem is not that programmes work around CVSS; it is that they work around it silently while continuing to invoke its authority.

## Why It's Still Broken

**The vagueness is useful.** A cited-but-unapplied standard confers legitimacy without constraint. Showing the vector would expose ratings to challenge, which is more work and occasionally more money.

**CVSS really is a bad fit and there is no agreed replacement.** SSVC and EPSS answer different questions and neither has been adopted here. So programmes are left with a standard that does not fit and no sanctioned alternative, which makes informal adjustment the only workable practice.

**Business impact is the real driver and is unscored.** What actually determines severity for a programme is what this means to the business, which no vulnerability scoring system captures. That judgement is legitimate and has no vocabulary, so it gets expressed through a CVSS band.

**Nobody audits the citation.** No platform checks whether a programme's stated scores are consistent with the vectors, or whether vectors are recorded at all. There is no cost to citing a standard loosely.

**Researchers cannot challenge what they cannot see.** Without a published vector there is no specific point of disagreement, which suits the party making the decision.

## What a Fix Looks Like

**Require the vector, not just the score.** Every rating published with the full vector. This is the fix. It costs a triager a minute, converts an opaque verdict into a specific claim, and turns most disputes into a disagreement about one component that can actually be resolved.

**Add an explicit business-impact modifier and name it.** A separate, stated adjustment — this is on a payment path, this handles regulated data, this is a deprecated asset behind a compensating control — applied on top of the technical score, recorded with a reason. This gives the legitimate judgement its own vocabulary instead of smuggling it into a CVSS band, and it makes the reasoning inspectable.

**Audit consistency.** Platforms should check that published vectors produce the stated scores and that similar findings at the same programme receive similar vectors. Both are mechanical and neither is done.

**Publish the programme's own rating distribution.** A programme's history by finding class, visible to researchers. Internal consistency becomes checkable without anyone needing a cross-programme reference, which makes this available immediately.

**Say plainly if a programme does not use CVSS.** A programme with its own severity rubric should publish the rubric and stop citing a standard it does not apply. Honest idiosyncrasy is better than borrowed authority, and researchers respond well to a clearly stated rubric.

**Let researchers submit a proposed vector.** The researcher understands the finding best and can supply the vector with their submission. The triager then disagrees with something specific rather than issuing a verdict, which reframes the entire interaction.

## Who Feels the Pain

The researcher, handed an unexplained band and told it reflects a standard, with no component to point at and no basis to appeal.

The triager, obliged to invoke a framework that does not fit the judgement they are actually making, with no vocabulary for the business impact that is genuinely driving their assessment.

Programmes that do apply CVSS rigorously, indistinguishable from those that do not, and therefore earning no credit for the discipline.

And the standard itself, whose credibility erodes as it is cited by an industry that does not apply it.

## Impact If Fixed

Publishing the vector costs a minute per finding and transforms severity from a verdict into a claim with components. Almost every dispute in this area becomes narrower and more resolvable.

Separating a named business-impact modifier from the technical score gives the legitimate part of the judgement somewhere honest to live, instead of distorting a framework that was never designed to carry it.

And a programme publishing its own rating distribution provides accountability immediately, without waiting for any cross-programme reference to be built.
