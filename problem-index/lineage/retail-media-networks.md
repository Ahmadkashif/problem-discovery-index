# Lineage: Retail Media Networks

**Industry:** [[industries/retail-media-networks|Retail Media Networks]]
**Wave:** [[series/eras/wave-09-programmatic|9 — Programmatic]]
**The tool:** Amazon Sponsored Products — a cost-per-click listing, bought by keyword, automatic or product targeting, that places a supplier's own product at the top of, alongside or within the retailer's shopping results — scored by ACoS, ad spend divided by attributed ad revenue
**Builder:** Amazon
**Builder in vault:** **ABSENT**
**Verification:** partial — mechanics verified against Amazon's own pages; launch date not established, see Sources

## The Problem That Came First

Suppliers have always paid retailers for position. The end-cap, the eye-level shelf and the circular were bought with trade money long before anyone called it media, and the brand paying rarely learned whether the display moved product.

The earlier fix was to sell the brand the data instead of the shelf. Dunnhumby, founded by Clive Humby and Edwina Dunn in London on 24 May 1989, built the analysis behind Tesco's Clubcard after 1994 trials and a national launch on 13 February 1995, and went on to sell purchase insight drawn from it to suppliers including Procter & Gamble and Coca-Cola. That gave the brand a report. It did not give the brand a lever it could pull and price itself.

**The constraint was that the shelf could not run an auction.** Physical placement was negotiated quarterly, category by category, by a merchant and a sales rep. A search results page could be re-sold on every query.

## What Got Built

A listing that looks like a product and is paid for like a search ad.

Sponsored Products charges per click, with no monthly or upfront fee; the advertiser bids "the maximum amount that you're willing to pay when a shopper clicks an ad for your products." It targets by keyword, by product, or automatically — "let Amazon's systems target relevant keywords automatically." The ad appears "at the top of, alongside, or within shopping results and on product pages": in the shelf, not beside it.

The scoreboard came with it. **ACoS** is ad spend divided by ad revenue — spend $50, earn $100, ACoS 50% — and ROAS is its inverse. Both are denominated in sales the retailer itself recorded, attributed by the retailer itself.

## Who Built It, And Why Them

Amazon, and the reason is that it already owned both ends of the loop.

The auction was not new. GoTo.com's keyword-per-click mechanism — see [[lineage/performance-marketing-agencies|Lineage: Performance Marketing Agencies]] — had shown that advertisers would bid on intent. What a search engine could not do was see the purchase. **Amazon ran the query, the listing, the cart and the payment in one system**, so it could charge on the click and report the sale without anyone else's data.

It also had the sellers. A marketplace of third-party merchants and first-party vendors, each competing for the same result slots, supplied an advertiser base that already had a product on the page and nothing to build — the ad is the existing detail page, promoted. That is why the format is a product listing rather than a banner: the creative was already there.

The launch date could not be established this session, and no individual designer is named in any source reached.

## What It Cost

**The metric grades the retailer's own shelf.** ACoS counts attributed sales without subtracting the ones that would have happened anyway — the shopper who typed the brand's name and clicked the sponsored copy of the organic result. A lower ACoS reads as a better ad and can mean a more cannibalised one.

And the slot sold is a slot taken from organic relevance. Every sponsored listing displaces a product the ranking would otherwise have shown, and that cost lands in basket and repeat visits, not in the campaign report. This vault's own problem notes record that most networks since license the same auction technology and rank on bid times predicted click.

## What You Still Touch

The first several results for "paper towels" carry a small "Sponsored" label and look exactly like the rest.

- [[problems/retail-media-networks/high-impact|🔴 The Only Closed Loop in Advertising, Spent Counting Sales That Were Already Happening]] — ACoS without a counterfactual
- [[problems/retail-media-networks/worker-life-2|🟢 The Merchant Whose Shelf Was Sold]] — the organic slot the listing displaced
- [[niches/retail-media-networks/incrementality-and-cannibalisation/profile|Incrementality & Cannibalisation]]
- [[niches/retail-media-networks/auction-and-ranking-objective/profile|Auction & Ranking Objective]]

**Sources:** Amazon Ads, *Sponsored Products* product page (CPC pricing, no upfront fees, bid wording, keyword/automatic/product targeting, placement wording) and *ACOS* guide (ACoS and ROAS definitions and worked example); Amazon Ads *About us* (names Sponsored Products; no history); Wikipedia, *Dunnhumby* (founding 24 May 1989, Humby and Dunn, 1994 Tesco trials, supplier clients) and *Tesco Clubcard* (launch 13 February 1995); this vault's `lineage/performance-marketing-agencies.md` for GoTo.com and `history/retail-media-networks.md` for the scanner-to-loyalty-card chain (vault material, not independent corroboration). WebSearch was unavailable this session (session cap reached); the Internet Archive was offline, so no archived launch page could be checked. ⚠️ **Not established:** the year Sponsored Products launched, whether it began as a closed beta, and who at Amazon designed it — Wikipedia's *Amazon Advertising* and *Amazon Ads* titles returned 404, Amazon's pages give no history, and the vault's own history note records the same gap. The claim that attribution counts brand-name searches is the vault's problem framing, not a statement in Amazon's documentation.
