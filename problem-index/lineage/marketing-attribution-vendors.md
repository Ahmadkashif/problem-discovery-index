# Lineage: Marketing Attribution Vendors

**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Wave:** [[series/eras/wave-09-programmatic|9 — Programmatic]]
**The tool:** Robyn — Meta Marketing Science's open-source marketing mix modelling package for R (MIT licence, first commit 1 October 2020): ridge regression over adstocked and Hill-saturated media spend, hyperparameters searched with Nevergrad against three objectives, one of which is fit to lift experiments
**Builder:** Facebook
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Marketing mix modelling is old: regress sales on media spend, week by week, and read each channel's contribution off the coefficients. What kept it expensive was not the regression. It was the choices around it — how long an ad's effect lingers (adstock), where spend stops paying (saturation), which of many correlated channels gets the credit — each of which an econometrician set by judgement, per client, over weeks.

That made it, in Robyn's own words, "a resource-intensive technique that was only affordable for 'big players'." Everyone else used path-based multi-touch attribution, which needed no econometrician — only a user-level trail of clicks and impressions stitched by cookies and device IDs.

**When that trail began to fail, the cheap method broke and only the expensive one was left.**

## What Got Built

The repository's first commit is dated **1 October 2020**; tagged releases from v3.0.0 appear on GitHub on **27 October 2021**, and it later went onto CRAN.

The design choices are specific, and each one replaces a judgement call with a search:

- **Adstock** as geometric decay or a Weibull curve, and **saturation** as a Hill function, with the parameters of both searched rather than set.
- **Ridge regression** to hold together channels whose spends move in lockstep — which the documentation notes is equivalent to a Bayesian regression with a Gaussian prior.
- **Nevergrad**, Meta's evolutionary optimiser, running thousands of candidate models against three objectives at once: NRMSE for fit, DECOMP.RSSD for whether effect shares look plausible against spend shares, and **MAPE.LIFT** for agreement with experiments.
- Output is not one model but a Pareto front of them, plus a budget allocator.

The third objective is the telling one. Robyn accepts results from people-based Conversion Lift and geo experiments such as Meta's GeoLift, and the guide recommends running them "on an ongoing and regular basis in order to have results that can permanently calibrate the MMM."

## Who Built It, And Why Them

Meta Marketing Science. The package lists Gufeng Zhou as maintainer, with Bernardo Lares, Igor Skokan and Leonel Sentana as authors, and Meta Platforms as copyright holder and funder.

The stated reason is in the README: "As the privacy needs of the measurement landscape evolve, there's a clear trend of increasing demand for modern MMM as a privacy-safe solution."

The unstated one follows from the dates. Meta's ad business was measured largely by user-level tracking, and Apple announced on **3 September 2020** that iOS apps would need permission to read the advertising identifier — four weeks before Robyn's first commit. A platform whose own conversion tracking was about to go dark on iOS had every reason to put a spend-level model, needing no user data and calibratable with Meta's own lift tests, into advertisers' hands for free. **That motive is my inference; Meta has not said so in any source I read.**

Why free and open? A modelling method only moves budget if the buyer trusts it, and a platform grading its own channel invites suspicion. Open code is the answer to that suspicion.

## What It Cost

**It commoditised the method and left the answer underdetermined.** Search over adstock and saturation produces many models that fit about equally well and divide credit differently — which is why Robyn returns a Pareto front and asks a person to choose.

Calibration helps only where experiments exist, and the experiment tooling Robyn points to first is the seller's own. The documentation itself cites a third-party finding that uncalibrated models differ from ground truth by 25% on average — and ships the allocator with the caveat that Meta does not guarantee its predictions will meet business expectations.

## What You Still Touch

Every attribution vendor now sells against free code: Robyn, Google's Meridian, PyMC-Marketing. What remains to sell is specification, priors and validation.

- [[problems/marketing-attribution-vendors/low-impact-1|🟡 Mix Model Specification and Identifiability]] — the search Robyn made visible
- [[problems/marketing-attribution-vendors/high-impact|🔴 Selling a Causal Answer With No Way to Check It]]
- [[niches/marketing-attribution-vendors/mix-modelling/profile|Mix Modelling]]
- [[niches/marketing-attribution-vendors/validation-and-ground-truth/profile|Validation & Experimental Ground Truth]] — MAPE.LIFT's unfinished business

**Sources:** WebSearch was unavailable this session (session cap reached); research was by WebFetch and direct retrieval. GitHub, `facebookexperimental/Robyn` — README ("resource-intensive… big players", privacy-safe rationale), `R/DESCRIPTION` (authors, maintainer, Meta Platforms as copyright holder and funder, "ground-truth calibration"), repository API (MIT licence; oldest commit 1 October 2020 by Leonel Sentana; release tags v3.0.0–v3.0.4 on 27 October 2021); Robyn documentation, *Features* (ridge/Gaussian prior, Nevergrad objectives NRMSE / DECOMP.RSSD / MAPE.LIFT, Weibull and Hill, 25% uncalibrated-model finding) and *Analyst's Guide to MMM* (Conversion Lift and GeoLift quote, allocator disclaimer); CRAN archive listing (earlier versions, archive dates only); Wikipedia, *App Tracking Transparency* (3 September 2020). ⚠️ **Not established:** Robyn's public launch or announcement date and its first CRAN publication date (archive dates record supersession, not release); who at Meta originated the project; any Meta statement tying Robyn to Apple's tracking changes — the link is inference from dates. **Keying note (orchestrator):** keyed `Facebook`, the build-time name — the first commit (1 October 2020) predates the October 2021 rename to Meta, consistent with `Square` not Block.
