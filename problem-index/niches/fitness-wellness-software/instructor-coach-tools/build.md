# One Week Across Four Employers

**Niche:** [[niches/fitness-wellness-software/instructor-coach-tools/profile|Instructor & Coach Tools]]
**Industry:** [[industries/fitness-wellness-software|Fitness & Wellness Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An instructor teaching at four studios assembles their week from four systems and a group chat, and every product in the industry is scoped to one studio because every product is sold to one studio.
**Tags:** #data-integration #workflow-orchestration #evaluation-metrics #confidence-intervals #optimization-fundamentals #automation #worker-facing #revenue-impact
**Contested on:** Every serious competitor building for instructors is fighting to assemble a week that spans several studios — schedule, sub requests, availability and pay — into one place, and whoever the instructors actually carry takes the layer above the studios.

## The Problem
Monday. An instructor teaches at 6am at one studio, 9:30 at another across town, and 6pm at a third. Wednesday a fourth studio wants to add a class and needs to know if she is free, which she answers from memory. Thursday a sub request arrives in a group chat while she is teaching; by the time she sees it, it is covered or it is not and nobody knows which. Her availability is stated differently to each studio and is out of date at two of them. Her own record of what she taught is a note on her phone. This is the normal working life of the workforce that delivers the entire product.

## Why Nobody Has Built This
The business model of the category is studio software, and a cross-studio instructor product has no obvious buyer — the instructor will not pay much and the studios have no interest in a layer that makes their instructors more mobile. That is a real commercial problem and it is the reason this has not been built, not a technical one. The route through it is that the instructor-facing layer is genuinely valuable to studios too, because sub coverage and availability accuracy are studio problems that an instructor-side tool solves better than any studio-side one can.

## What to Build
An instructor-held application that aggregates across studios. Schedules are pulled from each studio's platform where an integration is possible and entered or parsed from messages where it is not, producing one week. Availability is stated once and published to every studio that subscribes to it, which removes the most common cause of scheduling friction on both sides. Sub requests arrive in one place with the relevant details and are accepted with a tap, and matching considers who is actually free and qualified rather than broadcasting to everyone. Classes taught accumulate as a personal record, with rates attached, so pay reconciliation becomes possible. The commercial model has to be honest about who benefits: studios will pay for reliable availability and faster sub coverage, and the instructor should not be charged for the tool that makes their own working life manageable.

## Target Customer
Instructors directly, with studios and platform vendors as the paying side; also the larger multi-location operators, for whom instructor scheduling across sites is already a recognised cost.

## Impact If Built
The instructor workforce carries an administrative burden nobody designed and nobody owns, in a role with low pay and high turnover where the friction is a genuine contributor to people leaving. Aggregating the week is a working-life improvement first and a studio operations improvement second — and the second is what makes it fundable.
