# Immigration Practice Profitability Dashboard

**Niche:** [[niches/small-law-firms/immigration-boutiques/profile|Immigration Boutiques]]
**Industry:** [[industries/small-law-firms|Small Law Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Tracks revenue per case type (H-1B vs. family-based vs. asylum), actual time invested against flat fees, paralegal utilization, and RFE rates as a quality metric — giving the immigration firm owner the first-ever view of which case types make money and which are subsidized by the profitable ones.
**Tags:** #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #descriptive-statistics #data-integration #revenue-impact #tacit-knowledge-ml

## The Problem
Immigration boutique owners set flat fees based on market rates and gut feeling: "H-1B petitions go for $3,500-5,000 in our market." They have no data on their actual cost to deliver each case type. An H-1B petition that goes smoothly might take 8 attorney hours and 12 paralegal hours — a profitable engagement at $4,000. But an H-1B that receives an RFE might take 15 attorney hours and 25 paralegal hours — a money-loser at the same fee. Asylum cases are even more variable: some resolve with a 20-page declaration and one hearing, while others require years of preparation, expert witnesses, and multiple continuances. Experienced immigration firm owners develop tacit intuition about case profitability — "I can feel when an H-1B is going to be complicated" — but this intuition is unreliable, biased toward memorable bad outcomes, and impossible to transfer to a new practice owner or associate.

## Why Nobody Has Built This
Immigration firms don't track time because they bill flat fees. Without time tracking, there's no data to analyze. But time tracking in a flat-fee practice feels pointless to the staff ("why am I recording time if we're not billing for it?"). Building a profitability dashboard requires either (1) introducing lightweight time tracking that staff will actually adopt (a major behavioral change), or (2) inferring time investment from proxy signals (INSZoom activity logs, email volume per case, document drafting sessions, portal interactions). The second approach is technically harder but operationally viable. Additionally, immigration case management and practice management data live in separate systems (INSZoom and Clio) with no standard integration, making cross-system analytics a data engineering challenge.

## What to Build
A profitability intelligence platform that combines data from INSZoom/Docketwise (case type, milestones, RFE status, filing dates) with Clio (financial data, time entries if available, trust account activity) and ambient activity signals (email volume per case, document creation, portal activity) to estimate actual time and cost per case. A gradient-boosted model trained on completed cases predicts total cost-to-deliver for new matters based on case characteristics (visa type, employer size, nationality, RFE risk factors) and paralegal assignment. The dashboard surfaces: profitability by case type (revenue minus estimated cost), paralegal utilization and quality scores (RFE rate by preparer), case portfolio balance (percentage of cases in profitable vs. marginal vs. unprofitable categories), and forecasted revenue with timing uncertainty (immigration case timelines are inherently unpredictable).

## Target Customer
Immigration boutique owners (1-3 attorneys) billing $500K-3M annually in flat fees, who suspect some case types are unprofitable but have no data to confirm or quantify the problem.

## Impact If Built
Enables immigration firm owners to adjust flat fees, decline unprofitable case types, or restructure staffing to improve margins. Firms that achieve visibility into case-level profitability typically improve margins by 15-25% within 12 months through pricing adjustments and case mix optimization. For a $1.5M firm, that's $225K-375K in additional profit without additional revenue. RFE rate tracking by preparer also enables quality improvement — reducing RFE rates from 25% to 15% saves $2K-5K per avoided RFE in rework costs.
