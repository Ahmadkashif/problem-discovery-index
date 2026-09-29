# Content Measured by Outcome, Not by Use

**Niche:** [[niches/customer-support-platforms/macro-content-lifecycle/profile|Macro & Content Lifecycle]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Support content is evaluated by how often it is used, which says nothing about whether the conversations it was used in went well, and the outcome of every one of those conversations is in the same system.
**Tags:** #survival-analysis #gradient-boosting #hypothesis-testing #evaluation-metrics #confidence-intervals #descriptive-statistics #automation #causal-inference
**Contested on:** Every serious competitor in support content is fighting to keep a library alive rather than merely large — and whoever can retire dead content with evidence takes the knowledge function.

## The Problem
A macro is used eleven hundred times a quarter. It is also followed by a repeat contact in a third of those cases, because it answers the literal question and misses the situation that usually produces it. A second macro is used ninety times and resolves every one. The reporting shows usage. The first macro is considered a success and is the one new agents are taught. The data that distinguishes them — what happened after the content was used — is in the ticket record and is joined to nothing.

## Why Nobody Has Built This
Usage counting is trivial and outcome attribution is not: the conversation's result depends on far more than the content used, so a naive comparison of resolution rates across macros confounds content quality with topic difficulty. Handling that requires comparing within topic and controlling for what the conversation was about, which is a modest analysis nobody has run. And the knowledge function is typically one person with no analytical support, so even an available analysis has no owner.

## What to Build
An outcome measure per content item, computed within topic. For each macro and article, the resolution rate, repeat contact rate and escalation rate of the conversations in which it was used, compared against other content used on the same topic rather than against the library average — which removes most of the confounding and is what makes the comparison fair. Trend over time, since a content item whose outcomes are deteriorating is the staleness signal this industry's first niche is about, arriving from a different direction. Coverage gaps identified from the other side: topics with high contact volume and no content, and topics where agents consistently write free text instead of using the available macro, which is direct evidence the macro is wrong. And the library health figure — what proportion of content has been used at all in the last period, and what proportion of usage is concentrated in how few items — which is the number that makes the state of the library visible and is a single query.

## Target Customer
Support platform vendors, knowledge management functions, and the support organisations whose generative answering layer now retrieves from a library nobody has audited.

## Impact If Built
Outcome measurement turns content management from a volume exercise into a quality one and identifies both the content to retire and the content to copy. The agents-writing-free-text signal is the most useful single finding, since it points precisely at the topics where the library is failing and does so without anyone having to review anything.
