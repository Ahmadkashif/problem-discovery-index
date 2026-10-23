# The Board Report Built From Six Dashboards

**Industry:** [[visitors-bureaus|Convention & Visitors Bureaus]]
**Type:** Worker Life Changing
**One-liner:** The bureau's research or marketing analyst rebuilds the monthly board report from hotel, rental, location, card and tax data that disagree with each other, then stands behind a number they know is soft when council members attack it.
**Tags:** #bayesian-inference #time-series-forecasting #large-language-models #descriptive-statistics #data-integration #worker-facing #automation

## The Problem
Each month someone at the bureau produces the destination performance report for the board and the city. At a large bureau it is a research manager. At most bureaus it is the marketing director or a communications coordinator doing it on top of their job. The inputs come from different vendors on different calendars. STR provides hotel occupancy, rate and RevPAR. AirDNA or Key Data covers vacation rentals. Placer.ai, Zartico or Datafy supply visitor counts and origin markets from mobile device panels, and Visa Spend Signals or a similar card product supplies visitor spending. Website analytics and campaign reports come from the agency, and the city sends hotel-tax collections ~2-3 months late (estimate).

The numbers never line up. Visitor counts from the location panel rise while hotel room nights fall. Card spending is up in a month when tax receipts are down. The panel's definition of a visitor (someone from more than 50 miles away, or an overnight stay, depending on the vendor) changes the answer by tens of percent (estimate). The analyst reconciles by hand, writes footnotes and picks the figure they can defend.

## Why It Matters to the Worker
The report is the bureau's public proof that the hotel tax is working, and it goes in front of people looking for a reason to cut the budget. In the 2025 DestinationNEXT survey, 42% of destination organisations said their funding was at risk. The analyst is the one asked, in a public meeting, why the visitor count went up when hotels say business is down. They know each vendor's caveats better than anyone in the room and cannot fully explain them.

The work is also lonely and repetitive. The same pulls, pastes and charts happen every month, in a bureau where nobody else understands the data well enough to check it or cover for a holiday.

## What a Solution Looks Like
A single destination data store that ingests every vendor feed on its own schedule, aligns definitions (visitor, overnight, day-tripper, origin market) and keeps the vendor caveats attached to each figure. The monthly report drafts itself: headline numbers, a reconciliation table showing where sources disagree and why, and a plain-language explanation of each change against last month and last year. When council members ask a question, the analyst can show which data says what and how confident each figure is, instead of defending a single number.

## Impact If Solved
Report production falls from ~3-5 days a month to under a day (estimate). The analyst goes into each hearing with an explanation instead of a guess, and the board gets numbers with their uncertainty stated, which is harder to attack than a single figure that later turns out wrong.
