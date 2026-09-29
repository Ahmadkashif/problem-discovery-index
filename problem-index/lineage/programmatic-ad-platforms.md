# Lineage: Programmatic Ad Platforms

**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Wave:** [[series/eras/wave-09-programmatic|9 — Programmatic]]
**The tool:** the OpenRTB bid request and bid response — a JSON object pair in which an exchange describes one impression opportunity with a millisecond deadline (`tmax`) and a floor (`bidfloor`), and a buyer answers with a CPM `price` and win, billing and loss notice URLs
**Builder:** IAB Tech Lab
**Builder in vault:** **ABSENT**
**Verification:** partial — origin dates verified against the specification's own history; motive is inference, see Sources

## The Problem That Came First

By 2010 an advertiser could buy a single impression rather than a block of them, but only if its buying platform and the publisher's selling platform could talk.

Without a common format, every pairing was bespoke. A demand-side platform that wanted to bid into a supply-side platform's inventory wrote an integration to that SSP's interface; the next SSP had a different one. The work scaled with the number of pairs, not the number of companies — engineering time spent on plumbing rather than bidding.

**The constraint was the cost of connecting, not the cost of deciding.** Bidding models existed. What did not exist was a common way to ask the question they were meant to answer.

## What Got Built

A pair of messages.

The **bid request** describes one or more impression opportunities: the site or app, the device, the user as far as the exchange knows them (`buyeruid`, derived from a cookie sync), a minimum price in `bidfloor`, the auction type in `at` — "1 = First Price, 2 = Second Price Plus" — and `tmax`, the milliseconds the exchange will wait before giving up.

The **bid response** returns a `price` "expressed as CPM although the actual transaction is for a unit impression only," plus three notice URLs: `nurl` when the bid wins, `burl` when the win becomes billable "based on exchange-specific business policy," and `lurl` when it loses.

The versions track the market: 2.0 unified display, mobile and video in June 2011; 2.2 added private-marketplace deals; 2.3 native; 2.4 audio; 2.5 header bidding and billing and loss notifications; 2.6 ad pods for connected TV.

## Who Built It, And Why Them

OpenRTB began, per its own specification, "as a pilot project between three demand-side platforms (DataXu, MediaMath, and Turn) and three sell-side platforms (Admeld, PubMatic, and The Rubicon Project) in November 2010." **Its first product was not a bid protocol at all but a block-list format**, released December 2010 — a standard way to tell a seller what a buyer refused to appear beside.

The bid protocol itself came from mobile. Nexage, a mobile exchange, proposed an API specification for the real-time request/response; a subcommittee of DataXu, Fiksu and [X+1] on the buy side and Nexage, PubMatic, Smaato and Jumptap on the sell side produced OpenRTB Mobile 1.0 in February 2011. OpenRTB was adopted as an IAB Tech Lab standard in January 2012 with version 2.1.

Why those parties — and this is inference, not the spec's account: they were the **mid-sized independents on both sides of the auction**. Each gained more from a shared interface than from a proprietary one, because the value of any single DSP rose with every SSP it could reach cheaply. The trade body arrived to own a standard that already ran, which is why this note is keyed to IAB Tech Lab as the standard's owner while the design credit belongs to the pilot companies.

## What It Cost

**The protocol carries the impression out and the price back — and nothing else.** There is no field for what the ad caused. The notices report winning, billing and losing; the sale, if one happens, occurs weeks later in a system the exchange never sees. A bidder optimising on OpenRTB optimises against whatever signal it can join back, which in practice means the click.

`burl` fires on "exchange-specific business policy," so what counts as billable was left to each exchange. And `buyeruid` depends on a cookie sync, which tied the whole identity layer to third-party cookies that later disappeared.

## What You Still Touch

Every banner that loads a beat after the page does is waiting on `tmax`.

- [[problems/programmatic-ad-platforms/high-impact|🔴 Bidding Against an Outcome Nobody Returns]] — the missing field in the bid response
- [[problems/programmatic-ad-platforms/worker-life-2|🟢 Ad Ops and the Discrepancy That Never Closes]] — billing left to exchange policy
- [[niches/programmatic-ad-platforms/outcome-feedback-and-bid-valuation/profile|Outcome Feedback & Bid Valuation]]
- [[niches/programmatic-ad-platforms/identity-and-addressability/profile|Identity & Addressability]]

**Sources:** IAB Tech Lab, *OpenRTB API Specification Version 2.6* (raw file from GitHub InteractiveAdvertisingBureau/openrtb2.x, `2.6.md`), §1.2 *History of OpenRTB* (November 2010 pilot and its six members, December 2010 block-list 1.0, Nexage proposal, February 2011 Mobile 1.0, June 2011 2.0, January 2012 IAB adoption with 2.1), §1.3 version history, and field definitions for `at`, `tmax`, `bidfloor`, `buyeruid`, `price`, `nurl`, `burl`, `lurl`; GitHub InteractiveAdvertisingBureau/openrtb README (3.0 on master; Programmatic Supply Chain Commit Group). WebSearch was unavailable this session (session cap reached); research was by WebFetch and direct download. ⚠️ **Not established:** the individual engineers who drafted the pilot or the Nexage proposal; the claim that bespoke pairwise integrations were the motivating cost is inference from the pilot's membership and first deliverables, not a statement in the spec. Wikipedia's *OpenRTB* page returned 404; its *Real-time bidding* article has no origin history.
