# A Document Describing a Version Nobody Runs

**Niche:** [[niches/software-supply-chain-security/sbom-consumption/profile|SBOM Consumption]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Fix (Pain Point)
**One-liner:** The bill of materials on file was supplied at procurement three years ago, the product has been updated eleven times since, and nobody has requested a new one.
**Tags:** #descriptive-statistics #change-point-detection #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #quick-win #data-integration
**Contested on:** Every serious competitor here is fighting to make a software bill of materials answer a question somebody actually has — and whoever does that takes the mandate, because the documents are generated, filed and read by nobody.

## The Problem
A security team queries their document index for an affected component and finds it in three products. What the index does not tell them is that the documents for those products describe versions from 2022, that the vendors have shipped many releases since, and that the component may have been removed or may have been added to four other products whose documents predate its introduction. The index answers the question about a software estate that no longer exists, confidently, which is worse than not answering it.

## Why It's Still Broken
The document is treated as a procurement artefact collected once, because the requirement was expressed as supply rather than as maintenance. There is no mechanism to request an updated one on each release, and no vendor volunteers them. Currency is not tracked, so a three-year-old document sits in the index looking identical to one from last month. And the receiving organisation has no deployment-version linkage, so even a current document may not correspond to what they are running.

## What a Fix Looks Like
Track currency and tie documents to deployed versions. Record the product version each document describes and the version actually deployed, and report the gap, which is the single change that makes the index's answers interpretable — a match against a stale document is a lead rather than a fact. Request documents per release rather than per procurement, which is a contractual term that costs nothing and is the structural fix; the vendor's build already generates one. Automate the request and the ingestion, so a vendor release triggers a document request and the response is indexed without anybody handling a file. Report index currency as a headline: what proportion of the estate has a document matching the deployed version, which is the honest measure of what the organisation can answer and is usually low. Flag the products with no document at all as a distinct gap, since they are invisible to every query. Prioritise currency by product criticality rather than uniformly, since the effort of chasing vendors is finite. And feed the gaps into procurement, since the leverage to obtain documents exists at renewal and is not currently used.

## Who Feels the Pain
Security teams answering a vulnerability question from a stale index; compliance functions attesting to a capability that describes an obsolete estate; and organisations that satisfied a mandate and cannot answer the question it exists for.

## Impact If Fixed
Recording the described version against the deployed version makes every answer interpretable and is a small schema change. Requesting documents per release is a contractual term that costs nothing and converts a one-off procurement artefact into a maintained record.
