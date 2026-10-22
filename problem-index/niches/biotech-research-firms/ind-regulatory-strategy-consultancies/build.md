# A Nonclinical Precedent Graph From FDA's Own Reviews

**Niche:** [[niches/biotech-research-firms/ind-regulatory-strategy-consultancies/profile|Nonclinical & IND Regulatory Strategy Consultancies]]
**Industry:** [[industries/biotech-research-firms|Biotech Research Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** FDA publishes the pharmacology and toxicology review behind every approved drug, a complete record of what nonclinical evidence it accepted, and consultants still answer "what will FDA require?" from memory.
**Tags:** #large-language-models #transformers #graph-neural-networks #word-embeddings #k-nearest-neighbors #compliance #revenue-impact
**Contested on:** Every serious competitor in this pocket is fighting to tell a sponsor, before the pre-IND package is due, exactly which nonclinical studies FDA will require for this modality and indication — and whoever can back that answer with what FDA actually accepted for comparable programmes wins the engagement.

## The Problem
A sponsor with a bispecific antibody for a solid tumour, or an siRNA for a rare liver disease, wants to know which species, study durations, safety pharmacology and reproductive toxicology FDA required for comparable products, and which it waived. Each approved product's review package records this: the studies, species, durations, NOAELs, margins and the reviewer's comments on adequacy. Consultants know a subset from their own engagements and search the rest by hand.

## Why Nobody Has Built This
The reviews are long PDFs, many of them scanned, with inconsistent structure across decades and divisions. Regulatory intelligence vendors index guidance and approval decisions, not the nonclinical substance inside reviews. And consultancies sell experience, so few have tried to codify it.

## What to Build
A precedent graph: every approved product's nonclinical package extracted into structured records — modality, target class, indication, species, study type and duration, key findings, NOAEL and margin, reviewer comments on adequacy — linked by target, modality and indication, with guidance versions attached by date. A consultant queries "antibody–drug conjugates with this payload class" and gets the packages and the reviewers' objections. The firm's own de-identified meeting outcomes are layered on top as private precedent.

## Target Customer
Practice leaders at nonclinical regulatory consultancies; regulatory strategy groups at CROs.

## Impact If Built
Every recommendation arrives with its precedent before the 30-day package deadline, which is the answer the contest in this pocket rewards and what a junior consultant cannot otherwise give.
