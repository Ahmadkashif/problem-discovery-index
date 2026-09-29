# Monograph Impact Router for New Evidence

**Niche:** [[niches/acupuncture-practices/herb-evidence-monograph-publishers/profile|Herb & Supplement Evidence Monograph Publishers]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An engine that reads each incoming trial, recall, or regulatory action and routes it to the exact monograph sections whose current wording it contradicts, so the editorial queue is ordered by consequence rather than by arrival date.
**Tags:** #large-language-models #transformers #bert #transfer-learning #word-embeddings #graph-neural-networks #evaluation-metrics #data-integration #compliance #revenue-impact

## The Problem
A monograph on a single herb is not one claim but dozens — an efficacy grade per indication, a safety rating, dosing ranges, pregnancy and lactation guidance, and an interaction matrix that may name forty drugs. A new publication rarely touches all of it; it usually bears on two or three specific assertions. But the intake process treats the paper as an undifferentiated unit assigned to whoever covers that botanical, and the editor has to reconstruct from memory which parts of a long monograph the paper actually bites on. With a few thousand active monographs and a literature stream that runs into the hundreds of relevant items a month, the queue is worked in the order things arrived rather than in the order of how much current published text they invalidate. The result is a systematic bias: high-traffic monographs stay current because someone is always looking at them, and the long tail drifts.

## Why Nobody Has Built This
The hard part is not reading the paper, it is knowing what the house already says. That knowledge lives in the monograph corpus as prose written by many editors over twenty years, with the connective tissue — this dosing range rests on those two trials, this interaction rating rests on a mechanistic argument rather than clinical data — held only in editors' heads. Botanical nomenclature compounds it: the same plant appears as a Latin binomial, a pinyin formula name, a common name, a proprietary extract designation, and several synonyms retired from the literature decades ago, and a matching system that misses any of these silently drops evidence. Generic literature alerting tools solve neither problem; they surface papers by keyword and hand the editor an undifferentiated inbox, which is the situation that already exists.

## What to Build
An engine that indexes the monograph corpus down to the assertion level — each graded claim, dosing statement, and interaction entry as a separate addressable object carrying its supporting citations and the rationale behind its rating. Incoming literature and regulatory actions are resolved against a botanical entity layer that unifies binomials, pinyin, common names, and extract designations, then matched not to the monograph but to the specific assertions the finding bears on. Each match arrives with a direction and a magnitude: this trial supports the existing grade, this one contradicts the dosing ceiling, this recall invalidates a safety statement in eleven monographs at once. The queue then sorts by how much published text is at stake and by subscriber exposure, and the editor opens a work item that already shows the current wording, the citations behind it, and the new evidence side by side.

## Target Customer
Editorial directors and VPs of content at evidence monograph publishers running 50-200 credentialed researchers, plus the smaller in-house content teams at supplement retailers and pharmacy systems that maintain their own derivative monographs.

## Impact If Built
Turns a volume problem into a prioritization problem. The publisher can state, with evidence, how current its corpus is and where the staleness sits — a claim its subscribers currently have to take on trust. Because assertion-level links accumulate, the corpus becomes traversable in ways it never has been: which claims rest on a single study, which interaction ratings have never been revisited, which grades would move if one pending trial reads out. That structural map is the asset, and no competitor can build it without the same twenty years of prose.
