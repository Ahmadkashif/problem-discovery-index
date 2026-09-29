# Traces Missing Exactly What You Need

**Niche:** [[niches/llm-application-tooling/instrumentation-completeness/profile|Instrumentation Completeness]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Tracing libraries are mature and standards-compliant, and the traces most applications actually emit are missing exactly the context needed to debug the failure you are looking at.
**Tags:** #data-integration #evaluation-metrics #automation #workflow-orchestration #descriptive-statistics #graph-theory #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to make the trace contain the thing you need at the moment you need it — and whoever does that takes the account, because a trace missing the decisive context is indistinguishable from no trace at all.

## The Problem
An engineer investigates a wrong answer from three weeks ago. The trace shows the final prompt and the response. It does not show which documents retrieval returned, which prompt template version was used, what the user's account state was, whether a cache was hit, or what the user did next. Each of those was available at request time and none was recorded. The investigation stops. The team adds the missing instrumentation, which helps with the next occurrence and does nothing for this one, and the cycle repeats with a different missing field.

## Why Nobody Has Built This
Instrumentation is added in a hurry during a build, by a developer who does not yet know which fields will matter. Automatic instrumentation covers the library calls and not the application logic around them, which is where most of the context is. There is no completeness check, so an inadequate trace looks identical to a good one until it is needed. And the cost is paid months later by whoever is debugging.

## What to Build
Make completeness measurable and mostly automatic. Define a completeness standard for an LLM application trace — the model call with prompt, parameters and response, the prompt template and its variables and version, retrieval inputs and results, tool calls, cache status, the model actually used, cost and tokens, and a correlation to the user's session — and score every trace against it, which turns an invisible gap into a number and is the core of the build. Warn at development time when a span is missing fields its type requires, which is where the fix is cheap. Capture the prompt template and its variables separately rather than only the rendered string, since attributing a failure to a template or to a variable is a common question and the rendered form answers neither. Instrument the application logic around the framework automatically where possible, since that is where the missing context lives. Correlate traces to user sessions and to the reactions that follow, which the fix note develops. Provide a debugging checklist that names what would be needed for each common failure type, so instrumentation is guided by the investigations it will support. Report completeness as an operational metric and its trend, so it improves deliberately. And backfill what can be reconstructed, since some context is recoverable from other systems after the fact.

## Target Customer
Platform and applied AI teams, the engineers doing investigations, and the tracing vendors whose libraries are good and whose customers' traces are not.

## Impact If Built
An inadequate trace is indistinguishable from a good one until the moment it fails, which is months after the cheap fix. A completeness standard scored per trace turns that invisible gap into a number, and capturing template and variables separately answers a question the rendered prompt cannot.
