# The Case That Was Solved Last Year

**Niche:** [[niches/customer-support-platforms/b2b-technical-support/profile|B2B & Technical Support]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A technical support organisation has solved nearly every problem it receives before, the resolutions are in the case history, and finding the prior case depends on an engineer guessing the words somebody else used to describe the same failure.
**Tags:** #bert #contrastive-learning #k-nearest-neighbors #large-language-models #evaluation-metrics #confidence-intervals #automation #tacit-knowledge-ml
**Contested on:** Every serious competitor in technical support software is fighting to make an escalation carry enough for the next person to diagnose without going back to the customer — and whoever makes escalations self-sufficient takes the account.

## The Problem
An engineer works a case for three days and determines that a particular interaction between a configuration setting and a version upgrade produces the failure. Eight months earlier a colleague diagnosed the same thing for a different customer and documented it in the case notes. The current engineer searched, using the words the customer used, and found nothing — because the earlier case was described in entirely different language by a different customer with a different symptom. The organisation solved the same problem twice at a cost of three days and has probably solved it four times.

## Why It's Still Broken
Case search is keyword search over text written by different people describing the same underlying fault in incompatible ways, which is exactly the retrieval problem that semantic search solves and which support platforms have been slow to adopt for historical cases. Documentation quality in case notes is variable because engineers write them at the end of a long case for nobody in particular. And converting a resolved case into knowledge is a manual step that competes with the next case and always loses.

## What a Fix Looks Like
Match on the failure rather than on the words. Cases are indexed on their technical signature — error messages, stack traces, log patterns, product version, configuration attributes and the resolution applied — in addition to their text, so similarity is computed on what actually failed rather than on how it was described. Surface similar prior cases automatically when a case is created, before an engineer searches, which is the intervention point. Cluster resolved cases to identify recurring issues that have been solved repeatedly without ever being turned into a knowledge article or a product fix — which is a list every technical support organisation would find uncomfortable and immediately valuable. Prompt for a short structured resolution at case close: what the cause was, what resolved it, what would prevent it, which is a minute of an engineer's time and is the difference between a searchable case and a thread. And feed the recurring clusters to the product organisation, which is the connection this industry's last niche is about and which technical support feels most acutely.

## Who Feels the Pain
Engineers rediscovering diagnoses their colleagues made; customers waiting three days for an answer the organisation already had; and product teams unaware that a particular interaction has generated forty cases.

## Impact If Fixed
Signature-based case similarity surfaced at creation is a substantial and immediate reduction in diagnostic time, and the recurring-cluster analysis identifies both the knowledge articles that should exist and the product defects that should be fixed. The structured close prompt is a minute per case and is what makes the whole corpus usable rather than merely stored.
