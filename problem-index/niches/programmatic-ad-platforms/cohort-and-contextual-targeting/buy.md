# Document Understanding Practice

**Niche:** [[niches/programmatic-ad-platforms/cohort-and-contextual-targeting/profile|Cohort & Contextual Targeting]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Understanding what a document is about is among the best-solved problems in applied machine learning, and contextual advertising still runs on keyword lists.
**Tags:** #bert #transformers #large-language-models #transfer-learning #evaluation-metrics #dimensionality-reduction #confidence-intervals #automation
**Contested on:** Every serious competitor in this niche is fighting to bid well on an impression where nothing about the person is known — and whoever extracts the most from the page, the moment and the aggregate wins the majority of inventory that is no longer addressable.

## The Problem
Topic classification, sentiment, stance detection, entity recognition, summarisation and semantic representation of text are all mature, cheap and available as commodity models. Any competent team can build a system that understands what a web page is about far better than a keyword list does, and many industries have. Contextual advertising — the one application where document understanding directly determines billions in spend allocation — is still predominantly served by taxonomy matching and negative keywords.

## What Already Exists
Pre-trained language models for classification and representation; entity and topic extraction; sentiment and stance detection; document embedding and semantic retrieval; and multilingual coverage as standard.

## The Customization Gap
The adaptation is to billions of URLs at bid latency with an advertising-specific notion of relevance. It requires: (1) precomputation and caching across a constantly changing corpus, since inference cannot happen inside the bid and the URL may be new — this pipeline is the real engineering work and is what has actually blocked adoption; (2) commercial adjacency rather than topical similarity as the target, because the useful question is whether this page's reader is receptive to this advertiser, which is not what any pre-trained model was trained for; (3) brand suitability as a graded, advertiser-specific judgement rather than a universal safety label, which no general classifier produces; (4) supervision from outcomes rather than from human labels, since what makes a page valuable is ultimately an empirical question and labelled contextual relevance is a proxy; and (5) resistance to gaming, as publishers whose inventory is priced by page understanding will optimise their pages against it — an adversarial dynamic absent from ordinary document classification.

## Target Customer
Demand-side platforms, contextual intelligence vendors, publishers, and language model vendors for whom advertising context is an unserved application.

## Impact If Solved
Document understanding is commodity and the one application where it allocates billions still uses keyword lists. Precomputation across a changing corpus is the blocking engineering work, and commercial adjacency rather than topical similarity is the target no pre-trained model was built for.
