# Rewards Liability and Redemption Cost Forecasting

**Industry:** [[credit-card-issuers|Credit Card Issuers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Loyalty platforms and generic forecasting tools can count points earned; neither can tell a card issuer what an outstanding point will actually cost by the time it is redeemed, transferred or forfeited.
**Tags:** #survival-analysis #time-series-forecasting #bayesian-inference #gradient-boosting #evaluation-metrics #revenue-impact #data-integration

## The Problem
Rewards cards carry 92% of general-purpose purchase volume (CFPB, 2024 data), and every point an issuer awards is a liability booked at its expected cost. That cost is not a constant. A point redeemed as statement credit typically costs about one cent; transferred to an airline or hotel partner it costs whatever the issuer pays that partner per unit; redeemed through a travel portal it costs the booking less any portal margin; never redeemed at all it costs nothing. The rewards finance team has to estimate, every quarter, how much of the outstanding balance will be redeemed, when, and through which channel — and the estimate moves the issuer's reported revenue, because rewards cost is booked against interchange.

The estimate is usually a spreadsheet. Breakage is set from historical averages by product, redemption mix is assumed from last year's share, and partner costs are applied at contract rates. When a cohort of cardholders behaves differently — a new premium card whose holders transfer far more than expected, a devaluation announcement that triggers a run of redemptions before the change — the true-up lands in a later quarter as a surprise.

## What Already Exists
Loyalty platforms such as Kobie, Ascenda, Augeo and the networks' own rewards services run accrual, catalogues and redemption; travel portals and transfer partners settle through them. Generic forecasting and planning tools (Anaplan, Oracle and SAP planning modules, Python forecasting libraries) project balances. Airline and hotel loyalty programmes have long used actuarial breakage models for their own miles and points.

## The Customisation Gap
The issuer-specific logic is what the generic tools miss: redemption propensity that depends on the card product, balance size, tenure, revolving status and whether the cardholder has ever transferred; transfer-partner economics that differ by partner and change on contract renewal; transfer bonuses and portal promotions that pull redemptions forward; the link between redemption and attrition (cardholders often redeem before closing an account); co-brand programmes where the currency belongs to the partner and the issuer buys it; and the accounting treatment that books expected cost at the moment of earn. A useful model joins earn, burn, account and partner data at cardholder level and forecasts cost per point by cohort, not a single breakage rate per product.

## Impact If Solved
A cardholder-level forecast of redemption timing and channel turns the quarterly true-up from a surprise into a known variance, lets the issuer test an earn or burn change before announcing it, and on a premium portfolio, where rewards cost runs at ~1.5–2.5% of spend against interchange of ~2% (estimate), most of the interchange is already committed to rewards — so a forecasting error of 5 basis points of spend on $100B of annual purchases is ~$50M (estimate).
