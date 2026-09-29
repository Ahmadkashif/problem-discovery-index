# What the Agency Actually Asked Lives in the Consultant Who Answered

**Niche:** [[niches/medical-device-mfg/device-regulatory-affairs-consulting/profile|Medical Device Regulatory Affairs Consulting]]
**Industry:** [[industries/medical-device-mfg|Medical Device Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** The firm's advantage is knowing what reviewers ask and what answers satisfy them, and it exists as a set of careers.
**Tags:** #tacit-knowledge-ml #large-language-models #graph-ml #worker-facing #compliance

## The Problem
Published summaries say what cleared. They do not say what the review looked like: which questions the reviewer asked, which answers closed them, where a sponsor conceded a claim to avoid a testing demand, which branch of the agency is strict about a particular standard, how a pre-submission meeting actually went.

A consultant who has run thirty submissions in a product area knows all of it. That knowledge is what a client is buying — it is the difference between a submission that clears in one cycle and one that takes three.

The engagement file holds the submission, the correspondence, and the outcome. The reasoning — why a claim was framed a particular way, which reviewer question the framing anticipated, what the firm has learned about how this branch behaves — is nowhere structured. It leaves when the consultant does, and in a market where regulatory professionals are scarce and heavily recruited, it leaves regularly.

## Why It's Still Broken
Engagements are organized by client and are confidential, which is the one axis nobody needs to search. Every question a practitioner has cuts across clients — how does this branch treat this type of claim — and all storage cuts along them.

The confidentiality objection is narrower than it appears. What is worth keeping is almost never client-specific: "this branch asked for additional bench data whenever this claim was made without it, and this framing avoided the question" is a fact about the agency, not about a manufacturer's device. Nobody has drawn the line, so the corpus stays locked at engagement level.

And the knowledge is a personal asset in a seller's market for talent.

## What a Fix Looks Like
Extract the agency-behaviour layer and leave the client layer alone.

**Interaction records, client-anonymized.** Product code, claim type, the question asked, the response that closed it, the cycle it occurred in. Populating these from correspondence files is largely extraction work on formulaic documents.

**Branch and reviewer behaviour profiles.** What each review branch focuses on, which standards it enforces strictly, what it typically asks for on a given technology. This is what every engagement currently starts by reconstructing from memory.

**Pre-submission meeting outcomes.** What was proposed, what feedback was given, what changed as a result. These meetings are the highest-leverage moment in the whole process and their content exists as meeting minutes in client folders.

**Retrieval at strategy.** A consultant opening an engagement should see the firm's accumulated experience with that product code and claim type, not have to find the colleague who did the last one.

**Confidentiality as a boundary, not a blanket.** The precedent layer carries no client identity and no device design. It carries what the firm learned about how an agency behaves, which is the asset it should be compounding.

## Who Feels the Pain
Consultants, re-deriving strategy colleagues have already worked out. New regulatory professionals, who take years to become credible in a product area. Practice leaders, whose differentiating capability is a handful of tenures in a market with acute talent scarcity. And clients, whose time to market depends on which consultant was available.

## Impact If Fixed
Review cycles are measured in months and each one costs a device company a quarter of market presence. Turning agency-behaviour knowledge from individual memory into a firm asset compresses ramp time where qualified people are the binding constraint, makes strategy consistent, and builds the one thing in regulatory consulting a competitor cannot acquire by hiring one person.
