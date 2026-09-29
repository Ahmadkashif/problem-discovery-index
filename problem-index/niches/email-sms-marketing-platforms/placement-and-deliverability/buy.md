# Reputation Monitoring Practice

**Niche:** [[niches/email-sms-marketing-platforms/placement-and-deliverability/profile|Placement & Deliverability]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Network operations built a discipline for inferring the state of systems they do not control, and deliverability infers it from a seed list and a forum.
**Tags:** #bayesian-inference #change-point-detection #confidence-intervals #evaluation-metrics #descriptive-statistics #hypothesis-testing #graph-theory #automation
**Contested on:** This niche is not terminal — inferring where an email landed and decoding why a carrier dropped a text are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
Inferring the state of an external system from its observable behaviour is routine network and service operations practice: active probing, passive measurement, distributed vantage points, reputation and blocklist monitoring, and change detection against a baseline. Content delivery and network operations teams do this continuously against networks they do not control. Deliverability, which is exactly this problem against mailbox providers and carriers, runs on a handful of seed addresses, vendor reputation scores and practitioner community knowledge.

## What Already Exists
Distributed active probing from many vantage points; passive measurement and inference from traffic behaviour; reputation and blocklist monitoring; change detection against behavioural baselines; and incident correlation across a network.

## The Customization Gap
The adaptation is to an adversarial counterparty who changes behaviour deliberately and undisclosed. It requires: (1) probes that are indistinguishable from real traffic, since seed addresses are detectable and a provider that treats them differently invalidates the whole measurement — this detectability problem is the central weakness of current practice; (2) inference from the real population's engagement rather than from probes alone, which is where a platform's corpus becomes the instrument; (3) attribution across shared infrastructure, since many brands share sending resources and reputation effects are collective in a way network monitoring rarely faces; (4) rapid detection of provider policy changes, which arrive without announcement and affect everyone at once; and (5) outputs that a marketer can act on, rather than a network engineer.

## Target Customer
Messaging platforms, deliverability service providers, and network monitoring vendors for whom messaging placement is an unserved application.

## Impact If Solved
Network operations infers external state from distributed measurement, and deliverability uses seed addresses that the counterparty can detect. Inferring from the real population's engagement across many brands is the instrument only a platform has.
