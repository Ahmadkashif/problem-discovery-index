# History: Affiliate Networks

**Industry:** [[industries/affiliate-networks|Affiliate Networks]]
**Primary Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**Secondary Wave:** [[series/eras/wave-09-programmatic|9 — Programmatic]]
**Episode Tier:** 1
**Transferable Pattern:** Whoever built the tool that computes credit decides, by accident, what "contribution" means for everyone downstream — and thirty years later the industry's biggest payees are frequently the parties best positioned to sit closest to that tool's blind spot.

> **No Origin Parent.** A search of every `origins/*/legacy.md` inheritance table turns up nothing for this industry, and that is a genuine finding rather than an omission. Unlike online marketplaces (which inherits its playbook from Online Travel Agencies) or e-commerce sellers (which inherits an unsolved cost-attribution problem from Package Carriers), affiliate networks were not born by a pre-existing industry moving onto the web. The mechanism this file describes — commission for a referred sale — long predates computing. What is native to this wave is not the *idea*, but the specific, accidental *machinery* that came to compute it.

## Before the Cookie

Paying someone for sending you a customer is not a web-era idea. Mail-order catalogues ran referral codes; direct-response television and radio used per-inquiry ("P.I.") deals with local stations going back decades; door-to-door and multi-level sales structures paid a finder's fee for an introduction. All of it required a human being, or at best a printed code, to record who deserved credit — which meant it was slow to reconcile, easy to dispute, and available only to advertisers large enough to run the paperwork.

What the commercial web changed was not the commission relationship. It was the **cost of computing who gets paid** — and, critically, *what that computation was capable of seeing.*

## The Origin Event

**November 1994.** **CDNow's "BuyWeb" programme** is a commonly cited early instance of a website paying another site for a referred sale — predating what most retrospectives treat as the category's beginning.

**1989, scaled by patent in 1996.** **PC Flowers & Gifts**, founded by William J. Tobin, launched on the Prodigy network in 1989 and applied for a patent on the affiliate-commission model on **22 January 1996** — a paper trail that predates Amazon's programme by six months and is the industry's own documentary answer to who actually originated pay-for-referral commerce online.

**July 1996.** **Amazon Associates** launches. It was not the first affiliate programme, and the vault's spine research has already flagged and killed the claim that it was. What Amazon did was **scale** the model past anything that preceded it, using its own already-vast catalogue as the inventory every publisher could plausibly link to.

> **Myth, killed at source.** "Amazon invented affiliate marketing" does not survive the CDNow and PC Flowers & Gifts dates above. Amazon scaled a mechanism that already existed; the scaling, not the invention, is the actual event worth dating.

The dedicated network layer followed within two years: **Commission Junction (CJ Affiliate) founded 1998**, consolidating merchant-publisher relationships that had previously been negotiated one at a time. *(LinkShare's and ShareASale's founding dates are widely reported as 1996 and 2000 respectively in trade retrospectives; I could not independently re-verify either against a primary source this session and flag both as approximate.)*

## What Became Cheap

**Computing, automatically and at scale, who gets credit for a sale that started somewhere else.** Before the cookie, "who referred this customer" required a printed code, a phone script, or a human matching an order to a mailing list. After it, a small file dropped in a browser could carry that answer silently across an entire session, and a network could reconcile millions of these against confirmed transactions without a person touching most of them.

**What that machinery could not do is the entire remaining story of this industry: it could only reliably answer *whose cookie was still there at the moment of purchase* — not who actually persuaded the buyer to want the product.** [[series/eras/wave-05-commercial-web|Wave 5]]'s own spine finding applies here with unusual precision, because affiliate tracking is the mechanism the finding was written about: DoubleClick's cookie tooling (founded Feb 1996) could reliably capture only the last touch before a conversion, and **last-click became the measurement the infrastructure could produce, not what anyone believed was correct.** Amazon Associates ran on the same logic from the same year, and — this vault's own hub note for the industry states it without qualification — **"affiliate networks still do."**

## How It Was Actually Solved — the mechanism, and its blind spot

A publisher's link carries a tracking parameter. A click drops a cookie, typically valid for a window from twenty-four hours to thirty days or more depending on the merchant's terms. If a purchase happens before that cookie expires, the network's server-side postback matches the sale back to the cookie and assigns commission to whichever publisher's cookie is present — and if more than one publisher's cookie is present, **the rule is almost universally last-one-in, last one credited.**

