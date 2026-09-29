# Shipper Evidence Rules as Executable Content

**Niche:** [[niches/freight-tech-platforms/freight-document-accessorial-billing/profile|Document & Accessorial Billing]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Whether a detention charge gets paid depends on evidence requirements written into a specific shipper's routing guide, and those requirements live in a PDF and in a billing clerk's memory.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in freight billing is fighting to get an accessorial charge paid on first submission against a specific shipper's evidence rules — and whoever holds first-pass payment rate highest takes the account.

## The Problem
A truck sits at a receiver for six hours. Detention is chargeable under the rate confirmation. The shipper's routing guide requires notification in writing within two hours of free time expiring, arrival and departure times signed by facility personnel, and submission within seven days on a specific form. The driver did not get a signature because nobody at the dock would sign. The notification was not sent because the dispatcher was managing forty other loads. The charge is submitted on day eleven and denied. The detention genuinely happened, the evidence for it exists in the telematics data, and the money is gone for reasons entirely procedural.

## Why Nobody Has Built This
Routing guides are per-shipper documents in inconsistent formats that nobody has assembled, and the requirements they contain are buried in prose alongside everything else about how to service the account. Encoding them requires reading them, which is exactly the work billing clerks do inconsistently and by memory. There is also a resigned culture around this: accessorial denial is treated as a cost of doing business rather than as a solvable process problem, and the write-offs are aggregated in a way that hides how much of the loss is procedural.

## What to Build
Extract each shipper's accessorial requirements from the routing guide and the rate confirmation into executable rules: what is chargeable, what evidence is required, in what form, notified to whom, within what window, submitted by when. Then drive the operation from them. When a chargeable event begins — a truck crosses a geofence and free time starts — the clock starts and the required notification fires automatically to the right address in the right form. The evidence package assembles itself from what the systems hold: geofence timestamps, position trace, driver messages, photographs, the signed document if one was obtained. Submission happens within the window, complete, without a clerk remembering. Where a requirement cannot be satisfied — no signature was obtainable — the system says so at the time, when something can still be done, rather than at denial.

## Target Customer
Freight brokerages and carriers of any scale, freight audit and payment providers, and the TMS vendors whose accessorial modules produce an invoice and stop.

## Impact If Built
A meaningful share of legitimate accessorial revenue is lost to procedure, and procedure is exactly what software fixes. Automatic notification within the window is the single largest component and requires no judgement at all. The asymmetry is worth noting: the parties losing this money are carriers and brokers, and the smallest of them lose the most because they have the least billing capacity.
