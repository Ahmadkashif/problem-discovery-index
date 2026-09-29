# Two Disciplines Sold as One Product

**Niche:** [[niches/marketing-attribution-vendors/the-modelling-stack/profile|The Modelling Stack]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Path-based attribution and mix modelling answer the same question from incompatible data with incompatible assumptions, and are sold as one category called measurement.
**Tags:** #causal-inference #bayesian-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #time-series-forecasting #graph-theory #monte-carlo-methods
**Contested on:** This niche is not terminal — path-based attribution and mix modelling are different disciplines with different failure modes and different winners, and they are stated separately in the sub-niches.

## The Problem
A client buys measurement and receives, depending on the vendor, a model that follows individuals through observed touchpoints or a model that regresses aggregate outcomes on aggregate spend. These rest on entirely different assumptions, fail in entirely different ways, and produce numbers that are not comparable — one allocates credit along paths it can observe and is blind to everything it cannot, the other estimates response curves from series that move together and depends on priors to separate them. They are sold as alternative implementations of the same thing, and clients choose between them on interface and price.

## Why Nobody Has Built This
The category is defined by the question rather than by the method, so products that answer it differently are marketed as competitors — that framing serves vendors and confuses buyers. Each vendor is expert in one and dismissive of the other. Explaining the distinction requires telling a client their existing approach has structural limits. And a unified framework that says when each applies would reduce every vendor's addressable claim.

## What to Build
Treat them as instruments with different domains of validity. State plainly what each method can and cannot answer — path attribution for within-observable-journey questions where identity holds, mix modelling for aggregate allocation across channels including unobservable ones — which is the clarity the category avoids and is genuinely useful to every buyer. Build both properly rather than one and a wrapper, since a serious answer requires both instruments and most vendors have one. Anchor both to experiments, connecting to the validation work, because the only thing that can adjudicate between two incompatible models is a third method that does not model. Model the identity loss explicitly in the path method, which is the first sub-niche's contest and is usually handled by ignoring the unobserved. Model the identification problem explicitly in the mix method, which is the second sub-niche's contest and is usually handled by a prior. Report which method produced which part of the answer and with what confidence, so a client can weigh them. Combine them with a stated method rather than telling the client to triangulate, which is the reconciliation niche and is currently outsourced to the buyer. Show where the two disagree and why, since disagreement is informative and is currently a problem to be smoothed over. Validate each separately against experiments, because their error profiles differ. And publish the domains of validity, since a vendor that tells a client when not to use its own product acquires credibility nothing else in this category can buy.

## Target Customer
Measurement vendors, client measurement functions choosing between methods, and the advertisers buying a category defined by a question rather than by a method.

## Impact If Built
Two methods with incompatible assumptions are sold as implementations of the same thing, and clients choose on interface and price. Stating each method's domain of validity, and anchoring both to experiments that do not model, is what makes the disagreement between them informative rather than embarrassing.
