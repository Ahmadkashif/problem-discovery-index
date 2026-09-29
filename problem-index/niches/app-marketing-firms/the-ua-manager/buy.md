# Portfolio Allocation Practice

**Niche:** [[niches/app-marketing-firms/the-ua-manager/profile|The UA Manager]]
**Industry:** [[industries/app-marketing-firms|App Marketing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Portfolio theory formalised allocating capital across uncertain returns, and the discipline allocating a ninety-billion-dollar market does it in a spreadsheet.
**Tags:** #convex-optimization #bayesian-inference #confidence-intervals #optimization-fundamentals #evaluation-metrics #monte-carlo-methods #revenue-impact #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to give the manager a defensible allocation instead of a weekly judgement across four disagreeing sources — and whoever does that changes how a large share of mobile advertising spend is decided.

## The Problem
Allocating capital across assets with uncertain and correlated returns is a formalised problem with a substantial apparatus: expected return and covariance estimation, constrained optimisation, uncertainty in the inputs handled explicitly, and rebalancing under transaction costs. It is applied routinely wherever money is allocated across uncertain opportunities. User acquisition is structurally the same decision — capital across channels with uncertain returns and a payback horizon — and is made by judgement with no formal treatment.

## What Already Exists
Mean-variance and robust portfolio optimisation; estimation error handling including shrinkage; constrained allocation with turnover costs; scenario and stress analysis; and rebalancing under uncertainty.

## The Customization Gap
The adaptation is to returns that respond to the allocation itself. It requires: (1) diminishing returns within each channel, since spending more moves the return, which portfolio theory's price-taking assumption excludes entirely — the response curve is the central addition and changes the optimisation's shape; (2) returns estimated from a measurement stack with known biases, so the inputs carry model error as well as sampling error and robust methods are necessary rather than optional; (3) a payback horizon that makes this an investment timing problem as much as an allocation one; (4) learning value, since allocating to an uncertain channel buys information as well as installs, which is an exploration term no portfolio model contains; and (5) a decision maker who is a marketer, so the output must be an allocation with reasoning rather than a covariance matrix.

## Target Customer
User acquisition and growth leadership, agencies, and quantitative allocation practitioners for whom marketing budgets are an unserved application.

## Impact If Solved
Portfolio theory assumes the allocator is a price taker and here spending moves the return, which makes the response curve the central addition. The exploration value of spending on an uncertain channel is a term no portfolio model contains and it is exactly what a new campaign is buying.
