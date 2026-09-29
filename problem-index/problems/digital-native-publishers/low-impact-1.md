# Ad Stack Yield and Leakage

**Industry:** [[digital-native-publishers|Digital Native Publishers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A long chain of intermediaries sits between an impression and the money, and the publisher can see neither where the value goes nor what a given page is actually worth.
**Tags:** #gradient-boosting #time-series-forecasting #causal-inference #confidence-intervals #evaluation-metrics #feature-engineering #data-integration #revenue-impact

## The Problem
An impression on a publisher's page is auctioned through header bidding across several demand partners, into an ad server, out to exchanges, through supply-side and demand-side platforms, each taking a fee. Industry studies have repeatedly found that a substantial fraction of advertiser spend never reaches the publisher, and that a meaningful share of the chain is not fully traceable by either end.

Configuration is a continuous optimisation with many interacting settings: which partners, what floors, timeouts, refresh behaviour, ad density, lazy loading thresholds. Each affects revenue and also page performance, which affects engagement, which affects revenue again on a longer loop that nobody measures.

Viewability, invalid traffic filtering and brand safety classification each remove inventory from monetisation, sometimes correctly and sometimes not. A brand safety tool blocking a serious news story about a disaster is a well-known and persistent problem that costs publishers real money on exactly their most important journalism.

Third-party cookie deprecation has proceeded unevenly, making addressability and therefore yield unstable, and pushing publishers toward first-party data programmes whose value is asserted more often than measured.

And attribution within the publisher is poor. Which content, which audience segment and which page configuration actually produce revenue is obscured by the chain, so editorial and product decisions are made without a reliable revenue signal.

## What Already Exists
Google Ad Manager, Prebid and the header bidding ecosystem are mature. Supply path optimisation is an established discipline. ads.txt and sellers.json improve chain transparency partially. Viewability and invalid traffic vendors are standard. Consent management platforms handle the regulatory layer. Some publishers run data clean rooms with advertisers.

## The Customisation Gap
Floor pricing is static or coarsely segmented when it should be dynamic. The optimal floor varies by placement, audience segment, time, device and demand conditions, and it is a well-posed optimisation problem that most publishers approach with a handful of rules.

The performance-revenue tradeoff is unmeasured. Ad density and page weight affect engagement and return visits, which affect lifetime revenue, and the tradeoff is resolved by intuition because the second-order effect requires an experiment nobody runs.

Brand safety false positives are unquantified. Publishers know their serious journalism gets blocked and almost none measure how much revenue it costs, which is the number required to negotiate with the vendors and the advertisers.

Supply path analysis is done by specialist consultants for large publishers and by nobody for everyone else, despite the data being in the publisher's own logs.

And first-party segment value is asserted. Whether a publisher's own audience segments actually command a premium is testable through controlled comparison and is usually taken on faith.

## Impact If Solved
Advertising remains a large revenue line in a business with compressed margins, and it is operated through a chain the publisher cannot see into with settings tuned by rule of thumb. Dynamic floors, measured performance tradeoffs and quantified brand safety loss recover revenue that is currently leaking in ways the publisher can observe in its own logs and does not.
