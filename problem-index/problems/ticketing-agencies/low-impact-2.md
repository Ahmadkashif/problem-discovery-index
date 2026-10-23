# Broker Inventory Across Five Marketplaces

**Industry:** [[ticketing-agencies|Ticketing & Reservation Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A resale broker lists the same seat on StubHub, Vivid Seats, SeatGeek, TickPick and Gametime at once, and has to delist it everywhere the second it sells and deliver it before a deadline set by the marketplace, using tools built for selling sweaters.
**Tags:** #feature-engineering #time-series-forecasting #gradient-boosting #evaluation-metrics #data-integration #automation #workflow-orchestration

## The Problem
A professional broker buys inventory at onsales and from season-ticket holders, then lists it across every major resale marketplace to reach the most buyers. When a seat sells on one, it must disappear from the others within seconds, or the broker sells it twice and owes a penalty or a replacement ticket at whatever the market now charges. Then the seat has to be delivered. Most tickets are now mobile, so delivery means transferring the ticket from the account that bought it to the buyer through Ticketmaster, AXS or a team's app. Many venues restrict transfers until days before the show, and each marketplace sets its own delivery deadline and penalty schedule.

Prices also have to move. A broker holding a few thousand seats across a hundred events reprices daily against competing listings, and in states with resale caps the reprice must stay under a percentage of face value.

## What Already Exists
Multichannel e-commerce tools such as ChannelAdvisor (now Rithum) and Linnworks keep product inventory in sync across marketplaces. The ticket industry has its own point-of-sale tools: SkyBox (owned by Vivid Seats), Ticketmaster's TradeDesk, Automatiq and TicketNetwork's broker tools, with marketplace APIs and pricing rules.

## The Customisation Gap
The generic tools assume fungible stock counted in units; a ticket is a unique seat with an event date that destroys its value. The broker-specific logic is: seat-level identity across marketplaces that describe the same seat differently (section aliases, row letters, piggyback pairs); delisting latency measured in seconds; a transfer calendar that knows each venue's and team's transfer restrictions and each marketplace's deadline; pricing that respects state resale caps and the marketplace's fee display; and reconciliation of payouts net of marketplace fees and penalties. The broker POS tools cover parts of this, but they are owned by marketplaces with their own interests, and the transfer and penalty workflow is still run from email and phone alerts.

## Impact If Solved
A broker with ten staff could cut double-sales and late-delivery penalties, often several percent of gross sales on a bad weekend (estimate), and free fulfilment staff from manual transfers in the 48 hours before each show, while staying inside the new state caps without a separate compliance check.
