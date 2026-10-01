# The Call That Repeats the Library

**Niche:** [[niches/expert-networks/public-equity-coverage-calls/profile|Public-Equity Coverage Calls]]
**Industry:** [[industries/expert-networks|Expert Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An analyst pays for an hour with an expert who says what three library transcripts already said, because nothing compared the request with what the analyst already had.
**Tags:** #large-language-models #transformers #word-embeddings #k-nearest-neighbors #evaluation-metrics #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to put an expert in front of a fund analyst who adds something the analyst's last calls and the transcript library did not already say, cleared under the fund's MNPI policy — and whoever does that most reliably becomes the fund's first call.

## The Problem
A fund analyst requests a call on a company's channel inventory. The library holds a dozen transcripts on the topic from the last six months, two of them from former employees of the same distributor, and the analyst had a call on it last quarter. The new call covers the same ground.

## Why Nobody Has Built This
Networks are paid per call and libraries per subscription; neither is paid to tell the client a call is unnecessary. The analyst's own call notes sit in the fund's research management system, which the network cannot see.

## What to Build
A pre-call novelty check on the client side: given the request and the proposed expert, retrieve the analyst's prior calls and the library transcripts on the topic, summarise what is already known, and propose the questions the existing material does not answer. On the network side, route requests toward experts whose role or recency differs from the experts already in the library on that topic.

## Target Customer
Directors of research at hedge funds and long-only managers; product leaders at networks with their own libraries.

## Impact If Built
Coverage calls are the most repeated purchase in the industry. Pointing each call at what is not yet known raises the value per call, which is the argument a fund's research budget holder responds to.
