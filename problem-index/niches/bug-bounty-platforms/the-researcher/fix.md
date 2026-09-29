# Fix: Paid for Being First, Not for Being Right

**Niche:** The Researcher
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A week of skilled work produces a genuine vulnerability, someone submitted the same thing that morning, and the payment is zero.
**Tags:** #evaluation-metrics #probability-distributions #confidence-intervals #worker-facing #revenue-impact #compliance
**Contested on:** Whether a week of skilled work has a knowable expected value, or a payoff decided by who submitted first and how someone rated it afterwards.

## The Problem

The duplicate rule is simple: the first valid submission of a finding is paid, subsequent ones are not. It is a reasonable rule and its consequences are severe.

A researcher does everything right. They pick a programme, invest a week, find a real vulnerability, document it carefully, and submit. The response says duplicate. Someone reported the same issue four hours earlier, or last month, and the work is worth nothing. The organisation still benefits from the confirmation that the finding is real and reachable, and pays nothing for it.

The researcher cannot verify the claim. They are told a prior submission exists and typically shown nothing. Almost every programme is honest about this, and the researcher has no way to know that, so an honest rejection and a dishonest one feel identical.

The distribution of this loss is what makes it corrosive. It falls hardest on newly public programmes where everyone arrives at once, and on the most obvious high-value findings, which is exactly where skilled researchers are drawn. The lottery is worst precisely where the work is most valuable, and researchers with alternatives respond rationally by taking them.

## Why It's Still Broken

**Paying duplicates costs money for information already held.** From the programme's side the second report adds little, and the budget argument is straightforward. It is also short-sighted: the cost of paying good-faith duplicates is small relative to the cost of losing the researchers who stop participating.

**Duplicate claims are unfalsifiable by design.** Showing the original risks revealing another researcher's work and sometimes the vulnerability detail. The privacy concern is real and is also solvable with timestamps and redaction, which nobody does.

**Researchers cannot see each other.** There is no signal of where others are working, so independent duplication is the expected outcome rather than an accident. This is an information problem the platform could fix and does not.

**Abuse fears block the obvious mitigations.** Any partial payment for duplicates invites low-effort submission of common findings in the hope of a small payout. The fear is legitimate and is manageable with a quality bar, which is exactly how contest platforms handle the same risk.

**The supply side has no voice.** Researchers cannot collectively negotiate, are bound by terms limiting public complaint, and the ones with the most leverage are the least likely to spend it.

**Duplicate rates are not published.** No programme reports what share of valid submissions it closes as duplicates, so a researcher cannot avoid the programmes where the lottery is worst.

## What a Fix Looks Like

**Show the duplicate.** Timestamp, finding class, and enough redacted detail to verify the claim. Honest programmes lose nothing, the unfalsifiable claim disappears, and the trust cost of the rule falls sharply. This is the cheapest fix available and almost nobody does it.

**Pay something for good-faith duplicates that meet a quality bar.** A fraction of the full award for a well-documented, independently-discovered duplicate submitted within a window of the original. Small in aggregate, and it converts the community's largest grievance into an acceptable cost of doing speculative work. Contest platforms use exactly this mechanism and manage the abuse risk with the quality bar.

**Publish duplicate rates per programme.** Researchers can then avoid the programmes and the moments where the lottery is worst, which is basic market information and is currently withheld.

**Show contest density.** How many researchers are active on a scope right now. Most duplication is independent people working the same newly public target with no way to see one another, and a density indicator would spread effort without revealing anyone's identity.

**Time-bound the duplicate window.** A finding reported and left unfixed for a year should not indefinitely block payment to someone who rediscovers it. If the organisation did not act on the original, the rediscovery is genuinely informative.

**Credit duplicates in reputation even when unpaid.** A researcher who independently found a real vulnerability demonstrated capability. Recording that in reputation costs nothing and preserves some value from the week.

## Who Feels the Pain

The researcher, who did skilled work correctly and received nothing, with no way to verify why.

The strongest researchers most, because they are drawn to the high-value findings where duplication is most likely and they have the best alternatives when they tire of it.

Newcomers, who lose their early weeks to duplicates on crowded public programmes and conclude the economics do not work — which they largely do not, at that stage.

And the programme, which is extracting confirmation of a real vulnerability for free and paying for it later in researcher attrition it never attributes to this.

## Impact If Fixed

Showing the duplicate removes the trust problem at essentially zero cost, and it is the change that would most improve how programmes are perceived in the community.

A partial award for good-faith duplicates addresses the defining economic grievance of this market for a small fraction of programme spend, using a mechanism proven in adjacent contest economies.

And publishing duplicate rates and contest density would let researchers avoid the worst lotteries — which spreads effort across more programmes, reduces duplication overall, and makes the whole marketplace work better for everyone in it.
