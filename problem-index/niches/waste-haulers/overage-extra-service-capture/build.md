# A Contract-Aware Charge Decision for Every Flagged Lift

**Niche:** [[niches/waste-haulers/overage-extra-service-capture/profile|Overage & Extra-Service Charge Capture]]
**Industry:** [[industries/waste-haulers|Waste Haulers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Cameras flag thousands of overfilled containers a week, and a clerk still decides one by one whether each may be billed under that customer's contract and that city's rules.
**Tags:** #cnns #object-detection #large-language-models #evaluation-metrics #compliance #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn what the truck camera saw into overage and extra-service charges that stick, and whoever has the lowest share of those charges credited back after dispute takes the account.

## The Problem
A flagged lift becomes a charge only if the container is the customer's, the overflow meets the contract's definition, the customer has had its warning, notice can go out in time, and the hauler did not miss the previous pickup. Clerks check these by hand, so most events are never billed and some are billed wrongly.

## Why Nobody Has Built This
Camera vendors sell detection and leave billing to the hauler; billing vendors post charges they are given. The rules sit in hundreds of franchise agreements and ordinances in prose, and until recently no court had set an evidence standard.

## What to Build
A decision service between camera and billing: it reads each franchise's charge rules from contract text into structured conditions, matches each event to the container record, checks warning history and missed-pickup logs, sends the notice with photo, posts the charge or warning, and tracks every dispute outcome so the rules and detection thresholds improve on the charges that get credited back.

## Target Customer
Billing directors at haulers with 5,000+ commercial containers and cameras on their front-load fleet.

## Impact If Built
Billing two more points of overflow lifts on ~1M commercial lifts a year at ~$25–50 each adds ~$0.5–1M (estimate), with credit-backs falling as only rule-compliant charges are posted.
