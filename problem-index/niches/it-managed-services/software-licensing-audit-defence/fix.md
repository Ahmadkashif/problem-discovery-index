# What Survived the Last Audit Lives in the Consultant Who Ran It

**Niche:** [[niches/it-managed-services/software-licensing-audit-defence/profile|Software Licensing & Audit Defence Practices]]
**Industry:** [[industries/it-managed-services|IT Managed Services]]
**Type:** Fix (Pain Point)
**One-liner:** The firm's only real advantage is knowing which arguments publishers actually concede, and it keeps that in people.
**Tags:** #tacit-knowledge-ml #large-language-models #graph-ml #worker-facing #compliance

## The Problem
Publisher licensing policy is written down. How a publisher behaves is not. A consultant who has run twenty audits against one publisher knows things that decide engagements: which policy positions that publisher will drop when challenged with a specific contract clause, which auditor teams are aggressive on which products, what a first finding typically settles at, which arguments have never worked, and what a particular contract vintage's terms actually permit despite what the current policy document says.

That is the firm's entire competitive advantage over a client trying to do this alone, and it exists as a set of individual memories. The engagement record contains the deliverable — the position, the response, the settlement — and not the reasoning, the arguments tried, or which of them moved the publisher.

So the next consultant against the same publisher rebuilds it. And in a field where the specialists are few and mobile, the advantage walks between firms rather than accumulating in any of them.

## Why It's Still Broken
Engagements are organized by client and are confidential, so everything is filed along the one axis nobody needs to search. Every question a practitioner has cuts across clients — how does this publisher treat this metric — and every storage decision cuts along them.

The confidentiality objection is real and narrower than it looks. What is worth keeping is almost never client-specific: "this publisher conceded the indirect access position when presented with this clause from a 2016 agreement" is a fact about the publisher, not about the client. Nobody has drawn that line, so the whole corpus stays locked at the engagement level.

And the knowledge is a personal asset. A consultant who knows how a publisher behaves is highly marketable, and nothing in the structure rewards making that portable.

## What a Fix Looks Like
Extract the publisher-behaviour layer and leave the client layer alone.

**Precedent records, client-anonymized.** Publisher, product, metric, the position asserted, the argument made, the contract basis relied on, and the outcome. Populating these from prior engagements is largely extraction, and the documents are formulaic.

**Publisher behaviour profiles.** How each publisher's audit teams open, what they concede, typical settlement ratios, which policy documents they cite versus enforce. This is the map every engagement starts by reconstructing.

**Contract clause library, linked to outcomes.** Specific clause language that has proven load-bearing — an audit clause limiting scope, a definition that pre-dates a policy change — indexed by publisher and vintage so a consultant reading a new agreement recognizes what they are holding.

**Retrieval at the point of drafting.** When a consultant opens an engagement against a publisher, the firm's precedent on that publisher and product should be in front of them, not findable by asking a colleague who may be on another client.

**Confidentiality as a boundary, not a blanket.** The precedent layer carries no client identity and no deployment data. It carries what the firm learned about a software publisher's behaviour by doing the work, which is exactly the asset it should be compounding.

## Who Feels the Pain
Consultants, re-deriving arguments colleagues have already won. New hires, who take a year or more to be useful against a given publisher. Practice leaders, whose capability is a handful of tenures in a mobile market. And clients, whose settlement depends on which consultant was available.

## Impact If Fixed
Publisher audit programmes are systematic and continuous, and the client's position depends almost entirely on knowing what has worked before. Turning that from individual memory into a firm asset compresses ramp time in a market constrained by scarce specialists, makes outcomes consistent, and builds the one thing a licensing practice can own that a competitor cannot hire away one person at a time.
