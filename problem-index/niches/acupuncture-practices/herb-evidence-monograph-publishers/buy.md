# Literature Surveillance Adapted to Botanical Synonymy

**Niche:** [[niches/acupuncture-practices/herb-evidence-monograph-publishers/profile|Herb & Supplement Evidence Monograph Publishers]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Systematic review screening software is mature and cheap, but none of it knows that Scutellaria baicalensis, Huang Qin, Chinese skullcap, and baicalin are the same surveillance target.
**Tags:** #bert #transformers #transfer-learning #word-embeddings #contrastive-learning #evaluation-metrics #automation #data-integration #workflow-orchestration

## The Problem
Monograph currency depends on catching every relevant publication, and the retrieval step is where the loss happens. A researcher maintaining coverage of several hundred botanicals runs saved searches across the biomedical databases and a set of regional sources, then screens the returns. The searches are hand-built and hand-maintained, each one a long disjunction of synonyms someone assembled years ago. When a new extract trade name enters the literature, or a Chinese-language journal indexes a formula under a transliteration nobody anticipated, the search simply returns nothing and no one knows. Recall failures are invisible by construction — the only way anyone discovers a missed trial is when a subscriber or a competitor cites it.

## What Already Exists
The systematic review tooling market is well developed and inexpensive. Covidence, Rayyan, DistillerSR, and EPPI-Reviewer all provide reference deduplication, dual screening with conflict resolution, active-learning prioritization that surfaces likely-includes first, and full audit trails. They are built for a review team working a defined protocol to a defined end, and at that job they are good.

## The Customization Gap
Two mismatches make them a poor fit here. First, they assume a bounded project with a closing date, whereas monograph maintenance is a standing surveillance obligation with no end — there is no "screening complete," only a corpus that is more or less current. Second, and more damaging, their entity handling is generic. They treat search terms as strings, so the botanical synonymy problem passes straight through untouched; a tool that deduplicates references perfectly still never sees the paper the search failed to retrieve. What the workflow needs is an entity layer that treats each botanical as a resolved concept with all its binomials, pinyin and common names, retired synonyms, constituent compounds, and commercial extract designations attached, and that proposes new surface forms as they appear in the literature. Layered on top of that, standing surveillance with active-learning triage and explicit recall estimation — a running answer to "what fraction of relevant publications are we catching" rather than silence.

## Target Customer
Research directors and senior editors responsible for corpus currency, and the medical librarians who build and maintain the saved searches that everything downstream depends on.

## Impact If Solved
Moves recall from an article of faith to a measured quantity. New surface forms get caught when they enter the literature rather than years later, which closes the specific failure mode that most damages a subscription product: the subscriber finding the gap first. The synonym layer, once built, is reusable across every product the publisher runs and is itself a saleable asset to anyone doing botanical literature work.
