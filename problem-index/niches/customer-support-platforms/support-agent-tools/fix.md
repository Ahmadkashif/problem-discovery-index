# Satisfaction Scores at Individual Volume

**Niche:** [[niches/customer-support-platforms/support-agent-tools/profile|Support Agent Tools]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** An agent's customer satisfaction score is computed from a handful of survey responses a month, heavily selected toward the annoyed, and it is used in performance reviews as though it measured them.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #probability-distributions #worker-facing #quick-win #compliance
**Contested on:** Every serious competitor building for support agents is fighting to measure and support whether the customer's problem was actually solved rather than how long it took — and whoever the agents experience as help rather than surveillance takes the deployment.

## The Problem
An agent handles four hundred conversations in a month and receives eighteen survey responses. Three are negative: one from a customer whose refund was declined by policy, one from a customer who was abusive and whom the agent handled correctly, and one about a product failure the agent could not fix. The score is 83%, below the team target of 90%, and it appears in a performance conversation. The same agent the following month receives twenty-two responses, none negative, and scores 100%. Nothing about their work changed. The metric's variance at this volume exceeds any plausible difference in performance, and it is nevertheless treated as a measurement of the individual.

## Why It's Still Broken
Satisfaction surveys were adopted as a customer-centred counterweight to handle time, which was the right instinct, and the statistical properties were never examined. Response rates are low and response selection is strongly non-random. Attribution is the deeper problem: a survey about a conversation captures the customer's feeling about the outcome, which is frequently determined by policy, by the product or by the situation rather than by the agent. And the number is easy, familiar and appears on every dashboard, which is enough to sustain almost any metric.

## What a Fix Looks Like
Report it honestly or stop reporting it individually. Compute the confidence interval on every agent-level satisfaction score and show it, which in most cases will be wide enough to make the point without any argument. Suppress individual reporting below a volume threshold where the estimate cannot support a conclusion. Separate the attributable from the unattributable: a dissatisfied customer whose request was declined by policy is telling the organisation something about the policy and nothing about the agent, and classifying survey responses by what drove them is straightforward and is the single most useful correction. Aggregate to the team and the topic where the volume supports it, which is where the signal actually is. Exclude responses from conversations where the customer was abusive, since scoring an agent on the opinion of someone who mistreated them is indefensible. And use resolution as the individual measure instead, which is computable at full volume and measures the right thing.

## Who Feels the Pain
Agents evaluated on a number dominated by noise and by circumstances outside their control; managers conducting performance conversations on evidence that does not support them; and the organisation, which is optimising against a signal it has never examined.

## Impact If Fixed
Showing the confidence interval is a trivial change that would end most inappropriate uses of the metric immediately. Classifying dissatisfaction by cause is the constructive half, since it redirects the finding to the policy or the product where it belongs, and excluding abusive interactions is an obvious fairness correction that costs nothing.
