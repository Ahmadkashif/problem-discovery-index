# AI-Assisted Termite Damage Assessment

**Niche:** [[niches/pest-control/termite-inspection/profile|Termite Inspection & Treatment]]
**Industry:** [[industries/pest-control|Pest Control]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool helps an inspector photograph crawl-space wood and get an automated assessment of termite damage type, severity, and treatment recommendation.
**Tags:** #cnn #object-detection #computer-vision #tacit-knowledge-ml #revenue-impact

## The Problem
Experienced termite inspectors identify damage type (subterranean vs. drywood vs. dampwood termites) and severity from visual cues that junior inspectors miss: frass color and shape (drywood termite frass is hexagonal pellets vs. subterranean mud), wood grain patterns in damaged timber, mud tube construction style, and moisture patterns. A senior inspector touches a baseboard and knows the damage extends 6 feet — a junior inspector sees only the visible surface damage. Misidentification leads to wrong treatment protocols (fumigation for subterranean termites wastes $3,000-$5,000, soil treatment for drywood termites fails completely).

## Why Nobody Has Built This
Termite damage evidence is subtle and variable: mud tubes range from pencil-thin to finger-width, frass can be confused with sawdust or dirt, and damaged wood may look intact from the surface. Training data requires pairing inspection photos with expert assessments and confirmed treatment outcomes — no labeled dataset exists. Crawl-space and attic photography is low-quality (dim lighting, awkward angles, dust), making visual recognition harder.

## What to Build
A mobile inspection app where the inspector photographs evidence of damage (wood surfaces, mud tubes, frass, moisture staining). Computer vision identifies termite species indicators, damage severity, and affected area extent. The system outputs a preliminary assessment with species identification confidence, recommended treatment type, and suggested treatment zone. Each confirmed diagnosis and treatment outcome improves the model.

## Target Customer
Termite inspection companies performing 20+ inspections per month who employ junior inspectors with less than 2 years of experience.

## Impact If Built
Reduces misidentification-driven treatment failures (currently 8-12% of treatments require retreatment) by 50-60%, saving $2,000-$4,000 per avoided retreatment and accelerating junior inspector competency from 2 years to 6 months.
