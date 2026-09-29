# Token Listing Due Diligence

**Industry:** [[crypto-exchanges|Crypto Exchanges]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Listing a token requires assessing code, distribution, team, legal characterisation and market integrity, and the same analysis is redone by every exchange for every asset by hand.
**Tags:** #large-language-models #bert #graph-neural-networks #gradient-boosting #word-embeddings #evaluation-metrics #compliance #data-integration

## The Problem
Before an exchange lists an asset it must form a view on several distinct questions. Is the contract code safe — upgradeable, mintable, does it have an owner function that can freeze balances or drain a pool. How is supply distributed, and does a concentrated holder set create manipulation risk or an imminent unlock. Who is the team, and is there anything in their history that matters. Is the asset plausibly a security under the exchange's legal analysis, which is the question with the largest consequences and the least settled answer. Is there enough genuine liquidity and organic volume to support orderly trading, or is the apparent activity wash trading.

Each question has its own evidence: contract source, on-chain holder and flow data, documentation and social presence of variable reliability, legal precedent, and market data from venues with varying honesty.

The work is done by a listings team reading, and it is redone at every exchange for the same asset. Then it must be redone periodically, because the answers change — a team departs, an unlock occurs, a contract is upgraded, litigation lands.

Delisting is the harder half and gets less attention. An asset whose liquidity has evaporated or whose legal characterisation has shifted has to be removed, which harms holders and is deferred.

## What Already Exists
Contract auditors (OpenZeppelin, Trail of Bits, Certik) publish audits of variable quality. Token sniffer tools flag common contract risks automatically. On-chain analytics platforms (Nansen, Arkham, Dune) expose holder and flow data. Exchanges maintain listing frameworks and committees. Regulatory guidance exists in the form of enforcement actions rather than rules.

## The Customisation Gap
Contract risk detection is partly automated by public tools and rarely integrated into the listing workflow as structured evidence with a confidence attached. The standard patterns — mint authority, upgradeable proxy, blacklist function, fee-on-transfer, unlimited approval — are mechanically detectable from bytecode.

Holder concentration and unlock scheduling are computable exactly from chain data and vesting contracts, and are frequently assessed from a project's own published schedule, which is the least reliable available source.

Wash trading detection is the gap with real money attached. Circular flow patterns, self-trading through related addresses and volume concentrated in a small set of counterparties are graph problems on public data, and exchanges largely rely on reported volume from other venues.

Continuous monitoring after listing barely exists. The listing decision is a snapshot and the risks are dynamic; re-evaluation happens when something goes wrong publicly.

And nothing learns from outcomes. Exchanges have listed thousands of assets and know which ones subsequently collapsed, were exploited, were delisted, or drew enforcement. That is a labelled dataset about listing decisions and it is not used to grade the framework that produced them.

## Impact If Solved
Listing decisions carry legal, reputational and customer-loss exposure, are made from evidence that is mostly public and mechanically derivable, and are reviewed by people reading documents. Automating contract and distribution analysis, detecting wash trading from flow graphs, and grading the framework against the outcomes of past listings turns a committee process into an evidenced one.
