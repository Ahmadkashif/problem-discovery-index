# Code Analysis Generated From the Model

**Niche:** [[niches/architecture-firms/code-analysis-permit-sets/profile|Code Analysis & Permit Set Preparation]]
**Industry:** [[industries/architecture-firms|Architecture Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The model knows every room's area and use; the code analysis sheet is still calculated in a spreadsheet and typed onto a sheet.
**Tags:** #large-language-models #feature-engineering #evaluation-metrics #compliance #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to get a permit set approved on the first review cycle in a specific jurisdiction, and whoever knows that jurisdiction's amendments and examiner demands before submission takes the account.

## The Problem
A project architect builds the code analysis by exporting areas, assigning occupancies, calculating occupant loads with the code's load factors, sizing egress, checking travel distances and fire separations, and counting plumbing fixtures — then redoes parts every time the design changes. Errors here are a top source of correction comments.

## Why Nobody Has Built This
Model-checking tools check geometry against generic rules; code research tools answer questions. Neither generates the jurisdiction-specific analysis sheet the examiner expects, in the format they expect, from the live model — and local amendments change the numbers.

## What to Build
A Revit add-in that reads spaces, assigns occupancies with confirmation, computes occupant loads, egress, allowable area and fixture counts under the adopted code and local amendments, flags non-compliance live as the design changes, and generates the code analysis sheets in the jurisdiction's preferred format.

## Target Customer
Project architects and technical directors at firms of 10 to 200 staff.

## Impact If Built
Hours saved on every project, fewer code-calculation corrections, and code compliance visible during design rather than at submission.
