# Clinical Assessment to Equipment Configuration Matching

**Niche:** [[niches/medical-supply-retail/mobility-wheelchair-dealers/profile|Mobility & Wheelchair Dealers]]
**Industry:** [[industries/medical-supply-retail|Medical Supply Retail]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool translates a patient's clinical assessment (diagnosis, functional abilities, body measurements, home environment) into a recommended equipment configuration — leaving this critical matching entirely to ATP expertise that takes years to develop and is in chronic shortage.
**Tags:** #gradient-boosting #multiclass-classification #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
An ATP evaluating a patient with multiple sclerosis must consider: current functional mobility (ambulatory with assistance? transferring independently?), progressive vs. stable condition, body habitus (weight, seated dimensions, postural asymmetries), skin integrity risk, home environment (doorway widths, flooring, ramp access), transportation (will the chair fit in the patient's vehicle?), and insurance coverage level. From these inputs, the ATP must select: wheelchair category (manual, tilt-in-space, power, complex rehab power), frame style, seat width/depth, cushion type, back support configuration, armrest style, and 20+ additional components. An experienced ATP narrows 500 possible configurations to 3-5 candidates in their first evaluation visit; a new ATP takes 3 visits and still may miss the optimal configuration.

## Why Nobody Has Built This
The clinical reasoning is deeply tacit — experienced ATPs say "I just know this patient needs a tilt-recline power chair with a ROHO cushion" based on pattern recognition from hundreds of similar patients. Codifying this reasoning requires structured capture of both the assessment inputs and the resulting equipment selection across thousands of cases, plus outcomes data (did the configuration work? was it returned? modified?). No DME software captures assessment-to-configuration data in a structured, analyzable format — assessments are narrative clinical notes, not structured data fields.

## What to Build
A clinical assessment tool that captures patient evaluation data in structured fields (functional mobility score, diagnosis category, body measurements, home environment parameters, insurance level) and recommends a ranked list of equipment configurations with rationale. The recommendation engine is initially rule-based (mapping diagnosis categories and functional levels to equipment categories per CMS coverage criteria) and evolves to ML-based as outcome data accumulates (which configurations were successful for patients with similar profiles?). The tool also generates the Letter of Medical Necessity documentation required for insurance authorization from the assessment data.

## Target Customer
DME suppliers with 2+ ATPs who want to: accelerate new ATP productivity, standardize assessment quality across clinicians, and reduce equipment returns caused by suboptimal configuration selection.

## Impact If Built
Reduces new ATP ramp-up time from 3-5 years to 12-18 months by providing decision support during assessments. Reduces equipment return/exchange rate from 15-20% to 8-12% through better configuration matching. Saves 30-60 minutes per assessment by auto-generating documentation from structured assessment data. Captures institutional knowledge that currently leaves with every departing ATP.
