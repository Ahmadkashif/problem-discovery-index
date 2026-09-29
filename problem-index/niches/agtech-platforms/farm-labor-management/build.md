# A Record the Worker Can Check

**Niche:** [[niches/agtech-platforms/farm-labor-management/profile|Farm Labour Management]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A farmworker's pay depends on a piece count made by someone else on a paper ticket and on hours recorded by someone else on a sheet, and the worker has no independent record of either.
**Tags:** #cnns #object-detection #evaluation-metrics #confidence-intervals #compliance #data-integration #worker-facing #automation
**Contested on:** Every serious competitor in farm labour software is fighting to make piece-rate pay, hours and compliance provable to the worker as well as to the regulator — and whoever makes the record trusted by both sides takes the operation.

## The Problem
A worker picks fruit all day. Each bin is credited by a crew leader who marks a ticket. At the end of the week a pay statement arrives with a total. Whether the count is right, whether all the hours were recorded, and whether the minimum wage make-up was calculated correctly are all things the worker cannot check, because they have no record of their own. Most of the time the count is right and the employer is honest. The structural fact remains that one party holds the entire record of a transaction that determines the other party's income, and disputes are resolved by whoever has documentation, which is never the worker.

## Why Nobody Has Built This
Agricultural labour software is sold to employers, whose requirements are payroll accuracy and compliance documentation, and a worker-facing record is not among them — in some framings it is actively unattractive. The workforce is also seasonal, mobile, frequently without reliable smartphone access in the field, and multilingual, which makes a worker-facing product genuinely harder to deliver than an employer-facing one. Both obstacles are real; neither explains the complete absence of the capability, which is better explained by who the customer is.

## What to Build
A record generated at the point of work and visible to both parties. Piece credit is captured at the collection point — a scan, a tag, or an image count — and attributed to the individual worker, not to a crew, which removes the largest category of dispute at its source. Hours are captured at clock-in and clock-out on a shared device or a badge, timestamped and located. The worker sees their own running total in their own language on whatever device they have, or on a printed daily slip where they do not, which costs nothing and is the version that actually reaches everyone. Pay computation, including the minimum wage make-up, is shown with its arithmetic rather than as a total. Disputes are raised against a specific entry and resolved against a record rather than a recollection. For the employer this is better compliance documentation than they currently hold and fewer disputes; for the worker it is the first independent view of their own earnings. Building it for both parties is what makes it credible, and building it for one is what every previous product has done.

## Target Customer
Labour-intensive specialty crop operations, farm labour contractors, H-2A employers with substantial documentation obligations, and the worker advocacy and legal services organisations who see the disputes.

## Impact If Built
Individual attribution and a worker-visible record remove the most common source of pay disputes in agricultural labour and give both parties documentation they currently lack. For the employer the compliance improvement is real and the dispute reduction is immediate; for the worker it is the difference between being paid on trust and being paid on a record they can see.
