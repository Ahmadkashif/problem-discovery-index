# Anonymisation That Measures Re-Identification

**Niche:** [[niches/expert-networks/transcript-library-platforms/profile|Transcript Library Platforms]]
**Industry:** [[industries/expert-networks|Expert Networks]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Statistical agencies and health-data publishers measure re-identification risk before release, and transcript libraries redact by entity type and editor judgement.
**Tags:** #transformers #bert #graph-theory #probability-distributions #evaluation-metrics #compliance #automation

## The Problem
Every published transcript must protect the expert's identity (and the client's, where a client call is published) while keeping the company-level substance subscribers pay for. Editors remove names and obvious identifiers and make judgement calls on the rest. Over-redaction destroys value; under-redaction can expose an expert to their former employer or breach a confidentiality obligation.

## What Already Exists
Statistical disclosure control from official statistics and health data: quasi-identifier analysis, k-anonymity-style risk measures, and formal release review. Privacy redaction tools detect and remove named entities in documents.

## The Customization Gap
The adaptation needs: (1) quasi-identifiers in free text — tenure, title, region, plant, team size — extracted as structured attributes so risk can be computed; (2) a population model of possible experts with that attribute combination, built from the network's own profile data; (3) asymmetric treatment of entities, since company names are the product and person-identifying combinations are the risk; (4) generalisation rather than deletion ("a Midwest plant" instead of a named town) chosen to preserve meaning; and (5) an editor workflow that shows the risk score and the contributing spans so review becomes exception-handling.

## Target Customer
Heads of content operations and compliance at transcript library platforms.

## Impact If Solved
Editorial review is the throughput constraint on library growth and the main source of publishing delay. A measured re-identification standard cuts review to the risky transcripts and makes the anonymisation defensible to experts and regulators.
