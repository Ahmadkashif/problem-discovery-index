# Shadow IT Discovery Applied One Level Deeper

**Niche:** [[niches/no-code-app-builders/shadow-app-inventory/profile|Shadow App Inventory]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Cloud access security brokers and SaaS management platforms have discovered unsanctioned applications from network and spend data for a decade, and they stop at the name of the platform.
**Tags:** #logistic-regression #k-means-clustering #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #data-integration
**Contested on:** Every serious competitor here is fighting to produce a complete list of the applications a company's employees have built, including the ones built on accounts IT does not know exist — and whoever can produce that list takes the security and compliance account, because nobody can produce it today.

## The Problem
Shadow IT discovery is a mature capability: correlate proxy logs, expense data and identity events, match against a catalogue of known services, and report which unsanctioned applications the organisation uses with a risk rating. Run against a no-code platform it produces one row saying the company uses it, with a user count. The question compliance needs answered is what has been built on it, and no discovery product goes there.

## What Already Exists
Cloud access security brokers with large service catalogues and traffic classification; SaaS management platforms correlating spend, sign-ins and usage; identity providers with detailed authentication logs; expense systems with merchant data; and endpoint and browser telemetry. Entity resolution across these sources is ordinary record linkage. The whole discovery pipeline exists and works.

## The Customization Gap
The adaptation is from service discovery to artefact discovery. It requires: (1) traffic patterns that distinguish building from using, since an employee viewing a colleague's app and an employee who owns a tenant with forty apps look similar at the domain level and differ in request patterns, timing and volume; (2) tenant and account resolution rather than user counting, because the governable unit is the workspace and the person who controls it; (3) the inbound direction, which conventional discovery ignores entirely — connections from the platform's infrastructure into the company's own systems are strong evidence of an integrated app and are visible in the company's own logs; (4) a claiming workflow with the platform vendors, since the only way to get true artefact-level inventory is a domain-verified tenant takeover, and that is a partnership rather than a detection; and (5) risk assessment framed around what the app does — data held, external exposure, process dependence — rather than the generic service risk rating these products emit, which is about the platform and not about the thing built on it.

## Target Customer
Cloud access security and SaaS management vendors, IT and security organisations directly, and the no-code platform vendors for whom claiming is a commercial opportunity.

## Impact If Solved
The discovery pipeline is mature and stops exactly one level above where the risk lives. The inbound-connection signal and the claiming workflow are the two additions, and the second is the only path to a genuinely complete inventory.
