# The Win-Back Campaign Sent to Everyone

**Niche:** [[niches/email-sms-marketing-platforms/list-health-and-reactivation/profile|List Health & Reactivation]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The re-engagement campaign goes to everyone who has not engaged in six months, which is mostly dead addresses and people who will complain, and it is sent from the main sending domain.
**Tags:** #gradient-boosting #evaluation-metrics #confidence-intervals #survival-analysis #quick-win #compliance #revenue-impact #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to tell a brand which of its subscribers are still reachable and worth reaching — and whoever does that stops a list from being both a liability and an unworked asset at the same time.

## The Problem
Quarterly, someone runs a re-engagement campaign: one message to everyone dormant for six months, asking if they still want to hear from the brand. A small number re-engage. A larger number complain, because they had forgotten signing up and are being contacted after months of silence, which is the pattern mailbox providers treat most harshly. A large portion are dead addresses that bounce. The whole thing is sent from the primary sending domain, so the complaint spike and the bounce spike land on the reputation that every other message depends on. The campaign is intended to improve list health and is one of the most reliable ways to damage deliverability.

## Why It's Still Broken
Re-engagement is treated as a campaign rather than as a risk-managed operation, so it is planned like a promotion and sent like one — the framing determines the execution. The complaint and bounce consequences are delayed and attributed elsewhere. The dormant segment is defined by a single rule that does not distinguish the populations within it. And the small number who do re-engage makes it look successful.

## What a Fix Looks Like
Target it and isolate it. Predict who is likely to re-engage and send only to them, which is the fix, is a straightforward model on data already held, and removes most of the complaint and bounce risk by removing the people who were never going to respond. Validate addresses before sending, since bouncing a large batch is a reputation event and the validation is cheap. Send from a separate domain or subdomain, which isolates the reputation consequence from the main programme and is standard practice that almost nobody follows for this. Ramp gradually rather than sending in one batch, because a sudden volume of mail to disengaged recipients is exactly the pattern providers penalise. Distinguish the filtered from the disinterested first, since sending more mail to someone whose mail is going to spam achieves nothing and worsens the signal. Make it easy to opt down rather than only to stay or leave, which converts a portion of the population who want less mail rather than none. Suppress rather than delete initially, so the decision is reversible and the data is retained. Measure the whole cost including complaints, bounces and placement effect, not just the re-engagement count — the campaign looks successful only because the cost side is never computed. Run it continuously in small volumes rather than quarterly in large ones, which is both safer and more effective. And stop sending to the population predicted not to return, because they are a liability and the honest action is to let them go.

## Who Feels the Pain
Brands damaging their deliverability with a campaign intended to protect it; recipients contacted after months of silence; and everyone else on the list whose mail is affected by the reputation hit.

## Impact If Fixed
Re-engagement is framed as a campaign and executed like a promotion, which is how a list-health operation becomes a reputation event. Predicting who will return, validating addresses and isolating the sending domain removes most of the risk with steps that are individually routine.
