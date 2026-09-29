# Supply Path and Inventory Quality Scoring

**Industry:** [[programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every buyer needs to know which of the fourteen paths to the same impression is real and which sites exist only to carry ads, and the tools that answer it score the open web generically rather than the buyer's own spend.
**Tags:** #graph-neural-networks #change-point-detection #k-means-clustering #gradient-boosting #dbscan #evaluation-metrics #feature-engineering #data-integration

## The Problem
The same impression is offered to a buyer through a dozen resellers at a dozen prices, and a meaningful share of the inventory available at any moment sits on sites built for no purpose except to carry advertising — thin syndicated content, arbitraged traffic, refreshing ad slots, forty units per page. A buyer who does not filter both problems pays multiple intermediary fees to reach inventory that nobody reads.

The industry's response has been supply path optimisation: pick the shortest, cheapest authorised route to each publisher, and blocklist the worst sites. Doing it well requires knowing, per seller, what fees are taken, what the win rate and price are relative to alternatives, whether the seller is authorised for that domain, and whether the domain is a real publication. Doing it at all requires reconciling `ads.txt` and `sellers.json` declarations against actual bid stream behaviour, which disagree constantly.

## What Already Exists
A real tooling layer has grown up here. `ads.txt`, `sellers.json` and SupplyChain Object are industry plumbing that make authorisation checkable. Jounce Media publishes made-for-advertising classifications and supply path research; Adalytics has repeatedly produced the studies that force the issue publicly; Scope3 scores inventory including its carbon cost; DoubleVerify and IAS sell pre-bid brand safety and fraud filtering at scale; Prebid's server-side infrastructure exposes path structure directly. Most large DSPs run internal SPO programmes, and the big holding companies negotiate direct supply deals that bypass the question.

## The Customisation Gap
The tools score the open web; a buyer needs their own spend scored. A made-for-advertising list is a universal artefact — it does not know that this advertiser's audience genuinely reads three sites on it, or that a domain classified as low quality outperforms for direct response in one vertical. Blocklists built from universal scores are known to be blunt: they remove reach, they disproportionately hit smaller and non-English publishers, and news blocklists have been shown to defund exactly the journalism advertisers claim to support.

The path question is even more buyer-specific. Which reseller is cheapest for a given publisher depends on that buyer's win rates, their negotiated terms, their creative formats and their geography — all of which sit in the buyer's own bid logs and none of which are in a vendor's universal ranking. And the scoring has to move: a clean path degrades when a seller changes its fee structure, a domain flips to arbitrage traffic after an ownership change, and the signal of that change is in the bid stream weeks before it appears in anyone's published list.

The gap, then, is a quality and path model fit to one buyer's actual spend, continuously updated from their own auction outcomes, that expresses its verdicts with uncertainty rather than as a blocklist — and that can say *this domain is worth less to you than the universal score suggests* and *this path costs you eleven percent more than the alternative for the same publisher*.

## Impact If Solved
The fee leakage and made-for-advertising share together account for a large fraction of the gap between what an advertiser spends and what a publisher receives; the ANA study put the recoverable portion in the billions. A buyer-specific model recovers a meaningful slice of that without the reach destruction that generic blocklists cause, and it does it continuously rather than in the annual audit that currently passes for supply governance.
