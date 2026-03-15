# Maintenance Request Triage and Vendor Dispatch Automation

**Industry:** [[property-management|Property Management]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic ticketing and workflow tools exist but don't model the property management-specific urgency criteria — habitability requirements, emergency vs. non-emergency classification under fair housing, and the contractor dispatch priorities that experienced property managers apply by judgment.
**Tags:** #llm #text-classification #nlp #automation #workflow-orchestration

## The Problem

Property managers receive maintenance requests continuously — a portfolio of 200 units generates 40-80 maintenance requests per month. Each request requires triage: is this an emergency (no heat in winter = habitability violation in most states, requires 24-hour response), urgent non-emergency (leaking sink, broken lock), or routine (paint touch-up, screen replacement)? The triage decision determines dispatch priority, which contractor category to call, and whether the property owner needs to be notified.

Experienced property managers triage these requests in seconds based on the description. Junior property managers or office admins who handle after-hours requests misclassify emergencies as routine (failing to dispatch the emergency plumber for a water heater leak at 9pm) or routine as emergencies (dispatching a plumber at overtime rates for a dripping faucet). Both errors are expensive.

## What Already Exists

AppFolio and Buildium have maintenance request intake with priority flags set by the tenant (which tenants routinely mark everything as urgent). Generic help desk software (Zendesk, ServiceNow) handles ticket triage but doesn't know habitability law urgency criteria or property management emergency dispatch protocols.

## The Customisation Gap

A property management maintenance triage tool needs: (1) urgency classification trained on the property management firm's own historical request resolution data and outcomes; (2) habitability law mapping by state (what constitutes an emergency under the applicable state landlord-tenant law); (3) contractor category routing (HVAC vs. plumber vs. general handyman vs. emergency locksmith based on request type); (4) auto-draft of the work order and contractor dispatch notification. The habitability law mapping and the property management-specific urgency criteria are not in any generic workflow tool.

## Impact If Solved

Reduces after-hours misclassification of maintenance emergencies. Reduces manager decision time per request from 5-10 minutes (looking up the contractor, deciding urgency, writing the work order) to 60 seconds of review. Enables vacation coverage — the on-call manager handles after-hours requests through an auto-triage system rather than making judgment calls without context.
