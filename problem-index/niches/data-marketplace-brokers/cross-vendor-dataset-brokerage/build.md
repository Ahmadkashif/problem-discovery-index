# A Market That Is Not Indexed

**Niche:** [[niches/data-marketplace-brokers/cross-vendor-dataset-brokerage/profile|Cross-Vendor Dataset Brokerage]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The suppliers who can answer a buyer's requirement are frequently companies that do not think of themselves as data providers, and no catalogue contains them because catalogues only hold people who listed themselves.
**Tags:** #graph-theory #large-language-models #evaluation-metrics #data-integration #descriptive-statistics #k-means-clustering #automation #revenue-impact
**Contested on:** Every serious competitor in this sub-niche is fighting to turn a buyer's vague requirement into a shortlist of suppliers that actually exist, including the ones with no digital shopfront — and whoever does that takes the account, because the buyer's alternative is a month of cold outreach.

## The Problem
A buyer needs equipment maintenance records across a particular industrial sector. The data exists — held by service companies, parts distributors and insurers as a by-product of their operations — and none of them have listed it anywhere, because none of them consider themselves data businesses. Every catalogue returns nothing. A broker with the right background knows to call three specific kinds of company, and that knowledge is not written down anywhere. The market's supply side is largely unindexed, and the fraction that is indexed is the fraction that thought to self-list.

## Why Nobody Has Built This
Indexing latent supply means identifying companies who hold data without knowing it is saleable, which is an outbound research problem rather than a catalogue problem and nobody has framed it as product. Brokers' value is precisely this knowledge, which makes systematising it feel like commoditising themselves. The matching is genuinely hard because requirements are expressed in the buyer's domain language and supply in the provider's. And unmet requirements leave the market silently, so the demand signal that would justify the work is never captured.

## What to Build
Index the supply that has not listed itself, and structure the demand. Build a latent supply map from what is publicly inferable — what kinds of company hold what kinds of operational data as a by-product, which regulatory filings and industry structures imply a dataset exists — which is research work that compounds and is the asset this business is actually made of. Structure requirements into a machine-matchable form — entity type, attributes, coverage, granularity, freshness, permitted use — translating from the buyer's language, which is where matching currently depends entirely on a person. Match structured demand against both catalogued and latent supply, ranking candidates with the reasoning visible so a buyer can judge the shortlist. Capture every unmet requirement, since the aggregate of what buyers asked for and could not get is the most valuable demand signal in the market and is currently discarded — it tells you what to go and source, and it is the fix note's subject. Approach latent suppliers with a specific demonstrated demand rather than a general pitch, which is a far stronger proposition and is only possible once unmet demand is recorded. Record the supply knowledge in the business rather than in brokers' heads, so it survives staff changes. And support commissioned collection where no supplier exists, which is the honest answer to a genuine gap.

## Target Customer
Data sourcing functions, investment firms sourcing alternative data, the latent suppliers unaware they hold saleable data, and the brokers whose knowledge is currently unretainable.

## Impact If Built
The suppliers who can answer a hard requirement are usually the ones who never listed themselves. A latent supply map plus a record of unmet demand lets a broker approach them with a specific buyer rather than a general pitch, which is a different conversation entirely.
