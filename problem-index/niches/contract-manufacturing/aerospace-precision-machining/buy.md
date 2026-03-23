# AS9100-Aware SPC Module for Job Shop ERP

**Niche:** [[niches/contract-manufacturing/aerospace-precision-machining/profile|Aerospace Precision Machining]]
**Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** SPC software packages like InfinityQS and Minitab handle statistical process control, but they don't understand AS9100 aerospace requirements — the specific Cpk thresholds per customer spec, the mandatory reporting formats for DCMA audit, and the process capability requirements that vary by drawing classification (critical vs. major vs. minor characteristics).
**Tags:** #gradient-boosting #evaluation-metrics #compliance #data-integration

## The Problem
Aerospace customers and AS9100 standards require demonstrated process capability (Cpk) on critical and major dimensions. Different customers specify different Cpk thresholds — Boeing requires Cpk >= 1.33 for critical characteristics, Lockheed may specify Cpk >= 1.67 for certain programs, and some specs require Ppk (process performance index) instead. The machine shop must track SPC data per dimension, calculate Cpk/Ppk per customer specification, and produce capability reports in the format each customer requires. Current SPC tools calculate statistics correctly but don't know which threshold applies to which dimension on which customer's part — the shop's quality engineer manually configures this for every part number and customer combination.

## What Already Exists
InfinityQS ProFicient and Minitab provide comprehensive SPC analysis with control charting, capability analysis, and reporting. Hexagon Q-DAS provides automotive-focused SPC with VDA/AIAG compliance. These tools handle the statistical calculations but not the aerospace regulatory context — customer-specific Cpk thresholds, characteristic classification-based reporting requirements, and DCMA audit report formats.

## The Customization Gap
An aerospace SPC module needs: (1) customer-specific capability threshold configuration — automatically applying the correct Cpk/Ppk requirement per characteristic classification per customer specification; (2) characteristic classification inheritance — reading critical/major/minor designations from the drawing and applying the corresponding SPC reporting requirements; (3) DCMA audit report generation — producing the specific capability summary formats that DCMA Government Quality Assurance Representatives review during surveillance visits; (4) process capability alerting that warns when a dimension is trending toward out-of-capability before it fails the threshold — enabling proactive tooling or process adjustment.

## Target Customer
Quality engineers at AS9100-certified machine shops serving 3+ aerospace prime customers with different capability requirements.

## Impact If Solved
Eliminates manual Cpk threshold configuration — saving 1-2 hours per new part setup and preventing mis-configured thresholds that cause incorrect capability assessments. Reduces DCMA audit preparation from days to hours by auto-generating required capability reports. Enables proactive capability monitoring that prevents out-of-spec conditions — each prevented non-conformance avoids 5-20 hours of MRB investigation and documentation.
