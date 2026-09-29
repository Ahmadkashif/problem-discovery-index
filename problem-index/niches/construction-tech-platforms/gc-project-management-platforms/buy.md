# Reality Capture Joined to the Schedule

**Niche:** [[niches/construction-tech-platforms/gc-project-management-platforms/profile|General Contractor Project Management]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Reality capture vendors have made site progress objectively observable and sell it as a visual record, while the schedule it should be validating is still updated from percentages supplied by the trades.
**Tags:** #cnns #semantic-segmentation #object-detection #evaluation-metrics #confidence-intervals #data-integration #automation #workflow-orchestration
**Contested on:** Every serious competitor in GC project management is fighting to tell a project team which activities will slip weeks before the schedule shows it — and whoever forecasts a slip earliest, with evidence a superintendent believes, takes the account.

## The Problem
A project captures the whole site weekly with a 360 camera or a drone, producing a navigable visual record that is genuinely useful for disputes and remote review. Separately, the schedule is updated in a Friday meeting from percent-complete figures reported by each trade. The two are never compared. So the record that could say objectively that the third floor drywall is 40% done sits beside a schedule that says 65% because that is what was reported, and nobody reconciles them until the discrepancy is large enough to be obvious by walking the floor.

## What Already Exists
OpenSpace, Buildots, Matterport, DroneDeploy and Reconstruct all provide site capture with increasing degrees of automated progress detection, and several already classify installed elements by trade. Photogrammetry, point cloud processing and construction-element segmentation are all mature enough to be bought rather than built. The schedule side is equally available: P6 and Microsoft Project expose their data, and platform APIs expose the activity structure. Both halves are purchasable products in wide deployment.

## The Customization Gap
The adaptation is the join, and it is more specific than it sounds. It requires: (1) mapping observed installed quantities to schedule activities, which needs a location breakdown structure — the correspondence between a physical area and an activity — that most projects do not maintain and that has to be either captured or inferred; (2) converting observed installation into progress against an activity's defined scope, which is a quantity question rather than a visual one and is where naive percent-of-pixels approaches fail; (3) reconciling observed progress against reported progress and surfacing the divergence as a specific, evidenced conversation rather than as an accusation, since the reported number came from a person who will be in Friday's meeting; (4) handling the trades where visual capture works poorly — anything above ceiling, in wall, or underground — honestly, by reporting coverage rather than implying completeness; and (5) feeding the reconciled progress into the forecast rather than only into a dashboard, which is what makes it worth the trouble.

## Target Customer
General contractors already paying for reality capture and receiving a visual record, and the platform vendors who could make progress objective rather than reported.

## Impact If Solved
An objective progress signal removes the single largest source of noise from the forecast and from the weekly meeting. Projects that reconcile captured against reported progress typically find divergences concentrated in specific trades and areas, which is actionable within a week. The capture is already being paid for; this adaptation is the difference between an archive and an instrument.
