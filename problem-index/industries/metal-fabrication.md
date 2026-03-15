# Metal Fabrication

**Category:** Manufacturing & Industrial
**Tags:** #computer-vision #tabular-ml #cnn #anomaly-detection #nlp #tacit-knowledge-ml #automation

## Industry Overview

The US metal fabrication industry generates approximately $380 billion annually. Metal fabricators cut, bend, weld, and finish structural metal components from raw stock — steel plate, aluminum extrusion, stainless sheet, and specialty alloys — into fabricated assemblies for construction, industrial equipment, automotive, aerospace, and consumer markets. The market ranges from small custom job shops ($1-10M revenue) to large structural fabricators ($50M+) producing bridge components, pressure vessels, and heavy equipment frames.

The defining characteristic of the industry: every job is custom or semi-custom. Unlike high-volume contract manufacturing, metal fabricators routinely produce one-off or short-run assemblies where the production routing is established from scratch for each new job. Estimating, nesting (optimizing raw material sheet layouts), welding, and quality inspection are the four core competencies — and all four rely heavily on skilled worker judgment developed over years of hands-on experience.

## Dominant Platforms

- **Fabricator ERP: Prodsmart / JobBOSS / Fishbowl Manufacturing** — job shop ERP for quoting, scheduling, and job tracking in metal fabrication shops
- **Structural fabrication: SDS/2 / Tekla Structures** — structural steel detailing software; Tekla is the dominant platform for structural steel fabricators
- **Nesting software: Hypertherm ProNest / Lantek / Sigmanest** — CNC plasma, laser, and waterjet cutting optimization; ProNest is the market leader for plasma/oxy-fuel; Lantek for laser
- **Welding: Lincoln Electric / Miller Welder data management** — welding machine data logging for weld parameter tracking; Lincoln Electric's CheckPoint is the primary platform
- **Quality: Roper Technologies / Creaform 3D scanning** — portable CMM and 3D scanning for dimensional inspection of fabricated components

## Workforce and Knowledge Structure

Metal fabrication depends on tacit knowledge at every production stage. Experienced estimators read a fabrication drawing and develop an accurate time and material estimate through years of quoting similar parts — understanding which geometric features create difficult weld access, which material thicknesses require specific consumable combinations, and where distortion will occur during welding and must be pre-compensated. This quoting intuition is the core competitive capability of any job shop: under-quote and the job destroys margin; over-quote and the job is lost.

Skilled welders develop the highest-value tacit knowledge: reading a weld pool, adjusting parameters in real time for material condition, gap variation, and joint geometry. A certified welder evaluating their own work or another's recognizes the surface appearance signatures of acceptable vs. rejectable weld conditions (porosity, undercut, lack of fusion, overlap) from experience with thousands of welds. This visual assessment is codified in AWS D1.1 and other standards but requires human judgment at the boundary conditions the standards describe inadequately.

Experienced press brake operators read springback — the elastic recovery of metal after bending — for each material and thickness combination, adjusting the over-bend angle to achieve the specified final angle. This parameter is theoretically calculable but varies with actual material properties, tooling wear, and operator technique in ways that require empirical calibration per job.

## Key Economic Pressures

- Estimating accuracy — systematic quote errors (consistently under- or over-estimating specific job types) compound across dozens of jobs before they're identified
- Material utilization — raw stock is typically 30-40% of job cost; nesting efficiency and remnant management directly affect material yield
- Welder shortage — certified welders are the scarcest labor resource; welder productivity and quality consistency determine shop capacity
- Rework and scrap cost — a distorted weldment or dimensionally nonconforming fabrication requires expensive rework or complete remake
- Inspection throughput — dimensional inspection of complex fabricated assemblies is time-consuming; bottlenecked inspection holds delivery on finished work

## Adjacencies

[[problems/metal-fabrication/high-impact|High Impact]] · [[problems/metal-fabrication/low-impact-1|Low Impact 1]] · [[problems/metal-fabrication/low-impact-2|Low Impact 2]] · [[problems/metal-fabrication/worker-life-1|Worker Life 1]] · [[problems/metal-fabrication/worker-life-2|Worker Life 2]] · [[problems/metal-fabrication/ml-opportunity|ML Opportunities]] · [[problems/metal-fabrication/ai-agents-platforms|AI Agents & Platforms]]
