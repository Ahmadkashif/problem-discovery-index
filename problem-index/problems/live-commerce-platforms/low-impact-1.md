# Real-Time Moderation of Live Video

**Industry:** [[live-commerce-platforms|Live Commerce Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Content classification for video, audio and text is mature and available as a service, and moderating a live stream is a different problem because the violation is broadcast before anyone can act.
**Tags:** #cnns #transformers #bert #object-detection #evaluation-metrics #confidence-intervals #compliance #worker-facing

## The Problem
Moderating recorded content is a review problem: the content exists, it is examined, a decision is made, and nothing was published in the meantime.

Live is different in kind. A host says something prohibited, shows a counterfeit, makes a false claim about a product, or displays something that should not be broadcast, and it has already reached every viewer. Removal is limited to stopping the stream, which affects everyone watching including the host's legitimate business.

The commerce dimension adds violation types that general moderation tooling does not cover. Counterfeits held up to a camera. Product claims that are regulatory violations — health assertions about a supplement, safety claims about a device. Pressure tactics and misrepresented scarcity. Undisclosed relationships in a promotion. Prohibited items in categories that are legal to own and not to sell.

Automated detection must run continuously across video, audio and chat with low latency, at high recall for serious violations, and with a false positive rate low enough that legitimate sellers are not repeatedly interrupted.

## What Already Exists
Content classification services for video, image, audio and text are mature and available from cloud vendors and specialists. Real-time speech transcription is fast and accurate. Chat moderation is a well-developed field. Live platforms already combine automated detection with human review queues. Delay buffers are technically possible and used in broadcast.

## The Customisation Gap
General classifiers cover general harms and not the commerce-specific violations that matter here. Recognising a counterfeit held to a camera, a prohibited health claim in speech, or a manufactured scarcity tactic are domain-specific detection problems with no off-the-shelf answer.

Latency and cost force sampling. Analysing every frame of every concurrent stream is expensive, so platforms sample, and a violation between samples is broadcast. Intelligent sampling — increasing rate on higher-risk streams and hosts, or when chat sentiment shifts — is a straightforward improvement rarely implemented.

Prioritisation of the human queue is coarse. Reviewers cannot watch everything, and directing them by predicted risk rather than by report volume is where their limited capacity would do most good.

The intervention range is too narrow. The choice between doing nothing and ending a stream is crude, and intermediate actions — a private warning to the host, a temporary chat restriction, a hold on purchases from a flagged item — are technically available and rarely built.

## Impact If Solved
Live commerce carries violation types that general moderation does not address, at a latency where prevention is barely possible and only intervention remains. Commerce-specific detection with intelligent sampling and graduated interventions is what would let platforms act before a violation reaches its full audience without punishing legitimate sellers for a false positive.
