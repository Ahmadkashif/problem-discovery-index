# One Operation, Two Unrelated Crafts

**Niche:** [[niches/print-on-demand-platforms/decoration-production/profile|Decoration Production]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Printing an image onto fabric and converting it into a stitch program are different crafts with different failure modes, and the platform routes both through one workflow with one file check and one quality standard.
**Tags:** #workflow-orchestration #evaluation-metrics #automation #data-integration #confidence-intervals #descriptive-statistics #compliance #worker-facing
**Contested on:** Not terminal — the contest differs by decoration method, and the decomposition is recorded in the profile.

## The Problem
A design is offered on a printed shirt and an embroidered cap. The same file goes through the same preflight, which checks resolution and dimensions — a sensible check for the print and nearly meaningless for the embroidery, which needs the artwork simplified, the colours reduced to available thread, the detail assessed against a minimum stitch size and a stitch file generated. The cap is produced from a digitisation somebody did quickly, puckers on the crown, and is reprinted twice. The workflow treated two crafts as one process because both involve putting a design on a product.

## Why Nobody Has Built This
The platform's core competence is the integration and order layer, which genuinely is method-agnostic, and the decoration specifics were pushed down to the facility. Embroidery is a smaller share of volume and inherits the printing workflow by default. Digitisation is a skilled manual craft that the platform treats as a supplier's problem. And the failures are attributed to the facility rather than to a workflow that never gave them what they needed.

## What to Build
Build the common substrate and let the methods diverge. What genuinely generalises is the order, the product model, the placement geometry, the facility capability record and the outcome capture — and the product geometry model in particular serves every method and is frequently absent, which is why placement failures recur everywhere. Make decoration method a first-class attribute driving the whole workflow, so a file destined for embroidery enters a different preparation path from the start. Maintain capability by facility and method rather than by facility, since a network partner excellent at direct-to-garment may be poor at embroidery and the routing currently cannot express that. Capture outcomes with method-specific failure vocabularies, since puckering and colour washout are not comparable and a single defect taxonomy makes both unanalysable. Model the product's physical geometry once — panels, seams, curvature, print areas by size — which every method needs and which is the most reusable asset here. Support method-specific preflight as a plug-in rather than as a shared check. Report cost and failure rates by method, since they differ substantially and a blended figure conceals which one is losing money. And let merchants know which methods their design suits, which is a product decision the platform is uniquely placed to make.

## Target Customer
Platform production engineering, partner facilities, and the merchants offering one design across incompatible decoration methods.

## Impact If Built
Two crafts share a workflow because both put a design on a product, and the shared file check is meaningless for one of them. The product geometry model is the genuinely reusable piece and is frequently absent, which is why placement failures recur across every method.
