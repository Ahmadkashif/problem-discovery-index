# Design-for-Low-Resource Constraint Checker

**Niche:** [[niches/medical-device-mfg/devices-for-low-resource-settings/profile|Devices for Low-Resource Settings]]
**Industry:** [[industries/medical-device-mfg|Medical Device Manufacturing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** CAD design rule checkers (DFM analysis in SolidWorks, Fusion 360) validate manufacturability but have no concept of low-resource deployment constraints — they will not flag that a device requires compressed gas unavailable in rural clinics or uses a battery chemistry that degrades above 40C ambient temperature.
**Tags:** #automation #compliance #worker-facing

## The Problem
Engineers designing devices for low-resource settings must consider constraints that do not exist in US/EU design: no reliable electricity (battery or manual operation required), ambient temperatures of 10-45C with high humidity, no biomedical equipment technician on site (device must be maintainable by a nurse or community health worker), consumables must be available from local suppliers or have shelf stability for 6+ months in uncontrolled storage, and the device must survive transportation on unpaved roads. These constraints are not encoded in any design tool — engineers learn them through painful field experience when their device fails in the deployment environment.

## What Already Exists
SolidWorks and Fusion 360 include DFM (Design for Manufacturing) analysis that checks wall thickness, draft angles, undercuts, and other manufacturability parameters. Altium and KiCad perform DRC (Design Rule Check) for electronics. Environmental testing standards (IEC 60068 for temperature/humidity, IEC 60601-1-11 for home healthcare environments) define test requirements but are not integrated into design tools as proactive checks.

## The Customization Gap
A low-resource DFM checker must evaluate: power architecture (can it operate on solar/battery for 8+ hours? What happens during power interruption?), thermal performance (rated operating range includes 45C ambient with no air conditioning?), serviceability (can a non-engineer replace consumables and perform basic maintenance?), supply chain assumptions (are all consumables available from WHO-prequalified suppliers?), and transportation survivability (vibration, drop, and dust ingress ratings appropriate for unimproved roads). These checks must run against the CAD model and BOM, flagging violations before the device enters prototyping.

## Target Customer
Product development engineers at global health device companies designing for deployment in Sub-Saharan Africa, South Asia, and Latin America. Approximately 50-100 companies. Also applicable to military/field medical device design (additional 50-100 companies).

## Impact If Solved
Design-stage detection of low-resource constraint violations prevents 30-50% of field failures that currently require costly redesign after deployment. Prototype-to-field-ready development time drops by 3-6 months by catching deployment-critical design issues earlier.
