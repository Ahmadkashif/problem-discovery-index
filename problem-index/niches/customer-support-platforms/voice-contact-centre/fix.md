# The Menu Nobody Has Tested

**Niche:** [[niches/customer-support-platforms/voice-contact-centre/profile|Voice Contact Centre]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The interactive voice menu is the first thing every caller experiences, it was designed in a workshop years ago around the organisation's internal structure, and no company has ever tested whether callers can navigate it.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #survival-analysis #automation #worker-facing #quick-win
**Contested on:** Every serious competitor in voice support is fighting to resolve a caller's issue without a human while they are on the line, and to make the agent faster when a human is needed — and whoever raises containment without raising repeat calls takes the account.

## The Problem
A caller hears eight options organised by the company's departments rather than by anything the caller would recognise. They choose the closest, are taken to a submenu with six more, choose again, and arrive at a queue for a team that cannot help them, who transfer them. The path through the menu is recorded in full for every call — every key press, every timeout, every zero-out, every mis-route that ended in a transfer — and nobody analyses it. The menu is revised when someone complains loudly enough, by the same committee, using the same organisational logic.

## Why It's Still Broken
Interactive voice response configuration is treated as a telephony setting rather than as an interface, and the people who own it are infrastructure rather than experience. The analytics exist in the platform and are used for volume reporting rather than for path analysis. And the menu reflects the organisation's own structure because that is how the requirements were gathered — each department specified its own option — which is the classic failure of any interface designed by the organisation rather than for the user.

## What a Fix Looks Like
Analyse the paths and redesign from the data. Every call's route through the menu is available: where callers drop out, where they time out, where they press zero, and — most informatively — which menu selection preceded a transfer, since a transfer is direct evidence that the routing was wrong. That analysis identifies the specific options that mislead and the specific intents the menu does not represent at all, which is usually several of the most common reasons people call. Restructure around caller intents rather than departments, which is the substantive change and is what the data will show. Test changes rather than deploying them, since a menu is trivially A/B testable by routing a fraction of calls to a variant and comparing mis-route and abandonment rates — an experiment every organisation could run and essentially none does. Measure time to the right place rather than containment. And make the zero-out path work, since a caller who has decided they need a person is going to get one eventually and every additional step is pure cost to both parties.

## Who Feels the Pain
Callers navigating a structure that describes somebody else's organisation chart; agents receiving transfers that should never have reached them; and operations leaders whose containment problem is partly a navigation problem nobody has diagnosed.

## Impact If Fixed
Path analysis is free and available in every platform, and the transfer-preceded-by-selection analysis locates the misleading options precisely. Menu A/B testing is trivially available and essentially unused, which makes this one of the cheapest measurable improvements in the whole category.
