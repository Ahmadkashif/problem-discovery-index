# Vetting Decisions Are Recorded as Pass or Fail

**Niche:** [[niches/freight-brokerage/carrier-vetting-fraud-prevention/profile|Carrier Vetting & Freight Fraud Prevention]]
**Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Type:** Fix (Pain Point)
**One-liner:** An analyst clears a flagged carrier after checking three things that did not appear in the automated report, and the system stores that the carrier was cleared.
**Tags:** #tacit-knowledge-ml #bert #transformers #word-embeddings #evaluation-metrics #k-means-clustering #descriptive-statistics #compliance #worker-facing #data-integration

## The Problem
Automated screening flags more carriers than can be blocked, so analysts review the flagged set and clear most of them. The clearing is a judgment: the analyst calls the carrier, checks a detail against an independent source, recognizes a pattern as benign, or notices something that changes the picture. What the system records is the disposition. The reasoning, the checks performed, and the signals the analyst actually relied on are not captured. So the firm cannot measure whether two analysts clear the same carrier, cannot tell which manual checks are diagnostic and which are habit, and cannot promote a check that works into the automated layer — because nobody knows which ones work. When an experienced analyst leaves, their pattern recognition leaves with them, in a domain where the patterns change every few months.

## Why It's Still Broken
Vetting runs against load tender deadlines measured in minutes, so anything perceived as documentation loses. The queue system was built to route and clear alerts, which is what a queue system does. And fraud analysis is treated as investigative craft — which it is — with the usual result that the craft stays personal and its variance is invisible until an expensive miss.

## What a Fix Looks Like
Capture of the review as it happens, at a cost of seconds: which checks were performed, what each returned, which signals drove the disposition, and the analyst's confidence. Once reviews carry that, several things follow. Consistency between analysts becomes measurable, and systematic divergence becomes a training input rather than an invisible quality gradient. The diagnostic value of each manual check becomes computable once outcomes are joined — which checks actually separated fraud from noise — and the ones that work become candidates for automation, which is the only sustainable way to keep pace with a queue that grows faster than headcount. Emerging methods surface as clusters of reviews where analysts relied on signals the automated layer does not use. And a cleared carrier that later proves fraudulent can be traced back to the reasoning that cleared it, which is how the review process itself improves rather than merely absorbing blame.

## Who Feels the Pain
Analysts re-deriving checks colleagues have already worked out; the fraud lead with no instrument to measure review consistency in a function where a miss is a full truckload; brokers relying on clearances whose basis they cannot see; and the provider, whose most experienced people hold knowledge that expires every time the adversary changes method.

## Impact If Fixed
Converts investigative craft into institutional capital in a domain where the adversary iterates continuously and the defence currently resets with every departure. It is also the prerequisite for outcome learning — a confirmed fraud is only instructive if you know what the review saw and concluded.
