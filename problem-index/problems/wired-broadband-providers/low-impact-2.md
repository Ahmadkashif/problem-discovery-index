# Save Offers at Promo Roll-Off

**Industry:** [[wired-broadband-providers|Wired Broadband Providers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every month a cohort of households sees its promotional rate expire, and the retention offer each one gets is set by a generic churn score that doesn't know whether fixed wireless or fibre is actually available at that address.
**Tags:** #gradient-boosting #survival-analysis #causal-inference #feature-engineering #evaluation-metrics #revenue-impact #data-integration

## The Problem
Residential broadband is sold on 12- to 24-month promotional prices (estimate). When the promotion ends, the bill jumps, and a share of customers call to cancel or simply leave. The save desk has a menu of offers — a new promotion, a speed upgrade, a mobile bundle, a price lock — and a target for saves. Offers are expensive: a discount given to a household that was never going to leave is margin thrown away, and one withheld from a household with a cheaper alternative at the door is a lost subscriber.

The alternatives are not uniform. Fixed wireless from T-Mobile and Verizon is available at some addresses and not others, depending on sector capacity; a fibre overbuilder may be live on one street and still under construction on the next. Leichtman Research Group found fixed wireless accounted for roughly 104% of US net broadband additions in 2023, with top cable operators losing subscribers; Charter lost 119,000 Internet customers in Q4 2025. The household's real alternative, not its tenure or its average bill, decides whether an offer is needed.

## What Already Exists
Churn models inside telecom BSS suites (Amdocs, CSG), CRM and marketing automation (Salesforce, Braze), and in-house data science teams at the largest operators. Small and mid-sized operators use billing-system reports of upcoming promo expirations and a save script.

## The Customisation Gap
Generic churn tools predict who is likely to leave; the save decision needs who will leave without an offer and stay with one. The broadband-specific layer is: address-level competitive availability built from public FCC National Broadband Map data (provider, technology and advertised speeds per Fabric location) plus fixed wireless eligibility checks and fibre construction footprints; the promotion and price-lock calendar per account; usage, outage and repeat-ticket history (customers who have had three outages respond to apology credits, not discounts); bundle status with mobile; and the obligations of the federal broadband label on how prices are displayed. With that, offers can be targeted by uplift rather than by risk, and measured against a holdout.

## Impact If Solved
For a cable operator with a million broadband customers, a cohort of tens of thousands rolls off promotion each month (estimate). Moving discount spend from households that would stay anyway to those with a live alternative at the address can cut retention discount cost by a meaningful fraction while holding or improving the save rate, and gives the retention team a defensible reason for each offer.