This is not a flaw introduced by any one network. It is the only rule the underlying data structure supports cheaply: a cookie does not carry a history of every publisher a shopper encountered, only whichever one wrote to it most recently. A rule that credited the *first* touch, or split credit across the *whole* path, would require a persistent, cross-site identity graph that nobody in 1996 had the infrastructure, or frankly the legal standing, to build. Last-click was not chosen. It was what the tool in hand could compute.

## The Contest — and the Thesis It Killed

**23 December 2024.** YouTuber MegaLag published an investigation alleging that **Honey**, the PayPal-owned browser extension, was silently overwriting other publishers' affiliate links at checkout — crediting itself with sales **even when it applied no coupon at all**, a mechanised version of the cookie-stuffing this vault's own hub note lists as a known category of fraud. The mechanism is exactly the one described above, weaponised: Honey's extension fired last, at the one moment that is definitionally decisive under a last-click rule, regardless of whether it had contributed anything a shopper could not have gotten without it.

Content creators — the publishers who had actually reviewed the product, wired an audience to it, and done the persuading days or weeks earlier — got nothing, because their cookie was no longer the one present at checkout. Honey lost roughly **3 million of its 20 million users within two weeks** of the video; by May 2025 the loss exceeded **4 million users**, Google had amended Chrome Web Store policy (**March 2025**) to bar extensions from claiming affiliate commission without providing an actual discount, and class actions had been filed against comparable extensions, including Capital One Shopping and Microsoft Shopping.

**PayPal's own defence is the closing artefact this file needs.** Asked to respond, PayPal told USA Today: *"Honey follows industry rules and practices, including last-click attribution."* That is not a denial. It is confirmation, from the accused party, that the mechanism functioned exactly as the industry's own rulebook says it should — and that the rulebook, not any one company's misconduct, is the actual object at fault.

**What died in this contest was not a company** — Honey still operates, modified. **What died was the public thesis that a browser extension sitting between a shopper and checkout is a neutral convenience rather than a claim on credit that belongs to whoever did the harder, earlier work of persuasion.** That thesis had been assumed, quietly, since the extension category began; it did not survive December 2024 in a form anyone can still defend in public.

## What's Still Open

- [[problems/affiliate-networks/high-impact|🔴 Paying the Last Click, Which Is Usually the Party That Did the Least]] — this file's entire mechanism, stated as the vault's own top problem for the industry
- [[niches/affiliate-networks/commission-attribution/profile|Commission Attribution]] and [[niches/affiliate-networks/channel-incrementality-verification/profile|Channel Incrementality Verification]] — measuring what last-click cannot
- [[niches/affiliate-networks/publisher-earnings-intelligence/profile|Publisher Earnings Intelligence]] — the creator with five dashboards and no way to know what actually earned
- [[niches/affiliate-networks/the-publisher-side/profile|The Publisher Side]] and [[niches/affiliate-networks/the-affiliate-manager/profile|The Affiliate Manager]] — the two humans standing on either side of the same unaudited rule
- [[niches/affiliate-networks/the-compliance-analyst/profile|The Compliance Analyst]] — policing the fraud category the Honey case made undeniable

## The Transferable Pattern

> **The party that built the measurement tool rarely intends to redefine merit — but whoever's tool computes credit ends up defining, by what the tool happens to be able to see, what "contribution" means for every participant downstream. Nobody voted on last-click. Everybody now has to build a business inside it.**

This vault's own hub note for the industry states the reason the fix keeps not happening, and it is worth repeating exactly because it generalises past affiliate marketing entirely: the network is the only party positioned to measure what each partner type actually contributes, and doing so would move a large share of commission away from the parties nearest the measurement tool's blind spot — who are, not coincidentally, **often the incumbent networks' own largest publishers.** An FDE should treat "who profits from the current metric" as the first diagnostic question whenever a measurement convention looks technically indefensible but institutionally unshakeable.

**Sources:** Wikipedia, *Affiliate marketing*, *Commission Junction*, *Honey (browser extension)* (via direct article retrieval, Sept 2026); MegaLag investigation (published 23 December 2024) and subsequent trade/consumer press coverage of the Honey/PayPal controversy; PayPal statement to USA Today on last-click attribution; Google Chrome Web Store policy update, March 2025; this vault's `industries/affiliate-networks.md` and `series/eras/wave-05-commercial-web.md`.
