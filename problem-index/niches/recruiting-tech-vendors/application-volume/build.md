# Build: Signals That Cost More to Fake Than to Earn

**Niche:** [[niches/recruiting-tech-vendors/application-volume/profile|Application Volume & Generative Noise]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Design application signals whose cheapest route to a strong value is actually being suitable, rather than filters that automated applications optimise against.
**Tags:** #large-language-models #evaluation-metrics #confidence-intervals #hypothesis-testing #graph-theory #descriptive-statistics #automation #worker-facing
**Contested on:** Whether any application signal survives being cheap to generate.

## The Problem

The screening filter and the application generator are now the same technology pointed in opposite directions, and the generator is winning because it has more attempts.

Keyword requirements are trivially satisfied. Cover letters are generated. Knockout questions are answered optimally. Each new filter becomes, within weeks, another thing the generator optimises for — and the filter degrades fastest against exactly the candidates who use the tooling well, which correlates with nothing an employer cares about.

Adding friction is the other common response and it does not discriminate either: a longer form costs an automated applicant nothing and costs a genuine one their evening.

The design question nobody is asking is which signals are inherently costly to fake — where the cheapest way to produce a strong value is to actually be suitable.

## Why Nobody Has Built This

The response to volume has been more filtering, because filtering is what the tooling does and because each new filter works for a few weeks.

Signal design of this kind — asking which quantities are cheap for the suitable and expensive for the unsuitable — is an economic framing that has not entered recruiting product thinking, though it is standard in adjacent adversarial settings.

And generative detection has offered an apparent answer that does not work: detectors have poor accuracy, and their errors fall hardest on non-native English speakers, so deploying one at scale produces discriminatory exclusion while the sophisticated generation passes.

## What to Build

Signals selected for manipulation cost, and honest measurement of what the current filters are doing.

**Score every application signal for cost-to-fake.** Keywords: free. A generated cover letter: free. A specific claim about work someone can be asked about: cheap to write and expensive to sustain. A demonstrated artefact with a verifiable provenance: expensive. A short live conversation about the work: very expensive to fake and cheap to conduct. Ranking the signals this way is the analysis that should precede any filter decision and nobody performs it.

**Ask for things that are cheap for the suitable.** A specific question about something the candidate actually did, answerable in three sentences by someone who did it and generatable-but-fragile by someone who did not, is a far better signal than a cover letter and costs a suitable candidate two minutes.

**Verify rather than detect.** Detecting generated text is a losing arms race. Verifying a claim — the employment existed, the artefact is theirs, the credential is real — is tractable and durable, and it shifts the contest from style to substance.

**Use brief live interaction early for high-volume roles.** A five-minute structured conversation, at scale, is expensive to fake and is now cheap to conduct. It is the single most manipulation-resistant early signal available and its cost has fallen dramatically.

**Measure what the filters are actually doing.** For each filter, the volume removed and the quality of what was removed, established through the rejection audit. Most employers have never checked whether a filter removes noise or removes people.

**Accept volume and screen better rather than suppressing it.** Friction reduces volume by deterring the marginal genuine applicant, which is the wrong population. Capability extraction at volume — reading every application properly rather than filtering it — is now affordable and is the honest response to a large pile.

## Target Customer

ATS vendors, for whom volume management is now the loudest customer complaint and whose current answer is a filter arms race. Also high-volume employers, and the verification vendors, for whom claim verification is a growing market as generation makes assertion worthless.

## Impact If Built

Application signals get selected for how expensive they are to fake rather than for how easy they are to filter on. Verification replaces detection, which is the only side of that contest that can be won. And volume gets read rather than suppressed, which is now affordable and which stops filtering out the candidates whose value is not in a keyword.
