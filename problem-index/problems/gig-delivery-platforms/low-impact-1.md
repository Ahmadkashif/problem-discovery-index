# Batching, Routing and Wait Time

**Industry:** [[gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Batched orders and merchant wait times are optimised for platform throughput and customer promise, and the courier absorbs the cost of every miscalculation.
**Tags:** #convex-optimization #time-series-forecasting #gradient-boosting #markov-decision-processes #confidence-intervals #evaluation-metrics #optimization-fundamentals #worker-facing

## The Problem
Dispatch decides which courier gets which order, whether to batch several orders together, and in what sequence. The optimisation targets delivery time promises, cost per order and merchant relationships. Courier earnings per hour are, at best, a constraint rather than an objective.

Batching is where the divergence is sharpest. Combining two orders raises platform efficiency and can leave the courier with a longer total route for a payment that does not reflect the added time, particularly when the second order comes from a merchant that is running late. Couriers experience batches as frequently unfavourable and cannot evaluate an offer's true cost in the seconds available.

Merchant wait is the other half. Some merchants are reliably late by a predictable amount at predictable hours, and the platform knows this from its own data. Dispatching a courier to arrive at the promised ready time rather than the actual ready time transfers the merchant's delay directly onto the courier as unpaid waiting.

Routing quality compounds it. Turn-by-turn guidance treats delivery as a driving problem and largely ignores the parts that consume the time — parking, building access, gated communities, apartment complexes with unclear unit layouts — which couriers solve from local knowledge that the platform does not capture.

## What Already Exists
Dispatch and batching optimisation at these platforms is genuinely sophisticated real-time operations research at very large scale. Demand forecasting drives incentive placement. Mapping and routing use standard commercial infrastructure. Some platforms surface merchant readiness signals and have built merchant-side tooling to improve order timing. Courier apps provide navigation and delivery instructions where customers supply them.

## The Customisation Gap
The objective function excludes the courier's realised hourly rate, and including it is the entire opportunity. Dispatch that accounted for expected net earnings per engaged hour — including predicted wait — would make different batching and assignment decisions, and the platform holds every input required.

Wait prediction is the most immediately actionable piece. Expected merchant delay by location and hour is estimable to useful precision from historical arrival-to-pickup intervals, and using it to time the dispatch rather than to construct a customer promise would remove a large share of unpaid waiting outright.

Batch evaluation for the courier is the third. The true marginal cost of accepting a batch — additional distance, additional wait, the risk of the second order being delayed — is computable and could be shown alongside the offer, so the decision is informed rather than a guess made in seconds.

And the local knowledge should be captured and returned. Which building entrance to use, where parking exists, how long a particular tower takes — couriers learn this repeatedly and individually, and aggregating it across a market would save time for everyone at essentially no cost.

## Impact If Solved
Batching and wait time are where a courier's realised hourly rate is actually determined, and both are currently optimised against objectives that treat their time as free. Wait-aware dispatch removes unpaid waiting that the platform can already predict, courier-visible batch economics make the accept decision informed, and shared local access knowledge is a pure efficiency gain that nobody has bothered to collect.
