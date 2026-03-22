# PERM Audit Risk Predictor

**Niche:** [[niches/immigration-law/employment-based-visas/profile|Employment-Based Visas]]
**Industry:** [[industries/immigration-law|Immigration Law]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Flag PERM labor certification applications likely to be audited by the DOL before filing — enabling attorneys to strengthen documentation proactively instead of scrambling reactively when an audit letter arrives 6 months later.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #cross-validation #evaluation-metrics #tacit-knowledge-ml #compliance #revenue-impact

## The Problem
PERM labor certification is the most complex and audit-prone step in employment-based green card processing. The employer must prove that no qualified U.S. worker is available for the sponsored position by conducting a structured recruitment campaign, documenting every applicant received, and explaining why each was unqualified. The DOL audits 20-30% of PERM applications, requesting the full recruitment documentation file. An audit adds 6-18 months to the process and can result in denial if documentation is incomplete. Experienced business immigration attorneys have developed tacit pattern recognition for audit triggers: certain SOC codes (e.g., software developers at non-tech companies), wage levels at or near the floor of the prevailing wage range, job requirements that appear tailored to the sponsored worker, and recruitment through only the minimum required channels. But this knowledge is personal — a senior attorney "feels" that a case is high-risk, while a junior attorney files the same application blind. There is no systematic way to quantify audit risk before filing.

## Why Nobody Has Built This
PERM application data is partially public through DOL quarterly disclosure files, but these files contain only approved and denied cases — not audit rates by case characteristics. Building a training dataset requires a law firm or consortium of firms to label their own historical cases as "audited" or "not audited" and share the case characteristics (without PII). No single firm has enough volume for a robust model, and firms are reluctant to share data with competitors. Additionally, DOL audit selection criteria are not published and may change with administration priorities, creating concept drift that requires continuous model retraining. The market (business immigration attorneys) is sophisticated enough to demand explainable predictions — a black-box "high risk" score without feature attribution won't change attorney behavior.

## What to Build
A risk scoring system trained on PERM application features: SOC code, job title, wage level relative to prevailing wage (Level I-IV), industry sector, employer size, job requirements (education, experience, skills), number of recruitment sources used, and geographic labor market conditions. The model (gradient-boosted trees for interpretability) outputs an audit probability score with feature-level explanations ("this application scores 78% audit risk — the primary drivers are: wage at Level I for this SOC code, job requirements include a specific technology stack that closely matches the beneficiary's resume, and only 3 recruitment sources were used vs. the 5+ that reduce audit rates"). Attorneys use the score pre-filing to decide whether to strengthen documentation (add recruitment sources, adjust job requirements, request a higher prevailing wage level) before submitting. A feedback loop where attorneys report actual audit outcomes improves the model over time.

## Target Customer
Business immigration firms filing 50+ PERM applications per year, where each audit consumes 8-20 attorney hours in documentation assembly and response drafting, and a denied PERM restarts a 12-18 month process from scratch.

## Impact If Built
Reduces unexpected audits by enabling proactive documentation strengthening — estimated 30-40% reduction in audit-related rework. For a firm filing 100 PERMs/year with a 25% audit rate, preventing even 10 audits saves 100-200 attorney hours ($30K-60K) and 6-12 months of processing time per avoided audit. Corporate clients receive faster green card processing, improving employee retention during the immigration process.
