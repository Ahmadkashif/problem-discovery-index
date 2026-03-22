# Mobile-First Large Animal Field Documentation Platform

**Niche:** [[niches/veterinary-practices/large-animal-equine/profile|Large Animal & Equine]]
**Industry:** [[industries/veterinary-practices|Veterinary Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A mobile-first practice management platform built for ambulatory veterinary medicine — offline-capable medical records, GPS mileage tracking, multi-animal farm visit invoicing, and truck-based drug inventory management that replaces the nightly 90-minute documentation session.
**Tags:** #large-language-models #feature-engineering #data-integration #worker-facing #automation #tacit-knowledge-ml

## The Problem
Large animal and equine veterinarians perform 4-8 farm calls per day, seeing 1-15 animals per stop. During each visit, they perform examinations, diagnostic procedures, treatments, and sometimes field surgery — all while standing in a barn, pasture, or paddock with no desk, no keyboard, and often no cell signal. Documentation is deferred until the vet returns home, relying on handwritten notes scribbled between stops, photos taken on a personal phone, and memory. By the time the vet sits down to type records at 8 PM, critical details have faded — drug doses administered from the truck pharmacy, specific lameness grades, palpation findings for reproductive exams. The resulting records are incomplete, inconsistent, and often entered days after the visit. This creates medical liability, billing inaccuracy, and an inability to track treatment outcomes across visits.

## Why Nobody Has Built This
Building for ambulatory vets requires solving three simultaneous problems: (1) offline-first architecture — farm calls happen in areas with no cell signal, so the app must function completely offline and sync when connectivity returns, (2) hands-free input — the vet's hands are on the animal, covered in exam gloves, or holding instruments, so data entry must work via voice with species-specific medical vocabulary recognition, and (3) multi-animal visit structure — a single farm call may involve examining 3 horses for pre-purchase, treating a colicking horse, and vaccinating 8 broodmares, each requiring separate medical records but billed as a single visit with shared travel fees. Existing PMS platforms assume one patient per appointment at a fixed location, and retrofitting them for this workflow has failed repeatedly.

## What to Build
A mobile application (iOS/Android) designed for field veterinary medicine. Core features: (1) voice-to-record documentation using a large language model fine-tuned on veterinary terminology, species-specific anatomy, and common large animal procedures — the vet dictates "Right front lameness grade 3 out of 5, positive to distal limb flexion, blocked sound to low four-point nerve block, radiographs taken of the navicular region" and the system structures it into a medical record, (2) offline-capable architecture that stores records locally and syncs when connectivity returns, (3) GPS-based mileage tracking that automatically calculates travel fees based on practice-configured rates, (4) truck pharmacy inventory — scan or select drugs administered in the field, auto-deduct from truck stock, trigger reorder alerts, (5) multi-animal farm visit invoicing that groups procedures by animal, applies herd discounts, and adds shared travel and call fees.

## Target Customer
Equine and large animal veterinarians (solo or 2-3 vet practices) currently documenting on paper or in their heads during farm calls and spending 60-90 minutes every evening typing records into a companion-animal-oriented PMS, willing to pay $149-249/month for a purpose-built mobile solution.

## Impact If Built
Eliminates the nightly 60-90 minute documentation session for 5,000+ large animal and equine practitioners, improving record quality and reducing medical liability exposure. Accurate truck pharmacy tracking reduces drug waste (estimated 8-12% of ambulatory drug inventory is lost to expiration or miscounting). Automated mileage and multi-animal invoicing recovers $15K-30K per year in travel fees that currently go unbilled because the vet forgets or underestimates distance.
