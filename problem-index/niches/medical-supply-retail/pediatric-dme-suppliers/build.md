# Growth-Triggered Equipment Review and Replacement Scheduler

**Niche:** [[niches/medical-supply-retail/pediatric-dme-suppliers/profile|Pediatric DME Suppliers]]
**Industry:** [[industries/medical-supply-retail|Medical Supply Retail]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No DME system schedules proactive equipment reviews based on a child's growth trajectory — so equipment becomes too small before anyone notices, causing skin breakdown, postural issues, and rushed emergency replacements.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #automation #revenue-impact

## The Problem
A pediatric wheelchair supplier manages 300 active pediatric patients. Each child will outgrow their equipment at a rate determined by age, diagnosis (some conditions affect growth), and individual growth trajectory. Currently, equipment reviews happen reactively: a parent calls when the chair is visibly too small, or a therapist notices at a clinic visit that the child has outgrown the seat width. By then, the child may have been using ill-fitting equipment for months — causing pressure injuries, postural deformities, and discomfort. The replacement process takes 4-8 weeks (assessment, authorization, order, delivery), meaning the total time in suboptimal equipment can stretch to 6+ months.

## Why Nobody Has Built This
Growth-based equipment scheduling requires integrating pediatric growth curve data (CDC/WHO growth charts), diagnosis-specific growth modifiers (children with cerebral palsy may grow differently than typically developing children), equipment sizing specifications from manufacturers, and the insurance re-authorization timeline (Medicaid typically allows wheelchair replacement every 5 years, but growth-based replacements can be authorized earlier with proper documentation). No DME system has integrated these data sources because the pediatric segment is a small fraction of total DME volume.

## What to Build
A growth-tracking and equipment review scheduler that: records the child's measurements at each equipment delivery, plots growth against age-adjusted curves, predicts when the child will outgrow current equipment dimensions (seat width within 1 inch of body width = time to plan replacement), and triggers a proactive review workflow 8-12 weeks before projected outgrowth. The trigger launches the replacement process: parent notification, clinical re-assessment scheduling, insurance pre-authorization initiation, and equipment ordering — all before the child actually outgrows the equipment.

## Target Customer
Pediatric DME suppliers managing 100+ active pediatric patients who want to shift from reactive "the chair is too small" calls to proactive growth-based equipment management.

## Impact If Built
Eliminates 3-6 months of ill-fitting equipment use per child per replacement cycle, preventing skin breakdown and postural complications. Reduces rush-order replacement costs (expedited shipping, temporary loaner equipment) by 40-60%. Demonstrates proactive care that differentiates the supplier from competitors and builds long-term family relationships worth $50K-100K in lifetime equipment revenue per pediatric patient.
