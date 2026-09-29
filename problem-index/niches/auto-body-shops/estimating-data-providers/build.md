# Supplement History as a Correction Signal on Labor Times

**Niche:** [[niches/auto-body-shops/estimating-data-providers/profile|Collision Estimating Data Providers]]
**Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every supplement is a written record of where the published estimate was wrong, the platform carries millions of them, and none of it is routed back to the researchers who set the labor times.
**Tags:** #gradient-boosting #feature-engineering #causal-inference #evaluation-metrics #cross-validation #bert #transformers #time-series-forecasting #data-integration #revenue-impact

## The Problem
A labor time in the database is a prediction: this operation on this vehicle takes this long. The industry then generates an enormous stream of evidence about that prediction and discards it. Thirty to fifty percent of initial estimates are revised by supplement once the vehicle is disassembled, and each supplement is a structured document naming exactly which operations were added, which times were increased, and — in the notes — why. Across the platform this amounts to millions of labeled corrections a year, keyed to vehicle, damage pattern, and operation. The research organization that maintains the times does not use it. Times are set and revised by study — a researcher observes or reasons through the operation — and validated against industry feedback that arrives as complaint volume rather than as data. The firm publishing the numbers the whole industry argues about holds the only dataset capable of settling those arguments and does not consult it.

## Why Nobody Has Built This
The supplement stream is noisy in ways that make naive use dangerous. A supplement can reflect a genuinely wrong labor time, hidden damage that no estimate could have anticipated, an estimator padding against a known-tight allowance, or a negotiated settlement bearing little relation to work performed. Treating all of these as evidence that a time is too low would ratchet times upward and destroy the product's credibility with the insurers who license it — which is the commercial reason the connection has never been made. There is also a positioning problem the firm feels acutely: it sells to both sides of the argument, and a system that visibly adjusts times toward observed reality will be read by whichever side it moves against as capture by the other.

## What to Build
An engine that treats supplements as a noisy but analyzable correction signal, with the confounders modelled rather than ignored. Each supplement is decomposed into its component adjustments and classified by cause — hidden damage discovered at disassembly, operation omitted from the initial estimate, time adjusted on an operation that was present, administrative or negotiated change — using the structured line items together with the free-text notes. Only the third category bears on labor time accuracy, and separating it out is the whole technical problem. With that separation, the accumulated evidence supports what the research organization currently cannot do: identify operations where observed time systematically diverges from published time, quantify how much of the divergence is explained by damage severity and vehicle configuration rather than by the allowance itself, and rank the research backlog by how much disputed dollar volume each entry drives. Outputs are evidence for researchers rather than automatic adjustments — the credibility of the database depends on a human owning every published number.

## Target Customer
Chief product officers and VPs of data at estimating providers running 300-1,500 researchers, and the research directors who currently set and defend labor times without access to the outcome data their own platform generates.

## Impact If Built
Turns the platform's transaction exhaust into the defence of its core product. The strategic value is in credibility rather than efficiency: a provider that can show a labor time is supported by observed outcomes across tens of thousands of repairs, with confounders separated, holds a position neither a shop association survey nor an insurer's internal analysis can contest. It also concentrates a large research organization on the entries that actually drive dispute, which is not where the effort currently goes.
