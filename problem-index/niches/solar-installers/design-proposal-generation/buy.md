# Aurora Instant Design Accuracy Enhancement

**Niche:** [[niches/solar-installers/design-proposal-generation/profile|Design & Proposal Generation]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Aurora's Instant Design feature auto-generates solar designs from satellite imagery, but 40-60% of designs require manual correction for roof segmentation errors, misplaced panels, and missed obstructions — improving the CV models to achieve 90%+ first-pass accuracy would make Instant Design reliable enough for customer-facing use without human review.
**Tags:** #semantic-segmentation #object-detection #automation #quick-win #cnns

## The Problem
Aurora's Instant Design uses computer vision to segment roofs from satellite imagery and auto-place panels. When it works, it produces a usable design in seconds. When it doesn't — and it fails on 40-60% of complex roofs — the designer must manually correct the 3D model: redrawing roof planes, adjusting heights and tilts, removing panels from obstructions, and fixing setback violations. The manual correction process takes 10-20 minutes, sometimes longer than designing from scratch. The unreliability means design managers can't trust Instant Design for customer-facing proposals, requiring human review on every design regardless. Common failure modes: hip roof intersections segmented incorrectly, dormers missed or merged with the main roof, skylights not detected, tree shade from adjacent lots not modeled, and multi-level roofs with incorrect height assignments.

## What Already Exists
Aurora's CV pipeline handles roof detection, plane segmentation, height estimation from shadow analysis, and panel placement optimization. The production modeling engine is excellent. The weak link is the initial roof model accuracy — everything downstream depends on correct roof geometry, and errors in segmentation cascade into wrong production estimates and incorrectly placed panels.

## The Customization Gap
Three improvement areas: (1) roof segmentation model upgrade — fine-tune the segmentation model on a larger, more diverse dataset of complex residential roofs (hip roofs, cross-gable, gambrel, mansard, dormered, multi-level), with particular focus on the failure modes that cause the most manual correction time; (2) obstruction detection model — train a dedicated object detection model for roof obstructions (skylights, chimneys, plumbing vents, HVAC units, satellite dishes) using Aurora's massive library of manually corrected designs as training data — every time a designer removes panels from a skylight that Instant Design missed, that's a labeled training example; (3) confidence scoring — for each auto-generated design, output a confidence score based on the models' uncertainty, and route low-confidence designs to human review while releasing high-confidence designs for instant customer delivery.

## Target Customer
Aurora Solar as the platform, seeking to improve Instant Design reliability to justify marketing it as a sales acceleration tool. Aurora's 8,000+ installer customers who would use Instant Design if they could trust it.

## Impact If Solved
Increases first-pass Instant Design accuracy from 40-60% to 85-95%, making it reliable for customer-facing use on the majority of homes. Reduces average design time from 20-30 minutes to 3-5 minutes (quick review of high-confidence designs). Enables Aurora to market Instant Design as a sales tool rather than a design starting point. Leverages Aurora's unique data asset — millions of human-corrected designs — as training data.
