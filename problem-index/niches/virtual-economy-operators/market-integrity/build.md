# Surveillance Instead of Reports

**Niche:** [[niches/virtual-economy-operators/market-integrity/profile|Market Integrity]]
**Industry:** [[industries/virtual-economy-operators|Virtual Economy Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A market with real money in it is policed by waiting for someone to complain.
**Tags:** #graph-theory #change-point-detection #compliance #evaluation-metrics #confidence-intervals #k-means-clustering #data-integration #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to police a market with real monetary value using rules written for stolen credit cards — and whoever brings real surveillance to it takes the account.

## The Problem
These are markets where people exchange goods with genuine monetary value at prices set by supply and demand. They attract the same abuses as any market: trades between colluding accounts to create false volume, coordinated buying to ramp a price before selling into it, cornering of a limited release, and trades whose purpose is moving value rather than obtaining an item. The operator's controls are payment fraud rules and a reports queue. Nothing watches the market itself.

## Why Nobody Has Built This
Surveillance implies the operator is running a market, which is a characterisation it has commercial and legal reasons to avoid. Trust and safety teams are staffed for fraud and abuse rather than for market conduct. Abuse that raises volume also raises revenue. And no regulator has yet compelled it.

## What to Build
Watch the market rather than the payments. Build surveillance over the order and trade record for the known abuse patterns — circular trading, self-dealing through intermediaries, price ramping, spoofing, supply cornering — which is the core and requires no data the operator does not already hold. Analyse the trade graph rather than individual transactions, since manipulation is a relationship pattern and is invisible one trade at a time. Detect coordination between accounts from timing and structure, which is where the strongest evidence lives. Distinguish manipulation from legitimate trading behaviour carefully, because false positives here mean banning people from things they paid for. Alert on abnormal price and volume movement relative to the item's own history rather than on absolute thresholds. Maintain case management with retained evidence, as enforcement decisions are disputed and the operator's position must stand up. Publish market rules so participants know what is prohibited, which most operators have never stated. Report enforcement statistics, since an unenforced rule is quickly discounted by the people gaming it. Cover third-party marketplaces where the trades ultimately settle on the operator's infrastructure. And establish an internal position on what the operator is running, which is the decision every technical choice here depends on.

## Target Customer
Virtual economy operators, marketplace and trust leadership, third-party trading platforms, and market surveillance vendors.

## Impact If Built
Manipulation is a relationship pattern and is invisible one trade at a time, which is why a fraud rules engine sees none of it. Graph surveillance over the trade record brings a market with real money into the same regime as any other market.
