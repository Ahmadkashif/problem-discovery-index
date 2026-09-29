# Build: An Integration That Carries the Context

**Niche:** [[niches/talent-assessment-platforms/ats-integration/profile|ATS Integration & Score Plumbing]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Carry the interval, the instrument version, the administration quality and the accommodation status alongside the score, and retain them into the employee record.
**Tags:** #data-integration #compliance #workflow-orchestration #confidence-intervals #evaluation-metrics #descriptive-statistics #automation #worker-facing
**Contested on:** Whether an integration's field list will be specified by what the decision requires rather than by what is easy.

## The Problem

The integration between the assessment platform and the applicant tracking system is where a measured quantity becomes a decision input, and it is specified as a number.

Everything that governs how the number should be used is dropped at that boundary. The standard error, without which the recruiter cannot know what distinctions are real. The instrument and version, without which no later validation is possible. The validated range, without which nobody knows the score is being used for a role it was not built for. The administration quality, without which a compromised session looks like a low score. The accommodation status, which matters for interpretation and for the legal record.

So the guardrails the assessment platform could provide stay on the assessment platform, and the decision is made in the applicant tracking system from a bare figure.

## Why Nobody Has Built This

The integration was scoped to the minimum that makes the workflow function: trigger the assessment, get the score back, advance or reject. Everything beyond that is a field nobody requested.

The applicant tracking systems also have limited fields for assessment data and the vendors build to what is available rather than asking for more, which has left the effective standard at one number.

And the parties who would benefit — the recruiter who would interpret better, the analyst who would validate later, the candidate who would be treated more carefully — were not in the integration's requirements conversation.

## What to Build

A richer payload and a retention path.

**Specify the field set from the decision.** Score, standard error, band, instrument identifier and version, validated range flags, administration quality indicators, accommodation status, completion time and date. Each of these exists on the assessment side and each changes how the score should be used.

**Render it in the applicant tracking system properly.** Not additional columns but a presentation — the interval shown, the band primary, warnings surfaced where the score is outside the validated range. This requires the ATS vendors to build a view, which is a partnership rather than a field mapping, and it is where the interpretation guardrails actually land.

**Carry warnings as first-class objects.** Out-of-validated-range, compromised administration, boundary-band candidate. These should arrive as flags the recruiter cannot avoid seeing, not as data buried in a detail pane.

**Write the score to the employee record at hire.** The single most consequential field in this niche, because it is what makes every future validation possible. Instrument, version, score and date, retained under a defined purpose limitation and excluded from operational visibility to managers.

**Retain the unselected distribution.** Scores for candidates not hired, under appropriate retention and consent, because range restriction correction is impossible without them and every future validation is weaker.

**Version everything.** Instruments change, cut scores change, configurations change. A score with no version is uninterpretable eighteen months later, which is exactly when the validation happens.

**Standardise it.** A common field set across vendors and applicant tracking systems is worth more than any one integration, and the HR data standards bodies are the natural home for it.

## Target Customer

Assessment vendors and applicant tracking system vendors jointly, since neither can do it alone. Also large employers' HR technology teams, who specify integrations and are the party who will later want to validate and find the data was never carried.

## Impact If Built

The score arrives with the context that governs its use, so the guardrails reach the person making the decision. The instrument version and the unselected distribution get retained, which makes local validation possible for the first time. And the field list — which is effectively the specification for how the score gets used — gets written deliberately rather than minimally.
