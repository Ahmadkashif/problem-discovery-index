# A Century of Editorial Judgment Used as Metadata Instead of Training Data

**Niche:** [[niches/small-law-firms/legal-research-content-publishers/profile|Legal Research & Practice Content Publishers]]
**Industry:** [[industries/small-law-firms|Small Law Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Attorney-editors have classified every American case into a subject taxonomy and judged how every citing case treated it, for more than a hundred years, and the result is used as search facets.
**Tags:** #transformers #large-language-models #word-embeddings #graph-neural-networks #evaluation-metrics

## The Problem
The opinions are public. Anyone can get them. What cannot be got is the layer these publishers built on top: headnotes stating the points of law a case decided, a hierarchical subject taxonomy assigning each of those points a place in a map of the whole law, and a citator in which analysts have read every citing reference and judged whether it followed, distinguished, criticised or overruled the case it cites.

That is tens of millions of expert judgments about legal meaning, made by trained attorneys, accumulated continuously since the nineteenth century, and structured. There is no comparable annotated corpus in any professional domain.

It is deployed as navigation. A researcher filters by topic, follows a citator flag, and reads. The corpus answers the question "show me documents matching this classification" and is not asked to answer "what does the law say about this situation", which is the question the researcher actually has and the question generative tools are now being pointed at.

The competitive position is what makes this urgent rather than merely interesting. Language models trained on public opinions can already produce plausible legal answers, and their characteristic failure is confident invention — a case that does not exist, a holding the case does not contain, an authority that was overruled. The publishers hold the exact asset that fixes that failure: a verified map of what each case actually held and whether it is still good law. They are competing against generative tools using it to power search facets.

## Why Nobody Has Built This
The editorial layer was designed for a print product and inherited by a database, and both were organised around retrieval. The taxonomy's structure encodes assumptions from a world where a researcher walked to a shelf, and nobody has had a reason to ask what else it could support.

Accuracy standards in this domain are also unusually unforgiving. A legal publisher whose product asserts a proposition the law does not support faces professional and commercial consequences a general search product does not, which makes the institutional instinct to ship retrieval and let the attorney draw the conclusion entirely rational — and, now, a strategic liability.

And the corpus is genuinely hard. Legal reasoning is jurisdictional, hierarchical, and time-dependent: a proposition true in one state is false in the next, and true until a date. Most machine learning on text ignores all three.

## What to Build
Retrieval and reasoning that use the editorial layer as supervision rather than as a filter.

**Treat headnotes as a supervised corpus of holdings.** Each headnote is an expert statement of what a case held, linked to the passage it came from. That is a paired dataset of source text and expert summary at a scale nothing else in law approaches, and it is exactly what is needed to build a system that states a holding without inventing one.

**Model the citation network as a graph.** Cases citing cases, with an expert label on each edge saying how it was treated. Treatment propagates — a case relying on an overruled proposition is weakened even if nothing says so directly — and that inference is a graph problem the citator's flags currently answer only one hop deep.

**Make jurisdiction and time first-class.** Every retrieved authority must carry where it binds and when it was good, and every answer must be scoped. This is the single most common failure of general models on legal questions and the publishers hold precisely the metadata to fix it.

**Ground every generated statement in a verified holding.** The defensible product is not a model that writes about law; it is a model that answers with an assertion traceable to a headnote that an attorney-editor wrote and a citator flag that an analyst assigned. The hallucination problem is solved by construction rather than by hope.

**Use the taxonomy as evaluation, not just as structure.** The classification hierarchy gives a ready-made test set: does the system retrieve the authorities a human classifier assigned to this point of law? That is a real benchmark, computable today, that no competitor without the taxonomy can even run.

## Target Customer
Chief Content Officer or Chief Technology Officer at a legal research publisher. The strategic argument writes itself: the public half of the asset is now free, and the private half is the only defensible half.

## Impact If Built
Legal research is a large fixed cost on every small firm in the country and the point at which artificial intelligence is arriving in legal practice fastest and least safely. A system whose every assertion is grounded in a verified holding with a current treatment flag is the difference between a tool a small firm can rely on and one that produces a citation to a case that never existed.
