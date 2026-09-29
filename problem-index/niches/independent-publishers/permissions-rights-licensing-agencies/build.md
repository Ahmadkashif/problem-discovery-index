# Chain of Title as a Graph Instead of a Lookup

**Niche:** [[niches/independent-publishers/permissions-rights-licensing-agencies/profile|Permissions & Rights Licensing Agencies]]
**Industry:** [[industries/independent-publishers|Independent Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Who controls a right is the answer to a chain of transfers, reversions, and territorial splits, and it is stored as a single current value.
**Tags:** #graph-ml #named-entity-recognition #large-language-models #binary-classification #evaluation-metrics

## The Problem
Determining whether a use can be licensed means answering who holds this right, for this use, in this territory, right now. That is rarely a fact; it is the outcome of a history. An author granted world rights to a publisher; the publisher licensed North America to another house; a clause reverted rights when the book went out of print; the original publisher was acquired twice; the estate now controls something and the imprint controls the rest.

The organization's databases hold a current answer per work — a rights holder, a set of permitted uses. When the answer is wrong, the licence is invalid and the exposure is an infringement claim. When it is unknown, the request is declined, which loses revenue on a use that was probably licensable.

Every hard determination is worked out by an analyst reading agreements and correspondence, and the output is an updated field. The reasoning that produced it, the evidence, and the parts that stayed uncertain are not retained in any form the next analyst can use.

## Why Nobody Has Built This
The data model is inherited. These systems were built as catalogues — a work, its rights holder, its permissions — because that is what a licensing transaction needs to read at the moment of sale. A catalogue is a snapshot, and rights are a history, and the mismatch has been absorbed by analysts ever since.

Migrating to a temporal, relational model means restructuring the core asset while it continues to serve live licensing traffic, which is the kind of project that gets deferred indefinitely.

There is also no feedback. A wrong determination surfaces only if someone complains, which is rare relative to how often the answer is uncertain, so the error rate is unknown and the case for investment has never been quantified.

## What to Build
Model rights as a temporal graph and derive the answer rather than storing it.

**Rights as edges with time, territory, and scope.** A grant from party to party, covering specified uses in specified territories, effective between dates, with conditions such as reversion. The current holder for a given use in a given place becomes a query over that graph — which is what it actually is.

**Entity resolution across the corporate history.** Publishers merge, are acquired, and change names constantly, and imprints move between owners. Resolving which present-day entity succeeded to a 1987 grant is a substantial matching problem in its own right and is currently done by analysts who happen to remember.

**Extract terms from the agreements.** Grants, reversions, and territorial splits live in contract text the organization already holds. Extracting them into structured edges is the input to everything else, and modern language models handle this document type well.

**Score confidence and localize the gap.** Where the chain is complete the answer is certain; where an agreement is missing or a reversion condition unverified, the system should say so and say which link is weak. That turns a binary decline into a specific question worth chasing, which is where the recoverable revenue is.

**Detect conflicts.** Two grants of the same right in the same territory cannot both be valid. A graph makes those findable; a table of current holders hides them by construction.

## Target Customer
Chief Data Officer or SVP of Rights Operations at a collective licensing organization. The forcing function is external and large: machine training has made rights clearance at corpus scale a live commercial question, and answering it requires exactly the ability to determine rights across millions of works quickly and defensibly.

## Impact If Built
Uncertain rights are the reason enormous quantities of published work sit unlicensable — the orphan works problem in its everyday form. Every determination that moves from unknown to licensable is revenue for a rights holder and access for a user. And the organization's core asset stops being a snapshot maintained by attrition and becomes a model that can explain and defend its own answers.
