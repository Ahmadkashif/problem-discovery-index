# Appraisal Compliance Checker Adapted for FHA/VA MPS

**Niche:** [[niches/mortgage-brokers/fha-va-government-brokers/profile|FHA/VA Government Lending Brokers]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic appraisal review tools check USPAP compliance but don't flag FHA Minimum Property Standards or VA-specific appraisal deficiencies that cause government loan delays.
**Tags:** #bert #text-classification #nlp #compliance #automation

## The Problem
FHA and VA appraisals must meet agency-specific property standards that go far beyond conventional appraisal requirements — FHA requires functioning heating, adequate roofing, safe water supply, and absence of lead paint hazards (pre-1978 homes); VA adds specific requirements around pest inspection, property access, and mechanical systems. When an appraiser misses an MPS deficiency or notes it ambiguously, the file gets stuck in a compliance loop that delays closing by 2-4 weeks. Brokers currently read every appraisal report manually to catch these issues before submission.

## What Already Exists
Appraisal review tools like Mercury Network, Reggora, and CoreLogic's appraisal products provide USPAP compliance checking, comparable analysis, and basic data validation. These tools flag conventional appraisal issues (comp distance, adjustment thresholds, form completeness) but don't apply FHA/VA-specific property standard checks against the narrative sections of the appraisal report.

## The Customization Gap
FHA MPS and VA MPR violations are described in free-text narrative sections of the appraisal report — phrases like "evidence of peeling paint on exterior trim" or "crawl space ventilation appears insufficient" that signal compliance failures requiring repair prior to close. An NLP layer needs to parse these narratives against the specific FHA/VA property standard checklists, flag violations, classify severity (required repair vs. cosmetic observation), and generate the exact HUD repair requirement reference for the loan officer.

## Target Customer
Government lending brokers and their processors who review 10-30 FHA/VA appraisals per month and spend 20-30 minutes per report checking for MPS/MPR compliance issues that generic tools miss.

## Impact If Solved
Catches MPS/MPR violations before lender submission, reducing appraisal-related conditions and delays by an estimated 50%. Saves 15-20 minutes per appraisal review and eliminates the risk of late-stage surprises where a repair requirement surfaces during underwriting.
