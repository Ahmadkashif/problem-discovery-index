# Automated Shade Analysis and System Performance Modeling from Aerial Imagery

**Industry:** [[solar-installers|Solar Installers]]
**Type:** High Impact
**One-liner:** Solar designers who manually position panels in Aurora Solar to optimize around shade from trees, chimneys, and roof geometry — a design task that takes 45-90 minutes per site and requires significant experience to optimize correctly — get that layout optimization automated by an ML model that analyzes the roof's shade pattern and returns the optimal panel placement and production estimate in minutes.
**Tags:** #cnn #regression #computer-vision #tabular-ml #revenue-impact

## The Problem

Solar system performance depends critically on shade avoidance. A single shaded panel in a series string significantly reduces the output of the entire string. Optimizing panel placement requires: identifying all shade sources on and adjacent to the roof (chimney, ridge, dormers, nearby trees, neighboring structures), modeling how shadows move across the roof surface throughout the day and across seasons, and positioning panels to maximize annual energy production while fitting within the roof's structural load constraints and setback requirements.

Aurora Solar and similar platforms automate the shade simulation using LIDAR data, satellite imagery, and 3D modeling. The time-consuming component is the human design iteration: which panels to exclude for shade optimization, how to string the panels for maximum production with minimum mismatch loss, and how to balance system size against roof space constraints. An experienced solar designer can do this well in 60-90 minutes; a junior designer takes 2-3 hours and produces a suboptimal layout.

## Why It's High Impact

Design efficiency determines how many proposals a solar company can generate per week. The design bottleneck limits sales capacity — a company whose design team can produce 20 proposals per week cannot close more than 20 new customers per week regardless of sales team size. Automated design optimization that cuts design time to 15-20 minutes doubles or triples design capacity.

Beyond throughput, optimized designs directly impact customer economics: a design that captures 5% more annual production over a 25-year system life generates thousands of dollars of additional value for the customer at no additional installation cost. Systematic design optimization closes the gap between experienced and junior designer output quality.

## What a Solution Looks Like

Integration with Aurora Solar's API: the model receives the property's aerial imagery, LIDAR data, roof geometry, and irradiance data. It returns: recommended panel count and placement (specific roof positions), stringing configuration, inverter specification, and annual production estimate. The designer reviews the auto-generated layout, adjusts for any on-site conditions not captured in the imagery (roof access, customer aesthetic preferences), and converts to a customer proposal. Total designer time: 15-20 minutes of review and customization vs. 60-90 minutes of design from scratch.

## Implementation Path

Aurora Solar has the training data — every completed design in their platform is a labeled example (panel placement → production estimate → actual performance from monitoring data). A reinforcement learning or optimization approach (not just a discriminative model) that maximizes simulated annual production given the constraints: 9-15 month development project. Aurora Solar is the natural acquirer or partner — they already have the platform, the data, and the customer relationship.
