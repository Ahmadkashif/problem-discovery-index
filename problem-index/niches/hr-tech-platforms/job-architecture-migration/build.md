# The Architecture Inferred From What the Organisation Actually Does

**Niche:** [[niches/hr-tech-platforms/job-architecture-migration/profile|Job Architecture & Migration]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An employer's real job architecture is visible in its titles, its pay distribution, its reporting structure and its internal movement history, and every implementation reconstructs it from workshops instead.
**Tags:** #bert #word-embeddings #k-means-clustering #graph-theory #evaluation-metrics #confidence-intervals #dimensionality-reduction #automation
**Contested on:** Every serious competitor in HCM implementation is fighting to infer an employer's job architecture and employment history from the data rather than rebuilding it from spreadsheets — and whoever shortens time-to-configured most takes the implementation.

## The Problem
An employer with four thousand people has eleven hundred distinct job titles. An implementation consultant runs workshops with HR business partners to define families and levels, produces a framework of eight families and seven levels, and then maps eleven hundred titles into it by hand over several weeks, with disputes escalated to a steering committee. The resulting architecture is a design rather than a description, and within a year hiring managers have invented ninety new titles that do not fit it. Meanwhile the data contains the answer to what the architecture actually is: titles cluster by pay, by reporting depth, by the moves people make between them, and by the skills the job postings described.

## Why Nobody Has Built This
Job architecture is sold as a consulting deliverable, and a consulting deliverable is a design produced by experts rather than an inference from data — which is a defensible framing and also explains why nobody has automated it. The inference is genuinely non-trivial: titles are noisy, pay reflects tenure and negotiation as well as level, and reporting depth varies by function. But every one of those is a modelling problem with a good answer, and the alternative currently in use is a workshop.

## What to Build
An architecture proposed from the data and refined by the experts. Titles are normalised and clustered using their text, the pay distribution of their holders, reporting depth, span, the moves people make into and out of them, and the content of the job postings that hired for them — which together separate genuine level differences from title inflation far better than any of them alone. Families emerge from movement patterns rather than from organisational charts, since the people who move between two job families are evidence that those families are adjacent, and that is the property a career framework needs to encode. The proposal is presented with its evidence — these are the same level because their pay distributions and reporting depths are indistinguishable and people move freely between them — which is what turns the workshop from a design exercise into a review. The consultant's expertise is redirected to the genuinely contested cases and to the deliberate choices about where the organisation wants to differ from what it currently does, which is where that expertise is worth most.

## Target Customer
HCM implementation partners, the HCM vendors whose implementation timelines are a competitive liability, and large employers undertaking architecture work without a migration.

## Impact If Built
Job architecture and title mapping is the longest pole in most HCM implementations and is rebuilt from scratch at every employer. Inferring it compresses weeks into days and — more importantly — produces an architecture that describes the organisation, which is why it survives contact with hiring managers rather than decaying within a year.
