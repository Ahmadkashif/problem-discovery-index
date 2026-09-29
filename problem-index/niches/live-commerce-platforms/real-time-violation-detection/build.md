# Detected After It Aired

**Niche:** [[niches/live-commerce-platforms/real-time-violation-detection/profile|Real-Time Violation Detection]]
**Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Content classification is mature and moderating a live stream is a different problem, because the violation is broadcast before anything can be decided about it.
**Tags:** #transformers #cnns #object-detection #large-language-models #change-point-detection #evaluation-metrics #confidence-intervals #automation
**Contested on:** Every serious competitor in this niche is fighting to catch a violation while it is still airing rather than after it has been broadcast — and whoever closes that gap defines what the platform can safely allow to go live.

## The Problem
The classifier samples a frame every two seconds, runs it, and returns a score. By the time three consecutive samples agree, eleven seconds have passed and four thousand people have seen it. Worse, most live commerce violations are not visible in a frame at all: a counterfeit sold as authentic, a prohibited item described in euphemism, a health claim made verbally, a stream that escalates gradually over twenty minutes. The detection stack was assembled from services designed to classify a finished upload, and it is being asked to supervise an unfolding event.

## Why Nobody Has Built This
Available classification services are built around a request-response model over a complete artefact, and streaming versions are thin wrappers over the same thing — the mismatch is architectural rather than a tuning issue. Temporal modelling over a live stream costs continuously rather than per item, which is a materially different cost structure. The category's real violations require commerce-specific understanding nobody sells as a service. And a missed violation is attributed to moderator capacity.

## What to Build
Detect over time, not over frames. Run continuous temporal models over the stream rather than classifying sampled frames, which is the architectural change everything else depends on and is where the borrowed stack fundamentally does not fit. Fuse video, audio, transcript and chat in one decision, since the chat reacting is frequently the earliest and strongest signal that something has happened and it is currently a separate pipeline. Model escalation explicitly, because live violations usually build and the detectable moment is well before the threshold crossing — this is the largest available latency gain and it comes from structure rather than from a faster model. Detect the category's actual violations: counterfeit and replica selling, prohibited and regulated goods, unsubstantiated claims, off-platform payment solicitation — none of which generic content safety services address and all of which are the majority of live commerce enforcement. Emit calibrated confidence with the evidence attached, since the downstream consumer is a human deciding in four seconds and an uncalibrated score is useless to them. Tier the response by confidence and consequence, so high-confidence high-harm cases can act automatically while ambiguous ones reach a person with context. Maintain a seller-level prior, because risk is not uniform and a first-time seller in a high-risk category warrants different sensitivity. Learn continuously from moderator decisions, which are the best labels available and are currently discarded. And measure time-to-detection in seconds as the primary metric, because that is the entire contest.

## Target Customer
Live commerce platforms, trust and safety engineering teams, and content safety vendors whose products assume a finished artefact.

## Impact If Built
Classification services answer questions about finished uploads and are being asked to supervise an unfolding event. Modelling escalation is the largest latency gain available and comes from structure rather than speed, and the category's real violations are commerce-specific and unaddressed by generic safety services.
