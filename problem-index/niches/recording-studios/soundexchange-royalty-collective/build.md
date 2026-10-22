# Line-Ups Resolved Before the Money Becomes Non-Distributable

**Niche:** [[niches/recording-studios/soundexchange-royalty-collective/profile|Sound-Recording & Performer Collecting Societies]]
**Industry:** [[industries/recording-studios|Recording Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A society can pay performers only on recordings whose line-up it knows, and session players' line-ups arrive years late or never, so their money sits unidentified until the three-year clock runs out.
**Tags:** #large-language-models #k-nearest-neighbors #graph-neural-networks #gradient-boosting #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this pocket is fighting to identify every recording played, and every rights owner and performer on it, and pay them inside the distribution window before unidentified money becomes non-distributable, and whoever matches plays to recordings and line-ups most accurately and fastest keeps the labels and performers, and the international mandates, whose repertoire makes its licence worth paying for.

## The Problem
Labels register recordings with their owner and featured artist. The session bassist, the string section and the backing vocalists are registered only if someone claims them, and claims arrive piecemeal: a performer's list of credits, a union contract, liner notes for an old album. Meanwhile broadcasters and services report plays of thousands of recordings each month whose line-ups are incomplete. Under Article 13 of Directive 2014/26/EU, a society must distribute within nine months of the end of the collection year and treats money still unidentified three years on as non-distributable. The performers on the most-played recordings are often the ones never identified.

## Why Nobody Has Built This
Each society works its own claims queue in order of arrival, not by money at stake or time left. SCAPR's IPD and VRDB give shared identifiers for performers and recordings, but line-ups still come from claims. The evidence that would settle most cases (studio session records, union session reports, credits databases, other societies' entries) sits in different hands and formats, and nobody joins it.

## What to Build
A line-up resolution engine. It ranks unidentified and partly identified recordings by money at stake and days left before the Article 13 cutoff. For each, it gathers external evidence: session credits sent by studios, union session reports, liner notes and credits databases, partner societies' VRDB entries and performers' claim histories. It resolves performer identities to an IPN, proposes the probable line-up with a confidence score, and routes uncertain cases to researchers with the evidence attached. Accepted line-ups flow to the VRDB so partner societies benefit.

## Target Customer
Chief distribution officers at performer and joint producer-performer societies, and US bodies paying session performers: SoundExchange and [[niches/recording-studios/session-performer-royalty-fund/profile|🔍 the AFM & SAG-AFTRA Fund]].

## Impact If Built
More money reaches session performers inside the window and less is written off as non-distributable. That is the result performers and international partners judge a society on, and it is now measurable.
