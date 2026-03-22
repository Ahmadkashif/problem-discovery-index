# AI Underground Utility Detection from GPR Data

**Niche:** [[niches/utility-contractors/locate-mapping-gis/profile|Locate, Mapping & GIS]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A computer vision system that analyzes Ground Penetrating Radar (GPR) data to automatically detect and classify underground utilities — identifying the hyperbolic reflection patterns that indicate buried pipes and cables — replacing the expert human interpretation that takes 2-5 years to develop and is the primary bottleneck in subsurface utility engineering.
**Tags:** #object-detection #tacit-knowledge-ml #automation #compliance #cnns

## The Problem
GPR produces B-scan images — cross-sectional slices of the subsurface showing radar reflections from buried objects. A utility appears as a hyperbolic reflection pattern whose apex indicates the utility's horizontal position and whose shape indicates depth. An experienced GPR operator scans a site, watches the real-time B-scan display, identifies utility signatures, marks them on the surface, and estimates depth and diameter. This interpretation requires recognizing utility patterns amid noise (soil layers, rocks, rebar, tree roots, archaeological features, void spaces). Experienced operators with 2,000+ hours of GPR field time detect 80-90% of utilities; novice operators with less than 500 hours detect 50-60%. The skill gap directly translates to utility strike risk: the 20-40% of utilities missed by inexperienced operators are the ones that get hit during excavation.

## Why Nobody Has Built This
GPR data is noisy and variable: signal characteristics depend on soil type (clay attenuates radar, sand transmits well), soil moisture (wet soil reduces penetration depth), utility material (metal produces strong reflections, plastic produces weak ones), and GPR frequency (low frequency penetrates deeper but with less resolution). A utility signature in dry sandy soil looks different from the same utility in wet clay. Training data requires thousands of labeled GPR scans with ground-truth utility positions verified through excavation — data that SUE firms have in their archives but haven't aggregated. The hyperbolic pattern detection is a well-studied signal processing problem in geophysics research, but translating from academic research to a field-deployable tool requires real-time processing on ruggedized hardware.

## What to Build
A GPR interpretation assistant that processes B-scan data in real-time as the operator collects it: (1) a CNN-based hyperbola detector identifies candidate utility reflections, marking them on the display with confidence scores; (2) a classification model estimates utility type (metallic/non-metallic), approximate depth, and approximate diameter from the hyperbola characteristics; (3) the system alerts the operator when a high-confidence utility detection occurs, drawing attention to a feature they might otherwise miss; (4) detected utilities are geo-referenced using the GPR unit's GPS and exported directly to GIS format. The system augments the operator rather than replacing them — it highlights features for human confirmation, reducing the experience threshold needed for reliable GPR interpretation from 2,000+ hours to 200-500 hours.

## Target Customer
Subsurface Utility Engineering (SUE) firms performing ASCE 38 utility investigations (Quality Levels A through D). Utility locating companies offering GPR-enhanced locate services. GPR equipment manufacturers (GSSI, Sensors & Software) seeking to add AI interpretation to their hardware.

## Impact If Built
Improves novice GPR operator detection rates from 50-60% to 75-85%, approaching experienced operator performance within 500 hours instead of 2,000+ hours. Reduces utility strikes caused by missed GPR detections by 20-35%. Enables SUE firms to scale their GPR operations without waiting 2-5 years per operator for expertise to develop. Creates a data flywheel — every confirmed detection improves the model, and every confirmed miss provides negative training data.
