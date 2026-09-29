# Every Ticket Is Treated as Equally Likely to End in a Struck Line

**Niche:** [[niches/utility-contractors/underground-locating-damage-prevention/profile|Underground Utility Locating & Damage Prevention]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Hundreds of millions of locate tickets a year, a small fraction of which precede a damage, and the system allocates the same effort to all of them.
**Tags:** #gradient-boosting #logistic-regression #evaluation-metrics #causal-inference #graph-neural-networks

## The Problem
An excavator files a ticket. It is screened against facility maps, the affected operators are notified, and each dispatches a locator who has a statutory window — usually forty-eight hours — to mark the ground. The volume is enormous and the workforce is finite, so the binding constraint is always technician hours against tickets.

Those hours are allocated by geography and by clock. Tickets are routed to balance travel and to meet the deadline. What almost never enters the allocation is risk: the probability that this particular excavation, at this location, by this excavator, near these facilities, ends with a struck line.

That probability varies by orders of magnitude and it is predictable. The ticket carries the work type, the excavation method, the depth, the extent of the dig site, and the excavator's identity. The facility records carry what is buried there, how old the records are, and how congested the corridor is. And the damage history carries the outcome — for the ticket, the excavator, the corridor, and the operator.

Nobody joins these. Quality assurance re-checks are typically allocated as a random sample or by simple rules. Emergency and high-priority tickets are flagged by category rather than by estimated consequence. And the excavators who cause repeated damages are identified after the fact, by claims, rather than before the dig, by the ticket.

The stakes are unusual for this index: the failure mode is a severed gas main in a residential street.

## Why Nobody Has Built This
The industry's regulatory framing is procedural. Compliance means responding within the window and marking accurately; it does not mean allocating attention by risk, and a locating contractor is measured on on-time completion and damage rate, not on how it prioritised.

Risk scoring an excavator is also commercially and legally awkward. The excavator is not the locator's customer — the facility operator is — and treating some diggers as higher risk than others invites disputes about fairness in a domain that ends up in litigation after every serious incident.

And the data sits in three places: the one-call centre holds tickets, the facility operator holds maps and damage claims, and the locating contractor holds field completions. Each is a different party, and no one of them sees the whole record.

## What to Build
Risk-based prioritisation, fitted on the damage outcomes the system already records.

**Model damage probability per ticket.** Work type, excavation method, site extent, facility mix and depth, corridor congestion, records vintage, excavator history and season, against whether a damage was reported. Tens of millions of labelled examples a year, with the label arriving within days.

**Predict consequence, not just probability.** A strike on a plastic service line and a strike on a high-pressure steel main are different events. Ranking by expected consequence rather than by probability is what actually reallocates attention correctly.

**Allocate quality assurance where the model is uncertain, not at random.** Re-checks are the main quality mechanism and they are currently sampled. Directing them at high-risk, high-uncertainty tickets converts a compliance activity into a targeted control.

**Model excavator behaviour explicitly and carefully.** Repeat-damage excavators are identifiable well before the incident, and the appropriate response is engagement and pre-dig contact rather than exclusion. The modelling is straightforward; the governance around it is the real work and should be designed first.

**Learn where the maps are wrong.** Every mislocate and every unmarked-facility damage is evidence about records quality in a specific area. That inference is the highest-value derived product in this whole business and nobody is computing it.

## Target Customer
Chief Data Officer or VP of Quality at a national locating contractor, or the executive director of a large one-call centre. The strongest version requires the ticket, the map and the damage record together, which means a data-sharing arrangement is part of the build.

## Impact If Built
Excavation damage to buried utilities causes hundreds of thousands of incidents a year in the United States, with a tail that includes explosions and fatalities. Allocating a fixed pool of locator hours by expected consequence rather than by geography is the highest-leverage change available to the system, and every input needed to do it is already being recorded.
