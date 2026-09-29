# An Industry Running on a Destroyed Metric

**Niche:** [[niches/email-sms-marketing-platforms/engagement-signal-reconstruction/profile|Engagement Signal Reconstruction]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A privacy feature inflated open rates by an unrecoverable amount five years ago, and opens still drive segmentation, sunsetting, send-time models and reported performance across the industry.
**Tags:** #bayesian-inference #gradient-boosting #confidence-intervals #evaluation-metrics #hypothesis-testing #descriptive-statistics #survival-analysis #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to rebuild the segmentation, sunsetting and send-time machinery on signals that still mean something — and whoever does that replaces an industry running on a metric a privacy feature destroyed five years ago.

## The Problem
A large share of the email population now has images pre-fetched by a privacy service, which registers as an open whether or not a human ever looked. Open rates rose across the industry and did not come back down. The inflation varies by audience composition, cannot be separated at the individual level, and is therefore uncorrectable in the way everyone assumes. Meanwhile engagement segments are defined on opens, sunset policies remove people who have not opened, send-time models are trained on open timestamps produced by machines, and every campaign report leads with an open rate. The entire downstream apparatus is running on a signal that no longer carries the information it was built on.

## Why Nobody Has Built This
The metric remained available and looked fine, which is the worst possible failure mode — a broken instrument that keeps producing plausible numbers gets trusted longer than one that breaks visibly. Clients expect an open rate and comparing to historical benchmarks requires keeping it. Rebuilding segmentation, sunsetting and send-time on different signals is a substantial change across a whole product. And the platforms' reported performance looks better with the inflated number.

## What to Build
Rebuild on signals that survived. Move every downstream system to clicks, purchases, site behaviour and message-level response, which are unaffected and are already collected — the replacement data exists and is the point. Estimate the machine-open proportion at the audience level from the population composition, since the correction is possible in aggregate even though it is impossible per recipient, and an aggregate correction is enough for reporting and benchmarking. Rebuild engagement segmentation on a multi-signal definition of engaged, which is more robust than the old one was even before it broke. Redefine sunsetting on signals that indicate a real person, which is the fix note's subject and has real deliverability consequences. Retrain send-time models on click and conversion timing rather than on open timestamps, since the current models are substantially fitting a machine's pre-fetch schedule. Report open rate with a caveat or retire it, and give customers a transition path with their historical series restated so the change does not look like a performance collapse. Segment the audience by whether their opens are informative, since a meaningful portion still are and discarding all opens is an overcorrection. Handle text messaging's different signal set, where opens never existed and delivery is the ambiguity. Publish the method, since every sender faces this and a credible standard is a durable position. And measure downstream outcomes under the new definitions against the old, because that comparison is what persuades a market to change a metric it has used for twenty years.

## Target Customer
Messaging platforms, lifecycle and CRM teams, and the brands whose segmentation and reporting rest on a signal that stopped working.

## Impact If Built
A broken instrument that keeps producing plausible numbers is trusted far longer than one that breaks visibly, which is why the machinery still runs. The replacement signals are already collected, and the inflation is correctable in aggregate even where it is impossible per recipient.
