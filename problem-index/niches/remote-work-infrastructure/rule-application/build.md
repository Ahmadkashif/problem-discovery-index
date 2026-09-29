# Build: A Structured, Versioned, Consistency-Checked Rule Base

**Niche:** [[niches/remote-work-infrastructure/rule-application/profile|Rule Application]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Turn prose guidance into structured, dated, sourced rules that can be applied mechanically, checked for conflict and updated with propagation.
**Tags:** #compliance #large-language-models #data-integration #evaluation-metrics #confidence-intervals #workflow-orchestration #hypothesis-testing #descriptive-statistics
**Contested on:** Whether legal rules across dozens of jurisdictions can be structured without losing the judgement they require.

## The Problem

Every country has its own payroll calculation, statutory contributions, leave entitlements and benefit expectations, and each one is implemented and maintained by hand.

The same is true of the classification and establishment rules. They live as prose in an internal knowledge base, read by a specialist, applied by judgement. That arrangement has three failures: the rules cannot be applied consistently because prose admits interpretation, they cannot be checked for conflict or gaps, and a change in one jurisdiction cannot be propagated to the determinations that relied on it because nothing links them.

The scale makes it worse. A platform operating in sixty jurisdictions has sixty rule sets across employment classification, tax establishment, benefits, leave and termination — three hundred rule areas maintained by reading.

## Why Nobody Has Built This

Structuring legal rules is genuinely hard and has a long history of overpromising. Classification tests are multi-factor judgements with case law and inconsistent enforcement, and a rules engine that pretends otherwise produces confident wrong answers.

The honest form is a structured representation that supports the judgement rather than replacing it — capturing the factors, their weights where known, the thresholds, the sources and the uncertainty — and that framing has not been common because the appeal of a rules engine is automation.

And the work is unglamorous and large: three hundred rule areas is a multi-year exercise nobody has funded.

## What to Build

Rules as versioned structured artefacts, with the judgement preserved.

**Represent the rule as factors, not as an answer.** For each jurisdiction's classification test: the factors the test turns on, how each is weighted or ordered, the thresholds where they exist, and the sources. This supports a specialist rather than replacing them, and it is what makes consistency measurable.

**Version with effective dates and sources.** Every rule as an object with a version, an effective date, a last-verified date, and a citation. Superseded versions retained, so a determination made two years ago can be evaluated against the rule that was live then.

**Extract the first draft from the existing prose.** Generative extraction from the current knowledge base and from published country guides produces a structured draft for specialist correction, which is what makes three hundred rule areas tractable at all.

**Check for conflict and gaps automatically.** Rules that contradict each other, jurisdictions with no rule for a scenario the platform operates in, and factors referenced in one rule and undefined elsewhere. These are static checks over a structured base and they surface problems nobody currently sees.

**Propagate changes.** A rule version change flags every determination that relied on the previous version. This is the capability that turns a knowledge base into infrastructure, and it is impossible with prose.

**Measure consistency.** Route the same facts to two specialists, blind, and compare determinations. Low agreement on a jurisdiction means the rule is underspecified, which is a finding about the rule rather than about the specialists.

**Prioritise by exposure.** Structure the jurisdictions with the most engagements and the most volatile law first. Uniform effort across sixty countries is how this project fails.

## Target Customer

Platform compliance leadership, for whom this is a direct reduction in their own exposure and in the key-person risk of specialists holding jurisdictions in their heads. Also the regulatory intelligence and legal knowledge vendors, for whom structured employment rules across jurisdictions is a product with an obvious buyer.

## Impact If Built

The rules become artefacts that can be applied consistently, checked, versioned and propagated, rather than prose read by whoever is available. Conflicts and gaps surface. Changes reach the determinations that depended on them. And the platform's central capability stops living in a wiki and in individual memory.
