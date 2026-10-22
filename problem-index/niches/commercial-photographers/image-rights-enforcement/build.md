# Licence-Aware Match Triage

**Niche:** [[niches/commercial-photographers/image-rights-enforcement/profile|Image Rights Enforcement & Licence Compliance]]
**Industry:** [[industries/commercial-photographers|Commercial Photographers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Image-matching finds thousands of uses of a commercial photographer's work, and nothing tells them which ones the client's own licence already covers.
**Tags:** #contrastive-learning #k-nearest-neighbors #large-language-models #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to prove which online uses of an image are unlicensed (checked against the licences actually granted) and convert them into paid licences without a lawsuit, and whoever keeps claims against licensed users near zero takes the photographer's archive.

## The Problem
Commercial images, unlike stock or editorial images, are licensed to a client whose partners, distributors and agencies may legitimately use them. A matching service sees a furniture retailer using a manufacturer's commissioned image and flags it. Whether that is infringement depends on the manufacturer's licence terms, which the service has never seen. False demands to licensed users are what earns enforcement the "troll" label and what costs photographers their clients.

## Why Nobody Has Built This
Enforcement services were built around stock and news archives, where most commercial uses are plainly unlicensed. Licence terms for commissioned work live in individual photographers' contracts and are not structured. Services paid on contingency profit from volume, not from restraint.

## What to Build
A triage layer between matching and action: licence terms extracted from the photographer's estimates, contracts and invoices into structured grants (licensee, permitted partners, media, territory, term); every match classified as licensed, probably licensed (a credited project party, a known partner of the licensee) or unlicensed using page context; and an action recommended by expected value and relationship risk. Precision on the "unlicensed" class is the metric that matters.

## Target Customer
Commercial photographers and studios with large commissioned archives, and enforcement services wanting to move into commissioned work without damaging reputations.

## Impact If Built
Demands go only to true infringers, recoveries per case rise, and photographers can enforce without risking the client relationships their business depends on.
