# Simplified Quoting Tool for Custom Fabrication

**Niche:** [[niches/metal-fabrication/small-custom-job-shops/profile|Small Custom Job Shops (<20 Employees)]]
**Industry:** [[industries/metal-fabrication|Metal Fabrication]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Quoting platforms like Paperless Parts and Rapid Quote use 3D model analysis for CNC machining quotes, but small fab shops don't receive 3D models — they get napkin sketches, verbal descriptions, and photos of broken parts that need replacing — and no quoting tool handles this unstructured input.
**Tags:** #large-language-models #transformers #tacit-knowledge-ml #revenue-impact #quick-win

## The Problem
A customer calls a small fab shop and says: "I need a set of handrails for a loading dock, about 40 feet total, with returns at both ends, galvanized, mounted to concrete." The owner estimates material (40 feet of 1.5" pipe rail plus posts, kickplate, baseplate anchors), labor (fit-up, welding, grinding, galvanizing coordination), and produces a quote — typically via text message, email, or a handwritten note. This quoting process depends entirely on the owner's experience-based estimation. No digital quoting tool accepts this kind of unstructured input (verbal descriptions, photos, rough sketches) and produces a material and labor estimate appropriate for custom fabrication.

## What Already Exists
Paperless Parts, Xometry, and Rapid Quote provide instant quoting for CNC machined parts from 3D model uploads. SteelCalc provides structural steel quantity takeoffs. These tools require structured input (3D models, engineering drawings) that small fab shops' customers rarely provide.

## The Customization Gap
A small-shop quoting tool needs: (1) unstructured input acceptance — entering a job description in plain language ("40 feet of pipe handrail, 42" height, galvanized, concrete mount"), a photo of the existing structure, or a rough sketch; (2) material estimation from description — calculating pipe, plate, and consumable requirements from the verbal/visual description; (3) labor estimation calibrated to the shop's actual productivity — not industry averages, but this shop's tracked hours per linear foot of handrail from historical jobs; (4) professional quote generation — turning the estimate into a customer-facing PDF quote with the shop's branding, terms, and signature line.

## Target Customer
Owner-operators who currently quote from memory and lose track of quotes because they're scattered across text messages, emails, and paper notes.

## Impact If Solved
Reduces quoting time from 15-30 minutes of mental estimation and manual document creation to 5 minutes of input and automatic quote generation. Creates a searchable quote history — enabling the owner to reference past quotes for similar jobs, improving consistency. Professional quote presentation improves win rate by 10-15% compared to text-message quotes. For a shop quoting 50 jobs/month, improving win rate by 10% adds 5 additional jobs per month — potentially $25,000-$75,000 in additional annual revenue.
