# Data Profiling and Record Linkage

**Niche:** [[niches/data-marketplace-brokers/pre-purchase-evaluation/profile|Pre-Purchase Evaluation]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data profiling and record linkage are mature disciplines with strong open implementations, and they run after acquisition when the entire value would be in running them before.
**Tags:** #descriptive-statistics #k-nearest-neighbors #evaluation-metrics #hypothesis-testing #probability-distributions #data-integration #bayesian-inference #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to let a buyer measure a dataset against their own requirement before paying for it — and whoever does that takes the market, because every purchase in it is currently made blind.

## The Problem
Characterising an unfamiliar dataset — completeness, distributions, key candidates, value ranges, anomalies — is what data profiling does, automatically and well. Determining how much two datasets about the same entities overlap is record linkage, which has decades of statistical foundation and several strong implementations. Both are deployed routinely after a dataset has been acquired and integrated, which is exactly one step too late to inform the decision that mattered.

## What Already Exists
Data profiling engines producing completeness, distribution and constraint reports automatically; probabilistic record linkage with established statistical foundations and open implementations; fuzzy matching and blocking techniques for scale; privacy-preserving record linkage using hashed and encrypted identifiers; and private set intersection protocols with practical performance.

## The Customization Gap
The adaptation is to run these before a commercial relationship exists, between parties who do not trust each other. It requires: (1) linkage executed without either party disclosing records, which private set intersection supports and which almost nobody in this market has deployed despite it being the enabling primitive; (2) profiling run by a neutral party or verifiably by the provider, since a self-reported profile has the same credibility problem as a self-reported statistic; (3) coverage reported by buyer-defined segment rather than in aggregate, because that is the decision-relevant figure and it requires the buyer to express their population in a form the protocol can use; (4) match quality reported honestly, since linkage on imperfect identifiers is itself uncertain and an overlap figure without a confidence statement repeats the market's existing problem in a new form; and (5) an economic model for who pays, since the evaluation costs something before a transaction exists and the current structure has no place to put that cost.

## Target Customer
Marketplaces, buyers, providers with strong data, and the record linkage and privacy technology communities.

## Impact If Solved
The profiling and linkage machinery is mature and runs one step too late. Private set intersection is the primitive that lets overlap be measured before a relationship exists, and almost nobody in this market has deployed it.
