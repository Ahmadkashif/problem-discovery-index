# AMI Meter Data Operations

**Parent Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to turn every exception in interval meter data into a correct bill and a correct grid model without a truck roll, and whoever resolves the most exceptions automatically, without a billing error reaching a customer, takes the account.

## Profile
**Market Size:** ~$1.2B a year of meter data management software, AMI operations staff, exception handling and meter analytics at US utilities (estimate)
**Share of Parent Industry:** ~0.2% of retail electricity revenue (estimate)
**Digital Adoption:** High — data arrives digitally every 15 minutes to an hour; exception work queues are still worked by people
**Target Buyer:** Director of Meter Operations / Manager of AMI & Meter Data Management
**Automation Potential:** Very high

## What Makes This a Distinct Niche
Form EIA-861 has tracked AMR and AMI meter counts since 2007, and most US meters now report interval data (estimate). Every day, meter data management systems run validation, estimation and editing (VEE). Meters that fail to report, read zero, read backwards or jump are flagged, estimated and queued for a person, who decides whether it's a communications gap, a failed meter, tampering, a solar installation nobody recorded or a real change. The same data could correct the grid connectivity model and detect overloaded transformers, but meter operations teams are staffed for billing exceptions. The analytics vendors that disaggregate meter data for efficiency programmes are covered in [[niches/energy-auditors/utility-ami-analytics-vendors/profile|🔍 Utility Meter Data Analytics Vendors]], and municipal billing offices in [[niches/municipal-services/utility-billing-departments/profile|⚡ Utility Billing Departments]].

## Current Tools & Gaps
Head-end systems from Itron, Landis+Gyr, Aclara and Honeywell; meter data management from Itron, Oracle and Siemens; theft and analytics modules; E Source's AMI testing and data management consulting. Gaps: exception queues worked one meter at a time; root-cause patterns across meters not learned; meter data not fed back to GIS connectivity.

## Problems
- [[niches/electric-utilities/ami-meter-data-operations/build|🔨 Build: Exception Root-Cause Learning Across the Fleet]]
- [[niches/electric-utilities/ami-meter-data-operations/buy|🛒 Buy: Meter Data Management With Connectivity Correction]]
- [[niches/electric-utilities/ami-meter-data-operations/fix|🔧 Fix: The Estimated Bill Nobody Reviewed]]
