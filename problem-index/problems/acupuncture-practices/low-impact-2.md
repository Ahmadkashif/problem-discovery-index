# Chinese Herbal Dispensary and Formula Management

**Industry:** [[acupuncture-practices|Acupuncture Practices]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic inventory management tracks stock levels, but it doesn't know that Chai Hu (Bupleurum) in a Xiao Yao San formula must be from a specific grade supplier, that the formula requires 7 herbs in precise ratios, that the patient's concurrent use of blood thinners contraindicates Dan Shen (Salvia), or that California requires different labeling than Oregon for herbal products.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #time-series-forecasting #probability-distributions #expectation-variance-covariance

## The Problem
Approximately 30-40% of acupuncture practices prescribe Chinese herbal formulas — either as raw herbs, granule concentrates, or patent pills. A practice maintaining a raw herb dispensary stocks 150-300 individual herbs, each with expiration dates, quality grades, and supplier variability. Classical formulas (Gui Zhi Tang, Si Wu Tang, Xiao Yao San) combine 4-15 herbs in specific ratios. Practitioners frequently modify classical formulas by adding or removing herbs based on the patient's TCM pattern. Inventory management is a nightmare: tracking which herbs are running low, reordering from approved suppliers (GMP-certified, heavy metal tested), managing lot numbers for traceability, checking for herb-drug interactions, and complying with state-specific labeling requirements.

## What Already Exists
Unified Practice offers basic herbal formula management with a pre-loaded formula database. Crane Herb Company and Mayway provide online ordering with some inventory integration. E-Fong and Sun Ten offer granule dispensing systems. No system integrates formula modification tracking, patient-specific herb-drug interaction checking, inventory management with automated reordering, and state-specific compliance labeling in a single platform.

## The Customisation Gap
A TCM herbal management system needs to: (1) maintain a complete Materia Medica database with classical formulas, modification principles, and contraindications, (2) check herb-drug interactions against the patient's medication list (critical safety gap — e.g., Ma Huang/Ephedra with hypertension medications, Dang Gui/Angelica with blood thinners), (3) track inventory by herb, lot number, and expiration with demand forecasting based on prescribing patterns, (4) auto-generate patient labels meeting state-specific requirements (ingredients, dosage, practitioner name, cautions), and (5) predict reorder points based on formula prescribing frequency and seasonal demand patterns.

## Impact If Solved
Reduces herb-drug interaction risk (currently estimated at 8-12% of herbal prescriptions have potential interactions that are unchecked). Cuts inventory waste from expired herbs by 30-40% through demand-based ordering. Saves 4-6 hours per week of manual dispensary management. Enables practices to maintain a broader formulary with lower working capital through optimized inventory.
