# Sourcing, Search and Application Volume

**Industry:** [[recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Applications per opening have risen sharply and both sides are now using generative tooling, so a keyword-matched pile has become a larger keyword-matched pile.
**Tags:** #bert #contrastive-learning #word-embeddings #large-language-models #graph-neural-networks #k-nearest-neighbors #evaluation-metrics #dimensionality-reduction

## The Problem
The volume of applications per opening has grown substantially, driven by frictionless application mechanisms and more recently by generative tools that make a tailored application cheap to produce. Recruiters cannot read them all, so they filter.

The filters are keyword-based in practice whatever the marketing says: required terms, years of experience, titles, institutions. Those proxies systematically exclude career changers, people whose experience is described in different vocabulary, candidates from adjacent industries and anyone whose background does not narrate conventionally — which is a large fraction of the people who would do the job well.

Generative tooling has broken the remaining signal on both sides. Applications are now polished uniformly, so writing quality no longer distinguishes; job descriptions are generated too, so the requirements listed are increasingly boilerplate rather than a considered statement of what the role needs. Both sides are optimising against each other's automation.

Sourcing has the mirror problem. Searching profile databases by title and keyword surfaces the same visible candidates to every recruiter simultaneously, which is why in-demand profiles receive dozens of near-identical messages and everyone else receives none.

## What Already Exists
Applicant tracking systems provide search and filtering. Sourcing platforms — LinkedIn Recruiter, SeekOut, hireEZ — offer boolean and increasingly semantic search across large profile databases. Matching and ranking features are built into most systems. Skills taxonomies from Lightcast and the vendors' own ontologies attempt to normalise vocabulary. Some systems support structured skills assessment integrated into the funnel.

## The Customisation Gap
Representing capability rather than vocabulary is the technical gap. What someone has demonstrably done — the shape of the work, the systems involved, the problems solved — can be represented in a way that matches across different descriptions of the same thing, which is precisely what keyword matching cannot do and is where the excluded candidates are.

Equivalence across career shapes is the harder and more valuable part. Recognising that a particular non-linear background provides the capability a role requires is the judgement a good recruiter makes and a filter cannot, and it is learnable only if there is some evidence about outcomes — which returns to the validation problem and means it must be built with honest uncertainty rather than a confident score.

Requirements need deflating. Job descriptions routinely list requirements the role does not have, which shapes who applies before any filter runs, and comparing listed requirements against what post-hire evidence says actually mattered is a straightforward analysis that would change the top of the funnel more than any ranking improvement.

And the scarcity problem needs addressing on the sourcing side. Surfacing the same visible candidates to everyone is a ranking design choice, and diversifying what a search returns — including well-matched candidates who are not already saturated — serves both recruiters and candidates and is against no one's interest except the illusion of a definitive ranking.

## Impact If Solved
Volume has outpaced human review and the filters that absorb it exclude by vocabulary rather than by capability, which is a systematic and invisible loss for both sides. Capability-based representation reaches candidates that keyword filters never surface, requirement deflation changes who applies at all, and sourcing diversity addresses a saturation dynamic that wastes recruiter effort and candidate goodwill simultaneously.
