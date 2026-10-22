# Walk-Through Capture That Quantifies While You Walk

**Niche:** [[niches/logistics-consultants/dc-operations-assessments/profile|DC Operations Assessments]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A senior assessor's photos, voice notes and the building's WMS task log could become a quantified findings list during the visit, instead of a memory reconstructed afterwards.
**Tags:** #tacit-knowledge-ml #large-language-models #cnns #object-detection #feature-engineering #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to find, in a two-to-five-day visit, the few constraints that actually cap a building's throughput, and whoever turns a walk-through into a quantified, defensible list fastest wins the implementation work that follows.

## The Problem
The value of an assessment is concentrated in what an experienced assessor notices on the floor — pickers waiting at an empty pick face, pallets staged in an aisle, a packer walking to fetch cartons. Those observations are captured as scattered photos and notes, and each must later be turned into a number: how many labour hours a week, how much throughput, what it would cost to fix. The quantification is where junior staff spend the week after the visit, and where findings are most often challenged by the client.

## Why Nobody Has Built This
Inspection apps capture observations but know nothing of warehouse operations; WMS analytics know the task data but not what the assessor saw. Joining them needs a model of warehouse process, and the market of assessment firms is fragmented and small.

## What to Build
A field tool where the assessor speaks and photographs as they walk; each observation is transcribed, tagged to a process step and location, and matched to the WMS task extract for that zone and hour to estimate its impact — idle time, travel, touches — with a savings range. Photos are screened for recognisable conditions (blocked aisles, overflowing staging, empty pick faces). Every observation the assessor confirms becomes a labelled example of what experienced assessors look for.

## Target Customer
Operations consultancies and the assessment practices of design and labour-standards firms.

## Impact If Built
Findings arrive quantified at the close-out meeting rather than two weeks later (estimate), which is when the client decides whether to buy the implementation.
