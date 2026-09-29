# Internal Developer Platforms

## Profile
**Category:** Developer Tools & Infrastructure
**Market Size:** ~$2B US internal developer platform and service catalogue software
**Tech Maturity:** Young and repeating a known failure pattern — Backstage, Port, Cortex, OpsLevel and Humanitec have given platform teams a product category, and most internal platforms are built rather than bought. The category's recurring outcome is a platform nobody uses, built by a team that never asked what developers actually needed.
**Workforce:** Platform engineers, developer experience specialists, service catalogue maintainers, golden path authors, internal product managers

## Key Pain Themes
The defining failure is a platform built as infrastructure rather than as a product. A team builds paved paths, templates and a portal, developers route around them for reasons the platform team never learns, and adoption stalls at the teams who were consulted. Nobody measures who uses what, where they abandon a golden path, or what they do instead. Below that sit two chronic problems: the service catalogue, which is the foundation of everything and is maintained by asking teams to fill in metadata that goes stale immediately; and golden path drift, where a template is generated once and every service diverges from it thereafter, so a platform improvement never reaches the services that already exist. Platform engineers spend their days on internal support for abstractions they built, and application developers navigate a platform whose boundaries they discover by hitting them.

## Current Tech Landscape
Backstage established the service catalogue and portal pattern and is widely adopted and widely regarded as expensive to operate. Commercial alternatives (Port, Cortex, OpsLevel) offer managed versions with maturity scorecards. Infrastructure-as-code modules and Terraform registries provide the provisioning layer. Kubernetes abstractions (Crossplane, Humanitec) attempt to hide cluster complexity. Golden path templates via cookiecutter-style scaffolding are near universal. Service maturity scorecards have become a standard feature and are frequently resented.

## Problems
- [[problems/internal-developer-platforms/high-impact|🔴 High Impact: Platforms Built Without Knowing What Developers Do]]
- [[problems/internal-developer-platforms/low-impact-1|🟡 Low Impact: Service Catalogue Metadata Decay]]
- [[problems/internal-developer-platforms/low-impact-2|🟡 Low Impact: Golden Path Drift After Generation]]
- [[problems/internal-developer-platforms/worker-life-1|🟢 Worker Life: Platform Engineer as Internal Support]]
- [[problems/internal-developer-platforms/worker-life-2|🟢 Worker Life: Discovering the Platform by Hitting Its Edges]]
- [[problems/internal-developer-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/internal-developer-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
An internal platform team is a product team whose users sit in the same building and whose usage it does not measure. Every signal that a consumer product company would consider essential — activation, funnel drop-off, feature usage, retention, support contact rate — is available from the platform's own systems and is almost never collected, because the team thinks of itself as building infrastructure. That single category error explains most of the failures in the space, and it is correctable with instrumentation nobody has to invent.
