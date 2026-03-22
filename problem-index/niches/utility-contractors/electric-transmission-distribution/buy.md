# GIS Platform Enhanced with Change Detection

**Niche:** [[niches/utility-contractors/electric-transmission-distribution/profile|Electric Transmission & Distribution]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ESRI ArcGIS maps utility assets at a point in time but doesn't detect changes — new construction near power lines, vegetation growth, unauthorized structures in rights-of-way — forcing utilities to rely on manual patrol to discover encroachments that could be detected automatically from regularly updated imagery.
**Tags:** #object-detection #data-integration #automation #compliance #cnns

## The Problem
Utility GIS systems contain detailed maps of every pole, conductor, transformer, and switch in the distribution network. These maps are updated when new assets are installed or existing assets are modified. But the environment around these assets changes continuously — trees grow, buildings are constructed, swimming pools are installed under distribution lines, unauthorized structures are built in easements — and GIS systems don't detect these environmental changes. A new building constructed within the right-of-way easement violates the utility's property rights and creates safety hazards, but the utility may not discover it until a crew visits the area months later. Vegetation growth is continuous but GIS maps are static.

## What Already Exists
ESRI ArcGIS is the industry standard for utility asset management GIS. It handles spatial data storage, visualization, and analysis. ESRI's satellite imagery integrations (ArcGIS Living Atlas) provide updated aerial imagery. What's missing is automated comparison between imagery captures to detect changes relevant to utility operations.

## The Customization Gap
A change detection module for ArcGIS that: (1) ingests regularly updated aerial/satellite imagery (quarterly or annual) for the utility's service territory; (2) compares current imagery against previous captures to detect new construction, vegetation growth, structure removal, and land use changes within utility right-of-way corridors; (3) classifies detected changes by type (new structure, vegetation encroachment, ground disturbance, new impervious surface) and risk level (within easement, within minimum clearance, approaching clearance); (4) generates work orders for field verification of detected changes, routed to the appropriate department (vegetation management, right-of-way enforcement, engineering review); and (5) maintains a change history for each corridor segment, building a longitudinal record of encroachment patterns. This leverages ESRI's existing spatial data infrastructure while adding the temporal analysis that static GIS lacks.

## Target Customer
Electric utilities using ESRI ArcGIS (virtually all US utilities) who currently rely on manual patrol to detect right-of-way changes. ESRI as a platform seeking to add utility-specific AI capabilities to ArcGIS.

## Impact If Solved
Detects right-of-way encroachments 3-12 months earlier than manual patrol, preventing safety hazards and property rights violations. Reduces patrol costs by 30-50% by replacing scheduled full-circuit patrol with change-detection-driven targeted investigation. Provides continuous monitoring documentation for regulatory compliance. Could be offered as an ESRI premium module at $50K-200K per utility per year.
