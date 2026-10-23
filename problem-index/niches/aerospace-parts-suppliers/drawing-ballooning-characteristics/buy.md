# Auto-Ballooning Extended to Model-Based Definition

**Niche:** [[niches/aerospace-parts-suppliers/drawing-ballooning-characteristics/profile|Drawing Ballooning & Characteristic Accountability]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Newer programmes define parts in the 3D model with no drawing, and FAI tools built around ballooning a sheet have nothing to balloon.
**Tags:** #feature-engineering #data-integration #evaluation-metrics #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in this sub-niche is fighting to extract every requirement on a drawing or model, notes included, into a ballooned Form 3, and whoever posts the highest characteristic recall on the shop's own scanned and model-based drawings takes the account.

## The Problem
Model-based definition puts dimensions, tolerances and notes as product manufacturing information in the CAD model. Suppliers receiving MBD either ask for a drawing, which the customer may not provide, or build the characteristic list by clicking through the model.

## What Already Exists
CAD viewers read PMI; some FAI tools import STEP AP242 PMI; CMM software can program from PMI.

## The Customization Gap
An MBD path for AS9102 needs PMI imported as characteristics with stable identifiers, notes in the model's attributes treated like drawing notes, and the customer's digital product definition rules applied (Boeing's D6-51991 for digital datasets, recalled). It must render a "ballooned" view the customer's quality representative accepts, and link each characteristic to the CMM program that measures it. Gaps in PMI must be flagged, not silently skipped.

## Target Customer
Suppliers on newer airframe and engine programmes that ship MBD, and their CMM programmers.

## Impact If Solved
A clean MBD path removes ~3–6 hours of manual characteristic building per FAI (estimate) and removes the excuse for asking customers for drawings they no longer make.
