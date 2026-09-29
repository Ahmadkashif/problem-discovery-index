# Nobody Knows Why It Cites What It Cites

**Niche:** [[niches/seo-tooling-vendors/entity-and-citation-optimisation/profile|Entity & Citation Optimisation]]
**Industry:** [[industries/seo-tooling-vendors|SEO Tooling Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Getting cited in a generated answer is the new objective and the advice being sold for it is a decade of ranking folklore with the nouns changed.
**Tags:** #large-language-models #transformers #graph-theory #contrastive-learning #evaluation-metrics #hypothesis-testing #confidence-intervals #word-embeddings
**Contested on:** Every serious competitor in this niche is fighting to work out what makes a generated answer cite one source rather than another — and whoever establishes that gets to sell the practice that replaces a twenty-year-old one.

## The Problem
A brand wants to appear in generated answers about their category. Their agency advises them to add structured data, build authoritative backlinks, write comprehensive content and use clear headings — which is the ranking advice of the last decade, offered because it is what the profession knows. Whether any of it affects citation is unestablished. The actual mechanism involves what the underlying model learned about the entity during training, what gets retrieved at answer time, how the source is written and structured, and how the entity is described across the web generally. Almost none of that is addressed by the advice being sold.

## Why Nobody Has Built This
The signal is unobservable and the systems are closed, so the profession fell back on analogy — which is a reasonable first response and a poor permanent one. Establishing what works requires controlled experimentation that nobody is set up to run. The old practice is profitable and relabelling it is easier than replacing it. And the answer probably differs across answer systems, which makes a single tidy practice unavailable.

## What to Build
Replace folklore with evidence. Build a corpus of observed citations at scale — which sources are cited, for which questions, alongside their characteristics — which is the evidence base and is exactly what the measurement sub-niche's sampling produces as a by-product. Separate the mechanisms, since what the model knows from training and what is retrieved at answer time respond to entirely different interventions and conflating them is why current advice is useless. Model entity representation across the web rather than page optimisation, because the unit is increasingly the entity rather than the document and this is the genuine conceptual shift. Test interventions properly with controlled changes and measured effects, which nobody is doing and which is the only route to a defensible practice. Examine source structure empirically — passage clarity, factual density, attribution, recency, format — rather than assuming the ranking heuristics carry over. Handle the several answer systems separately, since their retrieval and training differ and a blended recommendation serves none of them. Address what the model gets wrong about an entity, which is the fix note's subject and is a more urgent problem for most brands than citation frequency. Build the feedback loop from measurement to intervention to remeasurement, which is what turns advice into a practice. Publish findings openly, because credibility in a folklore market is the whole differentiator. And state uncertainty honestly, since the field is young and a confident practice built on nothing will collapse publicly.

## Target Customer
Brand and content teams, SEO agencies whose practice is being deprecated, and tooling vendors seeking the layer above measurement.

## Impact If Built
The profession fell back on analogy because the signal is unobservable, and is selling a decade of ranking advice with the nouns changed. Separating what the model knows from what it retrieves is the distinction that makes any intervention meaningful.
