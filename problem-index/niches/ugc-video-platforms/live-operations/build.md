# Governing Something That Is Happening Now

**Niche:** [[niches/ugc-video-platforms/live-operations/profile|Live Operations]]
**Industry:** [[industries/ugc-video-platforms|UGC Video Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every governance mechanism in the category assumes the content already exists and can be reviewed, and live content does neither.
**Tags:** #transformers #cnns #change-point-detection #evaluation-metrics #confidence-intervals #automation #workflow-orchestration #compliance
**Contested on:** Every serious competitor in this niche is fighting to moderate, monetise and deliver a broadcast while it is happening — and whoever handles the real-time case wins the surface where every decision has to be made before anyone can review it.

## The Problem
Live inverts the governance model. A removal after a broadcast addresses nothing because the audience already saw it. A chat moving at hundreds of messages a minute cannot be read by the volunteer moderators it is left to. A monetisation decision must be made about content that has not happened yet. An enforcement action during a stream cuts off a person mid-sentence in front of their audience, which is the most consequential thing the platform can do to them and is decided in seconds with no review.

## Why Nobody Has Built This
Governance was designed for recorded video where review precedes consequence, so the live case inherited the recorded model and the timing does not work — a process built around after-the-fact review cannot govern something that is over before the review happens. Real-time classification is harder and more expensive. Live is a smaller share of revenue. And chat moderation was handed to volunteers, which removed the pressure.

## What to Build
Intervene during, gradually, and review afterwards. Detect in real time and intervene gradually — a warning to the streamer, a delay, a restriction — rather than only cutting off, which is the core and is the difference between governance and a guillotine. Warn the streamer before acting where the situation allows, since most live violations are unintentional and a warning stops them. Support chat moderation properly, as it is left to volunteers facing a volume no person can read and is where most of the harm actually occurs. Moderate the chat with the same classification capability applied to video, which is currently far weaker. Review live enforcement afterwards, because a decision made in seconds with no review is the least accountable action in the category. Monetise live predictively rather than reactively, so a streamer is not demonetised mid-broadcast for something they cannot undo. Detect the escalating situation rather than the individual violation, since live incidents build and the early signal is the useful one. Protect the volunteer moderators, connecting to the moderation work, as they face real-time abuse with a delete button. Give the streamer visibility of what triggered an action immediately, which matters more live than anywhere. And measure live enforcement accuracy separately, since it is made under conditions that guarantee a higher error rate.

## Target Customer
Live platform and trust leadership, streamers, volunteer chat moderators, and real-time moderation vendors.

## Impact If Built
A process built around after-the-fact review cannot govern something that is over before the review happens, so live inherited a model that does not fit. Graduated real-time intervention with a warning first is what turns an unappealable cut-off into governance.
