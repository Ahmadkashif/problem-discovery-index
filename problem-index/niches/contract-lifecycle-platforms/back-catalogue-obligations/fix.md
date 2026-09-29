# The Amendment Chain Nobody Resolves

**Niche:** [[niches/contract-lifecycle-platforms/back-catalogue-obligations/profile|Back Catalogue Obligations]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A repository holds the master agreement and its five amendments as six separate documents, so the terms actually in force exist nowhere and are reconstructed by reading all six in order.
**Tags:** #graph-theory #bert #large-language-models #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to make the executed back catalogue answerable — what have we promised, to whom, and where — and whoever does that takes the account, because it is the question the category was bought to answer and the one every implementation declares out of scope.

## The Problem
Counsel is asked what the liability cap is for a particular customer. The repository returns a master agreement from 2018 with a cap, a first amendment that changed the fee schedule, a second that extended the term, a third that replaced the entire limitation of liability section, a statement of work with its own cap for that engagement, and an order form referencing a version of the terms that is not the current one. Determining the operative cap takes twenty minutes of careful reading. The structured record in the repository shows the 2018 figure, because extraction ran per document and the master agreement is the one that had a cap in it.

## Why It's Still Broken
Repositories model documents, and an amendment is a document, so the relationship between them is at best a link and usually a shared folder. Resolving a chain requires understanding what each amendment does — replace, add, delete, or supersede a specific provision — which is a semantic operation nobody implemented. And the failure is silent: the structured record shows a value, it is simply the wrong one, which is more dangerous than showing nothing.

## What a Fix Looks Like
Model the chain and compute the operative terms. Link documents into their agreement family automatically, using references, parties, dates and titles, which is ordinary entity resolution and is the prerequisite. Classify each document's role — master, amendment, order form, statement of work, side letter — and for each amendment determine what it does to which provision, which is a narrow, well-defined extraction task rather than open-ended reading. Compute the current operative value for each term with its provenance, so counsel sees the cap and the amendment that set it. Flag conflicts and ambiguity explicitly rather than picking one, since a genuine conflict between an order form and a master agreement is a finding a lawyer needs to see and not a field to populate. Show the term's history, because how a provision moved over five years is frequently the useful context. And report families where the chain is incomplete — an amendment referencing a document not in the repository — which is a common and serious gap nobody currently surfaces.

## Who Feels the Pain
Counsel reconstructing operative terms document by document; commercial teams acting on a repository value that is five years out of date; and organisations whose structured contract data is confidently wrong rather than merely absent.

## Impact If Fixed
Chain resolution converts a repository from a filing cabinet into a source of answers, and the underlying extraction task is narrow. Flagging conflicts rather than resolving them silently is what makes the output safe for a lawyer to rely on.
