# The Partner Suspended on One Merchant

**Niche:** [[niches/affiliate-networks/the-compliance-analyst/profile|The Compliance Analyst]]
**Industry:** [[industries/affiliate-networks|Affiliate Networks]]
**Type:** Fix (Pain Point)
**One-liner:** A partner caught stuffing cookies is removed from one programme, keeps running on the other four hundred on the same network, and nobody is told.
**Tags:** #graph-theory #compliance #evaluation-metrics #workflow-orchestration #quick-win #descriptive-statistics #automation #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to catch tactics that evolve faster than the rulebook, with an analyst who has rules and spot checks — and whoever gives them detection that learns replaces a policing model that is permanently one cycle behind.

## The Problem
A merchant's manager discovers a partner stuffing cookies. They investigate, confirm it, and remove the partner from their programme. That partner is running on four hundred other programmes on the same network, doing the same thing, and nothing happens to any of them. The finding is recorded as a programme-level removal in one merchant's account. The network, which could propagate it instantly, does not, because the removal was a merchant's decision about their own programme and there is no mechanism that turns it into a network-level signal. The most expensive investigation work in the category is done once and discarded.

## Why It's Still Broken
Programme removals are merchant actions and compliance findings are network actions, and the two are different objects in different systems with no connection — that separation is the entire cause. A network-level suspension has commercial consequences the network is cautious about. Merchants do not report their findings because there is nowhere to report them. And nobody counts how often the same partner is removed repeatedly.

## What a Fix Looks Like
Turn a removal into a signal. Capture the reason for every programme removal in a structured form, which takes one field and is the step that makes everything else possible. Aggregate removals by partner across merchants, since a partner removed by fifteen merchants for the same reason is a network-level case that currently never assembles itself. Trigger investigation automatically at a threshold, rather than waiting for a complaint loud enough to reach compliance. Alert other merchants running the same partner, which is the immediate protective action and is what merchants most want from a network. Link related partner accounts by behavioural and infrastructure signals, because operators re-register and single-account suspension is temporary. Give merchants a route to report findings with evidence, which does not meaningfully exist today. Publish removal reasons to the partner, so a legitimate partner removed in error can respond rather than simply losing income silently. Distinguish a performance removal from a compliance removal, since conflating them makes the aggregate useless. Feed confirmed cases into detection models, which are the highest-quality labels available and are currently thrown away. And report repeat-removal rates as a network health metric, because the same partners being removed by merchant after merchant is the plainest possible evidence that the policing model is not working.

## Who Feels the Pain
Merchants independently discovering the same bad actors; compliance analysts investigating cases other people already solved; and legitimate partners competing against operators nobody has stopped.

## Impact If Fixed
Merchant removals and network compliance findings are different objects in different systems, so the most expensive investigation in the category is done once and discarded. One structured reason field turns fifteen independent removals into a case that assembles itself.
