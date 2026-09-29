# The Mechanism: Credibility Weighting, and the Score Bolted on Top

**Origin:** [[origins/insurance-carriers/profile|Insurance Carriers]]
**Tags:** #bayesian-inference #maximum-a-posteriori-estimation #probability-distributions #descriptive-statistics #expectation-variance-covariance #evaluation-metrics #revenue-impact #compliance

## The Question, Stated Properly

Insure a single small business against fire. It has had zero claims in three years of coverage. **Is its true risk zero, or did it simply get lucky, and how would you tell the difference from three years of data?**

This is not a rhetorical question. Three years is not enough observations to estimate a rare event's true frequency with any confidence, for almost any individual risk. Price purely off that policyholder's own thin history and the estimate is dominated by noise. Price purely off the average of everyone in its class and territory and you ignore everything genuinely distinctive about this one business. **The mechanism this file describes is the formula that blends the two, and it predates the computer that made it practical by roughly four decades.**

## The Decomposition

**1. Pool the loss experience of a class.** For a given category of risk — small commercial fire, in a given territory — collect claims experience across every insurer willing to contribute it. This pooling is what the [[origins/insurance-carriers/the-fight|antitrust exemption]] exists to permit, and it is what became ISO's core function from 1971.

**2. Compute the class's pure premium.** Frequency (claims per unit exposure) times severity (average cost per claim) gives the expected loss cost for the class as a whole — a number with real statistical weight behind it, because it is built from a much larger pool than any one insurer's book.

**3. Weight the individual's own experience against the class average.** This is **credibility theory**, formalised by Albert Mowbray in 1914 and given its now-standard blending formula by Albert Whitney in 1918:

> *Estimated premium = Z × (individual's own experience) + (1 − Z) × (class average)*

where **Z**, the credibility factor, rises toward 1 as the individual's own volume of exposure and claims grows, and falls toward 0 when there is too little of it to trust. A policyholder with three years and no claims gets a premium close to the class average, weighted lightly by their own good luck. A policyholder with thirty years of claims history gets a premium that is mostly their own.

> **Worth flagging explicitly, because it is exactly the vault's recurring pattern:** this is a shrinkage estimator — borrowing statistical strength from a larger reference population when an individual sample is too thin to trust on its own — arrived at by actuaries in 1914–18, decades before statisticians formalised the general version of the same idea. The mathematics, again, was available long before the machine that let anyone apply it at population scale every renewal cycle instead of once by hand.

**4. Layer a privately computed score on top.** Once the shared, credibility-weighted loss cost exists as a floor, an individual insurer can add its own rating factors — since 1993, most commonly a **FICO-derived credit-based insurance score** — to sort applicants more finely than the pooled class average alone permits. This is the layer insurers compete on, because it is the layer each insurer owns exclusively.

## The Trade-Offs Taken

**Fairness to the individual was traded for statistical reliability of the price.** Any credibility-weighted system charges some individually low-risk policyholders more than their own true risk, and some individually high-risk policyholders less, because the class average is doing real work in the formula. This is not a bug to be engineered away — reducing Z to zero would mean pricing entirely off untrustworthy individual samples.

**A score built to predict loan default was repurposed to predict claims, and the justification is correlational, not causal.** Credit-based insurance scoring works because credit behaviour is statistically associated with claim propensity in large samples, not because anyone has shown that poor credit management causes house fires or car accidents. Several states restrict or ban its use in at least some insurance lines precisely on this ground — that a proxy correlated with an outcome is not the same thing as a fair basis for pricing that outcome.

## The Transferable Pattern

> **When an individual's own data is too thin to price or predict anything reliably, borrow strength from a larger reference population — weighted by exactly how much you can trust the individual's own signal — rather than choosing between "trust the individual" and "ignore the individual" as an all-or-nothing decision.**

An FDE building a personalisation model for a new user with three interactions, or a churn model for a business unit with a handful of historical customers, is solving Whitney's 1918 problem again, usually without knowing its name.

**Sources:** Mowbray (1914), *How Extensive a Payroll Exposure is Necessary to Give a Dependable Pure Premium?*; Whitney (1918), *The Theory of Experience Rating*; Wikipedia, *Credibility theory*; NAIC, *Credit-Based Insurance Scores*; FICO, insurance-score history.