# Analysts Know Which Buys Signal What and Publish a Number

**Niche:** [[niches/news-media-local/political-ad-tracking/profile|Political Advertising Tracking]]
**Industry:** [[industries/news-media-local|Local News Media]]
**Type:** Fix (Pain Point)
**One-liner:** A tracking analyst reads a buy the way a trader reads an order book, and the product reports the dollars.
**Tags:** #tacit-knowledge-ml #text-classification #anomaly-detection #worker-facing #data-integration

## The Problem
An analyst who has tracked campaigns for several cycles reads a buy as intent. A committee suddenly reserving time in a market it had ignored means internal polling moved. A candidate shifting from persuasion to turnout messaging in October means a strategic read. A buy cancelled and re-placed at a lower weight means money problems. A sponsor whose spots appear through an unfamiliar committee is a network worth mapping.

That reading is what makes the data valuable to a campaign, and it is what the firm's own analysts do all day. The product reports the dollars and the occurrences.

Some of the interpretation reaches clients as commentary or in briefings. None of it is captured as structured knowledge — the sponsor network relationships an analyst worked out, the tells they have learned to watch, which committees historically front for which interests. Analysts move between tracking firms, campaigns, and consultancies constantly, and each departure takes a cycle's worth of accumulated reading with it.

## Why It's Still Broken
The product is a data feed and the organization is built to deliver it accurately and fast. Interpretation is a value-add someone provides in a client call, not an artefact the system holds.

Cycle intensity makes it worse. During an election the operation is at capacity delivering coverage, and reflection happens afterwards if at all — by which point the analysts who did the reading are working somewhere else.

And attribution knowledge is sensitive. Asserting that a committee fronts for a particular interest is a claim with legal and reputational weight, so it stays as analyst understanding rather than becoming a recorded position.

## What a Fix Looks Like
Structure the reading and the network.

**Sponsor network records.** Committees, their funders where disclosed, their historical alignment and the evidence for it — maintained as a graph rather than reconstructed each cycle. This is the highest-value capture and it compounds across cycles because the same actors recur.

**Typed buy observations.** Unexpected market entry, message shift, weight change, cancellation pattern — recorded against the race and the advertiser with a short note. Seconds of work on a pattern the analyst already noticed.

**Test the tells against outcomes.** Which buy signals actually preceded a change in a race's competitiveness? With observations recorded and results public, this is answerable within two cycles, and it converts folklore into evidence.

**Retrieval during the cycle.** An analyst covering an unfamiliar race should see what the firm knows about the committees active in it, not start from the filings.

**Handle attribution carefully by design.** Recording evidence and confidence separately from assertion is what makes a sensitive claim usable internally, and it is a design choice the firm can make deliberately.

## Who Feels the Pain
Analysts, rebuilding sponsor networks every cycle. New analysts, who need a full cycle to become useful in a business with two-year rhythms and heavy turnover. Firm leadership, whose interpretive capability resets periodically. And clients, who get a data feed and whichever analyst's reading they happen to have access to.

## Impact If Fixed
The sponsor network in particular is a compounding asset — the committees and consultants recur cycle after cycle, and a firm that has mapped them properly holds something no competitor can assemble in one election. Capturing the buy-reading knowledge turns a data feed into an intelligence product, which is the only defensible position in a category where coverage can be matched.
