# Build: Reporting That Lands Where It Can Be Acted On

**Niche:** Finished Intelligence Reporting
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Assessments matched against each customer's actual environment, with the technical content extracted into implementable artefacts and delivered to the person who can use them.
**Tags:** #bert #large-language-models #word-embeddings #graph-theory #evaluation-metrics #confidence-intervals #automation #data-integration
**Contested on:** Whether a finished assessment reaches the person who can act on it in a form they can act on.

## The Problem

A report describes a campaign: the adversary, their targeting, the initial access vector, the malware, the infrastructure, the post-exploitation behaviour. It is twenty pages, well sourced and genuinely good.

For it to matter, two things must happen. Somebody at the customer must read it and recognise that it applies to them. And somebody must convert its technical content into something operational — detections for the described behaviours, blocks for the infrastructure, a hunt for prior activity, a patch for the exploited software.

Both steps are left to the customer and both are expensive. The first requires knowing whether the organisation runs the affected software, operates in the targeted sector, and has the described exposure — which is a comparison between the report and the environment that nobody performs. The second requires a detection engineer to read prose and write rules, which takes hours per report and is done for a small fraction of what arrives.

So the analytical work that took a week produces value only where a customer happened to have the capacity to consume it properly, which is a minority of subscribers.

The vendor could do both steps. They know what the report describes. With even coarse knowledge of the customer's environment they could assess relevance. And the technical content could be emitted as structured detections rather than as prose requiring translation.

## Why Nobody Has Built This

**The product is conceived as a document.** Intelligence reporting inherits a tradition of written assessment, and the deliverable is the report. Extracting it into operational artefacts feels like a different product.

**Relevance requires environment knowledge.** Assessing whether a report applies needs the customer's stack, exposure and sector at a granularity most vendors do not have and many customers will not share.

**Detection extraction is not the analyst's skill.** The person who wrote the assessment is an intelligence analyst, not a detection engineer, and producing tested rules is a different discipline requiring different people.

**Rules are environment-specific.** A detection that works in one organisation's logging configuration fails in another's. Generic rules require tuning, which pushes work back to the customer and limits how far the extraction can go.

**Nobody measures consumption.** Without knowing which reports were read or acted on, there is no signal telling a vendor that targeting and extraction would help.

**Broad distribution looks like value.** Sending everything to everyone produces a large content volume that appears in the subscription's value proposition.

## What to Build

**Assess relevance per customer.** Match the report's subject — affected software, targeted sectors, geographies, techniques — against what is known of the customer's environment, from telemetry, attack surface data or a declared profile. Deliver with a stated relevance and a reason, so the customer's first question is answered before they open it.

**Check the report against the customer's own telemetry.** Do the described indicators appear in their logs? Have the described techniques been seen? This converts a report about a campaign into a statement about whether that campaign has touched this organisation, which is a completely different product.

**Emit structured detections alongside the prose.** Behaviours described in the report expressed as detection logic in a portable format, with the caveats about environmental tuning stated. Imperfect rules that a detection engineer can adapt are worth far more than prose they must translate from scratch.

**Produce the hunt package.** Queries the customer can run against historical telemetry to check for prior activity. This is the highest-value operational output of most campaign reports and is almost never supplied.

**Route by role.** The strategic summary to the security leader, the technical detail and detections to detection engineering, the infrastructure to the blocking pipeline. Same analysis, different artefacts, delivered to the person who acts on each.

**Track what happened.** Whether the detections were deployed, whether the hunt ran, whether it found anything. This is the feedback loop that would tell the analyst their work mattered and the vendor which reporting is worth producing.

**Prioritise ruthlessly.** A small number of highly relevant, environment-checked reports is worth more than a large library. A vendor confident enough to send less would be making a quality claim.

## Target Customer

Detection engineering teams, who are the people who actually operationalise finished reporting and currently receive it in the least usable form.

Security leadership at organisations without a dedicated intelligence function, which is most of them — they buy reporting and lack the capacity to consume it, and the extraction is exactly what they need.

Vendors with telemetry, who can perform the environment check and for whom it is a differentiator no pure-play competitor can match.

## Impact If Built

Reporting reaches the person who can act on it in the form they need, rather than reaching a portal and waiting to be discovered by someone with spare capacity.

Checking a report against the customer's own telemetry turns a general assessment into a specific finding about that organisation, which is a categorically more valuable product.

And emitting detections and hunt queries alongside the prose removes the translation step that currently limits how much reporting any customer can actually use.
