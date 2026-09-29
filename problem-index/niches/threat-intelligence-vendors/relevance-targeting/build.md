# Build: Relevance From the Customer's Real Exposure

**Niche:** Relevance & Customer Targeting
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Assess relevance by matching the threat's actual characteristics against the customer's observed technology, exposure and supply chain rather than against a sector label.
**Tags:** #graph-theory #gradient-boosting #k-nearest-neighbors #evaluation-metrics #confidence-intervals #bert #data-integration #automation
**Contested on:** Whether relevance is assessed against what the customer actually runs and faces, or approximated by a sector label.

## The Problem

An adversary group targets organisations running a particular remote access product, in a handful of countries, in industries with a specific characteristic. A report describes them and is tagged with three sectors.

A customer in one of those sectors receives it. They do not run the affected product. They have no presence in the relevant countries. The report is irrelevant to them and arrives identically to one describing a campaign against their exact stack.

Meanwhile a customer in a different sector, who does run the product and does operate in those countries, receives nothing, because the sector tag did not include them.

The information to do this properly exists on both sides. The threat's characteristics are in the vendor's own reporting — the exploited software, the targeted geographies, the initial access vector. The customer's exposure is substantially observable: attack surface scanning reveals what they expose, technology fingerprinting reveals much of what they run, and public records reveal their footprint and supply chain.

Nobody matches the two. The vendor tags by sector because sector is what they capture about the customer, and the customer filters by hand because the tag does not tell them anything.

## Why Nobody Has Built This

**Customer environment data is not collected.** Vendors capture a sector and a size at onboarding. Assessing relevance requires knowing what the customer runs, which means either observation or a technology profile most customers have never been asked for.

**Observation raises questions.** Scanning a customer's external attack surface to improve their targeting is technically straightforward and requires explicit permission and a clear explanation, which is a conversation nobody has structured.

**Threat characteristics are prose.** Targeting patterns live in report narrative rather than as structured attributes, so matching requires extracting them first — which is now tractable and has not been done.

**Better targeting means sending less.** A vendor filtering aggressively delivers a smaller subscription, which looks worse in a comparison built on volume.

**Getting relevance wrong is asymmetric.** Failing to send something that mattered is worse than sending noise, which pushes every vendor toward broad distribution.

**Nobody measures whether the tagging was right.** Without feedback on relevance, the tags cannot improve, so they stay coarse indefinitely.

## What to Build

**Build a structured customer exposure profile.** Technology stack, exposed services, geographic footprint, supply chain dependencies, business characteristics. Derived from attack surface observation with permission, enriched by declaration, maintained continuously rather than captured once.

**Extract threat characteristics as structured attributes.** Which software, which versions, which techniques, which geographies, which organisational characteristics — pulled from the vendor's own reporting into a matchable form. This is the enabling step and it is a text extraction problem over the vendor's own corpus.

**Match and score.** Relevance as a computed score with a stated reason: you run this software, you expose this service, this adversary targets organisations with this characteristic. The reason matters more than the score, because it lets the customer judge whether the assessment is right.

**Model supply chain exposure.** A threat targeting a customer's critical supplier is highly relevant and is invisible to sector tagging entirely. This is where a meaningful share of real risk lives and no relevance model touches it.

**Use observed match behaviour as a signal.** Which threats have historically produced activity at organisations resembling this customer is a strong empirical relevance indicator and is available to any vendor with telemetry.

**Let the customer correct it.** A simple relevant-or-not signal on delivered content, feeding back into the model. This is the feedback loop that makes targeting improve and it costs the customer one click.

**Report what was filtered.** Relevance filtering is only acceptable if the customer can see what was withheld and why, and override it. This addresses the missed-threat concern directly and is what makes aggressive filtering safe to offer.

## Target Customer

Mid-sized organisations without dedicated intelligence functions, who receive the same volume as a large enterprise with a fraction of the capacity to filter it — the group for whom relevance is the difference between a useful subscription and an ignored one.

Vendors with attack surface or telemetry capability, for whom the exposure profile is obtainable and relevance becomes a differentiator.

Attack surface management vendors as adapters from the other direction, since they already hold the exposure half and lack the threat half.

## Impact If Built

Relevance becomes a computed match between what the threat requires and what the customer has, rather than a bucket label that contains organisations with nothing in common.

Stating the reason alongside the score is what would make customers trust the filtering, and it is the difference between a black-box relevance number and an assessment they can check.

And modelling supply chain exposure would surface the threats to critical suppliers, which represent real risk to the customer and are entirely invisible to every relevance model in use today.
