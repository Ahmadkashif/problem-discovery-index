# Historical Monument Locator Using GLO Notes and Aerial Imagery

**Niche:** [[niches/land-surveyors/rural-large-parcel/profile|Rural & Large-Parcel Surveys]]
**Industry:** [[industries/land-surveyors|Land Surveyors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool combines OCR'd General Land Office field notes from the 1800s with modern aerial/satellite imagery to predict where original survey monuments are most likely to be found in the field — surveyors spend days walking grid patterns searching for markers that an AI system could narrow to a 10-meter search area.
**Tags:** #cnn #object-detection #computer-vision #tacit-knowledge-ml #ocr

## The Problem
The U.S. public land survey system was established in the 1800s. Original surveyors set monuments (stone markers, wooden posts, witness trees with axe blazes) at section corners and quarter corners across hundreds of millions of acres. These monuments are the legal basis for property boundaries in 30 states. Finding them is the critical first step in any rural boundary survey. But they were set 100-200 years ago — wooden posts have rotted, stones have been buried by soil movement, witness trees have died or grown over their blazes. Surveyors search for these monuments by reading the original GLO field notes (handwritten, describing the monument and surrounding terrain) and then walking the area, sometimes for hours or days, looking for evidence. An experienced rural surveyor "reads" the terrain — they look for slight mounding where a stone cairn was buried, for old-growth trees that match the species and diameter described in the GLO notes, for subtle vegetation differences along old boundary lines. This tacit knowledge is the most experience-intensive skill in surveying.

## Why Nobody Has Built This
The input data is extraordinarily heterogeneous: GLO field notes are handwritten in 19th-century surveyor shorthand, vary by surveyor, and are stored across thousands of county and BLM offices. Aerial imagery can show vegetation patterns but not subsurface monuments. Combining these data sources requires: (1) OCR of handwritten historical documents, (2) extraction of spatial references from 19th-century descriptions, (3) correlation with modern aerial/satellite imagery and terrain models, and (4) probabilistic estimation of monument location. No single discipline (computer vision, NLP, geospatial analysis) covers the full pipeline.

## What to Build
A monument prediction system that: (1) OCRs and parses GLO field notes to extract monument descriptions, bearing trees, and terrain references; (2) overlays the original survey geometry on modern coordinate systems; (3) analyzes aerial imagery and LiDAR-derived terrain models for evidence of historical survey activity (linear features, old-growth trees, stone accumulations, vegetation boundaries); (4) produces a probability map showing the most likely location of each monument, with a search area ranked by confidence. The system reduces the field search from "walk the area until you find it" to "check these three spots in order of likelihood."

## Target Customer
Survey firms specializing in rural and timber boundary work, BLM and state land offices, and timber companies that need boundary surveys of large forested tracts.

## Impact If Built
Reduces monument search time from 2-8 hours per corner to 30-60 minutes. On a section corner survey with 4 corners plus quarter corners, this saves 1-3 days of field time. Enables less experienced surveyors to locate monuments that currently require a senior surveyor's field reading skills.
