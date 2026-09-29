# Fix: The Crises Do Not Coordinate

**Niche:** The Fractional CTO
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Fix (Pain Point)
**One-liner:** Four clients each buy a fraction of a person and each expect full presence during their emergency, and nothing in the arrangement anticipates that the emergencies will overlap.
**Tags:** #evaluation-metrics #markov-decision-processes #probability-distributions #confidence-intervals #workflow-orchestration #worker-facing
**Contested on:** Whether a practitioner holding four unrelated complex situations can reload each one to real depth in minutes.

## The Problem

The fractional arrangement sells a day a week. What it actually sells, implicitly, is availability at the moments that matter — the outage, the failed release, the resignation of the lead engineer, the investor asking a technical question on a Sunday. Everyone involved knows this and nobody writes it down, because writing it down would require pricing it.

The arrangement works while the crises are spaced. They are not spaced. Four independent companies generate independent shocks, and independent events cluster — the practitioner's experience of "everything happened at once" is not bad luck, it is the arithmetic of four Poisson processes. Two clients in genuine difficulty in the same week is a routine occurrence, not an exception.

When it happens the practitioner must choose, and the choice is invisible to everyone. Client A gets the practitioner. Client B gets slower responses, a rescheduled session, and an advisor who is clearly elsewhere. Client B does not know why. They know they are paying for senior attention and receiving distraction, and their conclusion is about the practitioner's commitment rather than about an arrangement that never specified what happens in this case.

The practitioner absorbs it as guilt and as hours. The standard adaptation is to work the weekend, which is why this profession's burnout pattern looks the way it does, and why most practitioners cap their client count well below what their calendar would allow.

## Why It's Still Broken

**The contract is deliberately vague about it.** Fractional agreements specify days per month and say nothing about response times, escalation or what happens when two clients need the same hours. The vagueness benefits the sale — a client hearing "if another client has an incident, you may wait a day" buys less enthusiastically — so nobody raises it.

**Admitting the constraint feels like admitting divided loyalty.** Clients know intellectually that the practitioner has others. They do not want it made concrete, and practitioners are reluctant to make it concrete, so the shared fiction is that each client has the practitioner's full attention whenever needed.

**No visibility across the portfolio.** The practitioner has no forward view of their own risk. A release scheduled at one client, a migration cutover at another and a board meeting at a third in the same fortnight is a foreseeable pile-up, visible only if someone holds all three calendars — and nothing does.

**Utilisation is the only metric.** Practitioners track days and revenue. Nobody tracks the tax: unbilled crisis hours, reload time, weekend work. The costs that actually determine sustainability are invisible even to the person paying them.

**The solutions cost money.** Surge capacity, a partner to cover, a smaller client count — each is a direct income reduction for a benefit that is a probability. Independent practitioners without a risk pool are poorly placed to make that trade.

## What a Fix Looks Like

**Put it in the contract, positively.** A stated service model: scheduled days, an emergency response commitment with a defined window, and an explicit statement of what happens when commitments collide — first-come, or a priority tier the client can pay for. Clients respond far better to a clear constraint than to a vague promise quietly broken. The practitioner who says "four-hour response during business hours, and if another client has a severity-one incident you will hear from me within four hours with a plan rather than my presence" is trusted more, not less.

**Price the tier.** Some clients genuinely need priority and will pay for it. Making it an explicit, purchasable tier converts an invisible and resented rationing into a transparent commercial choice, and it is how every other shared-capacity profession — legal retainers, managed services, on-call medicine — has solved the same problem.

**Hold one portfolio calendar.** Every client's releases, migrations, board meetings, audits and funding milestones in one forward view, so foreseeable pile-ups are visible a month out and can be moved. Most collisions are not random; they are scheduled events that nobody laid side by side.

**Measure the tax.** Track the unbilled hours: crisis response, reload, out-of-hours. A practitioner who discovers they are working fifty-eight hours to bill forty has the information needed to reprice or to drop a client, and almost none of them have ever counted.

**Build reciprocal cover.** A small network of practitioners who cover each other's clients during a collision, with a standing arrangement and enough shared context to be useful. This requires the handover discipline from [[niches/fractional-cto-services/handover-and-continuity/profile|🟠 Handover & Continuity]] to be practised routinely rather than only at engagement end, which is a further argument for it.

**Reduce the crisis rate.** A meaningful share of emergencies are the same recurring fragility at each client. Fixing the underlying cause is technical work the practitioner is well placed to do and rarely prioritises, because crisis response feels like the urgent thing.

## Who Feels the Pain

The practitioner most, and it is the reason experienced people leave fractional work for a single full-time role — not the money, the impossibility of being reliably present for four organisations that each reasonably expect it.

The client in second place during a collision, who receives degraded service without explanation and draws the natural conclusion.

The practitioner's family, absorbing the weekend that four independent Poisson processes produced.

And the market, which is capped below its potential because practitioners self-limit their client count to protect against collisions rather than because demand is short.

## Impact If Fixed

An explicit service model removes the largest source of relationship damage in fractional work, which is not failure but unexplained absence. Clients forgive a stated constraint and remember an unexplained one.

The portfolio calendar prevents the foreseeable collisions, which are most of them, at essentially no cost.

And a practitioner who can see and price their own capacity can carry a fourth or fifth client deliberately, with the response model adjusted, instead of self-limiting to three out of an entirely justified fear of a week they cannot survive.
