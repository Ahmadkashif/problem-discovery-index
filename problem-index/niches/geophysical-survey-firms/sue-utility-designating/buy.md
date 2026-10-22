# CAD and GIS That Carry ASCE 38 Quality Levels

**Niche:** [[niches/geophysical-survey-firms/sue-utility-designating/profile|Subsurface Utility Designating (QL-B)]]
**Industry:** [[industries/geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Civil 3D and ArcGIS Utility Network can draw and model utilities, but neither treats each segment's ASCE 38 quality level, source and confidence as first-class data that survives into the design plans.
**Tags:** #large-language-models #data-integration #workflow-orchestration #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to deliver QL-B utility designations that hold up when the QL-A test holes are dug, on the DOT's design schedule, and whoever's lines survive excavation most often keeps the on-call contract.

## The Problem
A SUE deliverable must show each utility segment with its quality level, owner, type, size where known, and the basis for the designation. DOTs publish CADD standards for line styles and layers. Firms hand-draft to those standards from field sketches and geophysical picks, and the quality-level information is often reduced to a line type the designer may not read.

## What Already Exists
Autodesk Civil 3D and AutoCAD with DOT-specific templates; Esri ArcGIS Utility Network for utility owners; field collection in ArcGIS Field Maps and Trimble apps.

## The Customization Gap
The adaptation needs: a segment-level attribute schema for ASCE 38-22 (quality level, method, date, confidence, test-hole links); automated conversion from geophysical picks to segments with those attributes; per-DOT CADD style mapping generated from one master record; validation that every segment has a quality level and basis; and record-drawing PDFs parsed for owner, size and material to pre-populate QL-D attributes.

## Target Customer
SUE practices delivering to multiple state DOTs with different CADD standards.

## Impact If Solved
Drafting hours cut per corridor and quality levels that reach the designer intact, so a QL-C line is not designed around as if it were QL-A.
