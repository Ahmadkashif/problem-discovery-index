# Job Order Margin Estimation at Quote Time

**Industry:** [[staffing-agencies|Staffing Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** When an account manager quotes a bill rate to a client on the phone, they're guessing at the true margin because the real cost — burden rate, workers' comp class code, SUTA rate by state, ACA obligations, and client-specific payment terms — lives in five different systems and one senior person's head.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #gradient-descent #expectation-variance-covariance #bias-variance-tradeoff #revenue-impact

## The Problem
Staffing agencies live and die on spread — the difference between what the client pays (bill rate) and what the agency pays out (pay rate + burden). But burden is not a single number. It includes FICA (7.65%), FUTA (0.6% on first $7K), SUTA (varies from 0.5% to 6.2% depending on the state and the agency's experience rating), workers' comp premiums (which vary by class code — office clerical at $0.30/$100 vs. roofing at $15.00/$100), ACA health insurance obligations if the worker hits 30 hours/week for a measurement period, and sometimes client-specific costs like required safety training or drug testing. An account manager quoting a bill rate of $22/hour for a warehouse worker in Ohio might assume 25% burden when the true burden is 31%, turning a healthy 28% gross margin into a break-even 19%.

Most agencies discover margin erosion only at month-end when the P&L is reconciled — weeks after the rate was locked in a client contract. Across a firm placing 500 temps, even a 2-point margin miscalculation on 20% of placements can cost $200K–$400K annually in unrealized profit.

## What Already Exists
Bullhorn's revenue analytics and TempWorks' margin reports provide retrospective margin analysis — what the margin was after the assignment is complete. Generic CRM tools like Salesforce can track bill/pay rates but have no concept of burden rate components. Some larger agencies build custom Excel models or Access databases that attempt to pre-calculate burden, but these break whenever SUTA rates change (annually), workers' comp class codes are reclassified, or a new state is added to the agency's footprint.

## The Customisation Gap
A staffing-specific margin calculator needs real-time access to: (1) the agency's current SUTA rate in every state where it operates, updated annually or after rate change notices, (2) workers' comp premium rates by class code and carrier, (3) ACA measurement period tracking per worker to predict when health insurance costs will attach, (4) client-specific cost adders (background checks, drug tests, safety gear, training hours), and (5) historical fill-rate data to estimate the probability of actually billing the quoted hours. A regression model trained on historical job orders can predict true realized margin at quote time, factoring in patterns like "light industrial job orders in Q4 in this metro always run 15% more OT than estimated" or "this client's payment terms average 52 days, add 1.2 points for cost of capital."

## Impact If Solved
Account managers quote with confidence, eliminating margin surprises on 20–30% of job orders. Average gross margin improves 1.5–3 points across the book of business, translating to $150K–$600K in annual incremental profit for a mid-size firm placing 300–800 temps. Sales teams close faster because they can respond to client rate requests in real time instead of saying "let me get back to you after I talk to payroll."
