# Rotation Engine for Exchange-Privilege Fixtures

**Niche:** [[niches/greeting-card-publishers/independent-store-fixture-programs/profile|Independent Store Fixture Programs]]
**Industry:** [[industries/greeting-card-publishers|Greeting Card Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A mid-size publisher with fixtures in thousands of independent stores decides which designs to swap in each store from a rep's memory, while the reorder history of every store, read together, says which designs sell where.
**Tags:** #k-nearest-neighbors #bayesian-inference #time-series-forecasting #feature-engineering #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to keep its own fixture in each independent store stocked with sellers, rotating slow designs out on its exchange terms with the fewest rep visits, and whoever turns pocket counts into automatic replenishment and rotation keeps the fixture when the owner reconsiders the space.

## The Problem
Exchange privileges are how a card publisher keeps an independent fixture fresh: slow designs go back for credit and new ones go in. Which designs to swap, and which new ones to send, is decided by the rep on the visit or by a customer service clerk filling a standard pack. A design that sells well in garden centres and hospital gift shops may be dead in a college bookstore, and the publisher's reorder data could show that, but nobody reads it by store type.

## Why Nobody Has Built This
Independent stores rarely share point-of-sale data, so the only signal is reorders by stock number, which are lumpy and late. Publishers in this channel are small, with no data team. Wholesale platforms see orders across many brands but not pocket-level rotation inside one publisher's fixture.

## What to Build
A rotation engine that infers each design's sell rate per store from reorder intervals and exchange returns, pools across similar stores (by store type, region and size) to estimate how a design would perform in a store that has never carried it, and proposes the exchange for each store at each visit or reorder: what to pull, what to send, and why. It learns from the next reorder whether the swap worked.

## Target Customer
VP of Sales or Specialty Channel Director at card publishers with 1,000–20,000 independent fixture accounts (estimate).

## Impact If Built
Fixtures that earn more per square foot are the ones store owners keep. Better rotation raises reorders per account and cuts the cost of exchanges that send the wrong designs back and forth.
