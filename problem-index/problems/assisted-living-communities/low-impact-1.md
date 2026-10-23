# Apartment Revenue Management Fitted to Care Fees and Length of Stay

**Industry:** [[assisted-living-communities|Assisted Living Communities]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Revenue management software prices apartments well, but an assisted living unit is a two-part price (rent plus a care fee) sold to a resident who stays about two years and leaves for reasons rent tools never model.
**Tags:** #time-series-forecasting #gradient-boosting #survival-analysis #causal-inference #feature-engineering #revenue-impact #data-integration

## The Problem
Every month a sales director and the regional VP decide the street rate for each vacant unit type, which move-in incentives to offer, and how large the annual increase on in-place residents should be. In many chains the rate sheet still comes from a spreadsheet, a competitor call-around and the regional VP's instinct. The decision matters more as occupancy recovers: NIC MAP put assisted living at 89.1% in Q3 2026, up from 88.3% a quarter earlier, and the large REITs credit pricing teams with their gains. Ventas's CEO credits "VentasOI" with the "calibration of rate and occupancy", and Welltower's senior housing RevPOR grew 5.2% in Q2 2026. Price too low and a full building leaves money on the table for two years. Raise the annual increase too far and families move residents out, or complain to the state and the press.

## What Already Exists
Multifamily revenue management, such as RealPage's and Yardi's pricing engines (named from recall), forecasts demand by unit type and recommends daily asking rents and renewal offers from lease-expiration curves and competitor rents. Some senior living suites include rate tables, and NIC MAP sells market occupancy and asking-rent data. These tools assume a 12-month lease, rent as the whole price, and a tenant who leaves when the lease ends or a cheaper apartment appears.

## The Customisation Gap
Assisted living breaks each assumption. Revenue per unit is base rent plus a level-of-care fee, a second-person fee and a one-time community fee, and the care fee moves with the resident's health, not the market. Stays end mostly through death, hospital stays or moves to a higher level of care, so move-out risk depends on acuity as much as price. Families decide within a few weeks of a crisis, often through a referral agency whose fee changes the margin on that move-in. Annual increases land on everyone at once, often in January. An adapted tool needs care-level revenue in its unit economics, survival models of length of stay by acuity, referral-source cost per move-in, and a measured link between the size of an increase and move-outs in the following 90 days. Medicaid waiver units at fixed state rates sit outside the pricing logic entirely.

## Impact If Solved
For an 80-unit community billing ~$5.3M a year (estimate), a 1% gain in revenue per occupied unit is ~$53,000 a year, and avoiding two price-driven move-outs saves ~$12,000–25,000 in vacancy and referral fees (estimate). The regional VP gets a rate sheet she can defend to an owner and a family alike.
