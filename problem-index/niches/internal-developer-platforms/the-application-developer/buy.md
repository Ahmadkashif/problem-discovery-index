# Capability Declaration From API Practice

**Niche:** [[niches/internal-developer-platforms/the-application-developer/profile|The Application Developer]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** APIs publish a machine-readable specification stating exactly what they support, and an internal platform — which is an API with a portal — publishes prose.
**Tags:** #graph-theory #bert #large-language-models #word-embeddings #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to let a developer find out what the platform supports before they build on the assumption that it does — and whoever does that takes the adoption, because discovery by failure is why developers route around.

## The Problem
An API publishes a specification: the operations, the parameters, the types, the constraints, in a machine-readable form that tooling validates against and that a developer can inspect before writing a line. An internal platform provides a set of operations with parameters and constraints and describes them in documentation, so the only way to know whether a particular combination is valid is to try it. The platform is an API without a specification.

## What Already Exists
Interface specification formats with tooling for validation, generation and documentation; schema validation frameworks; capability negotiation patterns from protocol design; feature detection conventions; and the infrastructure-as-code type systems that already validate much of what a platform accepts.

## The Customization Gap
The adaptation is to a platform whose constraints are semantic rather than syntactic. It requires: (1) expressing limitations rather than only structure, since the interesting constraints are behavioural — this scheduler does not guarantee exactly-once, this abstraction does not support that networking mode — and a type schema captures none of them; (2) queryability in natural terms, since a developer's question is about what they are trying to do rather than about a field, which is where a language model over the capability description is the practical interface; (3) versioning and deprecation of the capability surface, because a platform's capabilities change and a specification that silently shifts is worse than prose — which is the same deprecation discipline the API infrastructure industry describes; (4) derivation from the implementation where possible, since a hand-maintained capability document will drift exactly as every other declared artefact in this vault does, and deriving the constraints from the provisioning modules keeps it honest; and (5) validation at design time in the developer's own tooling, which is where the check must happen to prevent the two lost days.

## Target Customer
Platform tooling vendors, platform engineering teams, and the infrastructure-as-code ecosystem whose type systems are the natural place for this.

## Impact If Solved
A platform is an API without a specification, which is why its boundary is discovered empirically. Expressing behavioural limitations and deriving them from the implementation are the two adaptations, and design-time validation is where the value lands.
