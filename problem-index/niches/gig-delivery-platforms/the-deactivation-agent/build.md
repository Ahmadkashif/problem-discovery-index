# Build: Case Assembly, Base Rates and a Graduated Response

**Niche:** [[niches/gig-delivery-platforms/the-deactivation-agent/profile|The Deactivation Review Agent]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Assemble the evidence and the base rates before the agent opens the case, and give them actions between doing nothing and ending someone's income.
**Tags:** #gradient-boosting #large-language-models #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #worker-facing #workflow-orchestration
**Contested on:** Whether the evidence and the statistical context for a deactivation decision can be assembled without the assembly becoming the decision.

## The Problem

A flag arrives: two customer complaints about missing items, or a fraud signal, or a rating below a threshold. The agent has minutes. They see the reason code, the account, and whatever they can find by clicking.

What they do not see is the context that determines whether the flag means anything. How many deliveries has this courier completed, and what is the complaint rate for that volume across the platform — because two complaints in six hundred deliveries is below average and two in twenty is not. Does the GPS trace corroborate or contradict the complaint. Does the delivery photo exist. Is the complaining customer a repeat complainer, which some are at rates far above the population. Has this courier's pattern changed recently, or has it always looked like this.

All of it exists. None of it is assembled. So the decision gets made on the reason code and an impression, under a handle-time target, and it removes someone's job.

## Why Nobody Has Built This

Deactivation review is a cost centre and the investment goes to detection, which reduces the queue. The agent's decision quality is not measured, so there is no metric to improve and no case to make.

The binary action space is a policy vacuum rather than a technical gap. Platforms have deactivate and not-deactivate because nobody wrote the intermediate policies, and writing them means deciding what the platform owes someone it suspects at 60% confidence — a question with legal implications under contested classification that nobody wants to answer on the record.

And there is a genuine worry about automating any part of this, which has been allowed to block the evidence assembly along with the judgement. Assembling a case file is not deciding it.

## What to Build

A case file that exists before the agent opens it, with base rates attached, and an action space with a middle.

**Assemble the evidence.** Complete delivery history with volume. The specific incidents behind the flag, with GPS trace, timestamps, delivery photo, customer chat and any support contact. The complaining customers' own complaint history across all couriers. The courier's own history of complaints by type over time. Anything from the account that bears on the pattern.

**Attach the base rates, which is the part that changes decisions.** For a courier with this delivery volume, in this market, on this order type, what is the population distribution of this complaint type — and where does this courier sit in it. An agent looking at two complaints cannot tell whether that is remarkable. An agent looking at "two complaints, 640 deliveries, 88th percentile of cleanliness for this volume" can. This is a percentile lookup over the platform's own history and it is the single highest-value element.

**Surface the exculpatory evidence actively.** A missing-item complaint on a sealed bag the courier never opened. A late delivery whose GPS trace shows twenty minutes at the merchant. A complaint from a customer who has complained on nine of their last twelve orders. A fraud flag explained by a household sharing a vehicle. The system should look for these because the agent under time pressure will not, and this is where wrongful deactivations come from.

**Build the graduated actions.** Warning with specific evidence and a stated improvement window. Temporary restriction from a specific order type. Required re-training module. Enhanced verification. Review period with defined exit criteria. Reassignment away from a market or merchant where the complaints cluster. Each proportionate to a moderate suspicion, each currently unavailable, which is why moderate suspicion resolves to either nothing or removal.

**Leave the determination human, and keep the system out of the recommendation business** — a recommendation delivered under a handle-time target becomes the decision with a human's name attached. The system's job is that the agent sees everything relevant in thirty seconds.

## Target Customer

Trust and safety operations leadership, where the internal case is supply retention — wrongful deactivation of experienced couriers is expensive and invisible — and the external case is the deactivation protections now appearing in several jurisdictions, which require stated reasons, evidence and genuine appeal.

## Impact If Built

The decision gets made with the context that determines whether the flag means anything, in the same few minutes. Exculpatory evidence gets looked for by something not under time pressure. And moderate suspicion gets a proportionate answer instead of a binary one, which is where most of the harm in this function lives.
