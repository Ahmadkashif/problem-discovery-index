# Buy: Analyst Support From Security Operations

**Niche:** The Triage Analyst
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Security operations centres built alert triage tooling — enrichment, case management, playbooks, similar-incident retrieval — for analysts doing structurally the same job with better support.
**Tags:** #bert #large-language-models #gradient-boosting #evaluation-metrics #word-embeddings #workflow-orchestration #worker-facing
**Contested on:** Whether the person reading the queue is supported as a specialist making consequential judgements, or measured as a throughput worker.

## The Problem

A security operations analyst and a bounty triage analyst do recognisably the same job: work a queue of mostly-false signals, determine quickly which are real, escalate the ones that matter, and carry the consequence of missing something.

Security operations has spent fifteen years building tooling for this. Alerts arrive enriched with context automatically gathered from a dozen sources. Similar prior incidents are surfaced. Playbooks structure the investigation. Case management holds the evidence. Automation handles the repetitive gathering steps. Analyst performance is reviewed, and the industry talks openly about alert fatigue as an operational problem to be engineered against.

Bounty triage has a queue, a text box and a clock. The submission arrives as prose and the analyst gathers everything themselves.

## What Already Exists

Security orchestration and response: Splunk SOAR, Palo Alto XSOAR, Tines, Torq and Swimlane, with playbook automation, enrichment, case management and integration across the security stack.

SIEM and detection platforms: alert triage interfaces with context, similar-alert clustering and investigation workflows.

Threat intelligence platforms: automated enrichment of indicators, which is the enrichment pattern this problem needs applied to a different object.

Incident response: case management with evidence handling and timeline reconstruction.

Adjacent queue work: content moderation tooling, covered in [[industries/content-moderation-services|Content Moderation Services]], which handles adversarial high-volume queues with pre-classification and confidence-banded routing.

## The Customization Gap

**Enrichment has a different object.** SOAR enriches indicators — addresses, hashes, domains — from threat intelligence. Bounty triage needs enrichment of a claimed vulnerability: what is this asset, what is its exposure, what has been reported against it before, what does the programme's history say about this finding class. Same pattern, different sources, and nobody has assembled them.

**Playbooks transfer almost directly.** A structured investigation path per finding class — for an authorisation claim, check these things in this order — is exactly what SOAR playbooks are, and triage currently relies on each analyst's personal habit.

**The input is prose, not structured data.** SOAR consumes machine-generated alerts with fields. Bounty submissions are human narrative, so an extraction layer is needed before any playbook can run. This is the main adaptation and it is now tractable.

**Automation must assist, never close.** SOAR playbooks auto-resolve low-risk alerts. Here the failure cost makes auto-closure unacceptable, so the same machinery has to be used to prepare and present rather than to decide.

**Alert fatigue is a named problem there and unnamed here.** Security operations talks openly about analyst fatigue, measures it, and designs against it. Bounty triage has the same dynamic — high volume, low base rate, consequential misses — and no equivalent discourse.

**Case management is thinner than it should be.** SOAR holds evidence, timeline and decision rationale. Bounty triage records a state change and a canned response, which is why nothing can be re-examined later and why the wrongly-closed rate is unmeasurable.

## Target Customer

The bounty platforms, adopting SOAR patterns rather than SOAR products — the enrichment and playbook concepts transfer, the specific integrations do not.

Tines or Torq are plausible direct adapters given their general-purpose automation positioning and existing security customer base, for whom bounty triage is an adjacent workflow.

Programme managers running in-house triage inside a security team that already owns a SOAR platform are the most immediately reachable buyers, since the tooling is already there.

## Impact If Solved

Automatic enrichment would put the context an analyst currently gathers by hand in front of them before they start, which is the pattern that made security operations triage tractable at volume.

Playbooks per finding class would make investigation consistent across analysts, which directly addresses the variance that no operation currently measures.

And proper case management would make closed submissions re-examinable, which is the precondition for measuring the error that matters and for the incident-time lookback that should be standard.
