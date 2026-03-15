# Nesting Efficiency Feedback and Material Remnant Tracking

**Industry:** [[metal-fabrication|Metal Fabrication]]
**Type:** Worker Life
**One-liner:** CNC operators and estimators who track material utilization manually — logging remnant sizes in notebooks or spreadsheets, estimating nesting efficiency after the fact — need automated remnant inventory and nesting outcome tracking that identifies which job types systematically waste material and which remnant pieces can be reused on upcoming jobs.
**Tags:** #gradient-boosting #regression #tabular-ml #worker-facing #automation #revenue-impact

## The Problem

Material — steel plate, stainless sheet, aluminum — is typically 30-45% of job cost in a metal fabrication shop. Nesting efficiency (the percentage of raw sheet consumed by parts vs. scrap offcuts) directly affects material cost per job. ProNest and similar nesting software optimize the cutting layout for a given set of parts, but the achievable nesting efficiency varies with part mix, sheet size, and grain direction requirements. The actual efficiency achieved vs. the theoretical optimum — and whether remnant pieces from one job were reused on another — is rarely tracked systematically.

The remnant problem is acute: every cut sheet produces offcuts that may be large enough to use on a future job. A 4' × 6' remnant of 1/4" A36 steel is worth $120 in raw material. A shop producing 50 cut jobs per week generates dozens of usable remnants. Without systematic tracking, these remnants either accumulate without being used (warehouse material creep) or are discarded as scrap rather than inventoried for reuse. Experienced shop managers know from experience which jobs commonly produce large remnants and which upcoming jobs can use them, but this matching is done informally and misses most reuse opportunities.

## The Solution

An automated remnant tracking and matching system integrated with ProNest or Sigmanest: when a nesting layout is cut, the system records each offcut's dimensions, material specification, and quantity from the nesting file output. When a new job is quoted or nest planned, the system checks the remnant inventory for pieces that can satisfy part requirements before ordering new stock. A regression model predicts which incoming jobs are likely to produce reusable remnants and which pending jobs are likely to consume them, enabling proactive matching at planning time rather than reactive discovery at cutting time.

## Impact

Systematic remnant reuse on 15-20% of eligible jobs reduces material procurement cost by 2-4% of total material spend. For a fabricator with $2M annual material spend, this recovers $40,000-$80,000. Equally important: eliminates the hidden cost of remnant accumulation and eventual scrap-out of material that was never tracked but had reuse value.
