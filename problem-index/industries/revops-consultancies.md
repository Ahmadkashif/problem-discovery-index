# RevOps Consultancies

## Profile
**Category:** Digital Professional Services
**Market Size:** ~$6B US in revenue operations advisory, systems work and fractional RevOps staffing, a category that barely existed a decade ago and now sits between sales operations, marketing operations and finance
**Tech Maturity:** Sophisticated stack, unexamined outputs. These firms configure CRM, marketing automation, CPQ, attribution and forecasting across a client's revenue systems, and the two artefacts they are ultimately judged on — the pipeline forecast and the attribution model — are both produced by methods nobody grades against what actually happened.
**Workforce:** RevOps consultants and architects, systems administrators across CRM and marketing automation, analytics and reporting specialists, fractional RevOps leaders, data engineers

## Key Pain Themes
The deliverable is a set of recommendations — change this process, restructure these territories, adopt this forecast method, instrument the funnel this way — handed to a client whose pipeline performance over the following year is the only meaningful test of them. The consultancy is not there for the year. So a firm that has redesigned sixty go-to-market operations cannot say which of its recommendations improved anything, and the next engagement is argued from experience and conviction.

The forecast is the sharpest instance. Forecast accuracy is the single most requested improvement in this discipline, and almost no organisation retains its historical forecasts in a form that permits scoring them. The forecast is produced weekly, presented, and overwritten. The number that would tell everyone whether the new methodology helped is destroyed by the process that produces it.

Underneath sits the data. Every recommendation depends on CRM data whose quality is poor in specific, well-known and rarely-measured ways: stages advanced to satisfy a manager rather than to describe reality, close dates pushed by a fortnight indefinitely, opportunities created to hit an activity target. Consultants know this, work around it, and rarely quantify it — which means models built on it inherit the distortion silently.

## Current Tech Landscape
Salesforce and HubSpot dominate the CRM layer, with Marketo, Pardot and HubSpot on marketing automation. Forecasting and revenue intelligence come from Clari, Gong, BoostUp and InsightSquared. CPQ from Salesforce, DealHub or Conga. Data enrichment from ZoomInfo, Clearbit and Apollo. Attribution is contested ground occupied by Bizible, HockeyStack, Dreamdata and a warehouse-native approach. Reverse ETL and the warehouse-first pattern have moved much of the modelling out of the CRM, which is architecturally better and has not changed whether anyone checks the outputs.

## Problems
- [[problems/revops-consultancies/high-impact|🔴 High Impact: The Forecast Is Produced Weekly and Scored Never]]
- [[problems/revops-consultancies/low-impact-1|🟡 Low Impact: CRM Data Quality as a Measured Quantity]]
- [[problems/revops-consultancies/low-impact-2|🟡 Low Impact: Territory and Quota Design]]
- [[problems/revops-consultancies/worker-life-1|🟢 Worker Life: The Consultant Rebuilding the Same Funnel Model]]
- [[problems/revops-consultancies/worker-life-2|🟢 Worker Life: The Sales Ops Analyst Preparing the Forecast Call]]
- [[problems/revops-consultancies/ml-opportunity|🧠 ML Opportunities]]
- [[problems/revops-consultancies/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Revenue operations exists to make a company's revenue predictable, and the discipline's own central artefact is unscored almost everywhere it is produced. That is a remarkable state for a function staffed by quantitative people inside organisations that measure everything else, and the reason is mundane: the forecast is a snapshot in a spreadsheet or a CRM field that is overwritten each week, so the historical series required to grade it never exists. Creating that series is a week of engineering and it is the precondition for every other improvement this discipline claims to offer — because until forecasts are scored, a new methodology cannot be shown to be better than the one it replaced, and the consultancy selling it cannot demonstrate anything at all.
