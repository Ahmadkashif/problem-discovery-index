# Representment Assembled Against the Specific Reason Code

**Niche:** [[niches/retail-pos-platforms/chargeback-dispute-operations/profile|Chargeback & Dispute Operations]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Card networks publish exactly what evidence rebuts each dispute reason code, the platform holds that evidence, and representments are assembled from a template by whoever has time before the deadline.
**Tags:** #large-language-models #bert #gradient-boosting #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in dispute operations is fighting to win a representment against the card network's own evidence rules before the deadline — and whoever holds win rate highest per dollar of effort takes the merchant.

## The Problem
A dispute arrives under a reason code meaning the cardholder claims the goods were not received. What rebuts it is specific and published: proof of delivery to the cardholder's address, the address verification result at authorisation, and evidence of prior undisputed orders to the same address. The merchant's platform holds all three. The merchant, who is running a shop, receives a notification with a form and a deadline, attaches a screenshot of an order confirmation, and loses. The loss was not on the merits.

## Why Nobody Has Built This
Dispute handling has been treated as a merchant-facing form rather than as an automated evidence assembly problem, and the specialist vendors that do it well operate as services with analysts rather than as software the platform embeds. The rules differ by network and change periodically, which makes them content to be maintained — the same maintenance problem as court rules and screening ordinances, and solvable the same way. And the economics have been fuzzy: a platform that does not measure win rate by reason code cannot see how much a better representment is worth, so the investment case is never made.

## What to Build
An evidence-assembly engine driven by the reason code. Each network's reason codes are encoded with their rebuttal requirements and deadlines as maintained content. When a dispute arrives, the engine identifies the evidence the code requires, retrieves what the platform holds — transaction detail, authorisation results, delivery confirmation and tracking, customer communications, device and IP data, prior order history with the same cardholder, terms acceptance records — and assembles a representment in the required format. Where a required element is missing, the merchant is told exactly what is needed rather than presented with a blank form. Win probability is estimated per dispute so a merchant can decline to fight one that is not winnable, which is a legitimate answer nobody currently gives them. Deadlines are tracked and escalate, because a missed deadline is an automatic loss and is the most avoidable failure in the process.

## Target Customer
POS platforms and acquirers with merchant bases carrying dispute volume, the chargeback specialist vendors who could embed rather than staff, and directly the merchants bearing the losses.

## Impact If Built
Representment win rates on well-evidenced disputes are substantially higher than on template responses, and the difference falls directly to the merchant. The deadline tracking alone eliminates a category of automatic loss. For small merchants, who have the least capacity to fight and the most to lose proportionally, an automatically assembled representment is the difference between contesting and conceding.
