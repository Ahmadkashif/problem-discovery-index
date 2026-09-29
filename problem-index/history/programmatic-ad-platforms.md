# History: Programmatic Ad Platforms

**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Primary Wave:** [[series/eras/wave-09-programmatic|9 — Programmatic]]
**Secondary Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**Origin Parent:** [[origins/ad-holding-companies/profile|Ad Holding Companies]]
**Episode Tier:** 1
**Transferable Pattern:** An industry will optimise against the metric its tooling can observe, not the outcome it was hired to produce — and will then defend that metric long after everyone knows it is wrong.

## Before the Auction

*(This industry has no pre-computer era. It was born inside one. See the template note in `series/_bookmark.md` — "Before the Computer" does not fit a Wave 9 child and has been renamed here.)*

Advertising was bought in blocks. A page, a slot, a week, negotiated between two people in advance and priced from panel-based audience estimates. The unit of trade was **inventory**, not attention, and the buyer could not distinguish between two impressions of the same slot — because nobody could observe them separately.

The economic consequence was waste at the bottom. Remnant inventory — the impressions that did not sell through the direct sales force — was close to worthless, not because nobody wanted it but because **the cost of transacting it exceeded what it would fetch.** You cannot profitably negotiate a deal worth a fraction of a cent.

## The Origin Event

**Right Media went live on April 1 2005**, with dynamic CPM pricing from mid-2004. **AdECN** was operational by **October 2005**. The idea in both cases was the same and it is simple enough to state in a sentence: **auction each impression individually, and clear it in the time a page takes to load.**

Yahoo bought Right Media in 2007 for $680M; Microsoft bought AdECN. **Google's DoubleClick Ad Exchange in 2009** brought the model to mass scale, and the **OpenRTB** specification (2010, adopted by the IAB as 2.1 in **January 2012**) standardised how the parties talked to each other.

> **Correction — this industry is routinely mis-dated.** "RTB was invented in 2009" is the common claim and it is wrong by four years. 2009 is when Google scaled it. The mechanism was running commercially in April 2005. An episode that repeats the 2009 date is repeating Google's version of the history.

## What Became Cheap

**Pricing attention, one impression at a time.**

Remnant inventory stopped being waste and became a liquid market. More consequentially, the buyer stopped buying *placements* and started buying *people*: if you can identify who is behind the impression, the publisher's identity stops mattering and you bid on the audience wherever it appears.

That reversal — **from context to identity** — created every business in this vault's Adtech & Martech category. All eleven of them presuppose a stable cross-application identifier.

## How It Was Actually Solved

The mechanism is worth stating precisely, because the failure is inside it.

**The loop.** A page begins loading. The publisher's supply-side platform broadcasts a bid request — describing the slot, the page, and whatever it knows about the user — to many demand-side platforms at once. Each DSP has roughly 100 milliseconds to decide what this impression is worth to it and return a bid. The auction clears, the winner's creative is fetched and rendered, and the page finishes loading. The user notices nothing.

**The valuation.** Each DSP is solving a prediction problem under a hard latency budget: *given this user, this context, this moment, what is the probability of the outcome I am being paid for, and what is that outcome worth?* Early systems predicted click-through rate; later ones predict conversion, and some predict incremental conversion.

**The auction design.** The industry ran second-price auctions for most of its history, then moved broadly to first-price around the late 2010s as header bidding made second-price behaviour strategically incoherent. *(The direction of this shift is well established; I have not verified precise dates in this session — treat the timing as approximate and check before it goes in a script.)*

**The training signal — and here is the whole problem.** The model needs to learn from outcomes. The outcome the advertiser actually cares about is a sale. But the sale is observed by the *advertiser*, in *their* analytics, **thirty days later**, aggregated past the point where it can be joined back to the impression that caused it.

So the industry trained on what it could observe immediately: **the click.** And the click convention itself was not designed — it was inherited from [[series/eras/wave-05-commercial-web|Wave 5]], where DoubleClick's 1996 cookie tooling could reliably capture the last touch before a conversion and nothing else.

This vault's own hub note states the consequence without knowing its ancestry: *"the bid is priced in ten milliseconds against a click, because the sale it was supposed to cause is observed by the advertiser a month later and never joined back to the impression."*

## The Trade-Off

**The industry traded the outcome it was paid to produce for the proxy it could measure in time to train on.**

