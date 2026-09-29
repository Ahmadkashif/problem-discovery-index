# The Attribution Nobody Included

**Niche:** [[niches/game-asset-marketplaces/licensing-administration/profile|Licensing & Rights Administration]]
**Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** Four of the licences required attribution, the credits list none of them, and the game shipped last year.
**Tags:** #quick-win #compliance #automation #data-integration #evaluation-metrics #descriptive-statistics #workflow-orchestration #sets-and-logic
**Contested on:** Every serious competitor in this niche is fighting to let a studio know what it is actually permitted to do with the several hundred assets in its project, and whoever tracks that takes the account.

## The Problem
Attribution is the most commonly required and most commonly breached licence term in this category. Free and permissively licensed assets frequently require credit; the requirement sits in a text file inside the package, nobody reads it, and the credits screen is written by someone assembling names from memory near the end of the project. The breach is usually discovered by the creator, publicly, and the remedy is a patch and an apology.

## Why It's Still Broken
The obligation arrives inside the package — a requirement delivered as a text file in a folder will be read by nobody, and the person writing the credits has no list to work from. Credits are compiled manually at the end. Nobody tracks which assets carry the term. And the breach is embarrassing rather than expensive, so it never becomes a process.

## What a Fix Looks Like
Extract the requirements and generate the credits from them. Extract attribution requirements from every asset package automatically at import, which is the fix and is a file read rather than a project. Maintain a running credits list that accumulates as assets are added rather than being assembled at the end. Generate the credits screen from that list, so omission requires active effort rather than passive forgetting. Flag assets whose licence terms are unclear for a human to check, since a few always are. Cover free and bundled assets as carefully as paid ones, because that is where the requirement concentrates. Check the final build's credits against the register before shipping, which is a one-minute gate. Include the required wording exactly as specified, as paraphrase is itself a breach in some licences. Retrofit the check across already-shipped titles, which usually finds something worth fixing quietly. Store the licence text with the project rather than only the obligation. And make the register visible to whoever writes the credits, which is frequently not the person who bought the assets.

## Who Feels the Pain
Creators whose credit was omitted; studios apologising publicly for a clerical failure; whoever assembles the credits from memory; and the goodwill the category runs on.

## Impact If Fixed
A requirement delivered as a text file in a folder will be read by nobody, and the person writing the credits has no list to work from. Extracting attribution at import and generating the credits from the register makes omission require effort.
