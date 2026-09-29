# Vendor and Architecture Selection

**Industry:** [[fractional-cto-services|Fractional CTO Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The advisor recommends a database, a cloud, a framework or a build-versus-buy decision, and the evidence available is vendor documentation, analyst reports and their own last three projects.
**Tags:** #gradient-boosting #k-nearest-neighbors #bert #large-language-models #confidence-intervals #evaluation-metrics #survival-analysis #tacit-knowledge-ml

## The Problem
A significant part of advisory work is selection: which platform, which vendor, whether to build or buy, which architectural pattern. These decisions are durable — a database choice or a core platform commitment shapes a company for years and is expensive to reverse.

The evidence base is poor. Vendor documentation describes capability rather than experience. Analyst reports rank vendors on criteria weighted by a methodology the reader cannot inspect and are influenced by vendor relationships. Community discussion is loud, unrepresentative and dominated by recent enthusiasm. Benchmarks measure conditions unlike the client's. What remains is the advisor's own experience, which is a small sample drawn from their particular history.

The specific failures are consistent. The cost model is understood at the list price and not at the shape the client's actual usage will produce. The operational burden — what it takes to run this thing at three in the morning — is invisible until it is being borne. The migration cost out is never estimated, so lock-in is accepted without pricing. And the failure modes that matter are the ones that appear at a scale or a usage pattern the client has not reached yet.

## What Already Exists
Analyst firms — Gartner, Forrester, and the newer evaluation sites — provide structured comparisons. Community review platforms such as G2 and TrustRadius aggregate user opinion with known selection bias. Vendor documentation and reference customers are supplied on request. Cloud pricing calculators model list cost. Technology radars from consultancies publish opinionated positions. Benchmarking suites exist for databases and infrastructure and are notoriously easy to construct favourably.

## The Customisation Gap
What a practitioner needs is not a ranking but a fit assessment against this client's specific constraints: usage shape, team skills, operational maturity, compliance requirements, growth trajectory and exit cost tolerance. Nothing produces that, so the advisor constructs it mentally from a general ranking and a set of specifics.

Real operational experience is the missing evidence. What a platform is like to run — the failure modes, the upgrade pain, the support quality when something is genuinely broken, the surprises in the bill — is known to the people running it and is scattered across incident write-ups, engineering blogs, community threads and private conversation. Assembling that into a structured, attributable picture of operational reality is the analysis nobody does and the one that would change decisions.

Cost modelling against the client's own usage shape rather than a list price is the second gap, and it is straightforwardly computable where the usage pattern can be characterised.

And the exit cost belongs in the decision. Estimating what leaving would involve — data extraction, dependency depth, proprietary surface area — prices the lock-in that is currently accepted implicitly.

## Impact If Solved
Selection decisions are durable, expensive to reverse and made on an evidence base that is largely vendor-supplied or anecdotal. Fit assessment against the client's actual constraints, structured operational experience drawn from where it is actually recorded, usage-shaped cost modelling and explicit exit pricing address the four ways these decisions predictably go wrong — and they turn an advisor's personal experience into a position they can evidence rather than assert.
