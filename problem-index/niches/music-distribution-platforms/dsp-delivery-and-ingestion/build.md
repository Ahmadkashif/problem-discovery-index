# Accepted First Time, Everywhere

**Niche:** [[niches/music-distribution-platforms/dsp-delivery-and-ingestion/profile|DSP Delivery & Ingestion]]
**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A release misses its date because a service's artwork rule changed and the rule lived in an engineer's memory.
**Tags:** #data-integration #workflow-orchestration #automation #evaluation-metrics #change-point-detection #confidence-intervals #compliance #sets-and-logic
**Contested on:** Every serious competitor in this niche is fighting to get a release accepted by every streaming service first time, against rules that sit on top of a shared standard and change without notice — and whoever stops releases missing their date on a specification detail wins the artists who have one shot at a launch.

## The Problem
A release is delivered to a dozen services. One rejects it because the artwork contains text a service does not allow, another because a contributor role is not in its vocabulary, a third because the title formatting conflicts with a convention. Each rejection is discovered after delivery, each requires a fix and a redelivery, and each consumes days from a schedule built around a release date the artist has promoted. The rules that caused it were knowable before the delivery.

## Why Nobody Has Built This
Each service integration was built when that service was added, so the rules are embodied in code and in people rather than in a model — an integration written once encodes the rules as they were and has no mechanism for noticing they changed. Services document inconsistently and change without notice. Rejections are handled as support tickets. And nobody measures first-time acceptance, so the cost is invisible.

## What to Build
Model the rules and validate before delivering. Encode each service's rules as a queryable rule set rather than as integration code, which is the core and makes validation possible before anything is sent. Validate every release against every destination's rules at upload, so the artist fixes it while they are still in the flow rather than days later. Learn rules from rejection history, since the services' actual behaviour is better documented by their rejections than by their specifications. Detect rule changes from a spike in rejections for a specific reason, because that is how a change announces itself and nobody watches for it. Translate rejection codes into actionable instructions, as they are currently cryptic and go to support. Predict the risky release before delivery, which lets the schedule absorb a fix. Prioritise by release date proximity, since a release two days out is a different urgency from one two months out. Report first-time acceptance by service, which is the function's metric and does not exist. Keep the rules versioned, so a historical rejection can be explained. And share the rule observations across distributors where possible, since everyone is discovering the same changes independently.

## Target Customer
Integration and operations leadership, artists whose release dates slip, streaming services receiving invalid deliveries, and metadata standards bodies.

## Impact If Built
An integration written once encodes the rules as they were and has no mechanism for noticing they changed. Encoding rules as a queryable set and validating at upload moves every rejection from after delivery to before it.
