# Pediatric-Specific Clinical Decision Support for UC

**Niche:** [[niches/urgent-care/pediatric-urgent-care/profile|Pediatric Urgent Care]]
**Industry:** [[industries/urgent-care|Urgent Care]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Pediatric UC providers get clinical decision support that knows a 6-month-old with a 101F fever is a different clinical problem than a 5-year-old with the same fever — with age-appropriate workup recommendations, disposition guidance, and safety-net instructions built into the UC workflow.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #tacit-knowledge-ml #cross-validation #compliance

## The Problem
Pediatric urgent care clinical decisions are age-dependent in ways that general UC decision support does not capture. A febrile infant under 90 days old requires blood cultures, urinalysis, and possibly lumbar puncture — a workup that a 3-year-old with the same fever does not need. An experienced pediatric UC provider applies these age-based decision rules automatically; a new NP or PA (who may have trained primarily in adult medicine) must recall and apply dozens of age-threshold clinical rules while managing throughput. Current EHR systems do not surface age-specific clinical guidance at the point of care — the provider must carry these rules in their head or reference external guidelines (AAP, PECARN) on a separate screen.

## Why Nobody Has Built This
Pediatric clinical decision support systems exist in academic hospital settings (PECARN decision rules for head CT, Rochester criteria for febrile infants) but have never been embedded into UC workflow tools. The challenge is translating evidence-based clinical rules — which are published as academic guidelines — into actionable, workflow-integrated prompts that fire at the right moment without alert fatigue. Pediatric UC is a small market segment, and EHR vendors prioritize adult UC (90%+ of the market) for feature development. Building this requires both pediatric clinical expertise and UC workflow understanding — a rare combination.

## What to Build
A clinical decision support layer for pediatric UC that integrates with the existing EHR and activates based on patient age and chief complaint. When a provider opens a chart for a 2-month-old with fever, the system surfaces: age-specific workup recommendations (Rochester criteria, UTI screening guidance), weight-based dosing calculations for likely medications (acetaminophen, ibuprofen thresholds, antibiotic dosing), age-appropriate vital sign interpretation (highlighting that this patient's heart rate is elevated for age, not just elevated for adults), and disposition guidance (when to send home with safety-net instructions vs. when to transfer to a pediatric ED). The system adapts its recommendations as the provider documents findings — if a febrile infant's urinalysis returns positive, it updates disposition guidance accordingly. Alert sensitivity is calibrated to pediatric UC acuity (less aggressive than PICU, more aggressive than primary care).

## Target Customer
Pediatric UC owners and clinical directors at pediatric-focused UC chains (PM Pediatrics, NightLight, After Hours Pediatrics) and general UCs with significant pediatric volume, staffed by providers who may not be pediatric-trained.

## Impact If Built
Reduces missed high-risk pediatric presentations (estimated 2-4% of pediatric UC visits involve conditions requiring ED-level workup that are undertriaged at UC level). Decreases unnecessary ED transfers for low-risk presentations by giving providers evidence-based confidence to manage locally. Reduces weight-based dosing errors (a leading cause of pediatric medication errors) through automated calculation at prescribing. Provides documentation that supports medical decision-making for the highest-liability patient population in urgent care.
