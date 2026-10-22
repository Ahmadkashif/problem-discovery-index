# The Traffic Director and Tomorrow's Log

**Industry:** [[broadcast-stations|Broadcast TV & Radio Stations]]
**Type:** Worker Life Changing
**One-liner:** Every afternoon a station's traffic director has to turn hundreds of orders, copy instructions and late changes into tomorrow's on-air log with no missed spots and no conflicts, and spends evenings fixing what arrived after the log closed.
**Tags:** #large-language-models #transformers #seq2seq #dynamic-programming #optimization-fundamentals #worker-facing #automation #workflow-orchestration

## The Problem
The log is the station's legal and commercial record of what will air, unit by unit. The traffic director, often with one or two assistants per TV station or radio cluster (estimate), builds it daily from the traffic system's scheduled orders. Then comes everything the system cannot do alone. Copy has to be matched to orders using rotation instructions that arrive as agency emails, PDFs and portal messages. Ad-ID or ISCI codes that do not match must be chased. Competitive separations (two car dealers, two law firms) have to be resolved by moving spots within dayparts. Preemptions and makegoods follow the sales manager's priorities. Programs run long, and the ballgame goes to extra innings. A TV station can carry ~2,000–4,000 spots a week (estimate). After the log goes to master control or automation, changes keep arriving: new copy for tomorrow morning, an advertiser pulling a spot after a news event, a political order that must run tonight.

Errors are expensive and visible. A spot aired with the wrong copy or outside the ordered window becomes a credit or makegood. A missed political spot can become a complaint. Every discrepancy then returns at month-end, when affidavits and invoices are reconciled against what the agency ordered.

## Why It Matters to the Worker
Traffic is the job everyone depends on and no one sees until something goes wrong. The director absorbs the sales staff's late promises, the agencies' late copy and the newsroom's schedule changes, and is blamed for the resulting discrepancy. Evenings and weekends disappear in the weeks before holidays and elections, when order volume peaks and political orders bring legal exposure. Stations have hubbed traffic for several markets into one centre. That means one person handling several stations' logs, buyers and copy rules at once, and losing the local knowledge that used to prevent errors.

The skill itself is tacit and stressful: knowing which agency's "rotate evenly" means equal weighting and which means "whatever fits", which advertisers will tolerate a move and which will audit. It is rarely documented. When an experienced traffic director leaves, the error rate rises for months.

## What a Solution Looks Like
Copy instructions read from email and PDF and turned into structured rotation rules attached to the right order, with low-confidence items shown for confirmation rather than guessed. A log optimiser that resolves separations and placement against the order windows and the sales manager's priorities, and explains each move. Late changes applied with a clear before-and-after and an automatic note to the salesperson and the agency. A discrepancy view for each spot that will need a makegood, raised before air rather than at month-end, so the director fixes problems while they are still cheap.

## Impact If Solved
Taking the copy-matching and conflict-solving half of the day off the traffic desk would give back ~1–2 hours a day per traffic person (estimate) and cut month-end discrepancies. That is the difference between a hubbed traffic centre that drowns in late changes and one that can absorb another market. For the worker, it means leaving when the log closes rather than when the last email arrives.
