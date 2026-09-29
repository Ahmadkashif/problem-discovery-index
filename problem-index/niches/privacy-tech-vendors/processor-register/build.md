# Build: The Register Built From Observation

**Niche:** Third-Party & Processor Register
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Derive the processor register from every party actually receiving data — browser-side, server-side and through SaaS grants — and reconcile it against what was registered.
**Tags:** #graph-theory #gradient-boosting #evaluation-metrics #confidence-intervals #change-point-detection #compliance #data-integration #automation
**Contested on:** Whether the list of parties receiving personal data is derived from what actually leaves the organisation, or from what somebody remembered to register.

## The Problem

The register is populated by registration, and registration requires an act of recognition by a person. Somebody must notice that a tool will process personal data, know that a process exists, and start it.

That filter removes most of the population. The analytics pixel added by a marketer for a campaign. The session recording tool a product manager enabled on a trial. The customer support widget that loads a third-party script. The advertising tag that fires a redirect chain to four companies the organisation has never evaluated. The SaaS application a team authorised with OAuth scopes granting read access to the entire customer database.

Each of those is a processor relationship requiring a contract, a transfer assessment and inclusion in deletion forwarding. None of them appears on the register, because none of them passed through a person who recognised what it was.

So the register lists the enterprise vendors with contracts and misses the long tail that accumulated through the tag manager and the OAuth consent screen — which is frequently the larger population and consistently the one with no agreement in place.

## Why Nobody Has Built This

**Registration is a process, and processes are what privacy teams control.** Building a register from observation requires technical access to networks, browsers and identity systems, which a privacy function does not command.

**The finding is a list of contractual failures.** Every unregistered party receiving personal data is a processing relationship without a data processing agreement, which is a documented breach. Producing that list creates an obligation.

**The tail is long and awkward.** Discovering four hundred unregistered third parties is accurate and unmanageable for a team of two, and a product that produces it without prioritisation is unusable.

**Server-side is invisible to the tooling that exists.** Cookie scanners cover the browser. Server-side integrations — increasingly the main route as browser restrictions tighten — are observed by nothing in the privacy stack.

**Attribution is hard.** Resolving a destination to a named company with a jurisdiction is the difficulty described in [[niches/privacy-tech-vendors/data-flow-observation/profile|🎯 Data Flow Observation]], and without it the observed list is not actionable.

**Nobody is measured on register completeness.** Regulators check that a register exists. Its correspondence to reality is not assessed, so there is no pressure.

## What to Build

**Assemble recipients from every route.** Browser-side from page execution including redirect chains; server-side from egress and API telemetry; SaaS from OAuth grants and their scopes; data platform from warehouse egress and reverse ETL destinations. Each covers a different route and the union is the real population.

**Attribute and enrich.** Resolve each recipient to a company, jurisdiction and corporate structure, and pull their published subprocessor list and transfer mechanism statement. Most processors publish this and nobody harvests it.

**Reconcile against the register.** Parties observed and not registered, parties registered with no observed traffic, and parties whose observed jurisdiction differs from the registered one. This is the output that matters and it is a comparison.

**Prioritise the tail.** Rank unregistered recipients by data volume, data sensitivity and whether the traffic carries identifiers. A team of two can work through twenty ranked findings and cannot work through four hundred unranked ones, and this ranking is what makes the product usable.

**Watch for change.** New recipients appearing, subprocessor pages changing, transfer mechanisms updating, vendors being acquired. A new third party receiving personal data is the single most actionable privacy alert an organisation can get.

**Connect the register to the consequences.** A registered processor should automatically be included in deletion forwarding, in transfer assessment scope and in the vendor risk programme. Today these are separate lists maintained separately, which is why they disagree.

**Cover the OAuth grants properly.** A SaaS application with read access to the customer database is a processor with broader access than most contracted vendors, and is almost never on the register because nobody signed a procurement form.

## Target Customer

Privacy counsel and vendor management, where the unregistered-recipient list is directly actionable and directly addresses their largest documented exposure.

Organisations with substantial marketing technology estates, where the tag-driven tail is largest and least visible.

The privacy platforms, for whom an observed register would replace the weakest input in the product with a derived one — and SaaS security posture vendors, who already hold the OAuth half.

## Impact If Built

The register stops being a list of the vendors that went through procurement and becomes a list of the parties actually receiving data, which is what it was always supposed to be.

The reconciliation output is the finding most organisations most need: third parties processing personal data with no agreement, no assessment and no inclusion in deletion forwarding.

And change alerting on new recipients would catch the next unregistered processor at the moment it appears, rather than at the next annual review or not at all.
