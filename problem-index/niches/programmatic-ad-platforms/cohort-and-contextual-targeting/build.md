# Bidding on a Stranger

**Niche:** [[niches/programmatic-ad-platforms/cohort-and-contextual-targeting/profile|Cohort & Contextual Targeting]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Most impressions now arrive with nothing known about the person, and the industry responds with a keyword taxonomy designed two decades ago.
**Tags:** #transformers #bert #large-language-models #contrastive-learning #gradient-boosting #evaluation-metrics #dimensionality-reduction #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to bid well on an impression where nothing about the person is known — and whoever extracts the most from the page, the moment and the aggregate wins the majority of inventory that is no longer addressable.

## The Problem
The bid request arrives with a URL, a device type, a rough location, a time, and no identifier. The bidder's audience models have nothing to work with, so it falls back to contextual — which in practice means checking whether the page matches a category in a taxonomy, or contains a keyword from a list. That is a nineteen-nineties representation of a document, applied to an inventory that is now the majority of the market, while every tool needed to represent a page properly has become cheap and available. The category treats this inventory as degraded supply and prices it accordingly, which is a self-fulfilling assessment.

## Why Nobody Has Built This
Contextual was the thing identity replaced, so it carries a legacy status and attracts neither investment nor talent — this framing is the main obstacle and it is cultural rather than technical. Page understanding at bid latency across billions of URLs requires precomputation infrastructure nobody built for a channel they considered dying. Contextual signals are hard to connect to outcomes, so their value is unproven and therefore unfunded. And buyers ask for audiences, so that is what gets sold.

## What to Build
Treat the impression without an identifier as a rich signal rather than an absence. Represent the page properly with modern language models — topic, stance, sentiment, intent, reading context, commercial adjacency — precomputed per URL and refreshed as content changes, which is the foundation and is now cheap in a way it was not when the taxonomies were built. Model the moment as well as the page, since the same article at eight in the morning on a phone and at ten at night on a television are different opportunities and the request contains both facts. Learn contextual-to-outcome relationships directly, which connects to the outcome feedback niche and is what converts contextual from an assumption into a measurement. Build cohorts from behaviour that does not require an identifier — property-level, session-level and content-level aggregates — which is where the remaining signal lives. Handle brand suitability as a graded judgement rather than an exclusion list, which is the fix note's subject and currently destroys both reach and publisher revenue for no measured safety gain. Use the creative in the decision, since the fit between a specific advertisement and a specific page is the actual question and is treated as two separate ones. Exploit deliberately, because contextual value must be learned per advertiser and a purely exploitative bidder never discovers where it works. Price this inventory on measured performance rather than on the assumption that unaddressable means worse, which is the commercial argument and is frequently wrong. Give publishers the contextual signals about their own pages, which they can sell and currently cannot see. And evaluate against addressable inventory honestly, since the comparison is the whole case.

## Target Customer
Demand-side platforms and bidders, publishers whose unauthenticated inventory is underpriced, and advertisers losing reach to identity loss.

## Impact If Built
Contextual carries a legacy status from being the thing identity replaced, which is why a nineteen-nineties document representation still serves the majority of inventory. Modern page representation is now cheap, and learning contextual-to-outcome relationships converts an assumption into a measurement.
