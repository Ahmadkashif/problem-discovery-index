# Field Data Processing and Deliverable Generation

**Industry:** [[land-surveyors|Land Surveyors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Converting raw field data (GNSS observations, total station shots, point clouds) into finished deliverables (survey plats, legal descriptions, topographic maps) requires 4-8 hours of manual CAD work per project — generic point cloud and CAD tools don't understand survey-specific conventions, legal description formatting, or jurisdictional plat standards.
**Tags:** #gradient-boosting #regression #tabular-ml #automation #cnn #semantic-segmentation #computer-vision

## The Problem

A typical boundary survey generates 50-200 field observations (GNSS coordinates, total station angles and distances, level shots) that must be processed into a finished plat — a legal document with specific formatting requirements including a scaled drawing of the parcel boundary, a written legal description using metes and bounds or lot/block format, a title block with surveyor certification, and monuments shown with specific symbology. The CAD work to produce this plat takes 4-8 hours for a standard residential survey and 10-20 hours for a complex commercial ALTA survey.

The process is highly repetitive: the same steps (import points, draw boundary lines, annotate bearings and distances, calculate area and closure, generate legal description, place title block) are performed for every survey, but the specific parameters change. Each county may have different filing requirements (minimum sheet size, required certifications, specific symbology), and each project type has different content requirements (ALTA surveys require 19 specific table items; boundary surveys require monument descriptions; topographic surveys require contour intervals per client specification).

## What Already Exists

AutoCAD Civil 3D and Carlson Survey handle point import, coordinate geometry calculations, and drafting. Trimble Business Center and Leica Infinity process GNSS data and produce adjusted coordinates. SurvCE and FieldGenius collect data in the field with real-time coding. These tools are powerful but fundamentally require manual drafting — the surveyor or CAD technician must draw each line, place each annotation, and format each sheet manually. Point cloud processing tools (CloudCompare, Cyclone, RealityCapture) can register and clean point clouds but do not produce survey-ready deliverables.

## The Customisation Gap

The missing layer is a survey-aware automation pipeline that takes processed field data (adjusted coordinates with point codes) and generates a draft plat meeting jurisdictional standards. The system needs to understand: (1) the relationship between field codes and survey symbology (point code "IP" = iron pin found, drawn as a specific symbol per the office's standards), (2) jurisdictional plat formatting requirements (loadable as templates for each county the firm works in), (3) legal description generation from the coordinate geometry (metes and bounds with correct bearing format, distance precision, and curve data), and (4) quality checks (mathematical closure, area consistency, bearing/distance annotation vs. coordinate consistency).

The automation target is not full plat generation — professional judgment is required for boundary decisions, monument weighting, and legal description language choices. The target is eliminating 60-80% of the manual CAD drafting that follows those decisions, producing a draft plat that the PLS reviews and adjusts rather than building from scratch.

## Impact If Solved

Reduces per-project office time from 4-8 hours to 1-2 hours for standard boundary surveys, a 60-75% reduction. For a firm completing 200 surveys/year at an average of 6 hours office time each, that's 800-1,000 hours recovered annually — equivalent to adding 0.5 FTE of CAD capacity without hiring. At $75-$100/hour loaded cost, the savings are $60,000-$100,000/year for a mid-size firm. The faster turnaround also reduces the backlog that currently causes 2-4 week delivery delays, improving client satisfaction and enabling more projects per year.
