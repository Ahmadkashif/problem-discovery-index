# The Path That Works When Self-Service Does Not

**Niche:** [[niches/customer-support-platforms/customers-who-cannot-self-serve/profile|Customers Who Cannot Self-Serve]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Support is optimised end to end for customers who can use the automated path, and the ones who cannot are routed through every mechanism designed to stop them before reaching the help they need.
**Tags:** #bert #large-language-models #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to get a customer who cannot use the self-service path to a person quickly and in their own language — and whoever stops routing them in circles takes a population the category has optimised against.

## The Problem
A customer with limited vision uses a screen reader to open a support chat. The widget's controls are unlabelled, the automated responses appear in a live region that interrupts, and the option to reach a person is a graphical element with no accessible name. They try the phone line, navigate a menu by listening, and are returned to a recording suggesting they use the website. A second customer speaks Portuguese; the company supports English and Spanish. A third is a carer trying to resolve a deceased relative's account and finds no category that fits. Each is a person with a genuine need, each is prevented by a mechanism built for someone else, and none of them appears as a failure in any metric — they appear as abandonment, which reads as deflection.

## Why Nobody Has Built This
The metrics point the other way: every one of these customers reaching a person increases cost per contact and reduces deflection, so the system's incentives are actively opposed to serving them well. Accessibility is treated as a compliance checklist applied to a page rather than as a property of an interaction flow, which means the widget passes an audit and fails a screen reader user. Multilingual support is constrained by verification rather than by translation cost. And the affected customers are a minority in any single organisation's data and have no collective voice in a product decision.

## What to Build
An assisted path designed for the people the main path fails, and measured separately. Detection first: a customer using assistive technology, writing in an unsupported language, showing signs of distress or difficulty, or repeatedly failing to progress through an automated flow, is identified and routed to a person quickly rather than being cycled — which requires the system to treat repeated failure as a signal rather than as persistence. Accessibility tested as an interaction flow with assistive technology rather than audited as a page, which is where the current compliance approach fails. Language handled properly, as the buy note describes. Distress and vulnerability signals used to route and to inform the agent, with care, since the purpose is to help rather than to label. And measurement separated: time to human for customers on the assisted path, and resolution rate for them, reported alongside the headline deflection figure — because an organisation that reports only the aggregate has no visibility of the population its design excludes.

## Target Customer
Support platform vendors, regulated sectors with accessibility and fair treatment obligations, large consumer organisations with diverse customer bases, and the accessibility and consumer advocacy organisations who document these failures.

## Impact If Built
The population affected includes disabled customers, older customers, those with limited English and those in difficulty — which is a substantial share of any consumer base and disproportionately the people for whom the underlying issue matters most. Measuring their experience separately is the necessary first step, because the aggregate metrics the category runs on are structurally incapable of showing when this group is being failed.
