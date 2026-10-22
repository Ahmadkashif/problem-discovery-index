# Proposal Building for Ratings-Priced Inventory

**Industry:** [[media-rep-firms|Media Representative Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Configure-price-quote software already builds proposals for any catalogue, but spot inventory is priced per rating point against a ratings book that changes every quarter, so rep assistants still assemble every proposal by hand.
**Tags:** #large-language-models #transformers #seq2seq #feature-engineering #data-integration #automation #workflow-orchestration

## The Problem
An avails request names markets, a target demo, dayparts, flight weeks, spot lengths, a budget and a CPP goal. It arrives as an email, a PDF, an Excel grid or a structured RFP from the agency's buying system, in a different layout from every agency office. For each represented station, a sales assistant pulls available inventory from the station's traffic system, attaches projected ratings for the target demo from the current ratings book, prices each line against the station's rate grid and the AE's guidance, checks the total against the buyer's goal, and keys the proposal back into whatever system the buyer uses. A thirty-market request can mean thirty separate proposals across two or three traffic systems. When the buyer revises the demo or the weeks, much of it is done again.

## What Already Exists
Salesforce CPQ and similar configure-price-quote tools build quotes from a product catalogue and price rules. On the media side, WideOrbit's sales and traffic tools, Mediaocean's seller-side avails workflow and Hudson MX move requests and proposals electronically between agencies and stations. Each works where both sides use it.

## The Customisation Gap
Generic CPQ assumes a fixed catalogue with list prices. Spot inventory is perishable, sold per unit but priced per rating point. The "price" of a spot is the station's rate divided by its projected rating for the buyer's demo, so the same unit has a different CPP for every request. The rep-specific layer needs several things. It has to parse free-form requests into a structured spec. It must map dayparts and program names to each station's inventory codes and attach projections from the right ratings source; since January 2025 that means Nielsen Big Data + Panel for new buys and possibly Panel-Only for posting older ones. It has to price against the AE's floors and the station's sell-out level, and flag where the proposal misses the buyer's CPP goal and which units would close the gap. And it has to emit the proposal in the buyer's format. None of this exists in a horizontal CPQ, and the media workflow tools carry the data without building the proposal.

## Impact If Solved
A proposal built in minutes rather than hours lets the assistant answer more requests before the buyer's deadline. Proposals that arrive early and complete are better placed when the buyer allocates. Turning a demo or week revision into a re-run rather than a rebuild removes the most hated hour of the assistant's day.
