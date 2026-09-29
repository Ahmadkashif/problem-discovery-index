# The Mechanism: Name Your Own Price

**Origin:** [[origins/online-travel-agencies/profile|Online Travel Agencies]]
**Tags:** #probability-distributions #conditional-probability-and-bayes-theorem #optimization-fundamentals #evaluation-metrics #revenue-impact #data-integration #causal-inference

> Priceline's mechanism is usually described as a reverse auction. It was not one, and the difference is the entire lesson.

## What It Looked Like To The Customer

Name a route, name dates, name a price. Priceline would tell you, within moments, whether you had a ticket — at a fare you named, on a carrier it would not reveal until after you had committed to buy.

Consumers experienced this as haggling with the market. It felt probabilistic, a little bit like gambling, and Priceline's marketing leaned into exactly that framing.

## What Was Actually Happening

There was no auction. There was no bidding pool of competing sellers responding to your offer in real time. Instead:

1. **Airlines and hotels pre-set a hidden minimum threshold price** with Priceline, privately, in advance — a floor below which they would not sell that inventory, for that route or room type, in that window.
2. **The customer named a price blind to which supplier they were dealing with.**
3. **Priceline checked the named price against the relevant sellers' hidden floors.** If the bid cleared a floor, the system executed the transaction automatically and told the customer which airline or hotel they had "won." If it did not clear any floor, the bid was rejected (with limited resubmission allowed).

This is not a reverse auction. It is closer to a **blind clearing mechanism against a set of undisclosed reservation prices** — the interesting object here is not the bid, it is the seller's floor, which Priceline never disclosed and the customer never learned even after transacting.

## Why Sellers Agreed To This At All

The mechanism solved a real problem for airlines and hotels: **how to sell perishable, zero-marginal-cost excess inventory without publicly discounting the posted fare.**

A hotel with unsold rooms three days out, or an airline with unsold seats close to departure, loses that inventory's value entirely once the date passes. But publicly cutting the posted rate damages what a full-fare customer expects to pay, and a public discount is hard to walk back. Priceline let the same inventory clear at a discount **without ever publishing it** — invisible to anyone but the bidder who cleared the floor.

This is structurally identical to the fare fences in [[origins/airlines/the-mechanism|Airlines' mechanism file]] — Saturday-night stays, advance-purchase rules, non-refundability — devices that let a seller charge two prices for one seat without the customers comparing notes. Priceline automated the fence and hid the floor entirely, rather than encoding it as a visible restriction.

## What It Gave Up

**The customer never learned whether they overpaid.** A bid clearing well above the floor executed at the full named price — Priceline cleared at what the customer named, not at the floor. Customers had every incentive to underbid repeatedly, which Priceline limited by capping resubmissions and requiring rebooking between attempts.

**It only worked for price-elastic segments.** A business traveller needing a specific flight will not blind-bid; the mechanism captured only the leisure, flexible-date segment — the same segment yield management protects against, approached from the opposite direction.

**Priceline discontinued Name Your Own Price for flights in 2016**, by which point online fare comparison had made hidden-floor blind bidding a much smaller advantage than it had been in 1998 — customers could simply compare visible prices across OTAs instead of gambling on an invisible one.

## The Transferable Pattern

> **A price-discrimination mechanism does not need to look like price discrimination. Hiding the seller's reservation price from the buyer, rather than hiding the discount from other buyers, is a second way to build the same fence — and it works exactly as long as the buyer has no cheaper way to find the true market price.**

**Sources:** Priceline Group S-1 and subsequent 10-K filings describing the Name Your Own Price mechanism; Wikipedia, *Priceline.com*; contemporary (late 1990s–2000s) trade press on Priceline's model; Priceline Group public statements on discontinuing NYOP for airline tickets, 2016.
