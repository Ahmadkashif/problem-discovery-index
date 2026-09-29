# Lineage: Affiliate Networks

**Industry:** [[industries/affiliate-networks|Affiliate Networks]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** the Amazon Associates referral link — an associate ID embedded in a product URL and stored against the item in a persistent shopping cart (US Patent 6,029,141)
**Builder:** Amazon
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Paying for a referred customer was old. Computing it was not.

A mail-order referral or per-inquiry radio deal needed a printed code or a person matching an order to a source. That kept the arrangement to a handful of large partners, because every partner added reconciliation work. A bookseller with a catalogue of millions of titles had the opposite need: thousands of small websites, each able to sell a few books to a niche audience, none worth a phone call.

Amazon's own patent states the constraint plainly. An online merchant could not let customers handle the product or talk to a salesperson, writing reviews for a catalogue that size was impractical, and conventional advertising was expensive and hard to measure. The referral had to be recorded, credited and paid with no human in the loop, or the long tail of small referrers could not exist.

## What Got Built

A link that carried its own paperwork.

The patent, filed **27 June 1997** and granted **22 February 2000**, describes the machinery of the programme Amazon had launched in **July 1996**. An associate registers through automated software on the merchant's site. Its pages carry "referral links" with an identifier embedded in the URL in a predefined format — the patent's example string identifies both the referring associate and a commission scheme. When a customer follows the link, the associate ID is stored in the shopping cart **alongside the specific item selected**. The cart persists for an extended period — the patent gives one week — and the site uses cookies to reconnect a returning customer to it. On purchase, commission is computed as a fixed percentage of the selling price and paid periodically, the example being quarterly. Associates receive a weekly report of orders, link clicks and credit earned.

Self-service sign-up, an ID in the link, a cookie, a window, a percentage, a dashboard: all here.

## Who Built It, And Why Them

**Amazon**, and the patent names Jeffrey P. Bezos, Sheldon J. Kaphan, Ellen L. Ratajak and Thomas K. Schonhoff as inventors.

Amazon was not first. CDNow's BuyWeb programme dates to November 1994, and PC Flowers & Gifts ran an affiliate programme with 2,600 partners in 1995 and filed its own patent application on 22 January 1996. The party anecdote — Bezos meeting a woman who wanted to sell divorce books from her site — comes from Amazon's own FAQ and is treated sceptically.

Why them is the catalogue. A florist or a music retailer could offer partners a few hundred products. Amazon could offer a link to almost any book any website mentioned, so nearly every content site was a plausible associate. That volume only paid if registration, tracking and payout were fully automated — which is why the machinery Amazon patented is almost entirely about removing the human: registration, crediting, payment and reporting, each automated.

## What It Cost

The design answered "who sent this item?", not "who persuaded this buyer?".

Amazon keyed credit to the line item: whichever associate's link put a book in the cart earned on that book. When independent networks generalised the model across thousands of merchants from 1998 onward, the merchant's cart was no longer theirs to annotate. What remained portable was the cookie and the window, and a single cookie holds one referrer. Credit therefore went to whoever wrote to it last. The item-level record Amazon started with thinned into the last-click rule the industry now runs on — a rule a browser extension firing on a checkout page is built to exploit.

## What You Still Touch

Every affiliate link still carries an ID, sets a cookie with a window, pays a percentage and reports to a dashboard. The unsolved question is one the 1997 design never had to ask: what each touch contributed.

- [[problems/affiliate-networks/high-impact|🔴 Paying the Last Click, Which Is Usually the Party That Did the Least]] — the cookie-and-window rule, stripped of the per-item record
- [[problems/affiliate-networks/worker-life-2|🟢 The Publisher Who Cannot Tell What Earns]] — five copies of the weekly report
- [[niches/affiliate-networks/commission-attribution/profile|Commission Attribution]]
- [[niches/affiliate-networks/channel-incrementality-verification/profile|Channel Incrementality Verification]]

**Sources:** Google Patents, US 6,029,141 A, *Internet-based customer referral system* (filed 27 June 1997, issued 22 February 2000; inventors Bezos, Kaphan, Ratajak, Schonhoff; background problem statement, URL-embedded associate ID, per-item referrer stored in cart, one-week cart persistence, cookies, fixed-percentage commission, quarterly payment, Weekly Activity Report — all read from the patent text); Wikipedia, *Affiliate marketing* (Amazon Associates launch July 1996; CDNow BuyWeb November 1994; PC Flowers & Gifts 1995 website with 2,600 partners, patent application 22 January 1996, US 6,141,666 issued 31 October 2000); ClickZ, *History of Affiliate Marketing* (party anecdote, sourced to Amazon's Associates FAQ, and questioned there); this vault's `history/affiliate-networks.md` (cited as vault material, not independent corroboration). ⚠️ **Not established:** when Amazon moved from per-item cart attribution to the cookie-window model it uses today, and whether the July 1996 launch version already worked as the 1997 patent describes — the patent postdates launch by a year. The claim that later networks inherited the cookie-and-last-referrer rule is inferred from how a single cookie works, not from a dated primary source on Commission Junction's or LinkShare's original tracking design.
