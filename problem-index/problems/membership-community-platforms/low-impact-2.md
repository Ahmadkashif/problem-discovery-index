# Moderation Tooling for Communities That Cannot Fund It

**Industry:** [[membership-community-platforms|Membership & Community Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Serious moderation tooling is priced for platforms with trust and safety departments, and the communities that most need help have one founder and three volunteers.
**Tags:** #bert #transformers #large-language-models #gradient-boosting #dbscan #evaluation-metrics #compliance #worker-facing

## The Problem
A paid community of a few thousand members generates a steady stream of moderation work: a dispute between members, someone promoting a product against the rules, a newcomer breaching a norm they did not know existed, occasionally something genuinely serious — harassment, a member in crisis, a scam targeting the membership.

The tooling available at this scale is a report button, a delete action and a ban. There is no triage, no context on the reporter or the reported, no record of prior incidents, no severity distinction, and no guidance on what the community's own precedent has been. The founder or a volunteer sees a report, opens the thread, reads back through it, and decides — with no policy to lean on beyond a page of rules written at launch and no consistency across whoever happens to be on duty.

The consequential failures are in both directions. Under-moderation lets a few aggressive members set a tone that drives out quieter ones, which appears in the metrics as unexplained churn. Over-moderation on a misread situation loses a member and often their friends, and there is rarely an appeal process.

## What Already Exists
Every platform ships reporting, deletion, muting and banning, and keyword filters. Discord has a large ecosystem of moderation bots with automated rules. Enterprise trust and safety vendors — Hive, ActiveFence, Spectrum Labs — provide genuinely sophisticated classification and are priced for platforms with millions of users. Open-source tooling from the forum world provides flag queues and trust levels; Discourse's trust level system is the most thoughtful implementation in wide use. Legal and policy templates circulate among community professionals informally.

## The Customisation Gap
The gap is economic before it is technical. What a small community needs is the triage and context layer that enterprise tooling provides, at a price a few thousand subscriptions can support, and with the classification tuned to that community's own norms rather than to a generic policy — because norms differ enormously, and a directness that is ordinary in one community is a violation in another.

Context is the most valuable missing piece and the cheapest to build: when a report arrives, showing the surrounding conversation, both members' history in the community, whether either has been involved in prior incidents, and what the community decided in similar situations turns a cold decision into an informed one. Nearly all of that is a query, not a model.

Consistency is the second. Decisions made by different volunteers on different days diverge, which members notice and resent. A record of precedent — what happened last time something like this occurred — makes a small moderation team behave like one moderator.

The third is early detection of the slow failures. Escalating conflict, a member being consistently talked over, a subgroup turning hostile to outsiders, and the gradual tone shift that precedes an exodus are all detectable in the conversation record and none are reported. They are also the failures that actually kill communities, whereas the reportable incidents are usually survivable.

## Impact If Solved
Tone is what a member is buying, and it is protected by people with no tools working from a rules page. Context-rich triage and precedent are affordable to build and would immediately improve both the consistency and the speed of decisions; early detection of escalating conflict addresses the failure mode that ends communities and that no report button ever catches.
