# Relevance Learned From the Archive

**Niche:** [[niches/newsletter-media/editorial-research-and-sourcing/profile|Editorial Research & Sourcing]]
**Industry:** [[industries/newsletter-media|Newsletter Media]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** What this audience cares about is fully documented in what the publication has covered and what readers clicked, and the morning's filtering uses none of it.
**Tags:** #bert #transformers #word-embeddings #gradient-boosting #evaluation-metrics #confidence-intervals #k-nearest-neighbors #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to surface what is genuinely new and genuinely relevant to one specific audience from a stable source set — and whoever learns relevance from the publication's own archive replaces the hours that precede every issue.

## The Problem
Generic news filtering is useless here because the question is not what is important but what is important to this audience — a distinction that is entirely legible in the publication's history. Every issue is a labelled example of what was worth including, and every engagement measurement is a labelled example of what readers actually wanted. The writer performs the filtering manually anyway, because no tool knows the publication.

## Why Nobody Has Built This
Monitoring products are built to be general, so they filter for broad newsworthiness rather than for one publication's specific relevance — a product sold to many customers cannot afford to learn any of them deeply. The archive is unstructured and was never treated as training data. Engagement outcomes sit in the sending platform. And the writer's relevance judgement is tacit and nobody attempted to capture it.

## What to Build
Learn this publication's relevance function. Train relevance on the archive — what was covered, how prominently, and what readers engaged with — which is the core and is the only thing that distinguishes this from a feed reader. Rank incoming candidates rather than filtering them, since a ranked list with the writer deciding is usable and an automatic filter is not. Check novelty against the archive, because a substantial share of what looks new is a restatement. Cluster the same story across sources, as the same event arriving eleven times is most of the morning's volume. Surface the primary source rather than the coverage, since the writer will go there anyway and finding it is a step. Learn from the writer's own selections continuously, so the ranking improves with use rather than requiring configuration. Retain the rejected candidates, because they recur and the decision not to use something is a label too. Review source coverage periodically, as sources go stale and new ones appear and nobody audits the list. Feed engagement outcomes back, since what readers clicked is the strongest relevance signal available. And preserve the writer's authority over selection completely, because the judgement is the product and automating it away would destroy what readers subscribe to.

## Target Customer
Editorial leadership and writers, newsletter platforms, media monitoring vendors selling general relevance, and media companies operating multiple titles.

## Impact If Built
A product sold to many customers cannot afford to learn any of them deeply, so monitoring filters for general newsworthiness. The archive and its engagement record are a precise, labelled definition of this audience's relevance and nothing uses them.
