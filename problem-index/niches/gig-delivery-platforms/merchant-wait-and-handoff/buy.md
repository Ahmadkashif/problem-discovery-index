# Buy: Kitchen and Order Management Systems Adapted to Delivery Handoff

**Niche:** [[niches/gig-delivery-platforms/merchant-wait-and-handoff/profile|Merchant Wait & Handoff]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Kitchen display and order management systems sequence food for a dining room; delivery orders arrive with a courier already en route and a handoff the system does not model.
**Tags:** #time-series-forecasting #gradient-boosting #evaluation-metrics #data-integration #confidence-intervals #workflow-orchestration #automation #quick-win
**Contested on:** Whether restaurant order management software can treat an approaching courier as a constraint rather than a customer who happens to be standing there.

## The Problem

Restaurants run kitchen display systems, POS platforms and order management software, and the better ones sequence production well against dine-in and takeout demand. Delivery orders arrive into that system through an integration and are treated as takeout: a ticket with items and a target time.

What the system does not model is that a specific person is driving toward the restaurant right now, that their arrival time is known to the platform and predictable, that every minute they wait past readiness is a cost, and that food finished early sits and degrades while food finished late holds a courier. Delivery is a just-in-time production problem with an external clock, and the kitchen software has no representation of the clock.

## What Already Exists

Toast, Square, Olo, Otter, Chowly, Deliverect and the order-aggregation and kitchen-display category, covered more fully in [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]. Order injection from delivery platforms into POS. Kitchen display with routing by station. Prep-time configuration per item. Some demand forecasting at the larger chains. The integration plumbing is mature and widely deployed.

## The Customization Gap

**Courier ETA is available and unused.** The delivery platform knows when the courier will arrive and can push it. The kitchen system does not consume it, so production sequencing cannot target the handoff. Feeding courier ETA into the display as a live countdown — and re-sequencing against it — is the single highest-value change and is an integration rather than an invention.

**Prep times are configured, not learned.** Almost every merchant sets prep time as a static per-item or per-order value, entered once and never revisited, and it is wrong in the direction of optimism and wrong differently at 7pm than at 3pm. The POS holds order-to-ready timestamps and can learn the actual distribution by item, hour and current load. Nobody does this, and it is a straightforward forecasting problem on data already captured.

**The handoff is not an event in the system.** An order is marked ready and then something happens involving a shelf, a counter, a name called out and a courier finding it. That interval is frequently several minutes, is invisible to both the kitchen system and the platform's readiness model, and is where a large share of avoidable waiting lives. Instrumenting the handoff — a scan, a shelf assignment, a courier-facing pickup display — is a product gap nobody owns.

**Multi-platform orders are sequenced blind.** A merchant on three delivery platforms has three order streams, three sets of couriers and one kitchen, and no system sees all of it. Aggregators partially solve the ticket problem and not the sequencing problem. The merchant's actual production queue is the union, and the readiness prediction for any one platform is wrong without it.

**Nobody benchmarks the merchant.** The POS knows this restaurant's order-to-ready distribution. It does not know how that compares to comparable restaurants, which is the number that would prompt action. The vendor has that comparison across its entire customer base and does not surface it.

## Target Customer

Restaurant technology vendors and aggregators, for whom courier-aware sequencing and learned prep times are a real differentiator as delivery becomes a larger share of merchant volume. Also delivery platforms' own merchant tooling teams, who ship tablets into restaurants and could ship the countdown and the benchmark with them.

## Impact If Solved

The kitchen gets the one piece of information it lacks — when the courier arrives — and production can target it. Prep times become learned rather than guessed, which fixes the readiness estimate at its source. And the handoff becomes an instrumented event instead of the unmeasured gap where several minutes of every delivery disappear.
