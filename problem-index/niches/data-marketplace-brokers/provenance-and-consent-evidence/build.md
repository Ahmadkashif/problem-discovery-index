# A Warranty Is Not Evidence

**Niche:** [[niches/data-marketplace-brokers/provenance-and-consent-evidence/profile|Provenance & Consent Evidence]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Buyers need to know how data was collected and whether it may lawfully train a model, and the answer arrives as a representation in a contract rather than as anything a regulator would accept.
**Tags:** #compliance #graph-theory #data-integration #evaluation-metrics #descriptive-statistics #automation #workflow-orchestration #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to replace a contractual warranty about lawful collection with evidence a buyer can rely on — and whoever does that takes the account, because the buyer now carries the regulatory risk and a warranty does not discharge it.

## The Problem
A company wants to train a model on a purchased dataset. Their counsel asks where the data came from, what the individuals were told, whether any of them are in jurisdictions with stricter regimes, and whether the consent obtained covers model training. The provider's answer is a warranty of lawful collection and a completed questionnaire. The dataset was itself assembled from four upstream sources, two of which the provider licensed from others. Nobody in the chain can produce the original consent language. The company either declines the purchase, which is the common outcome, or proceeds on a risk acceptance that will not survive scrutiny.

## Why Nobody Has Built This
Chain of custody was never required, so it was never recorded, and reconstructing it retrospectively for historical data is frequently impossible. Providers who aggregate from upstream sources would have to obtain evidence from parties who do not have it either. The market grew during a period when provenance was a formality. And a provider who builds real provenance evidence competes against ones who assert compliance for free, which is the same coordination problem the rest of this market has.

## What to Build
Make provenance an artefact rather than a promise. Build a chain-of-custody record that travels with the dataset — collection method, collection date, the notice and consent language actually presented, jurisdiction, upstream sources with their own records, and each transformation applied — which is the artefact, and it is buildable for data collected from now on even where historical data is beyond recovery. Record the consent language verbatim rather than summarising it, since the question is always whether a specific use is covered and a summary cannot answer it. State the permitted uses explicitly including model training, which is the most-asked question and is frequently answered by silence in the original notice. Break coverage down by jurisdiction, so a buyer can scope their obligations and exclude segments rather than declining the whole dataset — this alone rescues transactions that currently fail. Make the record verifiable by a third party rather than self-asserted. Propagate the record through aggregation, so a derived dataset carries its constituents' provenance, which is where most chains currently break. Support consent withdrawal propagation, which the fix note develops. And distinguish clearly between data with evidence and data with a warranty, because collapsing the two is what lets the market avoid the problem.

## Target Customer
Legal and compliance functions, model training buyers, providers with genuinely clean collection practices, and the regulators whose obligations flow through to buyers.

## Impact If Built
A warranty allocates liability and answers nothing a regulator asks. A per-jurisdiction breakdown alone rescues transactions that currently fail wholesale, and recording consent language verbatim is the only way to answer whether a specific use was covered.
