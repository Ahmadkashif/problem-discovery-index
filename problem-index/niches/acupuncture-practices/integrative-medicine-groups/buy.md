# Multi-Provider EHR with Unified Patient Timeline

**Niche:** [[niches/acupuncture-practices/integrative-medicine-groups/profile|Integrative Medicine Group Practices]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Multi-provider EHRs support scheduling for different practitioner types but don't unify clinical documentation into a single patient narrative.
**Tags:** #transformer #text-generation #nlp #data-integration

## The Problem
Integrative practices buy multi-provider EHR platforms expecting a unified patient record. What they get is parallel siloed records — the acupuncture SOAP note stream and the chiropractic SOAP note stream exist side-by-side but are not synthesized. A practice director cannot pull up a single view showing "here's everything happening with this patient across all modalities and whether it's working."

## What Already Exists
Jane App supports acupuncture, chiropractic, massage, and naturopathy scheduling and charting. Practice Fusion and DrChrono handle multi-provider workflows. ChiroTouch is strong for chiropractic but bolts on acupuncture support. All allow multiple practitioners to document for the same patient, but none aggregate these notes into a unified clinical timeline or cross-modality progress view.

## The Customization Gap
The EHR needs a synthesis layer: an automated patient summary that pulls key data points from each modality's notes (diagnosis, treatment performed, outcome indicators) and presents them chronologically. It also needs shared outcome measures — a pain VAS score entered by the acupuncturist should appear in the chiropractor's view without re-entry. This requires modality-aware data extraction and normalization, not just a combined note feed.

## Target Customer
Practice administrators at 4-10 provider integrative clinics paying $500-1,500/month for EHR who would pay an additional $200-400/month for a unification layer.

## Impact If Solved
Eliminates 15-20 minutes of inter-provider communication per shared patient per week, and gives practice directors data to evaluate which modality combinations produce the best outcomes.
