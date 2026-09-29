# Cost Basis and Tax Reporting

**Industry:** [[crypto-exchanges|Crypto Exchanges]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The exchange must report a customer's gain on assets that arrived from somewhere else with no basis attached, and the 1099-DA regime made that a legal obligation rather than a customer inconvenience.
**Tags:** #gradient-boosting #k-nearest-neighbors #graph-theory #evaluation-metrics #feature-engineering #data-integration #compliance #workflow-orchestration

## The Problem
A customer buys an asset on one exchange, moves it to a wallet, uses it in a protocol, moves it to a second exchange and sells. The second exchange must report the sale. It knows the proceeds exactly and knows nothing about the basis, because the acquisition happened elsewhere.

Under the 1099-DA regime brokers report gross proceeds and, increasingly, basis where they have it, with transfer reporting intended to carry basis between brokers over time. In the interim, and for anything touching self-custody or a decentralised protocol, the basis is missing and the customer receives a form that overstates their gain, sometimes enormously.

The intermediate events are the hard part. A swap is a disposal. Wrapping may or may not be. Providing liquidity, receiving staking rewards, an airdrop, a hard fork, a rebase, a bridge — each has a tax characterisation that is unsettled in places, and each changes basis.

Customers respond by using third-party tax software that reconstructs everything from exchange exports and chain data and produces a different answer than the exchange's form. Support receives the difference.

Internally, the exchange must also track its own positions, its staking rewards and the basis of assets it holds on customers' behalf, across chains with different accounting treatments.

## What Already Exists
CoinTracker, Koinly, TaxBit and ZenLedger reconstruct positions from exchange APIs and chain data. Exchanges provide transaction exports and are building 1099-DA reporting. The rules have become clearer with the broker regulations, and transfer statement requirements are intended to propagate basis over time.

## The Customisation Gap
Transaction classification from chain data is the core unsolved piece. Determining what a given on-chain interaction actually was — a swap, a deposit into a lending protocol, a liquidity provision, a bridge, a reward claim — requires decoding contract calls against a protocol taxonomy that changes constantly. Tax vendors do this with maintained rule libraries that lag new protocols by months.

Transfer matching is mechanical and unautomated. When a customer withdraws to an address and later deposits from an address, matching those legs across exchanges and wallets to carry basis is graph work on data the exchange has, and it is exactly what the transfer statement regime is trying to achieve institutionally.

Basis estimation under uncertainty is nobody's product. Where basis is genuinely unknown, the honest output is a range with a stated method, not a zero. A form asserting zero basis is a confident claim that the customer owes tax on the entire proceeds, and it is usually wrong.

And nothing anticipates the support load. The exchange can compute, before forms go out, which customers will receive a materially wrong number, and could tell them first.

## Impact If Solved
Tax reporting has moved from a customer service courtesy to a reporting obligation with penalties, and the data required to discharge it correctly is fragmented across exchanges, wallets and protocols by design. Classifying on-chain activity, matching transfer legs and reporting basis uncertainty honestly reduces a large seasonal support burden and removes a reporting error the customer cannot correct without professional help.
