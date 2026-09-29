# Wave 9 — Programmatic (2005–2021)

**Trigger:** Right Media exchange live April 1 2005 (dynamic CPM pricing from mid-2004); AdECN operational Oct 2005; Google's DoubleClick Ad Exchange 2009 brings scale; OpenRTB spec 2010, adopted by the IAB as 2.1 in Jan 2012
**Ended by:** **Apple App Tracking Transparency, iOS 14.5, April 26 2021**
**What went to ~zero:** the cost of **pricing attention, one impression at a time**
**Failure class produced:** the declined join at its most profitable

> This is the only wave in the spine with a **death date**, which makes it the best-shaped story in the vault: an entire industry built on an identifier, and then the identifier was switched off by a company that did not ask.

## What Was True The Day Before

Advertising was bought in blocks — a page, a slot, a week — negotiated between humans in advance, priced on audience estimates from panels. The unit of trade was inventory, not attention, and the buyer could not distinguish between two impressions of the same slot.

Remnant inventory, the stuff that did not sell, was nearly worthless because the cost of transacting it exceeded what it would fetch.

## The Trigger

Right Media built an exchange where each impression was auctioned individually, in the time it took a page to load. That is the entire idea: **make the unit of trade the impression, and clear it in an auction.** Remnant inventory stopped being waste and became a liquid market.

*(Correction, and an important one: RTB is routinely dated to 2009. That is wrong. Right Media was live in April 2005 and AdECN by October 2005. 2009 — DoubleClick Ad Exchange — is when RTB reached mass scale, and OpenRTB standardisation did not land until 2010–12. 2009 is a scaling milestone, not an origin.)*

## What Became Possible

Buying an audience rather than a placement. If you can identify the person behind the impression, the publisher's identity stops mattering and you bid on the user wherever they appear. That reversal — **from context to identity** — is what created the entire adtech and martech stack in this vault, and every business in it presupposed a stable cross-app identifier.

## The Competitive Fight

**Who owns the identifier**, and therefore who owns the audience graph. Exchanges, DSPs, SSPs, data management platforms and identity resolution vendors were all fighting over the same asset: the ability to say "this impression and that impression are the same person."

The publisher lost that fight comprehensively. Once the buyer could find the audience anywhere, the publisher's leverage collapsed to whatever the auction cleared at — which is the mechanism behind the decline of local news in this vault, and it is a market-structure story, not a story about journalism.

## What It Broke

**ATT ended it.** iOS 14.5, April 26 2021, made IDFA access opt-in rather than opt-out. Announced at WWDC in June 2020 and delayed to give developers time, it was nonetheless the single largest disruption to mobile targeting and attribution to date. An industry built on an identifier discovered that the identifier belonged to Apple.

**The deeper break is measurement, and it long predates ATT.** The whole stack reported on the last-click convention inherited from Wave 5 — a measurement chosen because cookies could produce it, not because it was right. Programmatic then industrialised that convention and priced against it.

This is the **declined join** in its highest-margin form. Retail media networks reporting last-click ROAS on their own closed loop; affiliate networks on last-click; attribution vendors selling multi-touch models that the buying systems then ignore. In every case the data is present, complete and in one company's hands, and the honest number is smaller than the reported one. **No new technique is required. Only a party willing to compute and publish.**

That the vault found this shape independently, across six adtech industries, before anyone here had drawn a timeline, is the strongest evidence the chronology-of-failure thesis is real.

## Children in This Vault

**Primary:**
- [[industries/audio-adtech-networks|Audio Adtech Networks]]
- [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
- [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
- [[industries/retail-media-networks|Retail Media Networks]]
- [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
- [[industries/privacy-tech-vendors|Privacy Tech Vendors]]

**Secondary:**
- [[industries/affiliate-networks|Affiliate Networks]]
- [[industries/app-marketing-firms|App Marketing Firms]]
- [[industries/customer-data-platforms|Customer Data Platforms]]
- [[industries/performance-marketing-agencies|Performance Marketing Agencies]]
- [[industries/d2c-brand-operators|D2C Brand Operators]]
- [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
- [[industries/creator-talent-agencies|Creator Talent Agencies]]
- [[industries/digital-native-publishers|Digital Native Publishers]]
- [[industries/conversion-optimization-firms|Conversion Optimization Firms]]
- [[industries/mobile-game-publishers|Mobile Game Publishers]]
- [[industries/news-media-local|Local News Media]]
- [[industries/marketing-agencies-smb|SMB Marketing Agencies]]
- [[industries/ecommerce-sellers|E-Commerce Sellers]]

**Sources:** Infectious Media, *The birth of real-time bidding*; AdExchanger (Right Media, AdECN); UMG, OpenRTB history; IAB OpenRTB 2.1 (Jan 2012); Orange Cyberdefense and Apple developer documentation (ATT, iOS 14.5, April 26 2021).
