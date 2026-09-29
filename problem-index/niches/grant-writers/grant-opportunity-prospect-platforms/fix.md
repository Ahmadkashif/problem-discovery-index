# Researcher Judgment About Fit Is Stored as a Match Score

**Niche:** [[niches/grant-writers/grant-opportunity-prospect-platforms/profile|Grant Opportunity & Funder Research Platforms]]
**Industry:** [[industries/grant-writers|Grant Writers]]
**Type:** Fix (Pain Point)
**One-liner:** Researchers form specific, well-founded views about who a funder actually funds, and the product can only express them as a number between 0 and 100.
**Tags:** #graph-ml #large-language-models #tacit-knowledge-ml #ml-recommendation

## The Problem
A researcher who has covered a funder for three years knows things that do not fit the schema. That this foundation says it funds nationally but has never made a grant outside two states. That the programme officer strongly prefers proposals naming a specific evaluation framework. That the stated $250,000 ceiling is real for new grantees and routinely exceeded for renewals. That the open call is effectively closed because the money is committed to a multi-year cohort.

All of it reaches the user as a match score and a paragraph of profile text. The score cannot say *why*, and the paragraph is read by a fraction of users. So the same researcher answers the same question in support tickets, month after month, and the knowledge stays with whoever happens to hold the account.

## Why It's Still Broken
The product was designed around structured fields because structured fields are searchable and filterable, and search is what customers evaluate during a trial. Everything a researcher knows that does not decompose into a field becomes prose, and prose is decoration in a product whose interface is a filtered list.

The rest is turnover. Researcher tenure is measured in a few years; funder relationships outlast it. When a researcher leaves, their portfolio's accumulated context leaves with them and the next person rebuilds it from filings — which is precisely where the undocumented knowledge is not.

## What a Fix Looks Like
Give the tacit layer a place to live and a way to reach the user at the moment it matters.

Structure it as **claims attached to funders**: a short assertion, its evidence, its confidence, who recorded it, when. "Has not funded outside CA and OR since 2019 — 47 of 47 grants in filings" is a claim with evidence and a decay date. "Programme officer prefers logic-model framing — from three conversations" is a claim with a source and lower confidence. Both are useful; conflating them is not.

Then surface claims where the decision is made — beside the match, not buried in a profile — and let the evidence-backed ones be checked automatically against each new filing. A claim that stops holding should flag itself rather than quietly misinform.

The capture path has to be nearly free. A researcher answering a support ticket should be able to promote the answer into a claim in one step. The knowledge is being written down already; it is just being written into places nobody can search.

## Who Feels the Pain
The research team, answering the same questions repeatedly and watching context walk out the door with every departure. Users, who receive a confident number with no reasoning and cannot tell a strong match from a keyword collision. And the platform, whose most valuable asset — accumulated human judgment about funders — is the one asset it does not store.

## Impact If Fixed
The difference between a searchable database of open opportunities, which is a commodity, and a body of accumulated funder intelligence, which is not. Every year the claim layer runs it gets denser and more valuable, and unlike the opportunity catalogue it cannot be replicated by anyone who has not spent the same years watching the same funders.
