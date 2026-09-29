# The Viewer Who Came to Buy One Thing

**Niche:** [[niches/live-commerce-platforms/purchase-intent-matching/profile|Purchase-Intent Matching]]
**Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A viewer says exactly what they want, in a search or a saved item or a chat message, and the platform files it and shows them a feed.
**Tags:** #word-embeddings #bert #evaluation-metrics #revenue-impact #workflow-orchestration #quick-win #k-nearest-neighbors #automation
**Contested on:** Every serious competitor in this niche is fighting to rank streams for what a viewer will buy rather than for how long they will watch — and whoever changes the objective successfully converts an entertainment feed into a commerce channel.

## The Problem
Someone searches for a specific item, finds nothing live at that moment, and closes the app. Eight hours later a seller puts that exact item up and sells it to whoever happened to be watching. The platform knew what the viewer wanted, knew when the item appeared, and connected neither. The same happens in chat — viewers state wants constantly, in plain language, to hosts who cannot act on them at scale — and in saved items, waitlists and follows, all of which are stored and none of which trigger anything. This is the most explicit demand signal in any commerce format and it is treated as a log.

## Why It's Still Broken
Search that returns nothing is treated as a failed query rather than as a recorded want, which is the framing error underneath everything else. Notification budgets are managed centrally and conservatively, so a team wanting to add a high-value alert competes with growth messaging. Matching a free-text want to live inventory requires understanding both, and inventory is described by the host verbally rather than catalogued. And nobody owns the gap between a search and a stream that starts later.

## What a Fix Looks Like
Turn the want into a standing order. Record every zero-result search as a persistent want rather than discarding it, which is the whole fix in one change and requires no modelling — the wants are already typed. Let viewers declare wants explicitly, since a large share of live commerce buying is for specific known items and the interface offers no way to say so. Match wants against announced inventory before a stream begins, which gives the viewer notice rather than an interruption. Match against what the host is showing in real time, using audio and on-screen understanding, since most live inventory is never catalogued and this is the only path to it. Notify with a hard deadline attached — this item is up now, in this stream — which is the rare notification that is genuinely time-critical and earns its interruption. Extract wants from chat, where they are stated constantly and lost entirely, and route them to hosts as demand rather than as messages. Report unmet demand back to sellers by category, which tells them what to source and is information no seller currently has. And measure fulfilled wants as a headline metric, because it is the cleanest available statement of whether the marketplace works.

## Who Feels the Pain
Viewers who state what they want and are shown a feed; sellers with the exact inventory and no audience; and the platform losing the easiest transactions it will ever have.

## Impact If Fixed
A zero-result search is a recorded want mis-framed as a failed query, and recording it is the entire fix. Chat and search already contain the most explicit demand signal in commerce, and matching it to a stream in progress is the rare notification that earns its interruption.
