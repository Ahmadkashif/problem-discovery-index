# Progress Benchmarking From Population Data

**Niche:** [[niches/fitness-wellness-software/personal-training-coaching/profile|Personal Training & Coaching]]
**Industry:** [[industries/fitness-wellness-software|Fitness & Wellness Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Coaching platforms chart a client's progress against nothing, while holding the progress records of millions of comparable clients that would say whether this trajectory is good, typical or a reason to change the programme.
**Tags:** #time-series-forecasting #gradient-boosting #bayesian-inference #confidence-intervals #evaluation-metrics #hypothesis-testing #transfer-learning #worker-facing
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A client has been training for fourteen weeks. Their squat has gone up, their weight has come down a little, their reported energy is better. Is that a good fourteen weeks? Neither the coach nor the client knows, because there is no reference. The coach has an impression from their own clients, which is a sample of a few dozen. The client has the internet, which is a sample of people selling things. The platform has millions of comparable trajectories and shows a line chart of this one.

## What Already Exists
Growth-curve and reference-percentile methodology is thoroughly developed in paediatrics and in sports science, and is exactly the right shape for this problem — a trajectory compared against a matched population with percentile bands. Hierarchical modelling for individual trajectories with population priors is standard. The platforms hold the data. Wearable and app integrations add further signal. Nothing in the method needs invention.

## The Customization Gap
The adaptation is to a population that is heterogeneous and self-selected, and to a use that can do harm if handled carelessly. It requires: (1) matching on the factors that genuinely drive trajectory — starting point, training age, age, sex, programme type, frequency, adherence — rather than presenting a single population curve, since an unmatched comparison is worse than none; (2) adherence handled explicitly as the dominant explanatory variable, because the most useful finding for most clients is that their trajectory is entirely normal for their actual adherence, which reframes the conversation from programme to consistency; (3) careful presentation around body composition and weight, where percentile framing can be actively harmful and where the product has a responsibility not to manufacture dissatisfaction — strength, capacity and consistency measures are safer defaults and the design should say so; (4) uncertainty shown honestly, since individual variation is large and a confident percentile on a noisy measure invites bad decisions; and (5) the coach as the primary audience, with client-facing presentation under the coach's control, because the interpretation matters more than the number.

## Target Customer
Coaching platform vendors, coaching businesses at scale, and the wearable and fitness app ecosystem holding parallel data.

## Impact If Solved
A trajectory with a reference is a far better coaching conversation than a trajectory alone, and it settles the most common source of client discouragement — the belief that progress is too slow, which is usually wrong and is currently unanswerable. The population data is the platform's unique asset and this is the most defensible use of it.
