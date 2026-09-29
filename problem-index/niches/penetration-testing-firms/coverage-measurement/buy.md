# Buy: Code Coverage Instrumentation, Pointed Outward

**Niche:** Coverage Measurement
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software testing solved the denominator problem decades ago with coverage instrumentation, and security testing — whose audience understands that tooling perfectly — has never adopted the idea.
**Tags:** #graph-theory #evaluation-metrics #confidence-intervals #automation #data-integration #k-means-clustering
**Contested on:** Whether an engagement can state how much of the attack surface it actually reached, by what technique and at what depth.

## The Problem

Software testing faced exactly this problem and solved it. A test suite passes; what does that mean? It means the code paths the suite exercised behaved correctly, and coverage instrumentation says precisely which paths those were. Every engineer understands that a passing suite with thirty per cent coverage means something entirely different from a passing suite with ninety.

Security testing has the identical structure — a test, a pass, an unstated denominator — and no instrumentation. The audience is the same people. Client security engineers and developers who would immediately understand a coverage statement receive a findings list instead and are left to infer the denominator from the day count.

Several adjacent capabilities already do most of the technical work. Interactive application security testing instruments a running application to see which code paths a security test reaches. Attack surface management enumerates assets continuously. API specifications enumerate endpoints and parameters exactly. None has been assembled into a coverage report for a manual engagement.

## What Already Exists

Code coverage: the entire established toolchain — line, branch and path coverage, with mature reporting and near-universal comprehension among technical audiences.

Interactive application security testing: Contrast Security, Seeker and similar agents that instrument a running application during testing and can observe which routes and code paths were exercised. This is the closest existing technology and it is sold for a different purpose.

Attack surface management: Randori, Censys, Bishop Fox's Cosmos, Detectify and the ASM modules inside the larger platforms, providing continuous external asset enumeration — a ready-made partial denominator.

API tooling: OpenAPI specifications, API gateways with full request logging, and API security platforms that enumerate and monitor endpoints.

Testing delivery platforms: the engagement management and reporting products testing firms use, which already sit on the engagement data and would be the natural host.

Framework: MITRE ATT&CK, providing the technique taxonomy that a coverage statement needs and that parts of the industry already use.

## The Customization Gap

**IAST is instrumented for the wrong reader.** It observes code paths reached during testing and reports to a development team about application risk. Turning the same observation into an engagement coverage statement for a report is a presentation and aggregation change over a capability that already exists — and it is a natural extension nobody has made.

**Coverage must be attacker-relevant, not code-relevant.** Line coverage is the wrong unit. What matters is authenticated roles exercised, parameter classes manipulated, state transitions reached and techniques attempted. The concept transfers; the unit does not, and choosing the unit is the real work.

**Manual testing has no test suite to instrument.** Code coverage assumes a deterministic suite. A penetration test is a human improvising, so the instrumentation has to observe traffic rather than execution, and infer intent and depth from patterns rather than reading a test definition.

**The denominator is external and incomplete.** ASM gives a good external asset denominator and says nothing about authenticated surface, internal services or business logic. Combining enumeration sources and stating what remains unenumerated is the adaptation, and no ASM product frames its output as a testing denominator.

**Depth banding has no analogue.** Code coverage is binary per line. Security coverage must distinguish touched from deeply tested, which requires a classification layer that does not exist in any of the source categories.

**Client-side deployment is required for the strongest version.** IAST agents run inside the client's application, which means a penetration testing firm asking a client to instrument their own system for the duration — a real adoption obstacle in a relationship where the client is often deliberately keeping the tester at arm's length.

## Target Customer

The testing delivery platform vendors are the most natural adapters: they hold the engagement data, serve the firms directly, and coverage reporting is a feature rather than a new product.

Contrast Security or another IAST vendor is the more technically capable route, since observing what a test actually reached is exactly what their agents do, and an engagement coverage product opens a services channel they do not currently serve.

Buyers are testing firms, with cyber insurers and enterprise security procurement as the parties who would eventually require the output.

## Impact If Solved

An idea that is universally accepted in software testing reaches security testing, where the same inference problem exists and the same audience is already fluent in the concept.

The technical pieces are mostly built. Traffic instrumentation, asset enumeration and technique taxonomy all exist as products; what is missing is the assembly and the reporting convention, which makes this unusually achievable for the change it would produce.

And a coverage statement expressed in terms a developer already understands would let client engineering teams engage with test results as a measurement rather than as a verdict, which is a better relationship than the one the current artefact produces.
