# Succession Planning From Production Scheduling

**Niche:** [[niches/agtech-platforms/small-diversified-farms/profile|Small & Diversified Farms]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Planning successive plantings across beds to meet weekly harvest commitments is a production scheduling problem with capacity constraints, and it is solved every winter with a spreadsheet and a seed catalogue.
**Tags:** #optimization-fundamentals #dynamic-programming #combinatorics-and-counting #time-series-forecasting #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor selling to small diversified farms is fighting to make recordkeeping and compliance work for an operation with twenty crops, five sales channels and nobody in the office — and whoever gets the record-keeping burden lowest takes the segment.

## The Problem
A farm needs a steady weekly supply of a dozen vegetables for twenty-six weeks of subscription boxes, plus market volumes, plus wholesale commitments. Meeting that means planting successions at intervals determined by each crop's days to maturity and harvest window, across a limited number of beds, with rotation constraints, greenhouse capacity for transplants, and labour peaks that must not all coincide. The plan is built in a spreadsheet over several winter evenings, is wrong by June, and is rebuilt next winter from the same starting point.

## What Already Exists
Production scheduling with capacity and sequencing constraints is a mature operations research area with free solvers. Crop maturity and degree-day models are established agronomy and published per crop. Rotation constraint modelling is straightforward. Several crop planning tools exist in this segment and are essentially structured spreadsheets that compute dates. The solver-based approach is not used anywhere in the segment.

## The Customization Gap
The adaptation is to a biological production system with uncertain timing. It requires: (1) maturity as a distribution driven by accumulated heat rather than as a fixed days-to-maturity number, since the difference between a cool spring and a warm one moves a succession by two weeks and is the main reason plans fail; (2) demand expressed as commitments with different flexibility — a subscription box needs something every week and a wholesale order needs a specific crop on a specific date, and treating them identically over-constrains the plan; (3) bed and rotation constraints including the multi-year restrictions organic certification and disease management impose, which is what makes this harder than it looks; (4) labour smoothing as an objective rather than an afterthought, since a plan that puts three harvest peaks in the same week is infeasible for a crew of four regardless of what the beds allow; and (5) in-season replanning as the primary use, because the plan's value is in adapting when a succession comes in early or fails, and a winter-only planning tool misses most of its own purpose.

## Target Customer
Diversified vegetable operations of any scale, the crop planning tool vendors serving them, and the agricultural extension programmes that teach succession planning.

## Impact If Solved
The crop plan is the document a diversified farm runs on and is currently built by hand and abandoned mid-season. Heat-unit-driven maturity and labour smoothing are the two adaptations that make a generated plan better than a spreadsheet, and in-season replanning is what makes it a tool rather than a document.
