# Risk Assessment Tools Adapted for Defense Advocacy

**Niche:** [[niches/public-defenders/mental-health-court/profile|Mental Health Court Defense]]
**Industry:** [[industries/public-defenders|Public Defenders]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Risk assessment tools like COMPAS and PSA are used by courts and prosecutors to argue for detention and supervision — defense attorneys need the same tools calibrated for liberty arguments.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #compliance #worker-facing

## The Problem
Courts increasingly use actuarial risk assessment instruments (COMPAS, Public Safety Assessment, ORAS) to make pretrial detention, sentencing, and supervision decisions. These tools produce risk scores that prosecutors cite to argue for incarceration or intensive supervision. Defense attorneys receive these scores but have no tools to challenge them — they can't audit the inputs, don't understand the algorithms, and can't generate counter-assessments that emphasize protective factors (treatment engagement, family support, stable housing) rather than risk factors.

## What Already Exists
Northpointe (Equivant) makes COMPAS, the Arnold Foundation's Public Safety Assessment (PSA) is used in dozens of jurisdictions, and Ohio's ORAS is common in the Midwest. These tools are designed for court administration and prosecution — they assess risk of recidivism and flight, not the client's capacity for rehabilitation. Academic tools like the HCR-20 and LSI-R exist in clinical settings but aren't integrated into legal defense workflows.

## The Customization Gap
Defense attorneys need a risk assessment interpretation layer: given a client's COMPAS or PSA score, what specific inputs drove the score? Which inputs are incorrect or based on stale data? What would the score look like if the client completed treatment, secured housing, or obtained employment? The tool should generate "what-if" scenarios for mitigation arguments — showing the court how the risk profile changes with the proposed treatment plan. It should also flag known biases in the assessment instrument (racial, socioeconomic) that the defender can raise in hearings.

## Target Customer
Mental health court defenders and pretrial services defense advocates in jurisdictions using actuarial risk assessment, estimated at 200+ counties.

## Impact If Solved
Enables defense attorneys to engage substantively with risk assessment evidence rather than accepting scores at face value. Estimated 15-25% increase in successful diversion arguments when defenders can present data-driven counter-narratives to prosecution risk scores.
