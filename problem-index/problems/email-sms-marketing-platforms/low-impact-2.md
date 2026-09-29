# Lifecycle Flows Built by Hand

**Industry:** [[email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every brand builds the same dozen automated journeys as hand-drawn rule trees, and then nobody can say which branches earn anything.
**Tags:** #hidden-markov-models #seq2seq #gradient-boosting #causal-inference #markov-decision-processes #evaluation-metrics #automation #workflow-orchestration

## The Problem
Lifecycle marketing means a set of automated journeys: welcome, browse abandonment, cart abandonment, post-purchase, replenishment, winback, loyalty. Each is built as a flow chart of triggers, waits, conditions and splits, drawn by a marketer in a visual editor, with copy for every branch.

A mature programme has fifty or more of these, some built years ago by people who have left. They interact: a customer can be in four at once, receiving messages that contradict each other or arrive within an hour. Nobody has a map. Changing one risks side effects nobody can enumerate, so flows accumulate rather than get rationalised, and the standard failure is a flow that silently stopped firing months ago because an upstream event name changed.

The evaluation is the weakest part. Flow revenue is reported as orders attributed to a click within a window, which credits the abandonment message for carts that would have been recovered anyway — a well-known and large effect that essentially no brand measures, because the holdout is easy to run and reduces a number everyone likes.

## What Already Exists
Visual journey builders are the core product of every platform in this category, and they are good: Braze, Iterable, Klaviyo and Customer.io all offer sophisticated branching, waits, channel selection and experimentation. Pre-built flow templates cover the standard dozen. Many platforms offer built-in holdout groups for journeys, which is more than most other channels provide. Reverse-ETL tools sync the customer attributes flows depend on.

## The Customisation Gap
The builder is generic by necessity and the resulting programme is bespoke by accident. What every brand actually needs and nobody has is a view of the programme as a whole: which flows a given customer can be in simultaneously, where messages collide, which branches have never been traversed, which are firing on events that no longer exist, and what each branch is actually worth.

Branch-level evaluation is the substantive gap. A flow is a tree and the industry evaluates it as a single unit, so a welcome series reports revenue and nobody knows that the third message earns nothing and the fourth generates most of the unsubscribes. Per-branch holdouts are runnable in most platforms and essentially nobody runs them, which means a decade of programme design rests on assumption.

The more ambitious version is to stop drawing trees. The sequence of contacts that maximises long-run value per customer is a policy over states, learnable from observed journeys and outcomes, and the hand-drawn tree is a coarse human approximation of it. That reframing is well within reach of the data these platforms hold and is blocked mainly by marketers reasonably wanting to see and control what is sent — which argues for inducing a policy and expressing it as an editable flow, rather than replacing the editor with a black box.

## Impact If Solved
Lifecycle flows generate the majority of email and SMS revenue for most direct-to-consumer brands and are the least-examined part of the stack. A programme-level map ends the silent breakages and collisions; branch-level holdouts reveal which of the fifty flows are load-bearing and which are attrition generators wearing a revenue label. Both are achievable with what the platforms already hold, and both are resisted for the same reason — they produce a smaller reported number and a better business.
