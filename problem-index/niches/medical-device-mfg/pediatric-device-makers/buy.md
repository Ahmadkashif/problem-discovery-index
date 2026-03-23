# Multi-Size-Variant Production Management

**Niche:** [[niches/medical-device-mfg/pediatric-device-makers/profile|Pediatric Device Manufacturers]]
**Industry:** [[industries/medical-device-mfg|Medical Device Manufacturing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ERP systems handle BOMs and production planning for single-size products efficiently, but a pediatric device with 5-8 size variants (neonate through adolescent) generates exponential BOM complexity that standard ERP configuration cannot manage without extensive customization.
**Tags:** #workflow-orchestration #data-integration #automation

## The Problem
A single pediatric orthopedic implant product line may require 6 sizes spanning neonate to adolescent, each with its own BOM (different component dimensions, sometimes different materials), its own tooling, its own sterilization packaging, and its own labeling — but sharing 60-80% of the manufacturing process. Production planning must balance inventory across sizes when demand per size is low and unpredictable (a hospital might order 2 units of size 3 and 0 units of size 6 one quarter, then reverse the next). Standard ERP treats each size as a separate SKU with independent demand forecasting, but the shared tooling and process steps create dependencies that the ERP cannot model.

## What Already Exists
SAP, Oracle, and Epicor handle multi-variant product configuration through variant BOMs and configurable routing. These capabilities exist but require extensive implementation customization (50-100 hours of ERP configuration per product family) that small pediatric device companies cannot afford. Smaller ERPs (NetSuite, IQMS) have more limited variant management.

## The Customization Gap
The system needs to model the specific structure of size-variant medical devices: shared base process with size-specific branches (component selection, tooling setup, packaging), cross-size demand pooling for production scheduling (produce all sizes when any size triggers a production run), size-specific sterilization and labeling requirements, and growth-accommodating design tracking (which design features change across sizes and which are constant). This structured variant model must generate individual DHRs per size while sharing process documentation across the common steps.

## Target Customer
Operations managers at pediatric device companies producing 3+ product families with 4+ size variants each. Approximately 100-150 US manufacturers.

## Impact If Solved
BOM management effort drops by 50-60% per product family. Production scheduling optimization across size variants reduces inventory carrying cost by 20-30%. New size variant introduction (adding a size to an existing product line) drops from 4-6 weeks to 1-2 weeks of configuration.
