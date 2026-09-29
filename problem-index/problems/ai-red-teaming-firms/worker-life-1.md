# Researcher Exposure to Harmful Content

**Industry:** [[ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Worker Life Changing
**One-liner:** Red team researchers spend their working days deliberately eliciting the worst outputs a model can produce, and the industry has largely not addressed what that does to people.
**Tags:** #large-language-models #bert #evaluation-metrics #k-means-clustering #hypothesis-testing #confidence-intervals #worker-facing #compliance

## The Problem
The work requires generating and reading harmful content. To test whether a model can be induced to produce instructions for violence, a researcher constructs prompts intended to elicit them and reads what comes back. The same applies to content depicting abuse, to hate speech, to material involving children, and to detailed technical content whose misuse is the reason it is being tested.

This is not incidental exposure. It is the job, performed for hours daily, with the researcher actively trying to produce the worst output the system will emit.

Content moderation confronted this and the industry took years to acknowledge it, following litigation and journalism documenting psychological harm. AI red teaming is younger, smaller, staffed by people who are frequently framed as researchers rather than as reviewers, and has largely not built the same protections.

The framing itself is part of the problem. A moderation queue is understood as difficult work requiring support. Red teaming is understood as a technical role, which makes it harder for a researcher to say they are struggling.

## Why It Matters to the Worker
Cumulative exposure to graphic material has documented psychological effects and there is no reason the mechanism differs because the reader has a security title.

The active elicitation may make it worse rather than better. A moderator encounters content; a red teamer works to produce it, iterating until the model complies. The relationship to the material is different and the industry has not studied what that difference does.

Support structures are thin. Mental health provision, mandatory rotation, exposure limits and clinical supervision exist in mature moderation operations and are inconsistently present here, particularly at smaller firms and among contractors.

Isolation compounds it. The work cannot be discussed outside the team, sometimes not outside a cleared group, so the ordinary decompression of talking about a hard day is unavailable.

And the incentives push the wrong way. A researcher who finds more severe vulnerabilities is more valuable, which rewards going further into the material, and nothing in the structure pushes back.

## What a Solution Looks Like
Exposure measurement and limits, treated as a safety control rather than a wellbeing gesture. How much harmful content of what severity a researcher has encountered is measurable, and capping it with enforced rotation is standard practice in mature moderation operations.

Automated pre-screening so humans see less. Much of a red teaming run is confirming that a probe failed, and classifying outcomes automatically means the researcher reads only what needs judgement. This reduces exposure without reducing coverage.

Presentation controls that reduce impact without reducing information — summaries rather than full content, blurring, text rather than imagery — which are established in moderation tooling and largely absent here.

Clinical support as standard, including for contractors, and not on request. Requiring someone to ask is a barrier precisely for the people most affected.

Rotation across engagement types so that no researcher works only on the most severe categories, which is currently a specialisation people fall into and stay in.

## Impact If Solved
This work is necessary and the people doing it are exposed to material that harms readers, in an industry that has not yet built the protections a comparable field learned to build only after documented damage. Measuring exposure, automating what does not need a human, and providing clinical support are known interventions that work, and adopting them before the harm is litigated rather than after would be a first for this pattern.
