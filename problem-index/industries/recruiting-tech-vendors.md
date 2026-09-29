# Recruiting Tech Vendors

## Profile
**Category:** Platform Labour & Digital Work
**Market Size:** ~$12B US in applicant tracking, sourcing, candidate relationship management and recruiting automation; Workday, SAP SuccessFactors, Greenhouse, Lever, Ashby, iCIMS and the sourcing layer of LinkedIn, SeekOut and hireEZ hold most of it
**Tech Maturity:** Comprehensive workflow, absent evaluation. These systems record every application, every screen, every rejection and every hire, across millions of decisions, and none of them grade the decisions. Matching models trained on this data learn to reproduce recruiter behaviour, which is the well-documented failure the field already has a canonical example of.
**Workforce:** Recruiters and sourcers, coordinators, talent operations and systems administrators, hiring managers, and the candidates on the other side of the process

## Key Pain Themes
The system records rejections and never learns from them. Nobody knows whether a rejected candidate would have succeeded, because they were not hired, so any model trained on this data learns which candidates recruiters selected rather than which candidates would have performed. Amazon's abandoned resume-screening tool is the canonical public example — a model trained on historical hiring that reproduced the pattern in that history — and the structural condition that produced it is present in every system in this category.

The second theme is volume without signal. Application volume per opening has risen sharply, partly because applying became trivial and more recently because generative tooling makes tailored applications cheap to produce. Recruiters respond by screening faster and by leaning harder on filters, which raises the false rejection rate on exactly the candidates whose value is not legible in a keyword.

The third is the candidate's experience of it. Applications disappear without response, status is unknowable, and rejection arrives late or never. That is a well-documented and universal complaint, it is entirely a workflow choice, and it degrades the applicant pool for the employers who do it worst.

## Current Tech Landscape
Applicant tracking systems from Workday, SuccessFactors, Greenhouse, Lever, Ashby, iCIMS and Taleo hold the pipeline. Sourcing runs on LinkedIn Recruiter, SeekOut, hireEZ and Gem. Scheduling automation, assessment integrations and interview intelligence from BrightHire and Metaview sit around them. Matching and ranking features are increasingly built in and their provenance is inconsistently disclosed. Regulatory attention to automated employment decision tools — New York City's bias audit requirement and the broader direction elsewhere — now reaches features that were previously shipped as convenience.

## Problems
- [[problems/recruiting-tech-vendors/high-impact|🔴 High Impact: The System Records Every Rejection and Learns From None of Them]]
- [[problems/recruiting-tech-vendors/low-impact-1|🟡 Low Impact: Sourcing, Search and Application Volume]]
- [[problems/recruiting-tech-vendors/low-impact-2|🟡 Low Impact: Interview Scheduling and Coordination]]
- [[problems/recruiting-tech-vendors/worker-life-1|🟢 Worker Life: The Recruiter With Forty Open Requisitions]]
- [[problems/recruiting-tech-vendors/worker-life-2|🟢 Worker Life: The Candidate Who Never Hears Back]]
- [[problems/recruiting-tech-vendors/ml-opportunity|🧠 ML Opportunities]]
- [[problems/recruiting-tech-vendors/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Recruiting technology holds the largest record of hiring decisions ever assembled and has no mechanism for establishing whether any of them were correct. The counterfactual is structurally unavailable — a rejected candidate generates no performance data — which means the honest position is that the sector cannot validate its matching claims and should say so rather than training models on recruiter agreement and calling it fit. There are partial routes: hires can be evaluated, rejections can be audited by re-review, and selective randomisation at the margin of a screening threshold would produce genuine evidence at a cost most employers could absorb. None are standard practice. Until one of them is, every ranking feature in this category is a model of past recruiter behaviour, and the field already knows what that produces.
