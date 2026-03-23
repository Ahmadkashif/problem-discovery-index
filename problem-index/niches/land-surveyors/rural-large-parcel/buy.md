# LiDAR Processing Adapted for Under-Canopy Feature Detection

**Niche:** [[niches/land-surveyors/rural-large-parcel/profile|Rural & Large-Parcel Surveys]]
**Industry:** [[industries/land-surveyors|Land Surveyors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** LiDAR processing tools (CloudCompare, TerraScan) filter vegetation to create bare-earth models for engineering, but surveyors need to detect subtle human-made features under canopy — old roads, fence depressions, stone walls, cairns — that these tools treat as noise.
**Tags:** #cnn #semantic-segmentation #computer-vision #tacit-knowledge-ml

## The Problem
Aerial LiDAR can penetrate forest canopy and generate point clouds of the ground surface. These point clouds, when processed into bare-earth digital terrain models, reveal micro-topographic features invisible from the surface — old road beds, building foundations, stone walls, earthen berms, and even the slight depressions left by rotted fence posts. These features are critical evidence in rural boundary surveys: a stone wall marks a property line, an old road indicates an easement, a foundation suggests a homestead that anchors a legal description. But standard LiDAR processing tools are designed for engineering — they classify points as ground, vegetation, or buildings, and they treat small ground features as noise to be smoothed out.

## What Already Exists
TerraScan (Terrasolid), CloudCompare (open source), LAStools, and Global Mapper are the dominant LiDAR processing platforms. They excel at vegetation filtering and bare-earth model generation for engineering and topographic purposes. USGS and state agencies provide free LiDAR coverage for much of the U.S. through the 3DEP program. Some academic tools exist for archaeological feature detection from LiDAR (e.g., Relief Visualization Toolbox), but these are not integrated into surveying workflows.

## The Customization Gap
The tool needs a "boundary evidence" processing mode that: (1) preserves micro-topographic features instead of smoothing them; (2) classifies features relevant to boundary surveying — linear features (fences, walls, roads), point features (cairns, posts, foundations), and vegetation boundaries (tree lines, clearing edges); (3) overlays detected features on the property's legal description geometry to highlight correlations (a linear feature aligned with a deed bearing is likely a boundary marker); (4) exports findings to the surveyor's CAD system with attribute data. The interface must be usable by a surveyor, not a LiDAR specialist.

## Target Customer
Rural and timber survey firms, particularly those serving regions with public LiDAR coverage (now covering ~80% of the contiguous U.S.).

## Impact If Solved
Enables surveyors to identify boundary evidence from LiDAR before going to the field, reducing field time by 30-50% on forested parcels. Detects features that are invisible from the ground surface (buried stone walls, filled-in ditches) that experienced surveyors would otherwise find only by chance or decades of local knowledge.
