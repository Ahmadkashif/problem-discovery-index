# Build: Evidence Before Determination

**Niche:** Infringement Determination
**Industry:** [[industries/brand-protection-firms|Brand Protection Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Route the lawful categories away from the counterfeit queue, put authorised-seller and channel evidence in front of the reviewer, and record the rationale so a determination can be contested against what was actually decided.
**Tags:** #bert #cnns #gradient-boosting #evaluation-metrics #confidence-intervals #compliance #worker-facing #data-integration
**Contested on:** Whether a flagged listing is actually infringing, which is a legal judgement that no image match settles.

## The Problem

The determination is made from a photograph, a price, a title and a seller name. The categories it must distinguish are not distinguishable from those.

A repair shop listing "iPhone screen replacement" uses the brand name lawfully to describe what it repairs. A reseller listing a genuine handbag bought at retail is exercising a right the law generally permits. A parallel importer selling genuine goods sourced in another market may be entirely lawful depending on jurisdiction. A refurbisher selling restored genuine goods is lawful if the condition is disclosed. A compatible-parts manufacturer may name the brand their part fits. A reviewer or critic may use the mark.

Each of these looks, from a product photo and a low price, indistinguishable from a counterfeit. And each, when wrongly actioned, harms a business that has done nothing wrong and that must contest the action through a process designed for the party who filed it.

The evidence that would distinguish them mostly exists. Whether the seller is an authorised distributor is a list the brand holds. Whether goods are genuine parallel imports is frequently determinable from serialisation or batch data. Whether a listing is a repair service is determinable from its text. Whether this seller has been correctly determined before is in the firm's own record.

None of it reaches the reviewer.

## Why Nobody Has Built This

**The cost of over-enforcement falls outside the system.** The harmed party is a seller with no relationship to the firm, the platform absorbs the appeal, and the firm's count rises. There is no cost signal, which is the root of it.

**The evidence lives with the brand.** Authorised seller lists, distribution records and serialisation data sit with the client, are frequently stale, and are treated as the client's problem.

**Jurisdiction makes the legal answer genuinely variable.** Parallel import legality differs between markets, and modelling it properly is real legal work rather than a rule.

**Notice processes do not require it.** Platform notice forms generally require an assertion of good-faith belief rather than evidence of the determination, so no external standard forces better practice.

**Routing lawful categories separately reduces volume.** Sending repair listings to legal review rather than to enforcement produces fewer notices, and notices are what the contract is priced on.

**Nobody measures the error.** The wrongful-action rate is not computed at most firms, so the problem has no number and no owner.

## What to Build

**Classify the legal category before the queue.** Apparent counterfeit, apparent authorised resale, apparent parallel import, apparent refurbishment, apparent repair or compatible part, apparent commentary. This is largely determinable from listing text and seller characteristics, and routing each to an appropriate path is the single most effective protection available.

**Maintain the authorised-seller and channel data as a live integration.** Current authorised distributors, known resellers, serialisation and batch records where they exist. Stale or absent lists are the largest single cause of wrongful action against legitimate sellers, and this is a data maintenance problem shared with the brand.

**Raise the evidence bar for the lawful-adjacent categories.** Actioning a repair service or a suspected parallel import should require more than a visual match — a test purchase, a serialisation check, a legal review. Slower, fewer, and correct.

**Model jurisdiction explicitly.** Which market the seller ships from and to, and what the applicable rule is. Parallel import determinations made without this are guesses.

**Require a structured rationale on every determination.** Category, basis, evidence relied on. Seconds to record, and it is what makes an appeal evaluable and a firm's accuracy measurable.

**Surface prior determinations on the same seller.** A seller previously determined legitimate should not be re-actioned by a different reviewer next month, and this recurs constantly.

**Measure and publish the wrongful-action rate.** Sampled re-review with full context, reported. A firm that can state its own precision is offering something no competitor currently can.

## Target Customer

Brands with large authorised reseller and repair networks, who bear the direct commercial and relationship cost when their own channel partners are actioned by their own enforcement vendor.

Platforms, who absorb the appeals, face regulatory attention on notice accuracy, and could require rationale and precision data from notice senders.

Brand protection firms positioning on accuracy, particularly for clients who have been publicly embarrassed by a wrongful action.

## Impact If Built

The documented harm in this industry — legitimate sellers, repairers and resellers losing income to a determination made in seconds — is addressed at its source, which is routing and evidence rather than reviewer effort.

A current authorised-seller integration would prevent a large share of the most damaging errors on its own, and it is a data problem rather than a judgement one.

And recording a rationale makes the determination contestable against what was actually decided, which is the minimum a process with these consequences should offer the party it affects.
