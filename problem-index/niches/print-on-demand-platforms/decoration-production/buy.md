# Manufacturing Execution and Quality Systems

**Niche:** [[niches/print-on-demand-platforms/decoration-production/profile|Decoration Production]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Manufacturing built execution systems, traceability and statistical process control decades ago, and print-on-demand production runs on order management plus a printer.
**Tags:** #evaluation-metrics #change-point-detection #descriptive-statistics #confidence-intervals #hypothesis-testing #workflow-orchestration #automation #compliance
**Contested on:** Not terminal — the contest differs by decoration method, and the decomposition is recorded in the profile.

## The Problem
Running production with traceability from input to output, monitoring process parameters, detecting drift before it becomes scrap, and tying every defect back to the machine, material lot and settings that produced it is what manufacturing execution and quality systems do. They are mature, widely deployed and directly applicable. Print-on-demand production is largely an order queue, a press and an inspector at the end, with the process parameters unrecorded and the defect attributed to nothing.

## What Already Exists
Manufacturing execution systems with genealogy and traceability; statistical process control with control charts and drift detection; machine parameter logging and correlation to quality; defect taxonomy and Pareto analysis; and preventive maintenance scheduling driven by output quality.

## The Customization Gap
The adaptation is to a batch size of one with a different input every time. It requires: (1) traceability that records the artwork alongside the machine, ink lot, substrate lot and settings, since the input varies per unit and the usual genealogy assumes a common recipe — capturing the input as part of the record is what makes every defect analysable and is not done; (2) process control on output quality rather than on process parameters alone, since the parameters can be in specification and the result still wrong for a particular artwork; (3) drift detection across a partner network where the platform does not own the machines, which requires the partners to report and is a contractual as much as a technical problem; (4) a defect taxonomy per decoration method, which the build note requires; and (5) economics that fit a unit worth twenty dollars, which rules out the inspection intensity manufacturing assumes and argues for sampling plus prediction.

## Target Customer
Platform and partner production operations, quality functions, and the manufacturing systems vendors for whom unit-batch decoration is an unserved shape.

## Impact If Solved
Traceability and process control are mature and assume a common recipe, which this operation never has. Recording the artwork as part of the production genealogy is what makes every defect analysable and it is the piece nobody captures.
