# A Rate a Small Shipper Can Check

**Niche:** [[niches/freight-tech-platforms/small-shipper-freight-buying/profile|Small Shipper Freight Buying]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A business shipping four loads a month is quoted a rate by a broker who knows the market and has no way to evaluate it, because every rate benchmark in the industry is sold to people who ship thousands.
**Tags:** #gradient-boosting #time-series-forecasting #confidence-intervals #evaluation-metrics #descriptive-statistics #hypothesis-testing #revenue-impact #transfer-learning
**Contested on:** Every serious competitor selling freight to small shippers is fighting to give a business with no volume a rate it can trust and a way to check it — and whoever makes pricing legible to a shipper with no leverage takes the segment.

## The Problem
A manufacturer needs to move a truckload from Cleveland to Atlanta on Thursday. The broker quotes $2,900. Is that reasonable? The answer depends on the current spot market on that lane, the day of week, the equipment type, how tight capacity is this week, and how much lead time the shipment has — all of which are knowable and none of which the shipper has access to. The rate benchmarking subscriptions that would answer it are priced and packaged for shippers with volume. So the shipper accepts, or calls a second broker and takes the lower of two numbers, which is a comparison rather than an evaluation.

## Why Nobody Has Built This
Rate data has been a subscription business sold to the parties with the volume to justify it, and the small shipper is a poor subscription customer — infrequent need, low willingness to pay, high acquisition cost. The information asymmetry is also, for brokers, a source of margin, which means the party best placed to provide the benchmark has a reason not to. And a benchmark for an occasional shipper has to be right on a specific lane on a specific week rather than on an average, which is a harder estimation problem than a lane average precisely because the shipper's question is narrow.

## What to Build
A lane-level rate estimate delivered per shipment rather than as a subscription, expressed as a range with the factors that move it named — this lane, this equipment, this week, this lead time. Estimation combines public and commercially available market signal with the shipper's own accumulated quote history and, where a platform has one, a pooled corpus of quotes and accepted rates. The output is not a number to argue with but a context: this quote sits at the high end of the range for this lane this week, largely because the pickup is in two days. Accumulate the shipper's history into something useful — lanes shipped, rates paid, seasonality — so that a business shipping fifty loads a year eventually has a position rather than a stack of invoices. Be honest about uncertainty on thin lanes, because a confident wrong benchmark will cost the shipper a broker relationship over nothing.

## Target Customer
Small and mid-size manufacturers, distributors and e-commerce businesses shipping occasionally, and the digital freight platforms whose differentiation could be transparency rather than speed.

## Impact If Built
The gap between an informed and an uninformed rate on a single truckload is frequently several hundred dollars, which for a business shipping fifty loads a year is real money and is currently a pure transfer to the better-informed party. The accumulated history is the longer-term value: it converts an occasional buyer with no leverage into one with a documented pattern, which is the only foundation for any better arrangement.
