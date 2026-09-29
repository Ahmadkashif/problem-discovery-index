# Cloud Cost Management

## Profile
**Category:** Developer Tools & Infrastructure
**Market Size:** ~$3B US cloud financial management and optimisation software
**Tech Maturity:** Crowded and shallow — CloudHealth, Apptio Cloudability, Vantage, CloudZero, Finout and the hyperscalers' native tools all ingest billing data and render it well. The category has converged on reporting the same numbers, and the decisions that actually change spend still require engineers who do not read the reports.
**Workforce:** FinOps practitioners, cloud economists, platform engineers, solutions architects, commitment and contract analysts

## Key Pain Themes
Cloud cost tools tell finance what was spent and cannot tell engineering what to do. The gap is attribution: a bill arrives organised by service and resource, and the questions that matter are organised by team, product, customer and feature — a mapping that depends on tagging discipline nobody has. Around that sit two chronic problems: commitment purchasing, where reserved instances and savings plans require forecasting usage one to three years ahead and the tools recommend from the recent past; and the recommendation credibility problem, where a platform confidently proposes downsizing an instance that is small because it is a standby, and after two such recommendations engineers stop reading them. FinOps practitioners spend their days chasing teams for tags and explaining variances, and engineers experience cost as an intermittent demand to cut something with no way to know what is safe.

## Current Tech Landscape
The hyperscalers' native cost tooling has improved substantially and covers the basics well within a single provider. Third parties differentiate on multi-cloud, Kubernetes attribution and unit economics. Kubernetes cost allocation is a distinct hard problem served by OpenCost and commercial equivalents. Commitment marketplaces and management services have emerged around reserved capacity. The FinOps Foundation has given the discipline a vocabulary and a maturity model. Automated rightsizing and scheduling exist and are adopted cautiously.

## Problems
- [[problems/cloud-cost-management/high-impact|🔴 High Impact: Attribution to Decisions Engineers Can Make]]
- [[problems/cloud-cost-management/low-impact-1|🟡 Low Impact: Commitment Purchasing Under Uncertainty]]
- [[problems/cloud-cost-management/low-impact-2|🟡 Low Impact: Recommendation Credibility]]
- [[problems/cloud-cost-management/worker-life-1|🟢 Worker Life: The FinOps Practitioner Chasing Tags]]
- [[problems/cloud-cost-management/worker-life-2|🟢 Worker Life: The Engineer Told to Cut Costs]]
- [[problems/cloud-cost-management/ml-opportunity|🧠 ML Opportunities]]
- [[problems/cloud-cost-management/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These vendors sit across the infrastructure spend of thousands of organisations and observe what everyone actually runs, at what utilisation, on which instance families, with which commitment coverage, at what effective rate after discounts. That is a cross-organisational benchmark nobody else holds: what a workload of this shape should cost, and what comparable companies pay. The category instead resells the customer's own bill back to them in a nicer interface, which is why every product in it looks the same.
