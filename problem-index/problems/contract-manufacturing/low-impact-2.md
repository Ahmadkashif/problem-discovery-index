# Automated Visual Inspection for Surface Defect Detection

**Industry:** [[contract-manufacturing|Contract Manufacturing]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic computer vision models can detect anomalies in images, but don't know a specific part's acceptance criteria — which surface conditions are cosmetic defects vs. acceptable variation vs. functional defects, as defined in the OEM's workmanship standard for that specific part number — the product-specific classification logic that makes automated inspection useful rather than a source of false rejects.
**Tags:** #cnns #object-detection #transfer-learning #loss-functions #backpropagation #gradient-descent #evaluation-metrics #matrix-algebra #compliance

## The Problem

Manual visual inspection is one of the highest labor-cost and highest-variability steps in contract manufacturing. Human inspectors classifying surface conditions — scratches, pitting, discoloration, porosity, weld spatter, solder bridging — make different accept/reject decisions based on experience level, fatigue, and subjective interpretation of the workmanship standard. Inspector-to-inspector variation creates quality escape risk (defective product passed) and over-rejection (acceptable product scrapped), both of which destroy program profitability.

Automated optical inspection (AOI) systems exist for PCB assembly (Koh Young, Mirtec) and semiconductor fab. For machined parts, castings, molded plastics, and medical device subassemblies, automated visual inspection deployment is limited because each part requires a custom inspection program — defining the field of view, illumination, comparison reference, and accept/reject criteria for that specific part number.

## What Already Exists

Generic anomaly detection models (PatchCore, EfficientAD) can identify image regions that deviate from a reference image without labeled defect examples. These work well for detecting any anomaly but cannot classify defect type, severity, or accept/reject disposition per the OEM workmanship standard — which may accept minor surface scratches but reject pitting of the same visual severity.

## The Customisation Gap

A production-ready visual inspection model needs: (1) part-specific reference image library — acceptable reference images under controlled illumination for that part number; (2) defect taxonomy from the OEM workmanship standard — translating the written standard into machine-readable classification categories; (3) severity calibration — training the model on labeled examples of accept vs. reject conditions at the boundary, where inspector judgment matters most; (4) illumination control to ensure consistent imaging conditions on the production line. The workmanship standard translation and boundary-condition calibration are the customization gap that makes generic anomaly detection insufficient for production deployment.

## Impact If Solved

Reduces inspector headcount or redeploys inspectors to boundary-condition review rather than routine pass/fail decisions. Eliminates inspector-to-inspector variation — the primary source of quality escape risk in manual inspection. For a CM with 10 dedicated inspection staff at $55,000/year fully loaded, reducing inspection headcount by 30% saves $165,000 annually while improving consistency.
