# Fix: The Breakdown That Arrives After the Decision

**Niche:** [[niches/gig-delivery-platforms/pay-composition-disclosure/profile|Pay Composition Disclosure]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Several platforms do show the pay breakdown — after the delivery is complete, when the only decision it could have informed is already made.
**Tags:** #descriptive-statistics #evaluation-metrics #workflow-orchestration #compliance #confidence-intervals #worker-facing #quick-win #data-integration
**Contested on:** Whether an existing disclosure can be moved from after the work to before it.

## The Problem

Platforms are not uniformly silent about pay composition. Several show a breakdown in the earnings history: base pay, promotion, tip, itemised per delivery, available once the delivery is complete and the tip has settled.

This is presented, in platform communications and sometimes to regulators, as pay transparency. It is not, in the sense that matters. The courier's decision is the accept-or-decline in the seconds after the offer arrives, and a breakdown available afterwards informs nothing about it. It also makes the gap harder to argue about, because the platform can truthfully say the information is disclosed.

The practical consequence is that a courier cannot distinguish a durable offer from a promotional one, or a base-heavy offer from a tip-estimate-heavy one, at the only moment the distinction could change what they do. They can only reconstruct it, delivery by delivery, from the history — which a few do, manually, in spreadsheets, and which is the origin of most of the courier-side tooling ecosystem.

## Why It's Still Broken

Because moving the disclosure earlier changes behaviour and the post-hoc version does not. That is the whole of it, and it is worth stating plainly rather than looking for a technical explanation that is not there.

The secondary reasons are genuine but small. The tip component before delivery is an estimate rather than a settled amount, and platforms are wary of displaying a number that may change — although they are entirely willing to include that same estimate inside the headline guarantee, undisclosed. And the offer screen is small and time-pressured, which is a real design constraint and is solved by progressive disclosure rather than by omission.

## What a Fix Looks Like

Move the existing breakdown into the offer. The data is the same data; the rendering already exists.

Show the components on the offer card, compactly, with the headline retained. Base and distance as settled amounts. Promotion with its expiry. Tip as an explicitly-marked estimate with the realisation rate for comparable orders. Progressive disclosure handles the space constraint: a one-line summary that expands, with the expansion state remembered so a courier who wants the detail sees it every time.

Be explicit about the conditional component rather than hiding it inside the guarantee. "Includes an estimated $4 tip, which customers adjust downward on about one in nine comparable orders" is honest, is computable from the platform's own history, and is a far better position than the alternative the industry has already tested publicly.

Reconcile afterwards and show the reconciliation. Disclosed estimate against realised amount, per delivery, in the earnings history. This closes the loop, gives the courier a basis for calibrating their own trust in the estimates, and gives the platform a quality signal on its tip prediction that it does not currently have.

Aggregate weekly. What share of this week's earnings was base, distance, promotion and tip, by market and daypart. This is the version that supports a courier's planning rather than a single decision, it is a group-by over records that already exist, and it is the answer to the most common question couriers ask each other in forums.

## Who Feels the Pain

Couriers, who are told the information is available and find it is available too late to use. Full-time couriers most of all, whose planning depends on knowing which of their earnings are promotional and therefore temporary. Regulators and researchers, who receive "we disclose pay composition" as a true statement that does not describe the situation. And the platform, which is absorbing the reputational cost of opacity while already having built the disclosure.

## Impact If Fixed

The disclosure starts informing the decision it was ostensibly built for. The distinction between durable and promotional earnings becomes visible to the people planning their weeks around it. And a platform that moves it voluntarily gets credit for transparency it has, in data terms, already implemented — which is the cheapest goodwill available anywhere in this industry.
