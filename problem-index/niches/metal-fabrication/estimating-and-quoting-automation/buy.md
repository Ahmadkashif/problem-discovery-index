# Quote Management with Actual-vs-Estimated Feedback Loop

**Niche:** [[niches/metal-fabrication/estimating-and-quoting-automation/profile|Estimating & Quoting Automation]]
**Industry:** [[industries/metal-fabrication|Metal Fabrication]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** CRM and quoting tools like JobBOSS and Salesforce track quote status (sent, won, lost), but don't close the feedback loop — comparing the quoted price to the actual job cost after completion to tell the estimator where their assumptions were wrong.
**Tags:** #gradient-boosting #evaluation-metrics #revenue-impact #automation

## The Problem
A fabrication shop sends 200 quotes per month and wins 40-60 jobs. Each quote contains the estimator's assumptions about labor hours, material cost, and overhead. When the job completes, the actual cost is known — but at most shops, nobody compares quoted cost to actual cost at the job level. The estimator moves on to the next quote without learning whether their estimate was accurate. Systematic errors — consistently under-estimating setup time on new part numbers, or over-estimating material waste on nesting-optimized parts — persist for years because the feedback loop doesn't exist.

## What Already Exists
JobBOSS, E2 Shop System, and Prodsmart capture both quoted and actual job costs in their ERP databases. CRM platforms (Salesforce, HubSpot) track quote activity and win rates. These systems store the data needed for a feedback loop but don't present it in a way that an estimator can act on — the actual-vs-quoted comparison requires custom reports that most shops never build.

## The Customization Gap
An estimating feedback system needs: (1) automatic actual-vs-quoted comparison — when a job completes, display the quoted hours vs. actual hours per operation, quoted material vs. actual material, and quoted vs. actual total cost; (2) trend analysis by job type — aggregating actual-vs-quoted data across dozens of jobs to identify systematic estimating biases by job category (e.g., "on plate-heavy weldments over 500 lbs, you under-estimate fit-up time by an average of 18%"); (3) quote win/loss analysis linked to pricing — showing whether lost quotes were priced above or below the shop's actual cost, distinguishing "lost because overpriced" from "lost for non-price reasons"; (4) estimating accuracy scorecard — tracking the estimator's accuracy over time as a KPI.

## Target Customer
Estimators and shop owners at fabrication shops with ERP systems that capture both quoted and actual job costs but don't have a systematic feedback mechanism.

## Impact If Solved
Creates the feedback loop that transforms estimating from experience-based art to data-informed practice. Identifies systematic biases that compound across dozens of jobs before detection. For a shop with $10M annual revenue and 5% average margin, correcting a 1.5% systematic under-estimation bias adds $150,000 in annual profit.
