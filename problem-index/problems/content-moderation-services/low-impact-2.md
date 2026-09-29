# Coverage in Languages Nobody Built For

**Industry:** [[content-moderation-services|Content Moderation Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Classifier performance and reviewer availability are both worst in the languages where the platform's growth is fastest and the offline consequences of failure are most severe.
**Tags:** #transfer-learning #bert #transformers #large-language-models #contrastive-learning #evaluation-metrics #compliance #confidence-intervals

## The Problem
Automated classification works considerably better in English and a handful of other high-resource languages than in the hundreds of languages that make up most of the world's online population. That performance gap has been documented repeatedly — by researchers, by regulators and in disclosures about the platforms themselves — and it means the automated first line is weakest exactly where it is most needed.

Human coverage has the same shape. Reviewer recruitment in a given language and dialect depends on the labour market where that language is spoken, and the vendors' delivery centres are concentrated in a small number of countries. Languages with large online populations and small pools of available reviewers are chronically under-resourced, and the reviewers who do cover them handle a wider category range with less specialisation.

The consequences are not symmetric with the resourcing. The situations where moderation failure has the most serious offline consequences — organised incitement, coordinated harassment campaigns, content connected to communal violence — have repeatedly occurred in exactly these markets, and have been the subject of public findings.

Dialect, code-switching and local context make it harder still. Content mixing languages, using local slang, or referring to events a reviewer in another country would not recognise requires knowledge that neither the classifier nor a generically-trained reviewer has.

## What Already Exists
Multilingual models have improved substantially and transfer to lower-resource languages better than earlier generations. Platforms publish language coverage commitments of varying specificity. Vendors operate delivery centres across many countries and recruit for language capability. Translation is used as a fallback and degrades badly on slang, dialect and context-dependent meaning. Regional expertise exists in specialist civil society organisations and is consulted inconsistently.

## The Customisation Gap
Transfer is the technical opportunity and it needs honest measurement per language rather than an aggregate multilingual score. A model performing well on average across fifty languages may be unusable in fifteen of them, and reporting the aggregate is how the gap stays invisible. Per-language precision and recall on locally-labelled data is the requirement, and creating that labelled data is the actual work.

Local context is the part no model supplies. Whether a phrase is a threat depends on who is saying it to whom in what situation, and in markets with active conflict that knowledge sits with people in the region. Building it into the operation — through regional expert panels, local civil society input, and escalation paths staffed by people with the context — is an operational design question that technology supports rather than solves.

Reviewer support in low-resource languages is where the gap can be closed fastest. A reviewer working across many categories in an under-resourced language benefits most from precedent retrieval, from translation assistance that flags where it is unreliable, and from the ability to escalate to someone with regional knowledge.

And the resourcing decision itself should be evidence-based. Where coverage is thinnest relative to volume and risk is computable, and it is currently set by contract negotiation and labour market availability.

## Impact If Solved
The moderation gap in lower-resource languages is one of the most consequential known failures in this field and has been connected in public findings to serious offline harm. Per-language performance measurement rather than aggregate scores, locally-grounded escalation paths, and decision support targeted at the reviewers working with the least automated assistance address it at the points where it is actually addressable — which is not a model improvement alone.
