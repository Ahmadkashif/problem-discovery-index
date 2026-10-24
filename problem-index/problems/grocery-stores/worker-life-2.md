# The Self-Checkout Attendant Policing Six Lanes

**Industry:** [[grocery-stores|Grocery Stores]]
**Type:** Worker Life Changing
**One-liner:** One attendant now watches six to eight self-checkout lanes, clearing weight errors, checking IDs and confronting customers over missed scans, and is blamed for shrink they cannot see and for confrontations they did not choose.
**Tags:** #cnns #object-detection #transformers #evaluation-metrics #worker-facing #automation #compliance

## The Problem
Self-checkout moved the cashier's job from scanning to supervision. One front-end associate stands at a podium covering six to eight lanes. Every few minutes a lane freezes: an "unexpected item in the bagging area", an age-restricted item needing an ID check, a coupon, a produce code the customer cannot find, or a SNAP or WIC card that needs help. Each freeze is a customer waiting and annoyed. The attendant clears it, then turns back to find another lane frozen.

The harder part is theft. Self-checkout lanes lose more to missed scans than staffed lanes. Some losses are honest mistakes, some are "banana trick" produce-code swaps, and some are items that never leave the cart (estimate from trade press). Vision systems from Everseen, NCR Voyix and others now flag suspected missed scans and pause the lane. That puts the attendant in the middle: they must walk over and ask a customer to rescan an item, without accusing them, often several times an hour, sometimes with a customer who becomes abusive. Store policy usually forbids them to stop anyone, and they know the store is measuring their lanes' shrink anyway.

## Why It Matters to the Worker
The job combines the boredom of watching screens with the stress of constant small confrontations. Front-end associates are among the lowest paid and youngest in the store, and the attendant role puts them in the most adversarial customer contact the store has. False alerts are the worst of it. A system that flags an honest shopper makes the attendant the person who accused them. A system that misses the real theft lets the attendant's lanes show shrink they will be asked about. Age-check errors carry personal fines in some states (estimate).

## What a Solution Looks Like
Alerts the attendant can trust and act on quietly. A vision model at each lane matches what was placed in the bag to what was scanned. It shows the attendant a three-second clip and a confidence score rather than freezing the lane on every doubt. The customer gets a neutral on-screen prompt to rescan, so most corrections happen without the attendant walking over. Age checks are queued by priority, and weight-error freezes caused by known scale problems are suppressed. Each shift ends with a summary of alerts, outcomes and false-alert rates, so the attendant's lanes are judged on what could be seen, not on a monthly shrink number.

## Impact If Solved
If false alerts fall from ~1 in 3 to ~1 in 10 (estimate), an attendant handling ~40 flagged events a shift avoids ~10 needless approaches to honest customers, and recovers the missed scans that matter without a confrontation.
