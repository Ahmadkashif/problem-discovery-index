# Document Ingestion Adapted to OEM Procedure Structure

**Niche:** [[niches/auto-body-shops/repair-procedure-publishers/profile|Repair Procedure & Service Information Publishers]]
**Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Document AI extracts text, tables, and layout well; a repair procedure's meaning lives in the relationship between a numbered step, a diagram callout, a torque table, and a warning box, and general extraction flattens exactly that.
**Tags:** #cnns #object-detection #semantic-segmentation #transformers #bert #transfer-learning #graph-neural-networks #evaluation-metrics #automation #data-integration #workflow-orchestration

## The Problem
The publisher's core industrial process is converting manufacturer documentation into structured, vehicle-indexed content. The source is heterogeneous by construction — each manufacturer publishes in its own format, structure, and terminology, and revises those without notice — so the conversion is largely manual. Technical writers read procedures and re-express them in the house structure, at a volume set by the model year calendar rather than by available staff. The bottleneck is not comprehension but throughput, and throughput determines how deep coverage goes on lower-volume vehicles, which is where the corpus is weakest and where competitors are weakest too.

## What Already Exists
Document intelligence is a strong and competitive market. Azure Document Intelligence, Google Document AI, AWS Textract, and several specialist vendors handle layout analysis, table extraction, figure detection, and key-value extraction at high accuracy on technical documents. Fine-tuning on domain documents is well supported. For turning a PDF into structured text with preserved layout, the off-the-shelf answer is genuinely good.

## The Customization Gap
These tools produce a faithful representation of the page and stop there, and the page is not the unit of meaning. A repair procedure is a graph: steps that reference diagram callouts, torque values that apply to specific fasteners identified only in an illustration, warnings scoped to a subset of steps, prerequisites stated three sections earlier, and applicability conditions — this trim, this build date, this equipment package — that determine whether the procedure applies at all. General extraction flattens the graph into a sequence, and every one of those relationships has to be reconstructed by a human afterward. The adaptation is a domain schema that models procedures as that graph, with extraction trained to populate it: callout-to-part linking across text and illustration, torque and specification binding to the fastener rather than to the paragraph, applicability conditions as first-class structured fields, and prerequisite and warning scoping resolved explicitly. Extraction confidence must be calibrated per relationship, because a wrongly bound torque specification is a safety issue and belongs in a human queue rather than in the corpus.

## Target Customer
Directors of content operations and automotive research leads at procedure publishers, and the technical writers whose throughput currently sets how far coverage extends into the vehicle long tail.

## Impact If Solved
Raises coverage depth without raising headcount, in the segment of the corpus where subscribers most often come up empty. Structured procedure graphs also unlock capabilities the flat corpus cannot support — answering whether a given repair triggers a calibration requirement, or which procedures a specific fastener change affects — which are exactly the questions the search demand map shows technicians asking most and finding least.
