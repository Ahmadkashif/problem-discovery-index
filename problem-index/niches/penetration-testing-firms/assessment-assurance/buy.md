# Buy: Assurance Language From Audit and Clinical Testing

**Niche:** Assessment Assurance
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Other professions that sample a population and report a conclusion have spent decades building language for scope, confidence and the meaning of a negative result, and security testing has borrowed none of it.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #bayesian-inference #compliance #descriptive-statistics #data-integration
**Contested on:** Whether a test report states what its clean results actually mean, or leaves the client to read two weeks of sampling as evidence of security.

## The Problem

Reporting a conclusion drawn from a sample, in a way the reader cannot over-interpret, is a solved problem in several professions — and each solved it because over-interpretation caused real damage.

Financial audit developed a precise vocabulary: an opinion is about the financial statements taken as a whole, with defined materiality, stated scope limitations, and explicit language about what the auditor did and did not examine. Clinical testing reports sensitivity and specificity, so a negative result carries a known and communicable meaning. Structural and safety inspection reports state which areas were accessible and which were not, and a competent inspector's report has a section listing exactly what could not be examined.

Penetration testing reports findings and stops. The profession has no materiality concept, no scope limitation language, no stated sensitivity, and no accessible-areas section — and its clients over-interpret the result in exactly the way all of those conventions exist to prevent.

## What Already Exists

Audit: the assurance standards and their report structures, with defined levels — reasonable assurance, limited assurance, agreed-upon procedures — that let a practitioner say precisely how much confidence their work supports. Agreed-upon-procedures engagements are the closest existing analogue to a penetration test and have a mature reporting convention that says exactly what was done and explicitly disclaims a broader conclusion.

Clinical: diagnostic test reporting with sensitivity, specificity and predictive values, and the well-developed practice of communicating what a negative result rules out.

Software engineering: code coverage tooling, which solved the analogous denominator problem for testing and is universally understood by the technical audience these reports go to.

Security-adjacent: the MITRE ATT&CK framework, which provides a shared technique taxonomy and is already used by some firms to describe what an engagement exercised — the single most promising existing foundation for coverage reporting in this industry.

## The Customization Gap

**ATT&CK is a taxonomy, not a coverage measure.** Firms increasingly map findings to ATT&CK techniques. Almost nobody reports which techniques were attempted and not successful, versus not attempted at all — which is the distinction that makes it a coverage statement rather than a labelling exercise. This is the highest-value adaptation available and requires no new framework.

**The population is not enumerable.** Audit samples from a known population of transactions. Clinical tests have a defined condition. Attack surface has no natural denominator, so the audit conventions transfer in spirit and need real work in substance — most plausibly as per-asset-class coverage rather than a single figure.

**Sensitivity has to be estimated from the firm's own history.** A clinical test's sensitivity comes from validation studies. A testing firm would have to estimate it from its own corpus — how often a subsequent deeper engagement found something an earlier one missed in the same area. Every firm has the data and none has done the calculation.

**Assurance levels are the missing commercial vocabulary.** Audit's tiering — reasonable, limited, agreed-upon-procedures — lets a buyer choose and price a confidence level explicitly. Penetration testing sells days and lets the buyer infer. Adopting an assurance-level vocabulary would let firms sell depth rather than time, which is the commercial restructuring this whole niche implies.

**Code coverage sets the wrong expectation if borrowed naively.** Technical buyers understand line coverage and will read any security coverage number the same way, which would badly overstate what it means. The framing has to be explicitly probabilistic and depth-banded rather than a percentage.

**Nobody owns the standard.** Audit has professional bodies and regulators. Security testing has CREST, OSCP-style certification and various methodologies, none of which specify a coverage reporting convention. Whoever writes a credible one has a strong position, and it is more valuable published than proprietary.

## Target Customer

The methodology and accreditation bodies — CREST and its peers — are the most credible homes for a coverage reporting standard, since the value is in adoption rather than exclusivity.

Commercially, the specialist boutiques whose work is genuinely deeper and who need a way to demonstrate it, and the security testing platforms that already structure engagement data and could compute coverage as a feature.

Cyber insurers and enterprise procurement are the demand side: both currently treat a report as binary evidence that testing happened, and both would use a confidence level if one existed.

## Impact If Solved

A profession that samples and reports would acquire the reporting conventions that every other sampling profession developed after being burned by over-interpretation.

ATT&CK-based attempted-versus-succeeded reporting is available today, costs almost nothing, and would immediately let a report distinguish "we tried this and it held" from "we never tried this" — which is most of the value.

And an assurance-level vocabulary would let the market price depth explicitly, which is the only mechanism by which a firm doing genuinely deeper work can be paid for it.
