# What the Corpus Knows About the Market

**Niche:** [[niches/crm-platforms/conversation-intelligence/profile|Conversation Intelligence]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A company's recorded sales calls are a continuous, unfiltered record of what buyers object to, which competitors they mention and how the market is moving, and the product surfaces it as a keyword search.
**Tags:** #large-language-models #bert #transformers #k-means-clustering #evaluation-metrics #confidence-intervals #change-point-detection #revenue-impact
**Contested on:** Every serious competitor in conversation intelligence is fighting to turn a recorded sales call into coaching a manager acts on and deal signal a forecast can use — and whoever converts recordings into acted-upon change takes the account.

## The Problem
Across four thousand recorded calls last quarter, buyers raised a pricing objection in a particular form with rising frequency, a competitor's new capability was mentioned in a way that suggests it is landing, a specific integration question came up repeatedly in one segment, and a feature the company shipped six months ago is almost never discussed. Product management learns these things through anecdote at the quarterly business review. The corpus that would establish each of them with a count and a trend is sitting in a search box, queried by individual managers looking for individual clips.

## Why Nobody Has Built This
The product was sold to sales leadership for coaching, so the roadmap followed coaching, and the market intelligence use has a different buyer — product, marketing, competitive intelligence — who was not in the original purchase. Synthesising across a corpus is also harder than retrieving from it: the useful output is a trend with a magnitude rather than three representative clips, and it requires classifying free conversation into stable categories that hold up over quarters. And there is a sensitivity about what the corpus reveals, since an honest account of what buyers say about the product is frequently unwelcome.

## What to Build
A synthesis layer over the corpus, producing counts and trends rather than clips. Objections are classified into a stable taxonomy that is learned from the corpus rather than configured, with frequency and trend by segment, by deal outcome and by stage. Competitor mentions are extracted with the context — what was said about them, in which situations, and whether deals where they appeared were won or lost. Feature and capability discussion is tracked, which tells product management what buyers actually ask about as opposed to what the roadmap assumes. Emerging topics are detected as they appear rather than when someone thinks to search for them, which is the capability that makes this an instrument rather than an archive. Everything is delivered with the evidence attached, since the value of a claim like "pricing objections in this segment doubled" depends entirely on being able to hear the calls behind it.

## Target Customer
Conversation intelligence vendors, product and competitive intelligence functions inside their customers, and the marketing organisations whose messaging is currently tested by intuition.

## Impact If Built
The corpus is the most direct, least mediated record of what a market thinks that a company possesses, and it is used almost exclusively for individual coaching. Trend detection on objections and competitor mentions gives product and marketing a feedback loop measured in weeks rather than in quarterly anecdote, and it opens a second buyer for a product currently sold to one.
