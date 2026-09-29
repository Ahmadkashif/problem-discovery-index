# Buy: HR Analytics Platforms Adapted to a Validation Study

**Niche:** [[niches/talent-assessment-platforms/local-criterion-validity/profile|Local Criterion Validity]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** People analytics platforms hold the outcome data and report dashboards; a validation study is a specific statistical procedure with a selection problem they do not model.
**Tags:** #causal-inference #maximum-likelihood-estimation #confidence-intervals #evaluation-metrics #hypothesis-testing #data-integration #compliance #descriptive-statistics
**Contested on:** Whether people analytics tooling can carry a psychometric validation rather than a dashboard.

## The Problem

People analytics is a real category. Platforms consolidate HRIS, ATS, performance and engagement data, and report on hiring funnels, attrition, performance distributions and diversity metrics. Large employers run them and the data for a validation study is sitting inside.

They are reporting tools. A criterion validation is a statistical procedure with a specific structure — a correlation between a predictor and a criterion, corrected for the fact that the predictor determined who is in the sample — and none of the platforms implements it, because it is a psychometric method rather than an HR metric.

## What Already Exists

Visier, Workday People Analytics, One Model and the people analytics category. HRIS and ATS integrations. Performance and compensation data models. Diversity and funnel reporting. Statistical packages that implement the psychometric corrections, in the hands of specialists who are not in the HR analytics team.

## The Customization Gap

**The assessment score is not in the data model.** People analytics platforms consolidate HR systems; assessment scores live with the vendor or in an ATS field nobody maps. Getting the predictor into the warehouse, linked to the person and the requisition, is the first and most mundane obstacle.

**Range restriction correction is the method and no platform has it.** Computing a correlation is trivial; computing the one that means something requires a correction the HR analytics world does not know about. This single procedure is the difference between a misleading answer and a useful one.

**The criterion has to be constructed and questioned.** Performance ratings exist in the platform as a field. Using them as a validity criterion requires understanding their rater effects, their inflation, their bias and their relationship to anything objective — a level of scepticism about their own data that HR analytics platforms are not built to encourage.

**The analysis is longitudinal with censoring.** Outcomes accrue over time; people leave; cohorts are incomplete. Survival methods rather than cross-sectional correlations handle tenure and progression properly, and the reporting tools are cross-sectional by design.

**The output is evidence, not a dashboard.** A validation result may be produced in response to legal scrutiny or used to justify continuing to use an instrument. It needs documented methodology, stated assumptions, reproducibility and versioning — a study, with the standards a study carries.

## Target Customer

Large employers' people analytics and assessment functions, who hold the data and need to know what the platform does not do. Also the people analytics vendors, for whom assessment validation is a high-value analysis their customers cannot currently run, and the established test publishers supporting client validations.

## Impact If Solved

The data consolidation, HRIS integration and reporting infrastructure gets reused, and the assessment score ingestion, range restriction correction, criterion scepticism, longitudinal treatment and study-grade documentation get built. Concretely: an employer can run a credible validation on their own data without hiring a consultancy for six months.
