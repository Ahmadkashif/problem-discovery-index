# Closing Date Misses from Appraisal and Title Delays

**Niche:** [[niches/mortgage-brokers/purchase-residential-brokers/profile|Purchase-Focused Residential Brokers]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Purchase transactions miss closing dates 15-20% of the time, and the two leading causes — appraisal delays and title clearance issues — are discovered too late because brokers have no visibility into third-party vendor timelines.
**Tags:** #time-series-forecasting #regression #tabular-ml #revenue-impact

## The Problem
A purchase contract specifies a close date 30 days out. The broker orders an appraisal on day 3 and expects it back in 7-10 days. On day 18 — with 12 days to close — the appraisal still hasn't arrived. The broker calls the AMC (appraisal management company) and learns the appraiser is backed up and won't deliver for another 7 days. With the appraisal arriving on day 25, the broker has 5 days to clear appraisal conditions, issue the closing disclosure (3-day waiting period required), and coordinate with the title company — mathematically impossible. The close date is missed. The real estate agent is furious. The borrower's rate lock may expire.

## Why It's Still Broken
Brokers have zero visibility into third-party vendor timelines. AMCs don't provide real-time status updates — the broker must call to check. Title companies operate on their own timelines. Employment verification services respond when they respond. The broker assumes normal turn times and only discovers delays when they follow up — often too late. No tool tracks historical vendor performance (this AMC averages 12 days in this zip code, not the 7 they quote) or alerts when a specific vendor engagement is exceeding expected timelines.

## What a Fix Looks Like
A third-party vendor timeline tracker that: (1) logs when each vendor service is ordered (appraisal, title search, employment verification, insurance binder); (2) predicts expected completion date based on historical performance data for that specific vendor in that geographic area; (3) alerts the loan officer when a vendor engagement exceeds the predicted timeline — "Appraisal ordered 10 days ago; this AMC averages 9 days in this zip code — follow up now"; (4) computes the impact on close date feasibility: "If appraisal arrives tomorrow, you have 14 days to close — feasible. If it takes 5 more days, close date will slip." Enables proactive intervention instead of reactive discovery of delays.

## Who Feels the Pain
Loan officers who discover third-party delays too late to prevent close date misses, processors who spend 20-30% of their time on "status check" calls to vendors, and borrowers who face the stress and potential financial consequences of missed closing dates.

## Impact If Fixed
Reduces close date misses from appraisal/title delays by 40-60% through early detection and proactive intervention. Saves processors 5-10 hours per week on vendor status check calls by providing automated timeline monitoring. Protects real estate agent referral relationships — the primary lead source for purchase-focused brokers — by delivering on close date commitments.
