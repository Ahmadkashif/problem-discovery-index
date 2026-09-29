# Build: Every Flow, Attributed

**Niche:** Data Flow Observation
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Assemble egress, API, database, lineage, OAuth and browser telemetry into one flow map, resolve every destination to a named organisation and jurisdiction, and diff it against the declared record.
**Tags:** #graph-theory #graph-neural-networks #gradient-boosting #evaluation-metrics #confidence-intervals #change-point-detection #data-integration #compliance
**Contested on:** Whether where data actually goes can be derived from the systems that already record it, across the whole estate and past the organisational boundary.

## The Problem

An organisation's data flows are recorded comprehensively and in fragments. Cloud flow logs record connections between resources and to the internet. API gateways record calls in and out. Database audit logs record who read what. Warehouse lineage records transformations. Identity systems record which third-party applications hold which OAuth scopes. Tag scanners record what the website sends to whom.

Nobody assembles them. Each lives in a different system, serving a different team, for a different purpose — security, cost, debugging, analytics — and none of them was built to answer the question privacy needs, which is: where does personal data actually go.

Attribution is the second half of the problem and is the one that makes the output useful. A flow log says traffic went to an address range. What a privacy officer needs to know is that customer records are being sent to a named analytics company incorporated in a particular country under a contract signed by a team in a different division. Resolving addresses, domains and API endpoints to organisations, and organisations to jurisdictions and contractual status, is where an observed flow becomes a privacy finding.

And then the comparison that matters: which of these flows appears in the record of processing, and which does not.

## Why Nobody Has Built This

**The sources belong to other teams.** Flow logs sit with the network and security teams, lineage with data engineering, OAuth grants with IT. A privacy platform asking for all of them is asking for a level of access and cooperation the privacy function rarely commands.

**Volume is enormous and mostly irrelevant.** A large estate produces vast flow telemetry, the great majority of which involves no personal data. Reducing it to the privacy-relevant subset without a classification layer is the practical difficulty.

**Attribution is genuinely hard.** Shared cloud infrastructure, content delivery networks, redirect chains and server-side integrations obscure the real recipient. A meaningful share of destinations resolve to a hosting provider rather than to the company actually receiving the data.

**Finding unregistered third parties creates an obligation.** The most valuable output is also a list of parties receiving personal data without a data processing agreement, which is a disclosable finding an organisation must then act on.

**Browser-side and server-side are different worlds.** Tag scanning and network observation use entirely different techniques and different vendors, and the same data can leave by either route. Nobody covers both.

**Privacy buyers are not equipped to evaluate it.** A legal buyer cannot assess the coverage claims of a network observation product, which makes it a hard thing to sell into the function that needs it.

## What to Build

**Ingest every available source and state what each covers.** Cloud flow logs, API gateway logs, database audit logs, warehouse lineage, OAuth grants and scopes, service mesh telemetry, DNS, and browser-side tag observation. Publish the coverage each source provides and the parts of the estate none of them reach — a flow map presented as complete is the same failure as a survey presented as complete.

**Attribute destinations to organisations.** A maintained registry resolving domains, address ranges, API endpoints and tag vendors to companies, with jurisdiction and corporate structure. This is the asset that makes the product valuable and it is maintenance work rather than research — the same shape of asset that makes threat intelligence useful.

**Determine the jurisdiction honestly.** Where a flow crosses a border, say so, with the basis for the determination and its confidence. Cross-border transfer is where the regulatory consequence concentrates, and the current state of practice is an assumption based on a vendor's stated headquarters.

**Reconcile browser and server routes.** The same third party frequently receives data both from the user's browser and from the organisation's servers. Presenting these as one relationship rather than two unrelated findings is what a privacy officer actually needs.

**Diff against the declared record continuously.** Flows present in observation and absent from the record of processing; third parties receiving data who are not on the processor register; transfers not covered by an assessment. This is the product's argument and it is a comparison, not a model.

**Alert on new relationships.** A destination appearing for the first time is the most actionable privacy event an organisation can receive, and today it is discovered at the next annual survey if at all.

**Pass volume and structure to classification.** Flow observation should report what moves, how much and how often, and hand the question of whether it is personal data to the classification layer rather than guessing.

## Target Customer

Privacy engineering and data governance teams at organisations large enough to have them, sold jointly with security or platform engineering — whose own interest in egress visibility is what unlocks the access.

The privacy platforms, for whom observed flows would replace the weakest input in their entire product with a derived one.

Cloud security posture and DSPM vendors as the most likely builders, since they already hold much of the telemetry and already sell to a buyer who can grant the access.

## Impact If Built

The map becomes evidence. Where data goes is an observable fact about an organisation's systems and is currently recorded as testimony from people who were asked.

Attribution to named organisations and jurisdictions is what converts network telemetry into a privacy artefact, and it is the piece every existing tool stops short of.

And the diff against the declared record would produce the finding most organisations most need and least want: the third parties receiving personal data that nobody registered, contracted with or assessed.
