# Quoting Drafting Effort From a Bid Set

**Industry:** [[drafting-services|Drafting Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A bureau prices a job per sheet, per ton or per hour from a quick read of the bid drawings, and the quote is the single decision that sets its margin, made from a takeoff tool built to count materials rather than drafting hours.
**Tags:** #gradient-boosting #feature-engineering #object-detection #cnns #loss-functions #cross-validation #revenue-impact

## The Problem
A fabricator sends a steel detailing bureau the structural drawings for a bid: forty sheets, a tonnage estimate and a due date for the quote. An architect sends a design-development set and asks what the construction documents will cost per sheet. A millwork shop sends elevations and asks for a price on shop drawings. The bureau's owner has a day or two to answer, usually alongside production work, and prices the job from experience: how many pieces and connections, how much is skewed or sloped, how many unique details, how complete the design looks, and how much the client usually changes things.

The errors are expensive both ways. Quote high and the job goes to an offshore competitor at half the rate; quote low and the bureau absorbs the overrun, often on a fixed price with one or two revision rounds included. A detailing job that looked like typical framing but turns out to have a hundred unique moment connections or an incomplete design can lose its whole margin before the first submittal.

## What Already Exists
Construction takeoff tools such as Bluebeam Revu's quantity takeoff, PlanSwift, STACK and On Center's On-Screen Takeoff count lengths, areas and items from PDFs for contractors' material and labour estimates. Steel estimating systems such as Tekla PowerFab Estimating and fabricator spreadsheets estimate tonnage and shop hours. Project accounting for small firms (BQE CORE, QuickBooks, Monograph) records hours after the fact.

## The Customisation Gap
None of these estimate drafting effort. The bureau-specific logic is: counting what drives drafting hours rather than material cost — unique piece marks, connection types, typical versus unique details, skews and slopes, sheet count by type, and the proportion of the design that is still clouded or marked "by others"; reading design completeness, since incomplete drawings mean RFIs and rework; adjusting for the client, because some architects and engineers revise far more than others; and converting all of it into the bureau's own pricing units — per sheet, per ton or hourly — with an explicit allowance for revision rounds. The data that would calibrate it already sits in the bureau's own past jobs, as quoted hours against actual hours, and nobody joins them.

## Impact If Solved
A quote built from the bid set's drafting drivers and the bureau's own job history would let a two-person shop answer bids in hours rather than days and stop pricing the jobs it loses money on. Even a modest cut in overrun jobs is material at ~$182,600 of receipts per employee, the 2022 industry average.
