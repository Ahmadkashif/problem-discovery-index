# Litigation Finance Underwriting Models Turned Inward

**Niche:** [[niches/legal-practice-software/plaintiff-contingency-platforms/profile|Plaintiff & Contingency Firm Platforms]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Litigation funders have spent a decade building underwriting models for exactly these portfolios and sell the resulting capital to firms who never see the model, which means the analytical capability the segment needs already exists and points the wrong way.
**Tags:** #bayesian-inference #survival-analysis #monte-carlo-methods #confidence-intervals #evaluation-metrics #hypothesis-testing #revenue-impact #compliance
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A firm takes a portfolio advance. The funder underwrites it: assesses case mix, venue distribution, expected duration, realisation rates, and prices accordingly. The firm receives money and a rate. It does not receive the analysis, and it has no basis on which to argue the rate, because it has never computed the numbers the rate is derived from. The information asymmetry is total, and it is not adversarial by design — the funder built a capability the firm could have built and did not.

## What Already Exists
Portfolio underwriting methodology in litigation finance is mature and, in its broad outlines, public: duration modelling under censoring, realisation-rate estimation by case type and venue, correlation and concentration analysis, and Monte Carlo simulation of cash flows are all standard practice with substantial published literature in insurance and structured credit. Court outcome data is commercially available from Lex Machina, Trellis and the docket analytics vendors. The methods and much of the reference data are purchasable or open; what the funder adds is the firm's own portfolio, which the firm already has.

## The Customization Gap
The adaptation is to run the funder's analysis with the firm as the audience and the firm's own matter records as the input. It requires: (1) mapping the practice management system's matter data into the schema an underwriting model needs — stage, venue, carrier, liability posture, costs advanced, and the dates that establish duration — which is mostly a data engineering exercise the vendors have never done; (2) replacing generic realisation assumptions with the firm's own resolved history, and being explicit where the firm's history is too thin to support that, falling back to the vendor's cross-firm base rates with the shrinkage stated; (3) simulating cash flow rather than reporting an expected value, because a contingency firm's real risk is timing, not expectation; (4) producing the same artefacts a funder produces, so that a firm entering a financing conversation has a symmetric document; and (5) refusing to output a number for a case type where the firm and the corpus both lack data, which is the discipline that makes the rest credible.

## Target Customer
Plaintiff firms that use or are considering portfolio financing, practice management vendors serving them, and the funders themselves, for whom a firm with clean portfolio analytics is a cheaper diligence target.

## Impact If Solved
The immediate effect is negotiating position: a firm that arrives with its own duration and realisation analysis prices differently than one that arrives with a case list. The larger effect is internal, because the same model that justifies a rate also tells the firm which parts of its portfolio are earning the capital they consume — a question the segment has never been able to ask.
