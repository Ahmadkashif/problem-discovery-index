# Prompts and Responses Shipped to a Third Party

**Niche:** [[niches/llm-application-tooling/tracing-and-prompt-operations/profile|Tracing & Prompt Operations]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Fix (Pain Point)
**One-liner:** Tracing captures the full prompt and response, which routinely contain customer personal data, and ships them to a vendor under a decision nobody reviewed.
**Tags:** #compliance #data-integration #descriptive-statistics #evaluation-metrics #automation #quick-win #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor in this sub-niche is fighting to let an operator explain a production failure and change a prompt without breaking anything — and whoever does that takes the account, because the buyer already has the application running and those are the only two things they need.

## The Problem
An engineer adds a tracing library in an afternoon. It captures every prompt and response. The prompts contain whatever the customer typed — names, account details, health information, a pasted document — and the responses contain whatever the application said back. All of it now sits with a third-party vendor, in an unknown jurisdiction, under a data processing arrangement nobody assessed, because the integration was a decorator and a key rather than a procurement event. The company's data protection register does not include it. A regulated buyer who asks the right question during procurement will stop the deployment.

## Why It's Still Broken
The tracing integration is designed to be effortless, which means it bypasses the review that a data transfer would normally trigger. Redaction reduces the trace's usefulness, so the defaults capture everything. Engineers adding a debugging tool do not think of themselves as exporting customer data, reasonably enough. And the problem surfaces only when compliance or a regulated customer asks, which is late.

## What a Fix Looks Like
Make the data decision explicit and give teams a usable middle. Default to capturing metadata and not payloads, with payload capture as a deliberate opt-in, which inverts the current default and is the change that would prevent most of these exposures. Provide client-side redaction that runs before anything leaves the application, with detection for the common sensitive categories, so a team can keep useful traces without exporting personal data. Support self-hosted and in-region deployment as a first-class option rather than an enterprise upsell, since for many buyers it is the only acceptable configuration. Offer payload sampling with short retention, which preserves debugging value at a fraction of the exposure. Store payloads separately from metadata with their own access control and retention, so the aggregate analysis does not require the raw content. Produce the processing documentation buyers need — what is captured, where it is stored, for how long, by whom it can be accessed — which is a document that costs a day and unblocks regulated procurement. Warn at integration time that payload capture is being enabled, which puts the decision in front of the engineer making it. And support deletion by end-user request, since the payloads contain their data and nothing currently handles that.

## Who Feels the Pain
Compliance functions discovering an unassessed data transfer; end users whose messages were exported to a vendor they have never heard of; and the teams whose deployment stalls in a security review they did not anticipate.

## Impact If Fixed
Inverting the default so payloads are opt-in prevents most of these exposures, and client-side redaction keeps traces useful without exporting personal data. The processing documentation costs a day and unblocks regulated procurement that currently stalls.
