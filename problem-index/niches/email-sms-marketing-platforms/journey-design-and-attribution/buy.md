# Policy Evaluation Practice

**Niche:** [[niches/email-sms-marketing-platforms/journey-design-and-attribution/profile|Journey Design & Attribution]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Sequential decision-making under uncertainty is a developed field with policy evaluation methods, and marketing journeys are drawn as flowcharts and judged on a total.
**Tags:** #markov-decision-processes #causal-inference #monte-carlo-methods #confidence-intervals #evaluation-metrics #hypothesis-testing #temporal-difference-learning #bayesian-inference
**Contested on:** Every serious competitor in this niche is fighting to tell a brand which branches of its automated journeys earn anything — and whoever does that turns a hand-drawn rule tree into something that can be improved.

## The Problem
Deciding what action to take next given a state, and evaluating whether a policy is any good, is a developed field. Sequential decision frameworks, off-policy evaluation, and policy improvement methods all exist precisely for situations where actions unfold over time and their value is not immediately observable. A customer journey is a textbook instance: a state, a set of possible messages, a transition, a delayed reward. The category builds them as flowcharts and evaluates them on a revenue total.

## What Already Exists
Sequential decision frameworks and dynamic programming; off-policy evaluation from logged data; policy improvement and comparison methods; contextual bandits for action selection; and simulation for policy testing.

## The Customization Gap
The adaptation is to a policy that must remain explainable and controllable by a marketer. It requires: (1) a policy a human can read and edit, since a learned policy that cannot be explained will not be approved by a brand that is accountable for what it sends — this explainability constraint rules out the direct application and is the central adaptation; (2) actions with a cost that is not monetary, since sending a message consumes the recipient's tolerance and the reward function must include the fatigue term from the adjacent niche; (3) rewards that are delayed by weeks and partially unobservable, requiring careful off-policy evaluation rather than naive logged comparison; (4) hard constraints from consent, frequency caps and compliance that the policy must respect absolutely rather than trade off; and (5) episodes that are long and sparse, with a customer entering a journey a handful of times rather than thousands.

## Target Customer
Messaging platform data teams, lifecycle and CRM functions, and decision-optimisation vendors for whom marketing journeys are an unserved application.

## Impact If Solved
A journey is a textbook sequential decision problem evaluated as a flowchart with a revenue total. Explainability is the constraint that rules out direct application, and the reward function must charge for the recipient's tolerance rather than only counting revenue.
