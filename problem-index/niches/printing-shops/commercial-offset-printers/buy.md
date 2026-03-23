# Press-Specific Waste Factor Calibration

**Niche:** [[niches/printing-shops/commercial-offset-printers/profile|Commercial Offset Printers]]
**Industry:** [[industries/printing-shops|Printing Shops]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** MIS platforms (EFI Pace, Avanti) use generic waste factors for estimating (e.g., "add 5% for makeready on 2-color jobs") — but actual waste varies 3-15% depending on press, substrate, color complexity, and operator, and the generic factors systematically over- or under-estimate for specific job types.
**Tags:** #gradient-boosting #revenue-impact #automation

## The Problem
Print estimators add waste factors to net quantity when ordering paper — these factors cover makeready waste, running waste, and finishing waste. MIS platforms provide default waste tables (percentage by number of colors, run length, and press size), but these defaults are generic industry averages that do not reflect the specific shop's equipment and crew performance. A shop running a well-maintained Heidelberg XL 106 with an experienced pressman will waste 30% fewer sheets on makeready than the industry average; a shop with an older Komori and a junior crew will waste 50% more. Using incorrect waste factors causes either paper over-ordering (excess stock, wasted capital) or under-ordering (production shortfall requiring a reprint).

## What Already Exists
EFI Pace, Avanti Slingshot, and PrintSmith include configurable waste tables where estimators can adjust waste percentages by job type. The configuration is manual — the estimator sets waste factors based on their experience and adjusts them when they notice patterns. No MIS automatically calibrates waste factors from actual production data.

## The Customization Gap
The system must connect to the MIS job records (estimated waste vs. actual waste per job, tracked by substrate, press, number of colors, run length, and finishing requirements), compute the actual waste factors for each job type combination, and automatically update the estimating waste tables to reflect the shop's actual performance. It should identify which job types are systematically over-estimated (opportunity to reduce paper ordering cost) and under-estimated (risk of reprint cost), and alert the estimator when a job's waste estimate deviates significantly from the calibrated factor.

## Target Customer
Owners and estimators at commercial offset shops tracking actual production data in their MIS. Approximately 2,000-3,000 US offset shops running EFI Pace or Avanti.

## Impact If Solved
Paper over-ordering decreases by 15-25%, saving $20-50K per year at a mid-size shop. Reprint incidents from under-ordering decrease by 30-50%. Estimating accuracy improves by 3-5% of total job cost, directly improving margin predictability.
