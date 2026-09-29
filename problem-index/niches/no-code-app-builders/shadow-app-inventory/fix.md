# An Inventory With No Risk Attached

**Niche:** [[niches/no-code-app-builders/shadow-app-inventory/profile|Shadow App Inventory]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Fix (Pain Point)
**One-liner:** A governance exercise produces a list of six hundred applications with no indication of which three matter, so nothing happens and the list is regenerated next year.
**Tags:** #descriptive-statistics #logistic-regression #decision-trees #evaluation-metrics #confidence-intervals #compliance #quick-win #automation
**Contested on:** Every serious competitor here is fighting to produce a complete list of the applications a company's employees have built, including the ones built on accounts IT does not know exist — and whoever can produce that list takes the security and compliance account, because nobody can produce it today.

## The Problem
IT finally gets access to the tenant and exports the inventory: six hundred and eleven applications, with names, owners and creation dates. It is circulated. Nobody can act on it, because six hundred is beyond triage capacity and nothing in the export distinguishes the app holding customer records with a public form from the one an intern built to track team lunches. The list is filed. The following year someone regenerates it, slightly longer.

## Why It's Still Broken
Inventory is treated as the deliverable, because producing it was hard and its production feels like completion. Risk assessment per application requires looking at each one, which nobody has capacity for at this volume. The attributes that would allow automated triage — what data it holds, who can reach it, what it connects to, whether a process depends on it — are available in the platform and are not in the export, because the export was designed for licensing. And the governance function's mandate usually ends at visibility.

## What a Fix Looks Like
Attach risk to the inventory automatically so triage is possible. Classify the data each app holds by inspecting field names, types and value patterns — which identifies personal data, payment details and health information at high accuracy and requires no human review of most apps. Record exposure: public links, anonymous forms, external sharing and guest access, each of which is a flag with an unambiguous meaning. Record dependence: user count, breadth beyond the builder's team, connected systems, scheduled automations that act in the world. Combine into a small number of tiers with the reasoning attached, so the output is fifteen applications needing attention this month rather than six hundred needing attention in principle. Route by tier: the top tier gets a review, the middle gets an automated prompt to the owner, and the bottom gets left alone, which is the correct treatment for most of the estate and is what makes the process sustainable. And re-run it continuously, since the estate changes weekly and an annual snapshot is stale before it is circulated.

## Who Feels the Pain
Governance and security teams holding a list they cannot act on; builders subjected to blanket policies because nobody could distinguish their app from a risky one; and organisations whose genuine exposure sits somewhere in an untriaged export.

## Impact If Fixed
Automated classification and exposure flags turn an unusable inventory into a short actionable list, and both are computable from platform metadata without opening an application. Routing by tier is what makes governance sustainable rather than a periodic campaign that produces nothing.
