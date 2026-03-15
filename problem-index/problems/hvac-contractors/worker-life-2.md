# Refrigerant Recovery and Charge Tracking Compliance

**Industry:** [[hvac-contractors|HVAC Contractors]]
**Type:** Worker Life Changing
**One-liner:** HVAC technicians handling refrigerants who are required by EPA Section 608 to log every refrigerant recovery and charge event — recording equipment identifier, refrigerant type, amount recovered/added, and technician certification number — get that logging done automatically from the service call data, eliminating a compliance documentation task that takes 5-10 minutes per call and is frequently done incorrectly.
**Tags:** #automation #compliance #worker-facing #llm

## The Problem

EPA Section 608 regulations require HVAC technicians to maintain records of all refrigerant purchases, recovery, and charge additions. Refrigerant tracking records must include: the type and quantity of refrigerant, the equipment serviced (by type and identifier), the technician's EPA certification number, and the date. Violations carry fines of up to $44,539 per day per violation. In practice, most small HVAC firms maintain inadequate refrigerant records — the logging is done inconsistently, on paper forms that aren't digitized, or skipped entirely for "small" additions.

The compliance gap is not lack of awareness — technicians know they're supposed to track refrigerant. The gap is friction: the logging task interrupts the service flow, the forms are structured differently from the service call data the technician has already entered, and there's no immediate consequence for incomplete records until an EPA audit.

## Why It Matters to the Worker

A technician who receives an EPA citation faces personal liability, not just company liability. Individual technicians with universal recovery certifications are the regulated party. The friction is the paperwork: the technician has already entered all the relevant information (equipment type, refrigerant used, job number) into ServiceTitan — recopying this into a separate refrigerant log is redundant and resented.

## What a Solution Looks Like

A ServiceTitan integration that automatically generates the EPA Section 608 refrigerant log from the service call data: equipment type (from job type + installed equipment record), refrigerant type and quantity (from the service call's parts/materials entry), technician certification number (from the technician's profile), date (from the job completion timestamp). The technician reviews the auto-generated log entry at job close and submits. The system maintains the running refrigerant log in EPA-compliant format and generates the periodic usage reports required for compliance audits.

## Impact If Solved

Eliminates duplicate data entry for refrigerant compliance tracking. Converts an inconsistently-performed manual task into an automatic output of the existing service workflow. Reduces EPA compliance risk for both the firm and individual technicians.
