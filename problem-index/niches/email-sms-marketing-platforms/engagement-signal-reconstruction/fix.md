# The Sunset Policy That Keeps the Wrong People

**Niche:** [[niches/email-sms-marketing-platforms/engagement-signal-reconstruction/profile|Engagement Signal Reconstruction]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The list prunes anyone who has not opened in six months, which now retains everyone whose mail client opens automatically and removes real readers who do not load images.
**Tags:** #survival-analysis #gradient-boosting #evaluation-metrics #confidence-intervals #compliance #quick-win #descriptive-statistics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to rebuild the segmentation, sunsetting and send-time machinery on signals that still mean something — and whoever does that replaces an industry running on a metric a privacy feature destroyed five years ago.

## The Problem
Sunsetting exists to protect deliverability: stop sending to people who never engage, because mailbox providers treat sustained non-engagement as a signal that the sender is unwanted. The standard policy removes anyone with no opens in a window. Since a large share of opens are now machine-generated, that policy retains every disengaged recipient whose client pre-fetches images, and removes engaged readers whose clients do not. The policy now does close to the opposite of its purpose, on a list that is simultaneously growing with dead addresses and shedding real readers, and the deliverability consequences arrive slowly.

## Why It's Still Broken
The policy was written before the signal changed and is embedded in platform defaults and agency playbooks, so it propagates automatically to new senders — a broken default is more durable than a broken metric. Its failure appears as a gradual deliverability decline rather than as an error. Removing subscribers reduces list size, which nobody volunteers for without certainty. And the correct definition requires the multi-signal engagement the category has not built.

## What a Fix Looks Like
Redefine engaged on signals that indicate a person. Sunset on clicks, purchases, site visits and message-level response rather than on opens, which is the fix and uses data already collected — every platform has these signals and none of the standard policies use them. Treat an open as informative only where the recipient's environment suggests it is, since a portion still are and blanket discarding is an overcorrection. Model the probability of a recipient being a live human from their whole behavioural history, which is a better basis than any single-signal rule and is well within reach. Stage the removal — reduce frequency, then attempt reactivation, then remove — rather than cutting at a threshold, since a quieter person is not a dead address. Measure the deliverability effect of the policy directly, connecting to the placement work, because the policy exists for deliverability and its effect on it is never checked. Audit the current list for machine-only engagement, which most senders have never done and which typically reveals a substantial share of their engaged segment is not human. Handle the text channel separately, where no open exists and the signals are entirely different. Report list health honestly, since a growing list of unreachable addresses is a liability presented as an asset. Update the platform defaults, because most senders will never change a default and the defaults are where the damage propagates. And measure revenue and placement before and after a corrected policy, since a list that shrinks and performs better is the argument that overcomes the reluctance to remove anyone.

## Who Feels the Pain
Senders whose deliverability declines while their engaged segment appears to grow; real readers removed for not loading images; and the channel, whose protective mechanism now inverts its own purpose.

## Impact If Fixed
A broken default is more durable than a broken metric, and this one now retains the disengaged and removes real readers. Sunsetting on clicks, purchases and site behaviour uses signals every platform already collects and that none of the standard policies use.
