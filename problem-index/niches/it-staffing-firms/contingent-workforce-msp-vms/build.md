# Rate Cards Set From Survey Data When the Market Is in the System

**Niche:** [[niches/it-staffing-firms/contingent-workforce-msp-vms/profile|Contingent Workforce MSP & VMS Programmes]]
**Industry:** [[industries/it-staffing-firms|IT Staffing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The programme sets rates from published benchmarks while holding every submission, every fill, and every declined offer in the market.
**Tags:** #gradient-boosting #survival-analysis #tabular-ml #evaluation-metrics #revenue-impact

## The Problem
A contingent programme's core commercial instrument is the rate card: for each skill and level, the maximum bill rate suppliers may submit. Set it too high and the client overpays across thousands of engagements. Set it too low and requisitions do not fill, and the hiring manager goes around the programme.

Rate cards are set from published benchmark surveys and periodic negotiation. Pass 1 describes the same problem from the supplier side — rate management is spreadsheet-driven and margins erode when recruiters misprice niche skills or miss market shifts.

The programme is the one party that does not need a survey. It holds every requisition, every supplier submission with its proposed rate, every fill and its final rate, every rejection, and every requisition that aged out unfilled. That is the demand curve, measured continuously, at skill and geography level. It is used to check whether submissions comply with the card.

So the card is a price control set from lagging external data, applied to a market the programme is observing in real time and not reading.

## Why Nobody Has Built This
The programme's mandate is savings and compliance, and both are measured against the card. Rate card adherence is a reportable metric; whether the card is set correctly is not, and a programme reporting 97% compliance against a card that is 15% too low looks excellent while quietly failing to fill.

Unfilled requisitions also disappear. A req that ages out is closed, and nobody attributes it to the rate. The cost of a card set too low is invisible by construction, while the cost of one set too high shows up immediately in spend reporting — so the incentive is asymmetric and pushes one way.

And rate setting is a negotiation ritual. Cards are agreed periodically with the client's procurement function using external benchmarks, because external benchmarks are what both sides accept as neutral.

## What to Build
A fill-probability model that turns the card from a fixed price into a demand curve.

**Model fill probability as a function of rate.** For a given skill, level, location, and requisition urgency, what proportion of requisitions fill within the target window at each rate point? Every input is in the system and the outcome is observed on every requisition.

**Report the cost of the ceiling.** Requisitions that failed to fill, and the estimated rate at which they would have, is the number nobody produces. It converts an invisible cost into a reported one, which is the whole change.

**Detect market movement in weeks, not survey cycles.** Rising submission rates, falling submission volumes, and lengthening time to fill in a skill are the leading indicators, and they are visible in the programme's own flow long before any benchmark publishes.

**Estimate supplier-level effects properly.** Which suppliers actually fill hard requisitions, controlling for which requisitions they were shown — because supplier performance is confounded by distribution, and the programme controls distribution.

**Price the tail explicitly.** Common skills are well benchmarked; scarce ones are where the money is lost in both directions, and they are precisely where survey data is thinnest and the programme's own observations are the only evidence.

## Target Customer
Chief Data Officer or SVP of Programme Analytics at an MSP or VMS provider. The client-facing argument is strong: savings reported against a card is a weak claim, and a programme that can show it optimized fill rate against cost is offering something no competitor currently quantifies.

## Impact If Built
Contingent labour is a very large line of enterprise spend governed by a price control set from lagging surveys. Fitting the card to observed fill behaviour improves both sides of the trade — fewer requisitions dying quietly at a rate nobody would accept, and less overpayment on skills the market has repriced downward — and it is computable today from data the programme already owns.
