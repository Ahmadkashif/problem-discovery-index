# Build: The Dose and the Cap

**Niche:** Presentation & Dosimetry
**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A unit of psychological exposure, a ledger that accumulates it per reviewer, and presentation controls that reduce the dose of each item a human must see.
**Tags:** #cnns #evaluation-metrics #confidence-intervals #survival-analysis #hypothesis-testing #markov-decision-processes #worker-facing #compliance
**Contested on:** Whether the intensity of each unavoidable exposure, and its accumulation across a shift and a career, is deliberately controlled or left to a full-fidelity default nobody chose.

## The Problem

When a human must see distressing material, almost nothing about how they see it has been decided deliberately. The review tool renders the file as uploaded, at full resolution, with audio, from the beginning, in colour. That is not a choice anyone made about occupational exposure; it is the default behaviour of a media player, inherited into a context where the media causes injury.

Several interventions are available and mostly unused. Greyscale substantially reduces the visceral impact of graphic imagery. Audio is disproportionately distressing in violent material and is trivially suppressible. Most decisions can be made from sampled frames rather than continuous playback. Most violations occur in a short segment that classifiers can already localise, so a reviewer can see eleven seconds instead of twenty minutes. Reduced resolution is often sufficient for a category judgement.

Above all, nothing accumulates. A reviewer who spent a morning on the worst category the platform has is routed into an afternoon of the same, because the routing sees an available worker. There is no ledger, no budget, no cap, and therefore no mechanism by which a bad morning changes anything about the afternoon.

The obstacle to all of it is a measurement that does not exist. Without a unit of exposure, a vendor cannot set a threshold, cannot demonstrate it is meeting one, and cannot show a court or a client that harm in its operation is bounded.

## Why Nobody Has Built This

**The unit does not exist and inventing it is exposed work.** Radiation has sieverts and decades of dose-response epidemiology. Psychological exposure to distressing media has neither, and a vendor proposing a unit is making a scientifically contestable claim in a domain where it will be attacked by plaintiffs for being too permissive and by clients for being too costly. The rational individual move is to let someone else go first.

**Reduced fidelity collides with the quality metric.** A reviewer who works in greyscale and is later graded by an auditor watching in full colour will lose on the cases where colour mattered. Until auditing is performed at the same fidelity as review, every protective control carries a personal accuracy penalty, which is why the toggles that do exist are barely used.

**Caps cost throughput and no client agreed to them.** Stopping a reviewer mid-shift because they have reached a severe-exposure budget has a direct cost under a per-decision contract, and the client did not sign up for it.

**The clinical evidence is a long project.** Establishing that a given dose regime reduces harm requires longitudinal outcome data over years, in a workforce with high turnover, where attribution is contested. No commercial builder gets a return on that timeline.

**Measuring creates discoverable evidence.** The same counsel's instinct that suppresses exposure measurement generally applies here with more force, because a ledger that shows a cap being exceeded is considerably worse than no ledger — which is an argument for enforcing the cap, not for refusing to count.

## What to Build

**Define the unit, openly and with clinicians.** A severity-weighted exposure measure combining category, intensity, duration, fidelity and victim characteristics, developed with occupational trauma specialists, published with its methodology and its uncertainty, and offered to the industry rather than held. Whoever defines it credibly sets the terms of every subsequent conversation, including the regulatory one.

**Presentation controls on by default, escalation on demand.** Greyscale, audio off, reduced resolution, frame sampling and classifier-localised segment isolation applied as the default rendering, with a single action to escalate to full fidelity when the decision genuinely requires it. The default has to invert — protection as standard, full exposure as the deliberate act — because a protective control that requires the reviewer to ask for it will not be used by the people under the most pressure.

**Audit at review fidelity.** Quality auditors grade what the reviewer actually saw, at the same fidelity, and escalate on the same terms. Without this the whole scheme penalises the people who use it, and no amount of encouragement will overcome that.

**The ledger and the cap.** Every exposure written with its computed dose; budgets per shift, week and quarter, with separate accounting for the categories clinicians and reviewers consistently identify as worst; routing that respects the budget by moving people to lower-intensity work rather than stopping them. Enforced by the system, not requested by the worker.

**Structural recovery.** Mandatory lower-intensity work after a severe run, scheduled automatically. The evidence across every trauma-exposed profession is consistent: discretionary recovery is taken least by those who need it most, because asking means identifying yourself as affected.

**Close the clinical loop.** Voluntary, confidentially handled screening outcomes related back to exposure records at the cohort level — never individually to management — so the dose-response curve is actually built rather than assumed. This is the part that takes years and is the part that eventually makes the unit defensible.

## Target Customer

The moderation vendors, bought jointly by operations, clinical staff and general counsel. The commercial argument is that a demonstrable bounded-exposure operation is a credential — for winning contracts with platforms under scrutiny, for insurance, and for defending claims already in progress.

Platforms buying moderation, who increasingly need to describe their supply chain's labour conditions and currently cannot.

The same apparatus fits emergency dispatch, child protection investigation, war crimes documentation and investigative journalism verification — every occupation where trauma arrives through a screen.

## Impact If Built

A unit and a cap convert an unbounded liability into a managed one. That transition — from a hazard that is regretted to a hazard that is measured and limited — is the single most consequential move in the history of occupational health, and this industry has not made it.

Default-protective presentation reduces the intensity of every unavoidable exposure at essentially no cost, and it is available today to any vendor that also fixes its auditing.

And the dose-response curve, once built, is a public good. It is the evidence base an entire category of screen-delivered occupational trauma currently lacks, and it would outlive any company that produced it.
