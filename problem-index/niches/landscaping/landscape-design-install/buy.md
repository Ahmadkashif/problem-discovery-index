# Design-to-Estimate Bridge

**Niche:** [[niches/landscaping/landscape-design-install/profile|Landscape Design & Install]]
**Industry:** [[industries/landscaping|Landscaping]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Landscape design software and estimating software exist as separate products with no data bridge — every design change triggers a full manual re-estimate, and the material quantities in the estimate frequently don't match the design intent.
**Tags:** #automation #data-integration #workflow-orchestration #quick-win

## The Problem
A landscape designer creates a planting plan in Vectorworks or SketchUp specifying 25 Knockout Roses, 8 Japanese Maples, 400 sq ft of Pennsylvania bluestone patio, and 120 linear feet of segmental retaining wall. An estimator then opens a completely separate tool — LMN, Aspire, or an Excel spreadsheet — and manually counts every item from the plan, looks up current pricing, estimates labor hours per task based on experience, and builds the proposal. This process takes 4-8 hours per project and introduces transcription errors: the designer drew 25 roses but the estimator counted 22, or the wall height changes from 24 inches to 36 inches in the design but the estimate still uses the 24-inch material and labor calculations. When the client requests a design revision — "can we make the patio smaller and add more plantings?" — both the design and estimate must be independently updated, doubling the revision time and re-introducing the risk of mismatches.

## What Already Exists
Vectorworks Landmark has a plant scheduling feature that exports a plant list, but it doesn't connect to material pricing or labor estimating. LMN and Aspire have robust estimating engines with assembly-based pricing (a "retaining wall" assembly includes block, cap, adhesive, gravel base, geogrid, and labor hours per linear foot per height) but cannot import from any design tool. BidScapes bridges Vectorworks to estimating but is limited to plant counts and doesn't handle hardscape material takeoffs. No tool provides a live two-way connection between a landscape design and its estimate.

## The Customization Gap
The missing layer is a data bridge that translates design objects into estimating assemblies in real time. When the designer places a "segmental retaining wall, 36 inches tall, 120 linear feet" in the design tool, the estimating system should automatically generate the full material list (specific block count by type, cap units, adhesive tubes, gravel tonnage, geogrid square footage) and labor estimate (crew size x hours based on wall height and access conditions) — and update both when the designer changes the wall length or height. This requires mapping design object types to estimating assemblies with parametric rules (e.g., wall material quantities scale non-linearly with height because geogrid requirements change at 24-inch thresholds). The bridge also needs nursery pricing integration: when the designer specifies a 6-foot Japanese Maple, the system should pull current availability and pricing from regional nursery inventories rather than using last season's catalog price.

## Target Customer
Landscape design-build firms with $1M-10M in revenue that produce 30-100 design-build proposals per year, where the estimating labor per proposal (4-8 hours) limits the number of proposals the firm can produce and delays client response time.

## Impact If Solved
Eliminates 4-8 hours of manual estimating per project and ensures design-to-estimate accuracy, reducing proposal turnaround from 5-10 business days to 1-2 days. For a firm producing 60 proposals per year, this recovers 240-480 hours of estimator time and eliminates the 5-10% of projects where estimate-to-design mismatches cause budget overruns on installation.
