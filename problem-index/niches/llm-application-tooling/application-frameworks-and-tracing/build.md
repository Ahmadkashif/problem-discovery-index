# Chosen at the Start and Bought Afterwards

**Niche:** [[niches/llm-application-tooling/application-frameworks-and-tracing/profile|Application Frameworks & Tracing]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A framework is adopted by a developer on day one against the option of writing it themselves, and observability is purchased on day ninety by whoever is on call, and the two decisions share nothing but the application between them.
**Tags:** #data-integration #workflow-orchestration #evaluation-metrics #automation #large-language-models #descriptive-statistics #graph-theory #compliance
**Contested on:** Not terminal — the contest differs by whether the buyer is starting the application or operating it, and the decomposition is recorded in the profile.

## The Problem
A vendor offering both pitches a developer and an operations lead. The developer wants to know how much the abstraction hides, whether they can drop to the raw API when they need to, and how painful the upgrade path is — and is comparing against a hundred lines they could write themselves. The operations lead wants to know whether a production failure can be explained from the trace, whether a prompt can be changed safely, and what it costs per thousand requests — and is comparing against their existing observability stack. A single product pitched at both tends to persuade neither, and the framework's abstractions frequently make the traces worse rather than better.

## Why Nobody Has Built This
Bundling looks natural because the framework is where instrumentation can be injected most easily, and vendors reach for the integration advantage. But framework adoption is an unpaid, developer-led decision and observability is a paid, operations-led one, and optimising a single product for both produces a framework that carries vendor telemetry concerns and an observability product that only works well with one framework.

## What to Build
Build the interchange between them and let each half compete on its own terms. The genuinely shared requirement is a semantic convention for what an LLM application emits — the model call with its prompt, parameters and response, the retrieval step, the tool call, the evaluation result, the prompt version, the cost — as a standard any framework emits and any backend consumes, which would let a developer choose a framework and an operator choose a backend independently and is the piece whose absence causes the bundling. Make the prompt version a first-class field in that convention, since attributing production behaviour to a prompt version is the question everyone has and nothing carries it. Include cost and token accounting as standard attributes rather than as a vendor extension. Define evaluation results as emittable events, so offline and online quality live in one place. Keep the framework's instrumentation optional and non-proprietary, so adopting a framework does not choose a backend. Support instrumentation without a framework, since many production applications call the model API directly and are the least served today. And treat the convention as a public good rather than a differentiator, because the vendor that fragments it loses the developers who would otherwise adopt freely.

## Target Customer
Framework authors, observability vendors, application developers and the teams operating what they build.

## Impact If Built
A shared semantic convention is what would let framework choice and backend choice be independent, which is the absence that drives the bundling. Carrying the prompt version as a standard field answers the attribution question everyone has and nothing currently supports.
