# Monday Morning in Four Retailer Portals

**Industry:** [[consumer-products-makers|Consumer Products Makers]]
**Type:** Worker Life Changing
**One-liner:** The demand planner at a mid-sized maker spends the first day of every week downloading point-of-sale and inventory reports from each retailer's portal into one spreadsheet, and would get back a day a week and a seat in the decisions that matter if that data arrived joined and checked.
**Tags:** #time-series-forecasting #temporal-fusion-transformers #k-nearest-neighbors #large-language-models #worker-facing #data-integration #automation

## The Problem
At a maker selling candles, cleaning tools or writing instruments to big-box retail, one person, often titled demand planner or sales analyst, owns the numbers. Every Monday they log into Walmart's supplier data platform (Scintilla, formerly Luminate), Target's partner portal, Amazon Vendor Central, Home Depot's or Lowe's vendor portal and a club or dollar-store portal, export last week's sales, store and distribution-centre inventory and open orders, and paste them into a workbook. Item numbers differ by retailer, weeks start on different days, and one portal changed its export layout last month. By Tuesday the workbook is ready for the meeting where sales, operations and finance decide what to make.

The questions that matter are the hard ones. Is the new holiday scent selling through fast enough to justify a re-order before the retailer's last order date? Which stores are out of stock on the hero SKU while the distribution centre holds plenty? Is the back-to-school marker set on track, or will the retailer send it back? There is little time left for them after the copying.

## Why It Matters to the Worker
The job is described as analysis and is mostly data handling. The planner is the person everyone blames when the plant built too much or too little, yet spends most of their week on the step before the judgement. They work late in season because the retailer's sell-through report lands the same morning the re-order call is due, and they are the single point of failure: when they are on holiday, nobody else can rebuild the workbook.

There is a career cost too. The planners who learn to forecast seasonal and new products well are valuable, but the role rarely gives them the hours to get good at it.

## What a Solution Looks Like
Retailer data that arrives on its own. Connectors pull each portal's sales, inventory and order data on schedule, map retailer item numbers to the maker's SKUs, align calendars and flag gaps and layout changes. The planner opens a single view on Monday morning: sell-through against plan by SKU and retailer, store out-of-stocks against distribution-centre stock, new and seasonal items compared with similar past launches, and re-order recommendations with a confidence band and the retailer's cut-off dates. They spend the meeting on the exceptions.

## Impact If Solved
A day a week back for the planner, roughly 50 days a year (estimate), and re-order and build decisions made on data that is a day old rather than four. The planner's role moves from report builder to the person who calls the season.