That was a real trade, not a mistake, and in 2005 it was the only available one. The honest accounting of what it cost:

- **Optimisation collapsed toward the bottom of the funnel.** Last-click credits whatever touched the user most recently, so budget flows to retargeting and branded search — the cheapest conversions to claim and frequently the ones that would have happened anyway.
- **Incrementality became unmeasurable in the system that spends the money.** You can measure it in a holdout experiment. You cannot measure it in the bidder, and the bidder is what allocates the budget.
- **The measurement became structurally self-serving.** The party selling the impressions also counts the conversions. Retail media is the extreme case and this vault documents it: last-click ROAS, reported inside a closed loop, by the seller.

Note the shape. **The data is present, complete, and in one company's hands. The honest number is smaller than the reported one. No new technique is required — only a party willing to compute and publish.** That is the **declined join**, and this industry is its purest expression.

## The Graveyard

**Apple, iOS 14.5, April 26 2021.** App Tracking Transparency made IDFA access opt-in rather than opt-out. Announced at WWDC in June 2020 and delayed to give developers time, it was still the largest disruption to mobile targeting and attribution the industry has experienced.

An industry built on an identifier discovered that the identifier belonged to Apple.

Third-party cookie deprecation has been the same story on a longer and far more erratic timeline. And the replacements — UID2, RampID, Topics, publisher first-party data — have fragmented reach measurement while the pricing models still assume the deterministic identity that no longer exists.

The **ANA's 2023 programmatic transparency study** supplied the other half of the obituary: a meaningful share of spend reaching made-for-advertising inventory, and reconciliation between what a buyer pays and what a publisher receives routinely losing about a quarter of the money to fees nobody can enumerate.

**There is no single corpse here and that is the point.** No company died the way People Express did. What died was a *thesis* — that identity would remain stable, observable and cheap — and it was killed by a platform owner's product decision rather than by a competitor.

## What's Still Open

The vault's existing analysis is downstream of everything above, and reads differently once you know the history:

- [[problems/programmatic-ad-platforms/high-impact|🔴 The ten-millisecond bid priced against a click]] — the missing join, inherited from 1996, now the industry's defining constraint
- [[niches/programmatic-ad-platforms/outcome-feedback-and-bid-valuation/profile|Outcome Feedback & Bid Valuation]] — closing the loop the auction was built without
- [[niches/programmatic-ad-platforms/incrementality-and-budget-allocation/profile|Incrementality & Budget Allocation]] — measuring what last-click cannot
- [[niches/programmatic-ad-platforms/supply-path-and-inventory-quality/profile|Supply Path & Inventory Quality]] — the ANA finding, as a business
- [[niches/programmatic-ad-platforms/spend-reconciliation-and-fees/profile|Spend Reconciliation & Fees]] — the quarter of the money nobody can enumerate
- [[niches/programmatic-ad-platforms/the-media-trader/profile|The Media Trader]] — the person dragging budget sliders to hit a delivery number

## The Transferable Pattern

> **Find what the organisation optimises against, then ask who chose that metric and when. Frequently nobody chose it — a tool could observe it, everyone built on it, and it became the definition of performance.**

An FDE arriving at any measurement-driven business should ask three questions in this order:

1. **What outcome is the customer actually paying for?**
2. **What does the system currently train on?**
3. **Why are those different — is it latency, ownership, or unwillingness?**

The answer to the third determines whether this is an engineering problem or a political one. **Latency** and **ownership** are the missing join, and are buildable. **Unwillingness** is the declined join, and is not — a better model will not make a company publish a number that shrinks its invoice.

Programmatic is the best available case study because it contains all three, layered chronologically: latency in 2005, ownership in 2009, and unwillingness by 2015.

**Sources:** Infectious Media, *The birth of real-time bidding*; AdExchanger (Right Media, AdECN); UMG, OpenRTB history; IAB OpenRTB 2.1 (Jan 2012); Orange Cyberdefense and Apple developer documentation (ATT, iOS 14.5, April 26 2021); ANA 2023 Programmatic Media Supply Chain Transparency Study; grokipedia.com, *DoubleClick*; mi-3.com.au (last-click attribution history, Greg Stuart/IAB) — **unverified: an H5 pass searched and found no corroboration; the URL returns 403. Do not rely on the quote or the 2004/2009 IAB dates; the mechanism argument stands without them.**; this vault's `industries/programmatic-ad-platforms.md`.
