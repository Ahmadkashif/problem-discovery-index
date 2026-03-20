# Reserve Study Analysis and Capital Planning Forecasting

**Industry:** [[hoa-management|HOA Management]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic financial modeling tools can project reserve fund balances forward, but don't integrate the community's reserve study (component inventory, useful life estimates, replacement costs) with actual assessment collection rates, inflation assumptions, and investment return scenarios to produce a defensible funding plan recommendation.
**Tags:** #gradient-boosting #linear-regression #time-series-forecasting #feature-engineering #sequences-and-series #arithmetic-and-basic-algebra #compliance #automation

## The Problem

HOAs are required in most states to maintain adequate reserve funds for major component replacement (roofing, parking lot, pool equipment, painting). A reserve study — conducted by a professional reserve study specialist — inventories all major components, estimates remaining useful life, and projects replacement cost and funding need. HOA managers receive this reserve study and must translate it into an assessment funding plan, but the financial modeling — computing the required monthly per-unit assessment increase to reach full funding within the statutory horizon — requires projections that most HOA managers either do manually in Excel or defer to the reserve study specialist.

## What Already Exists

Professional reserve study software (Superstudio, Reserve Data Analyst) is used by reserve study companies. The output is a report, not an integrated planning tool. Individual board members and managers model scenarios in Excel.

## The Customisation Gap

A reserve planning tool for HOA managers needs: (1) import of the reserve study component inventory (component name, current balance, remaining life, projected replacement cost); (2) a funding model that computes the required assessment increase under different funding strategies (threshold funding, percent funded, full funding); (3) scenario modeling (what if replacement costs are 10% higher due to inflation? what if assessments can only increase 3% per year?); (4) a board-ready presentation of the funding plan with clear language about the consequences of underfunding. The reserve study import parsing (extracting structured component data from PDF reserve studies) is the LLM-powered component that enables the planning tool to work without manual data entry.

## Impact If Solved

Enables HOA managers to produce reserve funding analysis that previously required engagement of a financial consultant. Enables boards to make informed assessment decisions rather than defaulting to the lowest politically acceptable increase.
