# Build: The Adjudicated Case Library

**Niche:** Policy Training & Consistency
**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Turn the operation's own millions of adjudicated decisions into a searchable, versioned case library that trains new reviewers and answers the hard case at the moment it appears.
**Tags:** #bert #word-embeddings #contrastive-learning #large-language-models #evaluation-metrics #transfer-learning #tacit-knowledge-ml #worker-facing
**Contested on:** Whether consistency across thousands of reviewers comes from a policy document they are asked to internalise, or from the adjudicated examples that show what the document means.

## The Problem

A moderation operation produces the ideal training corpus as a by-product of doing its work: millions of items, each with a decision, a policy citation, an audit outcome, often an appeal result, and in the contested cases an adjudication rationale. It is a record of exactly how this policy has been applied to real material, at enormous scale, across every category and language the operation covers.

It is used for nothing. Decisions are logged for audit and billing, retained for whatever the contract requires, and never turned into anything a reviewer can learn from. Training is built instead from the policy document plus whatever examples a trainer assembled by hand, which is typically a few dozen per category, chosen for clarity rather than for representing the distribution of what actually arrives.

The gap shows up in every direction. A new reviewer reaches competence in months rather than weeks because they are rebuilding a case library that already exists in the logs. A reviewer facing an unusual item has no way to ask what was decided on similar material, so they guess or escalate. Two reviewers in different sites decide near-identical items differently and nobody notices. And when an experienced reviewer leaves, the part of the corpus they had internalised leaves with them, in an industry where they leave constantly.

## Why Nobody Has Built This

**The decisions are client data under restrictive terms.** The adjudication record belongs to the platform and is governed by a contract written for audit and billing retention, not for building a derived training asset. Whether the vendor may use it this way is frequently unclear, and unclear defaults to no.

**The content is the problem.** A case library of moderation decisions is a curated collection of the worst material on the internet. Storing it, searching it and showing it to trainees creates severe handling, access and exposure issues — and the obvious mitigation, working from abstracted representations rather than the material itself, is a harder technical product than it first appears.

**Policy versioning makes old cases actively misleading.** A decision correct under the policy as it stood eight months ago may be wrong now. A case library without rigorous version tracking teaches people the wrong thing with the authority of precedent, which is worse than no library.

**Nobody owns training as a technical problem.** Training sits with learning and development, which buys learning management systems and builds slides. The data sits with operations. There is no function whose job is to connect them.

**Turnover undercuts the business case internally.** In an operation where the median reviewer stays under two years, investment in accelerating competence is easy to argue for and easy to defer, and it competes with throughput improvements that show up next month.

## What to Build

**Index the decision record as a versioned case corpus.** Every adjudicated item with its decision, the policy version in force, the citation, the audit and appeal outcome, and the adjudication rationale where one exists. Version is a first-class dimension: every retrieval is scoped to the current policy, with superseded decisions visible as history rather than as guidance.

**Retrieve by similarity, at the moment of decision.** A reviewer facing a hard item sees how similar items have been decided under the current policy, with the reasoning and the confidence that the precedent is settled rather than contested. This is the feature that matters most — it puts the operation's accumulated experience in front of the person who needs it, in the seconds they have.

**Work from abstracted representations wherever possible.** Embeddings, extracted features, textual descriptions and redacted or reduced-fidelity renderings rather than the original material, so the library can be searched and studied without re-exposing anyone. This constraint should shape the architecture from the start, not be added later.

**Generate training from the real distribution.** Curriculum built from the corpus rather than hand-picked: the genuinely common cases in proportion, the boundary cases where reviewers disagree most, and the categories where this cohort is currently weakest. Practice queues drawn from real adjudicated items with the known answer, so competence is measured against the operation's actual work rather than a trainer's examples.

**Surface disagreement as the signal it is.** Clusters of near-identical items decided differently are the most valuable output the library produces — they identify either a policy ambiguity or a site-level drift, both of which are invisible today and both of which are exactly what the policy team and quality leadership need.

**Ship policy changes with cases, automatically.** When the policy changes, retrieve the affected decisions, adjudicate a representative set under the new language, and distribute the change as worked examples rather than as a paragraph. This is the intervention that makes a weekly policy change actually land.

## Target Customer

Vendor quality and training leadership, where the corpus already sits and the internal case — faster time to competence, measurable consistency — is straightforward once the data rights are settled.

Platform policy teams are the more strategic buyer, because the disagreement clusters are a direct readout of where their policy is ambiguous, which is information they currently obtain only through escalation and anecdote.

## Impact If Built

Time to competence falls substantially, which in an industry with this turnover rate is the single largest operational lever available. New reviewers stop rebuilding by hand a library the organisation already has.

Consistency becomes measurable and then improvable. Near-identical items decided differently across sites is a defect this industry cannot currently see at all.

And the tacit expertise stops evaporating. The experienced reviewer's case library is the industry's most valuable and most perishable asset, and this is the only mechanism that would let it outlast the person holding it.
