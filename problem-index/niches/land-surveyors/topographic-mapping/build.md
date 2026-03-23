# Automated Feature Extraction from Survey-Grade Point Clouds

**Niche:** [[niches/land-surveyors/topographic-mapping/profile|Topographic & As-Built Mapping]]
**Industry:** [[industries/land-surveyors|Land Surveyors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool automatically extracts and classifies survey features — buildings, fences, trees, curbs, utility poles, signs, manhole covers — from point clouds at the accuracy level required for engineering design.
**Tags:** #cnn #semantic-segmentation #computer-vision #automation #tacit-knowledge-ml

## The Problem
A drone survey of a 20-acre commercial site generates 50-100 million point cloud points. The civil engineer needs a topographic map showing every structure, utility feature, vegetation boundary, and surface feature, classified by type and accurately positioned. Current automated classification can separate ground from vegetation from buildings at a coarse level, but it cannot identify specific feature types (curb vs. sidewalk edge, utility pole vs. tree, manhole cover vs. valve box) or place breaklines at grade changes. A survey technician manually identifies, classifies, and traces every feature — clicking thousands of points to draw building outlines, fence lines, edge of pavement, and utility locations. This manual feature extraction takes 4-8 hours per acre and is the primary bottleneck in topographic survey delivery.

## Why Nobody Has Built This
Survey-grade feature extraction requires sub-inch accuracy — the difference between a curb face and a gutter line is 6 inches, and both matter for drainage design. Generic point cloud classification (used in autonomous driving, forestry, urban planning) operates at resolutions 10-100x coarser than survey requirements. Training data for survey-grade feature extraction doesn't exist as a labeled dataset — it would need to be created from thousands of completed survey projects where a technician manually classified every feature. The survey industry is small and fragmented, providing insufficient market incentive for the major ML/CV companies to build this.

## What to Build
A feature extraction pipeline that takes a classified ground point cloud and: (1) detects and classifies survey features (buildings, fences, walls, curbs, sidewalks, utility poles, manholes, signs, trees, shrubs) using a CNN trained on survey-grade labeled point clouds; (2) traces feature boundaries at survey accuracy (within 0.1 feet of the true position); (3) places breaklines at grade changes (top and bottom of curb, edge of pavement, ditch flow lines); (4) exports classified features to CAD (Civil 3D, Carlson) as 3D polylines with attribute data. The system presents results for technician review — confirming or correcting classifications rather than creating them from scratch.

## Target Customer
Survey firms that perform topographic surveys using drone data, and engineering firms with in-house survey departments. Market entry: firms processing 5+ drone topographic surveys per month.

## Impact If Built
Reduces feature extraction time from 4-8 hours per acre to 1-2 hours per acre (technician review of automated results vs. manual extraction from scratch). For a 20-acre site, this saves 60-120 hours of technician time per project. Enables survey firms to deliver topographic surveys in days instead of weeks, matching the speed of drone data collection.
