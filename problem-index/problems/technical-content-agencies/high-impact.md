# Documentation Is Measured by Traffic and Judged by Whether Someone Finished the Task

**Industry:** [[technical-content-agencies|Technical Content Agencies]]
**Type:** High Impact
**One-liner:** Every documentation site has the exact record of where readers failed — the searches that returned nothing, the rephrasing, the ticket opened straight after — and reports pageviews instead.
**Tags:** #bert #transformers #large-language-models #word-embeddings #gradient-boosting #evaluation-metrics #k-means-clustering #data-integration

## The Problem
Documentation exists so that someone with a task can complete it. Whether that happened is not measured anywhere. The metrics reported are traffic, time on page, bounce rate and search ranking, all inherited from marketing content and all ambiguous here: a long time on page may mean thorough reading or total confusion, and high traffic to a page usually means the thing it describes is hard.

Meanwhile the failure signal is abundant and specific. Site search queries that return no useful result. The same user searching three times with rephrased terms. A reader who lands on a page from search and immediately returns to search. A support ticket whose answer exists verbatim in the documentation, which indicates a findability failure rather than a content gap. A community forum question that the docs already answer. The specific page someone was reading immediately before they opened a ticket.

Every one of those is a direct observation of documentation failing a person with a task, at a specific place, for a specific reason. They are recorded continuously, at high volume, in the search logs and the support system, and they are joined nowhere.

The consequence is that documentation investment is allocated by intuition and by whoever complained loudest. Writers work from a backlog assembled from feature launches and stakeholder requests rather than from evidence of where readers are failing, which means the worst pages — the ones people need and cannot use — stay worst, because nothing surfaces them.

And the measurement basis is now collapsing independently. As developers get answers from assistants that synthesise documentation without the reader arriving, pageviews stop describing anything at all. The industry is losing the proxy it should never have been using, without a replacement.

## Why It's Unsolved
The signals are in different systems owned by different teams. Search logs are in the documentation platform, support tickets are in the support system, community questions are in a forum, and product telemetry is in the product. Joining them requires someone to own the question, and documentation teams are typically small, embedded and under-resourced.

Content agencies have it worse: they deliver documentation and have no access to the reader signal at all, because the search logs and support data belong to the client and accumulate after the engagement. So the firms with the most accumulated craft knowledge have the least evidence about what works.

There is a definitional difficulty too. Task completion in documentation is not directly observable the way it is in a checkout flow — a reader who leaves may have succeeded or given up, and the two look identical. The observable proxies are failure signals rather than success signals, which means the honest metric is a failure rate rather than a satisfaction score, and failure rates are less comfortable to report.

And documentation is chronically under-funded relative to its importance, so measurement infrastructure competes with writing the next page and loses. The teams that would benefit most are the ones with the least capacity to build it.

## What a Solution Looks Like
Join the failure signals. Search queries with no useful result, rephrasing sequences, search-to-page-to-search loops, tickets whose answers exist in the corpus, and pre-ticket page visits — combined and clustered, these produce a ranked list of where the documentation is failing and how. That list is the work backlog, and it is derivable from data every organisation already has.

Distinguish the failure modes, because they need different fixes. Content that does not exist, content that exists and cannot be found, content that exists and is wrong, and content that exists and is incomprehensible are four different problems with four different remedies, and they are separable from the signals: a ticket answered by an existing page is findability, a repeated rephrasing is vocabulary mismatch, a page visited before a ticket is comprehension or accuracy.

Measure the corpus as a source for synthesis. If readers increasingly receive answers assembled by an assistant, the relevant quality is whether the documentation is accurate, unambiguous, self-contained and structured enough to be synthesised correctly — which is testable by asking questions against the corpus and checking the answers against ground truth.

Close the loop back to the agency. A content firm that contracts for search and support signal access can finally learn which of its patterns work, which is the same evidence problem every firm in this cluster has and is unusually tractable here because the signal is so direct.

## Impact If Solved
Documentation quality determines support cost, developer adoption and product usability, and it is currently improved by intuition because the abundant, direct, continuous evidence of failure is never assembled. Joining the failure signals produces an evidence-ranked backlog immediately, with no modelling required for most of the value. And measuring the corpus as a synthesis source addresses the shift in how technical content is actually consumed — which is happening to this industry whether or not it measures it.
