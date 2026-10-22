# Statistical Plans and Regulator Data Calls

**Industry:** [[property-casualty-insurers|Property & Casualty Insurers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Data warehouses and BI tools can produce any report, but statistical plan submissions and regulator data calls follow coding manuals, edit checks and reconciliation rules no generic tool knows, so each cycle is rebuilt by hand against a deadline.
**Tags:** #feature-engineering #descriptive-statistics #evaluation-metrics #data-integration #compliance #automation #workflow-orchestration

## The Problem
A P&C carrier reports the same business many times over. Premium and loss data go to its statistical agent (ISO, AAIS or another licensed agent) on that agent's statistical plan, coded to classes, territories, coverages and causes of loss defined in the plan manual. Workers' compensation unit statistical data goes to NCCI or the state bureau policy by policy. The annual statement and its Schedule P carry the same losses by accident year. On top of that, regulators issue data calls. The market conduct annual statement asks for claims and complaint counts by line and state. Catastrophe data calls follow major events. In 2024 the NAIC's property market intelligence call asked more than 400 insurers for ZIP-code-level premiums, policies, claims, limits, deductibles and non-renewals, more than 70 data points due within 90 days.

Each submission is drawn from policy and claims systems that were never coded for it. A statistical reporting team, often a handful of analysts at a mid-sized carrier (estimate), maps system codes to plan codes and fixes the records that fail the agent's edit checks. They reconcile totals to the annual statement and explain the differences. Then the next call arrives with different definitions.

## What Already Exists
Data warehouses (Snowflake, Databricks), ETL and BI tools, core-system reporting modules, and the agents' own submission portals and edit reports. Some core-system vendors and consultancies sell statistical-reporting adapters for ISO plans.

## The Customisation Gap
The hard part is the domain logic. Each statistical plan has its own class, territory and cause-of-loss codes, and they change with manual revisions. Coding has to be mapped from the carrier's product configuration, which changes with every rate filing. Edit-check failures need line-specific fixes. Data calls carry one-off definitions, such as whether a non-renewal at the insured's request counts. Every submission must tie to the annual statement within tolerances regulators accept. A useful tool keeps a versioned map from system codes to every plan and call definition, predicts which records will fail edits before submission, drafts the reconciliation and the variance explanations, and turns a new data call's definitions into a query in days, not weeks.

## Impact If Solved
Statistical and data-call reporting stops consuming a team's quarter. It also gets more accurate, which matters because these submissions feed the advisory loss costs and regulatory analyses that every carrier's future rates depend on.
