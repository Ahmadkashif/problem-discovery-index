# Lineage: Virtual Economy Operators

**Industry:** [[industries/virtual-economy-operators|Virtual Economy Operators]]
**Wave:** [[series/eras/wave-10-creator-platform|10 — The Creator Platform]]
**The tool:** the Steam Community Market — Valve's first-party order book for in-game items, opened in beta for Team Fortress 2 in December 2012, settled only in Steam Wallet funds that cannot be withdrawn, with a Steam fee and a separate per-game publisher fee taken on every sale
**Builder:** Valve
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Valve had already made its hats worth money, and had no place for the price to live.

The Mann-Conomy Update to *Team Fortress 2*, released 30 September 2010, added three things at once: the Mann Co. Store, which sold items for Steam Wallet funds; a trading system for swapping items between players; and crates whose rare "Unusual" contents could only be unlocked. The same update announced that "some items that used to be rare will become more common when they are available for purchase" and marked the older copies "Vintage" to keep them scarce. That sentence is monetary policy written as patch notes.

Trading of items and unopened gifts across Steam followed in September 2011. So Valve was now issuing a good, setting its supply, and letting it change hands — but every trade was a private negotiation: find a counterparty, agree a swap, hope the other side delivered. There was no price, only barter and rumour.

## What Got Built

A market with listings instead of haggling. A seller posts an item at an asking price; a buyer pays from their Steam Wallet; the item moves inside Steam's inventory system and the wallet balances settle, with no counterparty to trust.

Two design choices define it. **Fees are split in two**: per the Team Fortress Wiki, a Steam transaction fee of 5% plus a game-specific fee — 10% for *Team Fortress 2* — so the publisher of the item is paid on every resale. And **proceeds stay in the Steam Wallet**: money can come in but not go back out as cash.

## Who Built It, And Why Them

Valve, because it already owned every layer the market needed — the item database, the inventory, the wallet and the store — and it was the issuer of the goods being traded.

An outside marketplace could list the items but could not move them atomically or collect the issuer's cut. Only the party that controls the ledger can make a trade settle in one step, and only an issuer has a reason to want a royalty on the secondary market. Valve's stated aim was efficiency — buyers "will be able to locate them faster, folks looking to sell items will find the process a lot more efficient" — but the shape of the fee says who the market was for.

## What It Cost

The closed wallet solved a regulatory problem and created a larger one. Because proceeds could not be cashed out, the official market was not a money-transmission business — but real-money demand did not go away. Per Wikipedia, third-party sites used Steam's trading API to connect player inventories and settle outside Valve's fee and its $1,800 wallet ceiling, paying out through PayPal or Bitcoin.

The *Counter-Strike: Global Offensive* Arms Deal update of August 2013 put tradable weapon skins behind that same machinery, and skins became stakes. A Connecticut lawsuit filed in June 2016 accused Valve and three sites of facilitating illegal gambling; Valve said in July 2016 it was cracking down on those sites; and on 5 October 2016 Washington State regulators ordered it to stop allowing skin transfers for gambling.

The theft problem arrived by the same road: in March 2016 Valve put 15-day holds on traded items unless the account used the Steam Guard Mobile Authenticator — deliberately slowing its own settlement to make stolen inventories recoverable.

## What You Still Touch

Every drop rate, crate and limited release is still issuance into a market with a public price, and the operator still sets supply with no model of what it does to that price.

- [[problems/virtual-economy-operators/high-impact|🔴 Running a Monetary Policy Without Admitting It]] — the Mann-Conomy sentence, scaled up
- [[problems/virtual-economy-operators/worker-life-2|🟢 The Support Agent Recovering a Stolen Inventory]] — why trade holds exist
- [[niches/virtual-economy-operators/gambling-adjacency/profile|Gambling Adjacency]] — the off-platform settlement the closed wallet pushed outward
- [[niches/virtual-economy-operators/price-discovery-and-market-data/profile|Price Discovery & Market Data]]

**Sources:** Team Fortress Wiki, *Mann-Conomy Update* (30 September 2010; Mann Co. Store, trading, Vintage quote) and *Steam Community Market* (5% Steam fee, 10% TF2 fee, Valve's stated purpose, 7-day untradability of market purchases); Wikipedia, *Steam (service)* (December 2012 beta, TF2 first, September 2011 trading, March 2016 15-day holds, July 2016 crackdown, wallet-only funds) and *Skin gambling* (third-party API use, $1,800 limit, August 2013 Arms Deal, June 2016 lawsuit, 5 October 2016 Washington order). WebSearch was unavailable this session (budget exhausted); research was by WebFetch. ⚠️ **Not established:** the exact day of the December 2012 beta; Valve's primary announcement and Steam's own fee FAQ could not be retrieved (the support pages redirected to shells without content). Wikipedia gives the combined fee as 15%, consistent with 5% + 10% but not confirmed against a Valve primary source. The individual Valve engineers behind the market were not identified.
