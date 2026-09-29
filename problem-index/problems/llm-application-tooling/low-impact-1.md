# Trace Instrumentation Completeness

**Industry:** [[llm-application-tooling|LLM Application Tooling]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Tracing libraries are mature and standards-compliant, and the traces most applications actually emit are missing exactly the context needed to debug the failure you are looking at.
**Tags:** #large-language-models #bert #feature-engineering #evaluation-metrics #data-integration #workflow-orchestration #automation

## The Problem
An LLM application makes a request and something goes wrong. The trace shows the prompt sent and the response received.

What it usually does not show is everything that determined the prompt. Which documents were retrieved and their scores. What was in the conversation memory and what was truncated to fit the context window. Which tools were available and how they were described. What the user's session state was. Which prompt version and which model version. What the retrieval configuration was at that moment.

Debugging without those is guesswork. The engineer knows the model produced a bad answer and cannot tell whether it was given the right context, so the investigation begins by adding instrumentation and waiting for the failure to recur.

Getting complete traces requires deliberate instrumentation of every stage, and teams underestimate this consistently. Auto-instrumentation covers framework calls and misses the application's own logic, which is where the interesting decisions were made.

## What Already Exists
Langfuse, Helicone, Braintrust, LangSmith and the cloud observability vendors all provide capable tracing with nested spans, token accounting, latency breakdown and cost attribution. OpenTelemetry semantic conventions for generative AI have emerged. Framework auto-instrumentation covers the common paths. Session and user grouping is standard. Trace search and filtering are good.

## The Customisation Gap
Auto-instrumentation captures the model call and the application's own decisions are unrecorded, so the trace answers what was sent and not why. Retrieval results, memory truncation and configuration state are the three most commonly missing and the three most commonly needed.

Nothing validates completeness. A team believes it is instrumented and discovers during an incident that the field they need was never captured. Checking a trace against the fields required to debug the classes of failure this application produces is a straightforward validation nobody offers.

Instrumentation generation is the unexploited path. Application code follows recognisable patterns, and the vendor has seen very many instrumented applications; proposing the spans and attributes for an uninstrumented application is a well-shaped code task on a corpus the vendor holds.

Cost is the practical constraint that shapes all of it. Full-fidelity tracing at high volume is expensive to store, so teams sample — and sampling uniformly discards exactly the rare failures worth investigating. Sampling that retains anomalous traces preferentially is straightforward and rare.

## Impact If Solved
Traces are the primary debugging instrument for these applications and are routinely incomplete in ways discovered during an incident. Generating instrumentation, validating completeness against likely failure modes, and sampling toward anomalies rather than uniformly makes the instrument reliable when it is actually needed.
