# Knowing What You Are Allowed to Ship

**Niche:** [[niches/game-asset-marketplaces/licensing-administration/profile|Licensing & Rights Administration]]
**Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A shipped game contains hundreds of licences and nobody in the studio can list them.
**Tags:** #compliance #data-integration #workflow-orchestration #automation #evaluation-metrics #sets-and-logic #descriptive-statistics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to let a studio know what it is actually permitted to do with the several hundred assets in its project, and whoever tracks that takes the account.

## The Problem
Assets arrive from several marketplaces under several licence types, each with its own conditions: how many seats may use it, whether it may be redistributed in a source form, whether modification is allowed, whether attribution is required, whether a revenue threshold changes the terms. The purchases are made by different people over several years. Nothing joins the licence to the asset, and nothing joins the asset to whether it is actually in the build.

## Why Nobody Has Built This
The marketplace's interest ends at the sale and the studio's compliance function is usually one overworked person or nobody. Licence terms are prose, not data. The obligations rarely bite, so the risk is discounted. And the assets in the build are not tracked against the assets that were purchased.

## What to Build
Build the register and join it to the build. Maintain a licence register per project linking each asset to its terms, seat scope and obligations, which is the core and is what the studio reconstructs painfully when anyone asks. Parse the standard marketplace licences into structured terms rather than storing PDFs, since prose in a folder is not a register. Detect which purchased assets are actually present in the shipped build, as the difference between purchased and shipped is where most of the risk sits. Track attribution obligations and generate the credits automatically, which is the most commonly breached term and the easiest to satisfy. Alert when seat counts, revenue thresholds or platform scope are exceeded, because those change quietly as a studio grows. Flag licences that prohibit something the project is doing — redistribution in an SDK, use in a template, resale within a game. Produce an audit-ready export, which is what an acquisition or a platform certification requires. Cover assets from outside marketplaces too, since bespoke and free assets carry terms as well. Keep the register current automatically from purchase records rather than by manual entry. And make it cheap enough for a small studio, which is where the exposure is largest and the tooling is absent.

## Target Customer
Game studios of every size, asset marketplaces offering it as a service, publishers conducting diligence, and licence compliance vendors.

## Impact If Built
The difference between what was purchased and what actually shipped is where the risk sits, and nothing joins the two. A structured licence register linked to the build is what turns an archaeology exercise into an export.
