# The Mechanism: What DINAMO Computed

**Origin:** [[origins/airlines/profile|Airlines]]
**Tags:** #time-series-forecasting #probability-distributions #optimization-fundamentals #conditional-probability-and-bayes-theorem #evaluation-metrics #revenue-impact

> This is the file an FDE should read twice. It is a worked example of turning a commercial question into a modelling problem, and of what the modelling gives up.

## The Question, Stated Properly

A flight departs in 60 days with 150 seats. Requests arrive over those 60 days. Leisure travellers book early and are price-sensitive; business travellers book late and are not. Seats sold cheaply today cannot be sold expensively tomorrow.

**How many seats should be available at each fare, at each point in time?**

Note what this is not. It is not "what price should this flight be." Yield management does not set *a* price — it sets **how many seats are released into each fare bucket**, and it revises that continuously as real bookings arrive. The fares themselves are relatively static. The **allocation** is the product.

## The Decomposition

**1. Forecast demand per fare class per departure.** For this route, this day of week, this season, this departure time, how many bookings will arrive in each fare class, and when? Built from historical booking curves for comparable flights.

**2. Model it as a distribution, not a number.** This is the load-bearing step and the one most often skipped. The output the decision needs is not "we expect 34 full-fare passengers." It is **the probability that full-fare demand exceeds N**, for every N. Expected values are useless here — the decision is about protecting against a tail.

**3. Compute the protection level.** Hold a seat back for full fare when the expected revenue from doing so exceeds the certain revenue from selling it now:

> *P(full-fare demand ≥ N) × full fare > discount fare*

Which rearranges to a strikingly simple rule — protect seats up to the point where **P(demand ≥ N) = discount fare / full fare**. If the discount is a quarter of the full fare, protect seats until the probability of needing them drops below 25%. This is Littlewood's rule, and the multi-class generalisation (EMSR) is the working version.

**4. Revise continuously.** Bookings arriving faster than forecast means tighten; slower means release. The system is a control loop, not a one-time calculation.

**5. Overbook on top.** Passengers fail to show. The no-show rate is itself forecastable, so sell more seats than exist, trading the cost of denied boarding against the cost of flying empty.

## Why This Was Hard in 1985

None of the mathematics is exotic — Littlewood's rule dates from 1972. What was hard was everything around it:

- **Continuous real-time inventory**, which only SABRE-class systems had. People Express structurally could not do this, which is the whole story of [[origins/airlines/the-fight|the fight]].
- **Enough history to forecast at the flight-date-fare-class level** — thousands of forecasts, revised daily, across a network.
- **The compute to re-solve nightly** across every flight and fare class.

**The algorithm was the cheap part. The data infrastructure was the moat.** That generalises to almost every opportunity in this vault.

## What It Gave Up — the trade-offs

**Price fairness was abandoned deliberately.** Two identical seats sell for wildly different amounts, and the industry accepted the customer resentment as the cost of the revenue. That resentment is now permanent and it is why airline pricing is a byword for arbitrariness.

**The model optimises revenue per flight, not per customer.** It is myopic by construction — it does not know that the passenger it just charged £900 will remember. Loyalty programmes were bolted on afterwards partly to offset damage yield management caused.

**It assumes the future resembles the past.** Booking curves learned from history fail precisely when behaviour shifts, and they fail confidently. Every demand shock since has broken these systems in the same way.

**It requires segments that stay separate.** The entire structure rests on business travellers being unable or unwilling to buy the cheap fare — hence Saturday-night stays and advance-purchase rules, which exist to *build a fence*, not to serve anyone. When the fences leak, the model leaks.

## The Transferable Pattern

> **When inventory is perishable and customers differ in willingness to pay, the profitable decision is not what to charge but how much to withhold — and the constraint on doing it well is almost never the mathematics.**

An FDE meeting a hotel, a freight lane, a clinic's appointment book, an ad impression or a consultant's billable hour is meeting this problem again.

**Sources:** Littlewood, *Forecasting and control of passenger bookings* (1972); Belobaba's EMSR work on multi-class seat inventory control; Robert G. Cross, *Revenue Management*; INFORMS Edelman Prize records (American Airlines).
