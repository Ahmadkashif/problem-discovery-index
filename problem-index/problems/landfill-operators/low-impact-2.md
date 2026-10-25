# Closure Cost Estimates Rebuilt Every Year

**Industry:** [[landfill-operators|Landfill Operators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Construction estimating and asset-retirement accounting tools already exist; a landfill still rebuilds its closure and 30-year post-closure estimates in spreadsheets every year, once for the regulator and again for the auditors, from the same unit quantities and two incompatible rulebooks.
**Tags:** #monte-carlo-methods #linear-regression #large-language-models #data-integration #compliance #automation

## The Problem
Every municipal solid waste landfill must keep a written estimate, in current dollars, of what it would cost a third party to close the largest area that could be open and then to provide post-closure care: cover maintenance, leachate collection, groundwater and gas monitoring, for 30 years unless the state shortens or extends the period. The estimates must be adjusted for inflation every year and raised whenever the plan or the unit changes, and the operator must hold financial assurance for the full amount through a trust, surety bond, letter of credit, insurance or a financial test. The same physical obligations are also accounting liabilities. WM carries $3.3B of landfill closure and post-closure asset retirement obligations and its auditor treats them, and the landfill depletion rates behind them, as critical audit matters. Republic carries 124 closed landfills.

The work falls on a site or regional environmental engineer and the controller. The regulatory estimate uses third-party costs and undiscounted dollars, follows each state's form and inflation factor, and is filed with the permit. The accounting estimate uses the company's own expected costs and timing, is discounted and accreted, and moves with every change in airspace. Both start from the same quantities — acres of cap, cubic yards of soil, geomembrane, gas wells, years of leachate treatment — but they are maintained in separate spreadsheets, often by different people, and reconciled once a year under deadline.

## What Already Exists
Construction estimating software (RSMeans cost data, HCSS HeavyBid, B2W) prices earthwork and liner installation. ERP and asset-retirement modules book, accrete and report obligations under ASC 410. Engineering consultancies prepare the regulatory estimate as a fee engagement. Financial assurance is tracked in a spreadsheet of bonds, letters of credit and trust balances.

## The Customisation Gap
What is missing is one model of each landfill's closure and post-closure quantities, tied to the airspace survey and the cell plan, that produces both estimates on demand. It needs each state's required form, line items and annual inflation factor; the third-party versus own-cost and discounting differences between the regulatory and GAAP rules; post-closure leachate and gas costs projected from the site's own volumes instead of a flat allowance; and the financial assurance mechanisms and amounts that must move when an estimate rises. An extraction layer to pull quantities and unit costs from past estimates, bids and permit drawings would let a company with hundreds of sites stop rebuilding the same tables.

## Impact If Solved
For a company with 50 landfills and two estimates per site, cutting ~40 hours of annual rebuild and reconciliation per estimate (estimate) frees ~4,000 engineering and accounting hours a year, and a single model reduces the risk of a regulatory estimate that understates the assurance a state can call on.
