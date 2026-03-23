# Manual BOM Traversal for Change Impact

**Niche:** [[niches/contract-manufacturing/engineering-change-order-management/profile|Engineering Change Order Management]]
**Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** When an ECO changes a single component, engineers manually trace where that component appears across every BOM, every process routing, and every quality document — a 2-8 hour detective exercise that ERP where-used queries partially address but process and quality document traversal remains entirely manual.
**Tags:** #data-integration #automation #worker-facing

## The Problem
An OEM changes the torque specification on a fastener. The CM engineer must determine: which assemblies use this fastener (BOM where-used query — ERP can do this), which process routings have a torque operation for this fastener (not linked to BOM in most ERPs — must be manually traced), which work instructions reference the old torque spec (document search across the quality system), which inspection criteria include torque verification (another document search), and whether the torque change affects any validated process (cross-reference with process validation records). The BOM query takes 5 minutes in ERP. The process, quality, and validation traversal takes 2-8 hours because these documents are not linked to BOM components in any systematic way.

## Why It's Still Broken
ERP systems manage BOM structures with where-used queries. MES systems manage process routings. QMS systems manage quality documents. These three systems are not linked at the component level — there is no single query that returns "everywhere this component appears across BOM, process, and quality documentation." Integration between ERP, MES, and QMS at the component level requires a shared component identifier across all three systems, which most CMs have not implemented because the systems were deployed by different teams at different times with different data models.

## What a Fix Looks Like
A cross-system component linkage index that maps each BOM component to its associated process steps (from MES routings), quality documents (from QMS document metadata), and validation records (from validation database). When an ECO changes a component, a single query returns: all BOMs, all process steps, all quality documents, and all validation records that reference the changed component. The index is built once through a reconciliation exercise and maintained automatically as BOMs, routings, and documents are updated.

## Who Feels the Pain
Engineers who perform the manual traversal for every ECO — spending hours on data gathering before they can begin the actual engineering analysis. Quality engineers who discover missed document updates weeks after an ECO was implemented, creating non-conformance situations where production runs against outdated specifications.

## Impact If Fixed
Reduces ECO impact data gathering from 2-8 hours to 10-15 minutes per change. Ensures 100% of affected documents are identified — eliminating the missed-update non-conformances that currently create quality escape risk. For a CM processing 10 ECOs/week, saves 20-80 engineering hours weekly on data gathering alone.
