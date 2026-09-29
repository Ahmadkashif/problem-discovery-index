# What Goes Wrong Here Is Not on Any List

**Niche:** [[niches/ai-red-teaming-firms/domain-harm-taxonomies/profile|Domain Harm Taxonomies]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Generic harm categories are well established and widely published, and what actually goes wrong in a clinical triage assistant or a lending decision system is not on any of those lists.
**Tags:** #tacit-knowledge-ml #compliance #evaluation-metrics #graph-theory #descriptive-statistics #worker-facing #hypothesis-testing #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to enumerate what actually goes wrong in one regulated deployment rather than what goes wrong in general — and whoever does that takes the account, because the generic list is the part the client already has.

## The Problem
A firm assesses a clinical triage assistant against a thorough generic taxonomy and reports no critical findings. Six months later the system's real failure emerges: it gives confident, well-worded triage advice in a class of presentation where the standard of care is to escalate rather than to advise, and it does so in a way no generic category describes. A clinician on the assessment team would have named it in the first hour. The engagement did not have one, because the taxonomy did not call for one, because the taxonomy came from a published list of general harms.

## Why Nobody Has Built This
The knowledge is held by domain practitioners who are expensive, scarce and not part of a security firm's staff. Eliciting it is a structured exercise nobody has designed for this purpose. Taxonomies are treated as engagement deliverables owned by the client rather than as reusable firm assets, which prevents the second client in a sector from benefiting from the first. And a generic taxonomy is defensible in a report, which removes the pressure.

## What to Build
Build the domain taxonomy as a compounding asset. Elicit domain harms from practitioners with a structured method rather than an interview, asking what a bad outcome looks like, how it arises, what a practitioner would notice, and what the consequence is — since the tacit knowledge surfaces through cases rather than through categories, and structuring that elicitation is the substance of the build. Separate the sector-general layer from the client-specific one, so the fourth clinical engagement starts from a substantial taxonomy rather than from a published generic list. Map each domain harm to the regulatory obligations it implicates, which is what makes the taxonomy usable by the client's compliance function and is a translation only this exercise produces. Derive probes from each harm, since a taxonomy that does not generate tests is a document — this is the fix note's subject and is what turns the asset into an assessment. Include the harms that are not adversarial, because much of what goes wrong in these deployments is ordinary error in a consequential place rather than an induced failure, and an adversarial-only frame misses it. Retain practitioners on retainer per sector rather than hiring per engagement, which is how the expertise becomes available and affordable. Version the taxonomy as practice and regulation move. And publish the sector-general layers, since a firm that defines how a sector's harms are categorised holds a position no competitor can take from them.

## Target Customer
Regulated sector buyers, the assessment firms serving them, the domain practitioners whose knowledge this is, and the regulators defining what testing must cover.

## Impact If Built
A generic taxonomy examines the wrong surface competently, and a domain practitioner would name the real failure in an hour. Separating the sector-general layer from the client-specific one is what makes the expertise affordable, and mapping harms to regulatory obligations is the translation only this exercise produces.
