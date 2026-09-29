# Two Assessors, Same Building, Different Reserve Table

**Niche:** [[niches/home-inspection/commercial-property-condition-assessment/profile|Commercial Property Condition Assessment Firms]]
**Industry:** [[industries/home-inspection|Home Inspection]]
**Type:** Fix (Pain Point)
**One-liner:** The firm's output varies by who walked the building, and nobody can measure by how much.
**Tags:** #tacit-knowledge-ml #evaluation-metrics #worker-facing #transfer-learning #data-integration

## The Problem
Send two competent assessors to the same 200,000 square foot office building and you get two different reports. Different immediate repair totals, different remaining life on the chiller, different judgments about whether a roof needs replacing now or in four years. Both are defensible. They are not the same, and the difference flows directly into a lender's escrow requirement.

Everyone in the business knows this. Nobody measures it, because measuring it would require sending two assessors to the same building on purpose, and nobody wants to pay for that or to find out the answer.

Underneath the variance is real expertise. A senior assessor knows that a particular roof system fails at the seams before the field, that this vintage of rooftop unit is worth checking for a specific compressor problem, that a certain patching pattern means the owner has been deferring rather than maintaining. That knowledge is what the firm sells, and it exists only in individuals.

## Why It's Still Broken
Reports are reviewed for completeness and internal consistency, not for calibration. A reviewer checks that every required section is present and the numbers tie. Nobody asks whether this assessor's remaining life estimates run systematically longer than their colleagues', because the data to answer it is scattered across project files and nobody has assembled it.

Training is apprenticeship. New assessors ride along, absorb what they can, and become independent when someone judges they are ready. It works, slowly, and it transfers whatever the mentor happens to mention on the days they were together.

And there is a defensive reason nobody looks: a documented record of inter-assessor variance is a document opposing counsel would enjoy having. That concern is real and it is also the reason a known problem has gone unexamined for thirty years.

## What a Fix Looks Like
Make the judgment explicit and measure the variance where it can be measured without manufacturing it.

**Structured observations with reasoning.** Not just "roof — fair — 8 years remaining" but the specific conditions observed and how each affected the estimate. A controlled vocabulary per component type covers most of what assessors actually say, and it makes two assessors' judgments comparable for the first time.

**Calibration from the existing overlap.** The firm does not need a study. Buildings get assessed more than once — on resale, refinance, or portfolio review — often by different assessors. Those pairs already exist in the archive. Comparing them is free and answers the question directly.

**Peer benchmarking, held internally.** Every assessor should be able to see how their remaining life estimates and repair totals compare to the firm's distribution for similar components and building types. Most variance is unconscious, and simply showing it removes a good deal of it.

**Observation patterns as training material.** When a senior assessor records that a specific condition drove a specific adjustment, that is a teachable unit. A library of them, indexed by component and building type, is what a new assessor currently has to acquire by riding along for two years.

The liability concern is manageable and is mostly an argument for doing this rather than against it: a firm that measures and reduces variance is in a materially better position than one that has never looked, and structured observation records make each individual report better documented than the narrative it replaces.

## Who Feels the Pain
Junior assessors, learning by osmosis. Senior assessors, who are the quality ceiling and cannot be cloned. Practice leaders, who cannot answer a client asking why two reports on the same asset differ. And lenders, whose escrow requirement depends on which engineer was available that week.

## Impact If Fixed
Consistency is the product in a business where clients cannot evaluate the technical work and therefore buy on reputation and price. A firm that can demonstrate low inter-assessor variance has an argument no competitor is making, and it compresses the two-year ramp on new assessors in a market where qualified field staff are the binding constraint on growth.
