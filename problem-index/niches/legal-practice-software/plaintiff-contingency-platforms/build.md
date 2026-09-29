# The Portfolio View a Contingency Firm Has Never Had

**Niche:** [[niches/legal-practice-software/plaintiff-contingency-platforms/profile|Plaintiff & Contingency Firm Platforms]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A contingency firm is an investment portfolio managed without any of the instruments a portfolio manager would consider basic — no expected value per position, no duration estimate, no concentration view, no marginal return on the next dollar of case cost.
**Tags:** #survival-analysis #gradient-boosting #confidence-intervals #monte-carlo-methods #evaluation-metrics #bayesian-inference #revenue-impact #tacit-knowledge-ml
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A firm has 600 open cases, $4M of case costs advanced, a line of credit, and a partner's sense of how the year is going. It cannot state the expected value of its portfolio, the distribution around that expectation, when the cash is likely to arrive, or how much of its exposure is concentrated in one carrier, one venue or one theory of liability. When it decides whether to advance $30K for an expert, it is making a capital allocation decision with no estimate of the return. Litigation funders underwrite exactly these portfolios using exactly this data and price the risk; the firm that owns the portfolio has less information about it than the fund lending against it.

## Why Nobody Has Built This
Prediction in this domain is genuinely hard and genuinely consequential, which is a combination vendors avoid. Outcomes are heavy-tailed, censored — a case that has not resolved has no outcome yet, and the ones that take longest are systematically different from the ones that settle early — and confounded by the firm's own selection, since the cases a firm signs are not a random sample of cases available. There is also a real professional-responsibility unease: a model that recommends declining a case is a model making a decision about access to counsel, and vendors have preferred not to touch it. The commercial reason is simpler. Selling a dashboard is safe, and selling a number that will sometimes be wrong about a named case is not.

## What to Build
A portfolio layer that treats every open matter as a position with a distribution rather than a point estimate. Time to resolution is modelled with survival methods that handle censoring honestly, since the open cases are the whole question. Value is modelled conditionally on what is known now — venue, carrier, injury and treatment pattern, liability posture, stage — and updated as facts arrive, so the estimate moves when the medical records come back rather than staying fixed from intake. From those two, the firm gets an expected cash timeline, a concentration view, and a marginal-return figure for the next dollar of case cost, which is the actual decision being made. Calibration is the product: the interface should show, for every past prediction band, what actually happened, because a contingency firm will not and should not trust a number whose track record it cannot see.

## Target Customer
Plaintiff firms carrying 200+ open matters and meaningful advanced costs, the platforms serving them, and the litigation funders who already build these models externally and would rather have the firm's own data.

## Impact If Built
A calibrated portfolio view changes three decisions a firm currently makes by feel: which cases to invest in, when to borrow, and what a settlement offer is worth against the distribution of trying. Firms that adopt funder-grade portfolio analytics typically find their case-cost allocation is concentrated in positions with poor marginal return, and the correction is worth more than any workflow improvement the category has shipped.
