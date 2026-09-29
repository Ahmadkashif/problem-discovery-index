# Capacity Planning From Live Events

**Niche:** [[niches/streaming-video-platforms/streaming-reliability/profile|Streaming Reliability]]
**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Ticketing, betting and live sport streaming all plan for a known spike on a known date, and on-demand platforms plan from the average.
**Tags:** #time-series-forecasting #optimization-fundamentals #evaluation-metrics #confidence-intervals #monte-carlo-methods #automation #descriptive-statistics #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to survive the moment when a hundred million dollars of marketing delivers every subscriber to the same play button at the same second — and whoever predicts and absorbs that concentration keeps the launch that pays for the year.

## The Problem
Several industries live with extreme, scheduled, self-created demand spikes and have built the practice for it: ticketing for an on-sale, betting around a major event, live sport streaming at kick-off, retail on a sale day. They forecast from marketing and registration signals, provision for a multiple of the forecast, design queueing and degradation, and rehearse. On-demand streaming faces the same shape at every major launch and largely plans from historical averages.

## What Already Exists
Event-driven capacity forecasting from registration and marketing signals; virtual queueing and admission control; graceful degradation design; full-scale rehearsal practice; and post-event capacity review.

## The Customization Gap
The adaptation is to a spike whose degradation options are unusually constrained. It requires: (1) degradation that must preserve the viewing experience, since a queue is acceptable for a ticket purchase and unacceptable for a film someone sat down to watch — this shapes every mitigation; (2) delivery across every device type and network condition simultaneously, which is a far wider client surface than a web on-sale; (3) demand created by a marketing campaign rather than by a registration list, so the signal is softer and must be modelled; (4) a global release window with staggered territories, which both helps and complicates; and (5) a failure that damages a content investment rather than only a transaction.

## Target Customer
Engineering and reliability leadership, content and marketing leadership, content delivery vendors, and capacity planning vendors from event industries.

## Impact If Solved
Event industries plan for exactly this shape and rehearse it, and on-demand platforms plan from averages. The constraint is that queueing is unacceptable here, which makes graceful degradation of the stream itself the central design problem.
