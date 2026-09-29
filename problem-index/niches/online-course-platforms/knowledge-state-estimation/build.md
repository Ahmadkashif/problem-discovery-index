# What Does This Learner Actually Know

**Niche:** [[niches/online-course-platforms/knowledge-state-estimation/profile|Knowledge State Estimation]]
**Industry:** [[industries/online-course-platforms|Online Course Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The learner rewound the same ninety seconds four times, failed the question twice and moved on, and the system recorded progress.
**Tags:** #hidden-markov-models #bayesian-inference #gradient-boosting #evaluation-metrics #confidence-intervals #markov-chains #cross-validation #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to infer what a learner currently knows from pauses, attempts, abandonments and returns — and whoever estimates mastery accurately can tell each learner what to do next instead of what to watch next.

## The Problem
Every signal that indicates struggle is being recorded: the repeated rewind, the long pause, the multiple attempt, the abandonment at a particular concept, the return after a gap. Every signal that indicates mastery is there too: the first-attempt success, the skipped explanation, the accelerating pace. The platform aggregates all of it into a progress percentage that measures position in a video sequence, and serves everyone the same next segment.

## Why Nobody Has Built This
Progress was defined as position because position is trivially computable, so a proxy for effort became the measure of learning — a metric available on day one displaces a model that would have to be built. Knowledge tracing sits in academic and school-focused products rather than in consumer platforms. Adaptive paths conflict with a fixed course structure sold as a unit. And nobody is measured on whether learners learn.

## What to Build
Model mastery per concept and act on it. Estimate a per-concept knowledge state from behaviour and assessment, which is the core and is what turns telemetry into a model of the person. Use struggle signals as evidence, since rewinds, pauses and attempt counts are established indicators and are being discarded. Map the course's concepts and their prerequisites, because an estimate without a structure cannot say what to do next and most courses have no concept map at all. Diagnose the missing prerequisite when a learner fails, as that is the actionable finding and a score is not. Adapt the path — skip what is known, revisit what is not, insert practice where struggle is detected — which is the product that follows from the model. Handle the cold start, since a new learner has no history and a short diagnostic is cheap. Model forgetting and schedule retrieval, because durability is the point and nothing currently accounts for it. Express the estimate's confidence, as acting confidently on a weak estimate is how adaptive systems lose trust. Feed aggregate mastery patterns back to instructors, who would learn which explanations fail. And validate against later performance rather than against completion, which is the only honest test.

## Target Customer
Product and data leadership, learners who stall on an unnamed prerequisite, instructors who cannot see where teaching fails, and adaptive learning vendors.

## Impact If Built
A metric available on day one displaces a model that would have to be built, so position became progress. The struggle and mastery signals the platform already logs support a per-concept model of what a learner knows.
