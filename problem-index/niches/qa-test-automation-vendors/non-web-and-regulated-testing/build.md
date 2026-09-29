# Automated Execution, Manual Evidence

**Niche:** [[niches/qa-test-automation-vendors/non-web-and-regulated-testing/profile|Non-Web & Regulated Testing]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Regulated engineering teams automate the test execution and then assemble the evidence by hand, which is the larger half of the work and the one nobody has automated.
**Tags:** #graph-theory #bert #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to bring modern test automation to software that runs on hardware and must produce regulatory evidence — and whoever does that takes those industries, because the category's tooling assumes a browser and they do not have one.

## The Problem
A medical device team runs an automated test suite against hardware in the loop. It passes. Producing the evidence for the design history file then takes several weeks: linking each executed test to the requirement it verifies and the hazard that requirement mitigates, capturing the environment and configuration, formatting the results into the expected structure, and obtaining signatures. The test execution was automated years ago; the evidence assembly was not, and it is the larger cost. Every fact the evidence needs was present at execution time and was not captured in the form the record requires.

## Why Nobody Has Built This
The test tooling and the quality management system are different products with different vendors, and the join between them — which test verifies which requirement, run in which configuration, with what result — is maintained manually because nobody has built the bridge. The regulated industries' tooling is descended from document management and is oriented to producing records rather than to executing tests. The modern testing ecosystem has ignored these industries because their environments are awkward. And the manual burden is treated as the cost of regulation rather than as an automation gap, which it largely is.

## What to Build
Capture the evidence at execution time in the form the record needs. Attach the traceability links to the tests themselves, so a test declares which requirement it verifies and the link is maintained with the code rather than in a separate matrix — which is the structural change and eliminates the largest manual cost. Capture the full execution context automatically: software version, hardware configuration, calibration state, environment conditions, tool versions and operator, since these are what the record must contain and are all available at execution. Generate the evidence package from the execution record rather than assembling it, which turns weeks into minutes and is entirely mechanical once the links and the context exist. Maintain the traceability continuously rather than at milestones, so the coverage against requirements is visible during development rather than established at the end. Support the manual tests that genuinely cannot be automated with the same capture and evidence flow, since they will remain and their evidence is equally burdensome. And make the record tamper-evident and reviewable, because that is what a regulator and an auditor actually need and is a property rather than a document format.

## Target Customer
Medical device, automotive, industrial and regulated financial engineering functions, the quality management system vendors serving them, and the test tooling vendors who have written these industries off.

## Impact If Built
The execution is automated and the evidence is assembled by hand, which inverts where the effort actually is. Attaching traceability to the tests and capturing context at execution turn a multi-week assembly into a generated artefact.
