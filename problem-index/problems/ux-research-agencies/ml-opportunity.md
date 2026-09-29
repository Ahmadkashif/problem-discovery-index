# Machine Learning Opportunities — UX Research Agencies

**Industry:** [[ux-research-agencies|UX Research Agencies]]
**Derived from:** [[problems/ux-research-agencies/high-impact|High Impact]], [[problems/ux-research-agencies/low-impact-1|Low Impact 1]], [[problems/ux-research-agencies/low-impact-2|Low Impact 2]], [[problems/ux-research-agencies/worker-life-1|Worker Life 1]], [[problems/ux-research-agencies/worker-life-2|Worker Life 2]]

---

## 1. Finding Accuracy Tracking and Qualitative Base Rates
#hypothesis-testing #bayesian-inference #confidence-intervals #causal-inference #evaluation-metrics #probability-distributions #descriptive-statistics #tacit-knowledge-ml

**Problem statement:** Research produces testable predictions about behaviour at scale from studies of a handful of people, and nobody ever checks them. The discipline's central heuristics about sample size and what qualitative work can claim rest on decades-old work and have been argued ever since without new evidence.

**ML task:** Match recorded findings, stated as falsifiable predictions, against subsequent behavioural outcomes, and estimate base rates linking qualitative finding characteristics to observed effects
**Input data:** Findings recorded as predictions with their support characteristics — participant count, observed versus reported, severity rating; the product change actually shipped and when; post-release behavioural metrics for the relevant surface; the confounding releases in the window; study population and product context.
**Target:** Whether the predicted behavioural effect appeared, and at what magnitude.
**Evaluation metric:** The output is a base rate, not a classifier, so the question is the precision of the estimate: how often does a severe finding from an eight-participant study correspond to a measurable effect, with an interval. Report separately by finding type, because severe usability problems and generalisations about preference have entirely different expected hit rates and pooling them produces a number that describes neither — which is precisely the conflation the discipline's summaries currently make.
**Scope:** Attribution is the hard part: recommendations are implemented partially, in altered form, alongside other changes. The honest design restricts the corpus to findings whose implementation can be identified cleanly and reports how many were excluded for that reason. This needs many studies across many clients, so only an agency or a platform can build it. 1 data scientist plus a research lead, 12 months.
**Data availability:** Requires a contracted look-back window and access to client analytics. Neither exists today and both are negotiable.

---

## 2. Participant Validity From Behaviour and Account Structure
#gradient-boosting #dbscan #graph-neural-networks #k-means-clustering #bert #evaluation-metrics #feature-engineering #compliance

**Problem statement:** Screening asks people to describe themselves and the incentive rewards describing themselves as whatever qualifies. Professional participants, duplicate accounts and — in unmoderated studies — assisted responses corrupt findings invisibly.

**ML task:** Score participant and response validity from behavioural, relational and device signals rather than from declarations, with population-specific thresholds
**Input data:** Screener response timing and patterns; a participant's claimed attributes across their study history and their consistency; device, network and account characteristics; the account relationship graph; open-response text characteristics in unmoderated studies; confirmed fraud and misrepresentation cases.
**Target:** Misrepresentation or coordinated abuse as confirmed by moderator observation or investigation.
**Evaluation metric:** Precision at the exclusion threshold dominates, because a false positive removes an income source from a real person on the basis of an algorithm they cannot see. The system should flag for review rather than exclude silently, and a contest route is a design requirement rather than a courtesy. Thresholds must be fitted per population: a study of enterprise buyers has a tiny qualifying pool and a high incentive, so a globally-tuned model will over-filter exactly the hard-to-recruit populations that matter most.
**Scope:** Response-level validity in unmoderated studies is a separate and newer problem from account-level screening and is currently almost unaddressed; assisted or generated open responses are the fastest-growing failure. 2 ML engineers, 6-9 months.
**Data availability:** Strong at a panel platform, absent at an agency — which determines who can build this.

---

## 3. Claim-Level Retrieval Over a Research Corpus
#bert #contrastive-learning #word-embeddings #large-language-models #k-nearest-neighbors #dimensionality-reduction #evaluation-metrics #data-integration

**Problem statement:** Repositories hold years of transcripts and tagged findings and are described by their own users as write-only. The question arriving is about a decision; the index is organised by study and tag; and organisations routinely commission research whose answer they already own.

**ML task:** Retrieve at the level of the claim rather than the document, surface contradicting evidence explicitly, and weight findings by staleness against product change
**Input data:** Transcripts, findings, clips and tags across the corpus; study dates, populations and product context; product release history for staleness weighting; the questions people actually ask, captured from product discussions.
**Target:** Whether retrieved evidence answers the asked question, judged by researchers on a labelled query set.
**Evaluation metric:** Answer relevance on realistic questions, and — more importantly — recall of contradicting evidence, because the most valuable thing a corpus can return is that two studies disagreed and here is why they might have. A system that returns one confident answer from a corpus containing a contradiction is worse than the current situation, since it launders disagreement into false certainty.
**Scope:** Derived structure should replace maintained taxonomies, with manual tags as a weak signal rather than the primary index — tag decay is what kills these systems. Staleness weighting requires the repository to know what has changed in the product since a study, which is an integration nobody has built. Delivery into the tools where questions get asked matters more than the retrieval quality, since the failure is that nobody opens the repository. 2 engineers, 6 months.
**Data availability:** The corpus exists and is large. Realistic labelled queries do not and must be collected from actual product discussions.

---

## 4. Session Synthesis Assistance With the Interpretation Left Human
#large-language-models #bert #k-means-clustering #contrastive-learning #word-embeddings #evaluation-metrics #worker-facing #automation

**Problem statement:** Twelve hours of sessions become a findings deck through a compressed weekend of transcript reading, clustering and slide building, and the interpretation — the professional contribution — is squeezed between the mechanical work on either side.

**ML task:** Extract candidate observations from session material, propose thematic clusters with their supporting evidence, and locate illustrative clips, without producing finished findings
**Input data:** Session recordings and transcripts with speaker structure; the study's research questions and screener criteria; researcher notes; prior studies in the same programme; the deck structures the team actually uses.
**Target:** Agreement with the researcher's own final clustering and selected evidence, measured after the fact.
**Evaluation metric:** Cluster agreement with researcher judgement on completed studies, and time-to-first-draft as the operational measure. The specific failure to test for is semantic collapse — grouping two quotes that use similar words to mean opposite things, which automated clustering does readily and which produces a plausible wrong theme. Measure that error class explicitly; a plausible wrong synthesis is worse than no synthesis because it is harder to notice.
**Scope:** The design constraint is that the system proposes and never concludes. Interpretation is the entire professional contribution, and a tool that hands a researcher a finished finding under deadline pressure will get it shipped unexamined. Attaching support level to every generated summary claim — participant count, observed versus reported — keeps the caveat with the statement instead of stranding it on a later slide. 2 engineers, 4-6 months.
**Data availability:** Session material is abundant. Researcher-final clusterings exist in completed studies and make a good evaluation set.
