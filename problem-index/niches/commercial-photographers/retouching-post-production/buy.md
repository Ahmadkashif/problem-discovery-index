# AI Background Removal Adapted to Brand Style Guides

**Niche:** [[niches/commercial-photographers/retouching-post-production/profile|Retouching & Post-Production]]
**Industry:** [[industries/commercial-photographers|Commercial Photographers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Background-removal APIs already cut out products in seconds; they don't know this brand wants a 4% shadow, a 6% margin and a grey of 245, or that its knitwear fringe must stay.
**Tags:** #semantic-segmentation #cnns #transformers #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to return brand-consistent, spec-compliant edits overnight at a defect rate the client's QA never sees, and whoever automates the routine edit without letting errors escape takes the account.

## The Problem
Generic cutout tools produce a clean mask and a white background. A brand's style guide asks for much more: specific shadow type and opacity, margins and alignment, background value, treatment of transparent parts, retained texture at edges, and different outputs per channel. Retouchers re-do the automated output to meet the guide.

## What Already Exists
AI background removal and product-editing APIs (Photoroom, remove.bg, Adobe's automated selection tools) and outsourced editing services that combine AI with human editors.

## The Customization Gap
The adaptation needs: each brand's style guide encoded as parameters (shadow model, margins, alignment, background value, crop rules); per-category handling for hard materials (fringe, mesh, glass, hair) with uncertainty maps so humans touch only the uncertain regions; ghost-mannequin compositing from paired shots; colour checks against the sample reference; and per-channel exports that validate against retailer rules.

## Target Customer
Post-production managers at studios and retouching houses serving many brands with different style guides.

## Impact If Solved
The automated pass delivers on-guide images for the routine majority, and retoucher time goes to the hard tail, cutting per-image minutes substantially (estimate: by half on standard packshots).
