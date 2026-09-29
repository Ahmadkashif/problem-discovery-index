# Build: A Quality Function With Instruments and a Middle

**Niche:** [[niches/online-tutoring-platforms/the-tutor-quality-lead/profile|The Tutor Quality Lead]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Give the quality function an observation instrument over every session, a coaching path, and a graduated set of responses between guidance and removal.
**Tags:** #large-language-models #evaluation-metrics #hypothesis-testing #confidence-intervals #descriptive-statistics #transformers #worker-facing #workflow-orchestration
**Contested on:** Whether a quality programme can influence contractors it cannot direct.

## The Problem

The quality lead's instruments measure how parents felt. Their interventions are guidance documents and removal. Their evidence is an average that does not move.

Under those constraints the function degenerates predictably: it becomes a complaints operation. Tutors are contacted when a parent complains, which selects for the complaints parents happen to make rather than for the teaching that most needs improving, and it means the quality function's only contact with most tutors is adversarial. Tutors who are quietly mediocre and never generate a complaint are invisible; tutors who are demanding and occasionally generate one are over-represented.

Meanwhile the platform has video of every session.

## Why Nobody Has Built This

The observation instrument was expensive until recently, and manual review at any meaningful coverage was never affordable — which is why sampling a fraction of a percent became the norm and then became the definition of the job.

The intervention problem is structural rather than technical. Tutors are independent contractors. A platform that trains, directs and supervises them is doing employer-shaped things, and legal advice in this industry — as in the rest of platform labour — has generally been to keep the relationship thin. That advice has hollowed out the quality function: the platform cannot coach, so it can only remove.

And there is no evidence loop, so the function cannot demonstrate value and therefore cannot get funded to fix any of this.

## What to Build

An observation layer, a graduated response set, and a measurement of the programme itself.

**Observe every session, cheaply.** The instructional analysis over transcripts gives per-session structural measures on the entire population rather than a sampled fraction. That changes the function fundamentally: the quality lead can see the distribution of teaching behaviour across the whole tutor base, identify who is far from the norm in either direction, and find the excellent tutors as well as the struggling ones — which sampling never does.

**Build the graduated responses.** Automated private feedback after sessions, with specific suggestions. Optional coaching for tutors who want it. Targeted resources tied to a specific observed pattern. A structured improvement conversation with stated goals and a review point. Matching de-weighting while improvement is pending. Removal last. Each is proportionate to a different level of concern and currently only the last two exist.

**Design the contractor relationship deliberately with counsel.** Offered rather than required, resources rather than instructions, feedback rather than supervision, and standards attached to the service rather than to the person. This is a design constraint that can be met — it produces a genuinely different programme, not an impossible one — and getting the framing right at the start is what lets it exist at all.

**Find and use the good tutors.** The population-wide observation identifies tutors whose instruction is strong, and they are the most valuable and least used asset in the function. Peer mentoring, exemplar session libraries, and paid contributions to guidance are all more effective and less legally fraught than platform-delivered training.

**Measure the programme.** Did instructional measures improve for tutors who received feedback, against a comparison group that did not. This is a straightforward evaluation on data the observation layer produces, and it is the first time anyone in this role will have been able to answer the question of whether their work does anything.

## Target Customer

Platform quality and operations leadership, and particularly platforms selling into districts, where a demonstrable quality programme is a contractual requirement rather than an internal preference. The district segment is what funds this function properly at most platforms.

## Impact If Built

The quality function gets an instrument that measures teaching rather than sentiment, across every session rather than a sample. It acquires responses between a guidance document and removal. Its contact with tutors stops being purely adversarial. And for the first time it can show whether any of it worked.
