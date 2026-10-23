# Warranty Work Paid Twice

**Niche:** [[niches/facilities-management-firms/subcontractor-invoice-validation/profile|Subcontractor Invoice Validation & Pass-Through Billing]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A repair on equipment still under manufacturer or installer warranty is invoiced, paid and rebilled because nobody checked the warranty register.
**Tags:** #data-integration #descriptive-statistics #quick-win #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to validate every subcontractor invoice against its work order, rate card and not-to-exceed before it is rebilled to the client, and whoever catches the overbilling before the client's audit does takes the account.

## The Problem
New equipment arrives with parts and sometimes labour warranties; capital projects hand over with installer warranties; some assets sit under the client's own OEM service contracts. When they fail, the reactive call goes to whoever is on the rota, and the invoice is paid on a job that should have cost nothing.

## Why It's Still Broken
Warranty data arrives in project close-out documents that never reach the CMMS asset record. The coordinator validating the invoice has no field to check.

## What a Fix Looks Like
Extract warranty terms from close-out documents and OEM service contracts into the asset record at handover, check every new work order against them at dispatch (route to the warranty holder) and every invoice at validation (reject or recover), and report recovered value monthly.

## Who Feels the Pain
Account finance teams, clients paying twice, and project teams whose handover documents vanish into a shared drive.

## Impact If Fixed
A small, recurring leakage closes with a check at two points the workflow already passes through.
