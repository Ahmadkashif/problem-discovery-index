# Energy Auditors

## Profile
**Category:** Energy
**Market Size:** ~$5B US energy audit and weatherization market
**Tech Maturity:** Low-Medium — TREAT, OptiMiser, and Ekotrope handle energy modeling; field data collection still relies on clipboards, generic photo apps, and manual entry into audit software
**Workforce:** BPI- and RESNET-certified energy auditors, field technicians, report writers, and sales reps who convert audit findings into retrofit proposals

## Key Pain Themes
Auditors collect 200+ data points per residential visit — blower door readings, combustion safety tests, insulation depths, window types, duct leakage, appliance specs — then manually enter everything into modeling software to produce savings estimates. The translation from raw field observations to calibrated energy models is where most errors and time waste occur: auditors rely on professional judgment to fill gaps the software cannot see, but that judgment is invisible to downstream quality assurance. Utility incentive programs shift constantly across jurisdictions, and matching a specific building's retrofit measures to available rebates requires tracking dozens of overlapping program rules. Report formatting varies by standard (HERS, BPI, ASHRAE Level I/II/III), and auditors spend hours reformatting the same data for different audiences.

## Current Tech Landscape
TREAT and Ekotrope are the leading residential energy modeling tools, with manual data entry as the primary input method. Infrared cameras (FLIR, Seek) capture thermal images but require expert interpretation — there is no automated deficiency detection. CRM and scheduling tools are generic (Jobber, Housecall Pro) with no audit-specific workflow integration, and utility rebate databases (DSIRE, EnergySage) are reference-only with no automated matching to specific building conditions.

## Problems
- [[problems/energy-auditors/high-impact|🔴 High Impact: Building Energy Model Calibration from Audit Data]]
- [[problems/energy-auditors/low-impact-1|🟡 Low Impact: Audit Report Generation Across Standards]]
- [[problems/energy-auditors/low-impact-2|🟡 Low Impact: Utility Incentive and Rebate Matching]]
- [[problems/energy-auditors/worker-life-1|🟢 Worker Life: Field Data Collection Tedium]]
- [[problems/energy-auditors/worker-life-2|🟢 Worker Life: Scheduling and No-Show Management]]
- [[problems/energy-auditors/ml-opportunity|🔵 ML Opportunities]]
- [[problems/energy-auditors/ai-agents-platforms|🤖 AI Agents & Platforms]]
