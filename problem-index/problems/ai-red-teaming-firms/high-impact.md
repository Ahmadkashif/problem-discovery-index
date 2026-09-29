# Coverage Is Unmeasurable

**Industry:** [[ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** High Impact
**One-liner:** A clean report tells a client nothing unless somebody can say what fraction of the risk surface was examined, and no method exists for stating that about a system with an unbounded input space.
**Tags:** #hypothesis-testing #confidence-intervals #evaluation-metrics #pac-learning-and-vc-dimension #bayesian-inference #large-language-models #dimensionality-reduction #compliance

## The Problem
A traditional penetration test can be scoped. There is an asset inventory, a set of services, a defined perimeter, and a report can say what was tested and what was not.

An AI system has no equivalent. The attack surface is natural language, which is unbounded, and the failure modes range from producing harmful content to leaking training data to being manipulated through injected instructions in retrieved documents. A red team spends an engagement probing, finds some things, and writes them up.

The client receives a report. If it contains critical findings, that is informative. If it does not, the client cannot tell whether the system is robust or the team looked in the wrong places, and neither can the firm.

This matters commercially and increasingly legally. Regulatory frameworks are converging on requirements for documented adversarial testing, and organisations will be asked whether their testing was adequate. "We engaged a reputable firm for three weeks" is the current answer and it is not a coverage statement.

It also makes the market hard to buy in. A client comparing two firms cannot assess thoroughness, so selection happens on reputation and price, and there is no competitive pressure toward better coverage because coverage is invisible.

## Why It's Unsolved
The input space genuinely is unbounded, and no sampling of it constitutes coverage in the sense a security auditor means. Any coverage claim is therefore a claim about a structured space the firm has defined, which is a weaker statement and one the industry has been reluctant to make explicitly because it invites the question of whether the structure is right.

Harm taxonomies are the natural structure and they are contested. Reasonable people disagree about categories and severity, taxonomies differ across firms and frameworks, and mapping a finding to a category is itself a judgement.

Defences are model-specific and brittle in a way that undermines generalisation. A probe that fails against one model succeeds against another, and a model updated next month may behave differently on both, so a coverage claim has a short life.

The adversarial dimension is the deepest issue. Coverage against known attack classes says nothing about novel ones, and novel attacks are the ones that matter. This is a permanent property of security work, and the traditional discipline handles it by scoping to an asset inventory — which is exactly what is unavailable here.

## What a Solution Looks Like
Structured coverage over an explicit taxonomy, stated honestly. A report should say which harm categories were probed, with how many attempts, using which technique families, at what depth, and which categories were not covered — and it should say plainly that this is coverage of a defined space rather than of all possible failures. That is a much stronger artefact than a finding list and nobody produces it.

Sampling with statistical framing. Within a category, probes drawn systematically rather than opportunistically support statements like "of two hundred attempts across this category, none succeeded, giving an upper bound on failure rate at this confidence" — which is a real, bounded, defensible claim.

Cross-engagement calibration. A firm with thousands of assessments knows which probe families find things across models, and can prioritise the space rather than exploring it by habit — and can tell a client how this system compares to others tested.

Novelty measurement of the probes themselves. Whether an engagement explored genuinely new territory or reapplied the firm's standard set is measurable by embedding probes and comparing against the historical corpus, and it is what distinguishes real research from a checklist run.

## Impact If Solved
Assurance is the product and it currently rests on a finding list with no denominator, at a moment when regulation is about to ask organisations to demonstrate adequacy. Structured coverage reporting is what would make a clean result meaningful, make firms comparable, and create competitive pressure toward thoroughness rather than reputation.
