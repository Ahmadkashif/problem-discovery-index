# The Acid Bench

**Industry:** [[pawnshops|Pawnshops]]
**Type:** Worker Life Changing
**One-liner:** Behind the jewellery counter someone spends hours scratching, acid-testing, weighing and sorting gold by karat, breathing fumes and squinting through a loupe, because an XRF analyser costs more than most shops will spend and the refiner's assay will expose every mistake.
**Tags:** #cnns #random-forests #semantic-segmentation #evaluation-metrics #worker-facing #automation #quick-win

## The Problem
Gold arrives two ways: as pawn collateral and over the counter from customers selling outright, and forfeited jewellery that will not sell at retail joins it on the way to the refiner. Every piece is tested. The jewellery buyer reads the stamp if there is one, streaks the piece on a touchstone, applies nitric acid and karat-specific test acids, uses a magnet and an electronic tester, weighs on a legal-for-trade scale, removes stones, and sorts into 10k, 14k, 18k and silver lots. With gold near record prices the volume has surged: EZCORP's US scrap jewellery sales rose 58% to $85.7M in its 2025 fiscal year.

The bench is unpleasant and unforgiving. Test acids are corrosive and their fumes sting; small burns and stained fingers are routine; hours with a loupe strain the eyes. Plated pieces can pass a surface acid test and tungsten-cored fakes match gold's density, so the buyer runs more tests on anything that feels wrong. Then the lot goes to the refiner, which melts it, assays it and pays on the result. If the shop's karat sorting was optimistic the settlement comes in short, and the shortfall points back at whoever sorted the lot.

## Why It Matters to the Worker
This is skilled work that takes years to do quickly and accurately, done in a back room with chemicals, and the worker's reputation rests on a number — the refiner's assay — that arrives weeks later for a whole lot rather than a piece. There is no way to show which pieces were sorted right. The work also peaks exactly when gold spikes, the moment the queue of customers selling jewellery is longest.

## What a Solution Looks Like
Cut the acid and give the buyer evidence. A camera reads hallmarks and maker's marks; a lower-cost handheld analyser or density-and-conductivity rig, with a model trained on refiner assays, classifies karat without scratching; every piece is logged with its tests, weight and assigned lot. When the assay comes back, the system reconciles it against the piece log and shows where the gap came from — a single mis-sorted heavy piece or a consistent bias in one karat band. Suspect pieces get flagged for full testing rather than everything getting acid.

## Impact If Solved
Fewer hours a week at the acid bench (estimate), less chemical exposure, and assay disputes settled with a piece-level record rather than a shrug. The buyer's accuracy becomes visible and defensible, and a new buyer reaches competence faster because the system tells them which calls were wrong.
