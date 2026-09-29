# Staleness Detected Before the Answer Is Served

**Niche:** [[niches/customer-support-platforms/knowledge-generative-deflection/profile|Knowledge & Generative Deflection]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An article that has become wrong looks exactly like one that is still right, and every signal that would distinguish them — agent contradictions, rejected answers, tickets on covered topics, product releases — is already in the platform.
**Tags:** #bert #large-language-models #change-point-detection #evaluation-metrics #confidence-intervals #hypothesis-testing #automation #compliance
**Contested on:** Every serious competitor in support deflection is fighting to detect which knowledge has quietly become wrong before it is used to answer a thousand customers — and whoever keeps the corpus true takes the account.

## The Problem
An article explains how to change a billing plan. Four months ago the flow changed: the setting moved, one of the steps no longer exists, and downgrades now require a confirmation the article does not mention. Since then the generative layer has answered eleven hundred customers from it. Some followed the steps, could not find the setting, and opened a ticket — arriving in the queue as a new issue rather than as evidence that an article is wrong. Agents have corrected the flow in their replies eighty times. Nobody connected any of it. The knowledge manager, who is one person, reviews articles on a rotation that reaches this one in March.

## Why Nobody Has Built This
Knowledge management was built around authoring and review workflow, which assumes a human maintains freshness on a schedule — a design that was inadequate when the corpus fed a search box and is untenable now that it feeds an answering system. The signals that would detect staleness are scattered across the ticket record, the answering layer's feedback and the product's own release stream, and nobody owns the join. And the commercial incentive is awkward: a vendor charging for resolutions has an interest in resolution volume, and a wrong answer that the customer accepts counts as a resolution.

## What to Build
A staleness signal per article, computed continuously from the evidence the platform already holds. Agents contradicting or correcting an article's content in their replies — detectable by comparing agent responses on a topic against the article's claims — is the strongest single indicator and is currently discarded. Rejected generative answers and their follow-up tickets, clustered by the article that sourced them. Ticket arrival on topics an article supposedly covers, which should fall when an article is good and rises when it is wrong. Product release notes and changelog entries matched to the articles whose subject they touch, which turns a release into an automatic review trigger for the specific articles it invalidated. Each signal is weak alone and together they identify the articles that have gone wrong with enough precision to direct a single knowledge manager's attention. The article is flagged, optionally suppressed from generative answering pending review, and the review arrives with the evidence — here are the eighty agent corrections and the release that caused it.

## Target Customer
Support platform vendors, particularly those pricing on resolution outcomes; knowledge management teams; and the support organisations whose deflection rate is built on a corpus nobody has audited.

## Impact If Built
A generative answering layer amplifies whatever the corpus contains, which makes staleness detection the highest-leverage investment in the category — a wrong article now misinforms at machine scale. Release-triggered review is the single most effective mechanism and connects two systems every company runs, and the agent contradiction signal is free, abundant and currently thrown away.
