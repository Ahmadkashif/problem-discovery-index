# Open Telemetry and Semantic Conventions

**Niche:** [[niches/llm-application-tooling/application-frameworks-and-tracing/profile|Application Frameworks & Tracing]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The observability ecosystem solved vendor-neutral instrumentation and semantic conventions, and LLM tooling is re-fragmenting the same ground one vendor at a time.
**Tags:** #data-integration #workflow-orchestration #automation #evaluation-metrics #compliance #descriptive-statistics #graph-theory #quick-win
**Contested on:** Not terminal — the contest differs by whether the buyer is starting the application or operating it, and the decomposition is recorded in the profile.

## The Problem
The observability world spent years learning that vendor-specific instrumentation traps customers and fragments the ecosystem, and answered it with a neutral standard: one instrumentation API, one wire protocol, and semantic conventions defining what a span should carry for databases, HTTP and messaging. LLM application tooling has broadly adopted the transport and is re-fragmenting at the semantic layer, where each vendor defines its own attribute names for the same concepts.

## What Already Exists
Vendor-neutral instrumentation APIs and collectors; semantic conventions for common domains with a governance process; automatic instrumentation for popular libraries; collector-based routing and transformation; and the community process by which conventions are agreed rather than imposed.

## The Customization Gap
The adaptation is to a domain whose interesting attributes are large, sensitive and expensive. It requires: (1) conventions covering the prompt, the response, the model and parameters, the retrieval context, the tool call, the prompt version and the evaluation result, which is the missing work and is a convention exercise rather than a technical one; (2) handling of large payloads, since a prompt and response can be enormous and spans were designed for small attributes — sampling, truncation and referencing stored payloads need conventions of their own; (3) sensitivity classification, because these payloads frequently contain personal data and a trace that ships them to a vendor is a data transfer nobody assessed; (4) cost and token attributes as standard, since they are the operational metric this domain has that others do not; and (5) evaluation results as a span type, which connects offline quality to production behaviour and has no analogue in existing conventions.

## Target Customer
Framework authors, observability vendors, application teams, and the open telemetry community for whom this domain is an active and unfinished convention area.

## Impact If Solved
The ecosystem already learned that semantic fragmentation traps customers, and this domain is repeating it. Conventions for large sensitive payloads and for cost attributes are the domain-specific work, and evaluation results as a span type connects offline quality to production for the first time.
