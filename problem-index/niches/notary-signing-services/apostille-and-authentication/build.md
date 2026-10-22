# Destination-Aware Authentication Routing

**Niche:** [[niches/notary-signing-services/apostille-and-authentication/profile|Apostille & Document Authentication]]
**Industry:** [[industries/notary-signing-services|Notary & Signing Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Which offices a document must pass through depends on its type, its state of origin and the country it is going to, and customers find out by being rejected.
**Tags:** #decision-trees #large-language-models #bert #evaluation-metrics #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to get a document through the correct chain of certifications — notarial act, county clerk where required, secretary of state, and for non-Convention countries federal authentication and embassy legalisation — on the first submission, and whoever has the lowest rejection rate against the destination's deadline takes the immigration, adoption and corporate filing work.

## The Problem
A diploma copy for a work visa, a power of attorney for a property abroad, and a corporate resolution for a foreign subsidiary each need a different chain. Whether a copy must be certified by the issuer or notarised as a copy, whether the notary's county clerk must authenticate first, and whether the destination accepts an apostille or needs consular legalisation are all questions answered by trial and error.

## Why Nobody Has Built This
The rules are spread across fifty secretaries of state, thousands of county clerks, the US Department of State and every foreign consulate, and they change without notice. Facilitators keep the knowledge in their staff's heads as a competitive edge.

## What to Build
A routing engine that takes the document type, issuing state and destination country and returns the chain, the certificate wording each office accepts, fees, current turnaround and known rejection reasons. A language model reads the uploaded document to classify it and check the notarial certificate. Every rejection is captured with the reason and folded back into the rules.

## Target Customer
Apostille facilitation businesses; immigration and corporate law firms; university registrars.

## Impact If Built
First-time acceptance rises, and customers facing a consulate or court deadline stop losing weeks to a missing county step.
