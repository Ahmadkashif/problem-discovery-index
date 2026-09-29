# The Mechanism: Real-Time Bidding, and the Commission's Return in Disguise

**Origin:** [[origins/ad-holding-companies/profile|Ad Holding Companies]]
**Tags:** #optimization-fundamentals #probability-distributions #evaluation-metrics #revenue-impact #data-integration #causal-inference #compliance

## Part One: What RTB Actually Computes

Before programmatic, advertising was bought in **blocks** — a page, a placement, a week of airtime — negotiated between humans in advance, priced against an audience *estimate* drawn from panel research. The buyer could not distinguish between two impressions of the same slot; a visitor who had already bought the product and a visitor who had never heard of it were priced identically, because the unit of sale was the placement, not the person seeing it.

**Right Media's exchange, live from 1 April 2005**, changed the unit of sale to the individual impression, auctioned in the time it took a web page to load. **AdECN was operational by October 2005.** **Yahoo bought Right Media in 2007 for $680 million**; Microsoft bought AdECN the same year. **Google's DoubleClick Ad Exchange, launched 2009, brought the mechanism to mass scale** — RTB rose from roughly **2% of UK display spend in 2010 to 18% by 2011** — and the **OpenRTB** specification, standardised by the IAB from 2010 (version 2.1 in January 2012), let the exchanges, demand-side platforms and supply-side platforms speak a common protocol.

Mechanically: for every ad slot a webpage renders, an auction runs among buyers bidding for the right to show an ad to *that specific viewer*, informed by whatever data the buyer holds on that viewer — browsing history, prior purchases, demographic inference — and the highest bid (typically clearing at a second-price-adjacent rule) wins the impression before the page finishes loading.

## Part Two: The Rebate, Mechanically Restored

[[origins/ad-holding-companies/origin-story|The origin story]] traces the 15% commission's uneven death across the 1980s–90s. [[origins/ad-holding-companies/the-fight|The Fight]] documents its reappearance as undisclosed rebates. What the mechanism section adds is **why programmatic made the reappearance easier, not harder, to hide**.

A block media buy has a visible, comparable price — a full-page ad in a named publication for a named week. A programmatic buy clears at a price set by an auction across an opaque stack of exchanges, DSPs, SSPs and data providers, each able to take a margin, and the price the advertiser is billed can differ from what the publisher was actually paid by a spread that is structurally hard to observe without a specialist audit. **An undisclosed markup buried in that chain functions economically exactly like the old 15% commission — a percentage captured regardless of outcome — while being far better concealed than a disclosed flat rate ever was.**

This is not asserted lightly: the ANA's own transparency work has documented a **partial resurgence of 15%-equivalent economics inside programmatic**, via exactly this undisclosed-markup and rebate structure. **Fee-based compensation did not fully replace commission-based compensation — the commission changed shape and moved into a layer with less visibility, not less existence.**

## The Two Myths This Kills

**Myth one: "The 15% commission had a clean end date."** It did not. It eroded gradually from the 1980s, and its economic function has partially resurfaced inside programmatic's opaque intermediary chain. The industry never fully left the commission model; it changed the model's visibility.

**Myth two: "Programmatic killed agency margins."** An oversimplification the recent consolidation data does not support. Margins are currently **expanding for the surviving major holding groups** — driven by consolidation and cost discipline, most visibly in the Omnicom–IPG combination (see [[origins/ad-holding-companies/legacy|Legacy]]) — while programmatic's fee compression squeezed **mid-tier and independent agencies** disproportionately, who lacked the scale to negotiate favourable exchange and data terms. The industry did not uniformly lose margin; the smaller players did.

## The Transferable Pattern

> **A compensation structure that is banned, deregulated or exposed does not necessarily disappear — it frequently relocates to whichever layer of the transaction is least visible to the party paying for it, and each new layer of technical intermediation is a new place for it to hide.**

An FDE evaluating a marketing-attribution or programmatic-adjacent product should ask, before anything else: **can the advertiser actually see the full chain of who was paid what, or is opacity itself part of somebody's business model?**

**Sources:** Right Media, AdECN, Yahoo and Microsoft acquisition records (2005–07); Google DoubleClick Ad Exchange launch (2009); IAB OpenRTB specification history (2010, v2.1 January 2012); IAB UK and industry trade data on RTB share of display spend (2010–11); ANA and K2 Intelligence, *An Independent Study of Media Transparency in the U.S. Advertising Industry* (2016), on the persistence and partial resurgence of commission-equivalent economics.
