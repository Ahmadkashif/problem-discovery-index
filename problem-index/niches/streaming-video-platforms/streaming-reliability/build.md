# Engineering for the Deliberate Spike

**Niche:** [[niches/streaming-video-platforms/streaming-reliability/profile|Streaming Reliability]]
**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platform creates its own worst load event on a date it chose and is surprised by it.
**Tags:** #time-series-forecasting #change-point-detection #evaluation-metrics #confidence-intervals #automation #gradient-boosting #monte-carlo-methods #optimization-fundamentals
**Contested on:** Every serious competitor in this niche is fighting to survive the moment when a hundred million dollars of marketing delivers every subscriber to the same play button at the same second — and whoever predicts and absorbs that concentration keeps the launch that pays for the year.

## The Problem
A major release drops at midnight. Marketing has spent months creating exactly this concentration of demand. Millions of people press play within minutes, from every device type, across every network, in every territory in the release window. The peak is many times normal, it is entirely self-created, and platforms are regularly caught by it — with the failure visible publicly at the precise moment the investment was supposed to pay off.

## Why Nobody Has Built This
Capacity planning is driven by historical traffic patterns, so a self-created discontinuity is outside the model — a forecast built on what happened before cannot see a peak that a marketing campaign is about to manufacture. Marketing's demand signals sit in a different organisation from the engineering forecast. Rehearsing a launch at full scale is expensive and rarely done. And the failures are infrequent enough to be treated as bad luck.

## What to Build
Forecast the peak from the demand being created, and fail gracefully when it is exceeded. Forecast launch demand from marketing spend, pre-release signals, watchlist additions, territory mix and comparable launches, which is the core and is the forecast nobody builds because the inputs cross an organisational boundary. Model the shape of the spike rather than its total, since the concentration in the first minutes is what breaks systems. Design graceful degradation deliberately — lower bitrates, simplified interfaces, queued starts — because a degraded stream is enormously better than a failed one and the alternative is currently binary. Rehearse at full scale before major launches, as a launch that has never been tested at its predicted peak is a hope. Instrument client-side failure, since a substantial share of what viewers experience is invisible in server metrics. Prioritise the play path over everything else under load, because a viewer who cannot browse but can watch is a viewer who is fine. Coordinate with marketing on the release shape, as a staggered start is a reliability decision that is currently a marketing one. Quantify the business cost of a launch failure, which makes the investment case and has never been computed. Run the incident response with the public communication planned in advance, since a silent platform during a public failure compounds it. And review every launch against the forecast, so the model improves with each one.

## Target Customer
Engineering and reliability leadership, marketing leadership creating the demand, content leadership whose launch depends on it, and infrastructure vendors serving streaming.

## Impact If Built
A forecast built on historical traffic cannot see a peak that a marketing campaign is about to manufacture, and the inputs sit in another organisation. Forecasting launch demand from the spend and pre-release signals that created it is the missing model.
