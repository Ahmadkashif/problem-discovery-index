# The Same Model Listed by Four Sellers

**Niche:** [[niches/game-asset-marketplaces/asset-provenance/profile|Asset Provenance]]
**Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** The identical asset appears under four seller accounts at four prices, and only the creator who made it is unaware.
**Tags:** #quick-win #compliance #evaluation-metrics #descriptive-statistics #automation #data-integration #confidence-intervals #k-nearest-neighbors
**Contested on:** Every serious competitor in this niche is fighting to establish that a listing is what the seller says it is, when verification currently rests on the creator ticking a box — and whoever can establish it takes the account.

## The Problem
Straightforward resale is endemic and trivially detectable. The same asset, sometimes the same files with the same internal names, appears under multiple seller accounts, occasionally on the same platform. Buyers cannot tell which is legitimate. The original creator finds out by chance or from a customer. The platform acts only when reported, and the report requires the creator to be watching a catalogue of hundreds of thousands of listings.

## Why It's Still Broken
Nothing compares uploads to each other — a catalogue that is never checked against itself will accumulate duplicates indefinitely, and the only detector is a creator who happens to look. Takedown is reactive by design. Duplicate listings are revenue. And the creator has no standing tool.

## What a Fix Looks Like
Compare uploads against the catalogue at the moment they arrive. Hash and compare uploaded files against the existing catalogue, which is the fix and catches the exact and near-exact resales that are most of the volume. Match on internal file structure and naming as well as content, since resellers frequently do not repackage at all. Flag duplicates for review before listing rather than after reporting. Give creators a standing alert when something matching their work is listed, which is the tool they currently lack entirely. Cluster seller accounts by upload patterns, as resellers operate at volume and the pattern is obvious once anyone looks. Show buyers when multiple listings share content so they can choose knowingly. Act on account history rather than treating each listing as isolated. Preserve the evidence so disputes resolve on facts. Publish the volume detected, which is what makes the effort visible and sustained. And run the comparison retrospectively across the whole catalogue once, which will surface a large backlog and is worth doing anyway.

## Who Feels the Pain
Creators whose work is sold by others; buyers who cannot identify the legitimate listing; platforms carrying legal and reputational exposure; and honest sellers competing against copies of their own work.

## Impact If Fixed
A catalogue that is never checked against itself will accumulate duplicates indefinitely, and the only detector is a creator who happens to look. Hashing uploads against the catalogue catches most of it before listing.
