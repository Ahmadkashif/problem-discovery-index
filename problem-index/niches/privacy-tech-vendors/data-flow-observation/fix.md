# Fix: The Destination Is an IP Address

**Niche:** Data Flow Observation
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Observation tells you data went somewhere, and what the privacy officer needs to know is which company received it, in which country, under what contract.
**Tags:** #evaluation-metrics #confidence-intervals #graph-theory #compliance #data-integration #worker-facing
**Contested on:** Whether where data actually goes can be derived from the systems that already record it.

## The Problem

An organisation gains visibility of its egress traffic and discovers thousands of destinations. The output is a list of domains, address ranges and API endpoints with volumes attached.

This is useless to a privacy officer. Their question is whether personal data is being sent to a party outside the organisation, who that party is, whether there is a data processing agreement in place, and whether the transfer crosses a border in a way requiring assessment.

Translating one into the other is hard in specific ways. A domain may belong to a content delivery network fronting a dozen different companies. An address range belongs to a hosting provider, not to the company using it. A tag on the website fires a redirect chain ending at a party nobody can name from the first request. A vendor incorporated in one country processes in another and has subprocessors in three more. Server-side integrations show only the gateway of a service whose actual operator is stated nowhere in the traffic.

So an organisation ends up with technically accurate observation that cannot be acted on, and the privacy officer returns to asking people — which is where they started.

## Why It's Still Broken

**Attribution is maintenance, not technology.** Resolving destinations to organisations requires a registry that someone keeps current as companies are acquired, rebranded, and move infrastructure. That is ongoing effort with no elegant solution, which is why nobody has built it for this purpose.

**Infrastructure deliberately obscures the recipient.** Shared hosting, content delivery networks and redirect chains hide the actual party, sometimes as a side effect and sometimes by design, particularly in advertising technology where the chain of recipients is intentionally opaque.

**Corporate structure is a separate problem.** Knowing the destination is a named company is not enough; the privacy question involves where they process, who their subprocessors are and which corporate entity signed the contract. That information sits in contracts and in the vendor's own disclosures, not in traffic.

**Security tooling attributes to the depth security needs.** Determining that traffic goes to a known cloud provider is sufficient for a threat assessment and insufficient for a transfer assessment.

**Nobody owns the join to the contract register.** Even a correctly attributed destination has to be matched against the organisation's own processor register and contracts, which live in legal systems nobody has connected to network telemetry.

**Advertising technology defeats it deliberately.** The browser-side flows are the hardest to attribute and are where the most personal data goes, and the opacity is a feature of that market rather than an accident.

## What a Fix Looks Like

**Build and maintain the attribution registry as a product.** Domains, address ranges, API endpoints and tag signatures mapped to organisations, with jurisdiction and corporate structure, maintained continuously. This is the missing asset, it is achievable, and it is exactly the shape of thing threat intelligence vendors already maintain for a different purpose.

**Follow the chain, not the first hop.** Redirect chains and content delivery fronting require resolving to the end recipient rather than to the first destination. For browser-side flows this means executing the page and observing the full chain, which existing tag scanners partially do.

**Join to the contract register.** Every attributed destination matched against the organisation's processor register and its data processing agreements, so the output is a list of parties with and without contractual cover. That list is the finding; the traffic is only the input.

**Report attribution confidence honestly.** Some destinations resolve cleanly and some do not. Presenting an uncertain attribution as fact will produce a wrong transfer assessment, and the unresolved list is itself actionable.

**Start with the third parties, not the estate.** Attributing every internal service-to-service flow is expensive and uninteresting. Attributing everything leaving the organisation is the tractable and valuable subset.

**Use the vendor's own disclosures.** Subprocessor pages, transfer mechanism statements and privacy policies are published by most processors and are the authoritative source for the corporate and jurisdictional detail traffic cannot supply. Nobody harvests them systematically.

## Who Feels the Pain

The privacy officer, handed a technically accurate list of addresses that does not answer any question they have, and returning to interviews as a result.

The organisation, which has paid for observation and gained no more actionable insight than before.

The vendor management function, whose processor register is missing entries that the traffic could have identified if anyone could name the destinations.

And the data subjects, whose data reaches parties nobody in the organisation can name, which is the practical meaning of the advertising technology chain.

## Impact If Fixed

The attribution registry is the piece that converts telemetry into privacy findings, and it is maintenance rather than invention — which makes its absence a market gap rather than a technical barrier.

Joining attributed destinations to the contract register produces the single most valuable output in this niche: the parties receiving personal data with no agreement in place.

And harvesting processors' own published subprocessor and transfer disclosures would supply the corporate and jurisdictional detail that traffic never can, from sources that are public and currently unused.
