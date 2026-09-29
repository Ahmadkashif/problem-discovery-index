# Buy: Near-Duplicate Detection From Everywhere Else

**Niche:** Submission Deduplication & Filtering
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Semantic near-duplicate detection is commodity infrastructure in search, support, moderation and issue tracking, and bounty triage runs keyword search over a text field.
**Tags:** #bert #word-embeddings #contrastive-learning #k-nearest-neighbors #evaluation-metrics #data-integration #automation
**Contested on:** Whether the mechanical share of triage is removed before a human reads, or absorbed by analysts one submission at a time.

## The Problem

Finding the item in a corpus that means the same thing as a new item, regardless of wording, is a solved problem with commodity infrastructure. Vector embeddings, approximate nearest-neighbour search and the surrounding tooling are available as managed services, open-source libraries and features inside every major database.

Every adjacent industry uses it. Customer support surfaces similar tickets automatically. Issue trackers suggest duplicate issues as you type. Content moderation matches near-identical items against adjudicated history. Search engines have done semantic matching for years.

Bounty triage uses keyword search. An analyst types a term into a box and gets prior submissions containing that term. If the earlier researcher wrote "IDOR" and this one wrote "broken object level authorisation", the search returns nothing and the analyst starts from scratch.

The gap is not technology availability. It is that nobody has applied it here.

## What Already Exists

Embedding and retrieval infrastructure: sentence and document embedding models, vector databases and search services, and the approximate nearest-neighbour libraries underneath them — all commodity, all cheap, all well documented.

Support platforms: Zendesk, Intercom and their peers, with similar-ticket surfacing as a standard feature.

Issue trackers: GitHub, Jira and Linear, with duplicate suggestion at creation time.

Content integrity: perceptual and semantic matching against adjudicated corpora, discussed in [[industries/content-moderation-services|Content Moderation Services]].

Security-specific: vulnerability databases with CWE taxonomies providing a classification vocabulary, and the vulnerability management platforms that deduplicate scanner findings — though by identifier rather than by description.

## The Customization Gap

**The matching object is a finding, not a document.** Off-the-shelf text embedding will match submissions that read similarly, which is not the same as submissions describing the same vulnerability. Two reports of different flaws on the same endpoint read alike; two reports of the same flaw in different vocabulary do not. The representation has to be built from extracted finding attributes, which is the substantive adaptation.

**The corpus is adversarial.** Support tickets are written by people who want help. Bounty submissions are written by people who will learn how the matching behaves and adjust. Robustness to deliberate paraphrase is a requirement no adjacent application has.

**Duplicate means something specific here.** In support, a similar ticket is useful context. Here, duplicate has a financial consequence — it determines whether someone is paid — so the precision requirement is far higher and the presentation has to support a decision rather than merely inform one.

**Cross-tenant matching is where the value is and where the contracts bite.** The same researcher submitting the same finding across many programmes is the strongest available signal, and it requires comparison across customers, which needs abstraction that adjacent applications never had to design.

**CWE gives a taxonomy nobody applies consistently.** The classification vocabulary exists and submissions are labelled loosely or not at all. Inferring a consistent class from the text, as a matching feature, is a prerequisite that also serves the calibration work in [[niches/bug-bounty-platforms/severity-calibration/profile|🎯 Severity Calibration]].

**Scanner-output detection has no direct analogue.** The nearest is spam and low-quality content classification, which is mature and transfers reasonably, and nobody has pointed it here.

## Target Customer

The bounty platforms, where this is straightforwardly a build-versus-integrate decision on commodity infrastructure and the main obstacle has been roadmap priority rather than capability.

Vector search and retrieval vendors could package a finding-matching offering, though the adaptation is specific enough that the platforms are more likely to assemble it themselves.

Content integrity vendors are the closest neighbours, since adversarial semantic matching at volume is exactly their problem.

## Impact If Solved

The most mechanical, most expensive part of triage gets the technique that every comparable industry already uses. There is no research risk here, only application.

Matching on finding attributes rather than prose would catch the paraphrase duplicates that currently reach a human twice, which is where most of the wasted analyst time in this layer sits.

And a consistently inferred weakness classification, needed for matching, would unlock the severity comparison and programme measurement work elsewhere in this industry — one piece of infrastructure serving several of its largest gaps.
