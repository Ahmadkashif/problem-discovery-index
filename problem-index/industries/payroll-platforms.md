# Payroll Platforms

## Profile
**Category:** Horizontal SaaS
**Market Size:** ~$30B US payroll processing and services
**Tech Maturity:** Extremely high reliability, extremely low visibility — ADP, Paychex, Gusto, Rippling, Paycom and Paylocity move a substantial share of American wages. The engineering is genuinely hard and almost entirely invisible until it fails, at which point it is the most consequential software failure a company can experience.
**Workforce:** Tax research and filing analysts, implementation specialists, payroll operations staff, garnishment processors, compliance engineers, support representatives

## Key Pain Themes
There are more than eleven thousand US taxing jurisdictions, each with its own rates, wage bases, reciprocity rules, deposit schedules and filing formats, and they change constantly. Getting them right is the product; getting one wrong produces penalties, amended returns and a company discovering it under-withheld for a year. The rules that turn hours into gross pay are almost as fragmented — overtime calculation, meal and rest break premiums, shift differentials and the regular rate of pay differ by state and are frequently misconfigured. Garnishments are a compliance minefield handled largely by hand, with priority rules, disposable income calculations and state exemption limits that vary. All of it lands on a fixed calendar: payroll runs on Friday whether or not anything is ready, and a missed direct deposit is an emergency for a household, not a ticket.

## Current Tech Landscape
ADP and Paychex hold the largest installed bases with deep tax filing infrastructure built over decades. Gusto and Rippling have grown by making the small-employer experience genuinely good. Paycom and Paylocity serve the mid-market. Tax content is the moat and is maintained by in-house research teams at the large providers and licensed by smaller ones. Time and attendance is a separate but tightly coupled category. Earned wage access has grown quickly as an adjacent product. Filing and remittance infrastructure is largely invisible and largely uncontested.

## Problems
- [[problems/payroll-platforms/high-impact|🔴 High Impact: Multi-Jurisdiction Tax Determination and Filing]]
- [[problems/payroll-platforms/low-impact-1|🟡 Low Impact: Time to Gross Pay Rule Configuration]]
- [[problems/payroll-platforms/low-impact-2|🟡 Low Impact: Garnishment Order Processing]]
- [[problems/payroll-platforms/worker-life-1|🟢 Worker Life: Payroll Specialist Friday Close]]
- [[problems/payroll-platforms/worker-life-2|🟢 Worker Life: Support During a Missed Deposit]]
- [[problems/payroll-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/payroll-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Payroll providers hold the highest-frequency, highest-coverage economic dataset in the country: actual wages paid, hours worked, jurisdiction, industry and employer size, updated every pay period across tens of millions of workers. Federal statistics on employment and earnings are published monthly from surveys with substantial revisions. The providers know the answer in near real time and publish, at most, a quarterly index as marketing. The gap between what they measure and what they say is larger than in any other category in this vault.
