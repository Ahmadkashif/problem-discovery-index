# Weight-Based Estimation from Virtual Surveys

**Niche:** [[niches/moving-companies/long-distance-interstate/profile|Long-Distance Interstate Movers]]
**Industry:** [[industries/moving-companies|Moving Companies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Virtual survey tools generate inventory counts, but interstate movers need weight estimates — and converting inventory to weight requires the tacit judgment of an experienced estimator.
**Tags:** #cnn #object-detection #computer-vision #regression #tacit-knowledge-ml #revenue-impact

## The Problem
Interstate moving is priced by weight, not hours. A binding estimate requires predicting the total shipment weight before the truck is loaded — the actual weight is determined at the certified scale after loading. An experienced estimator walks the home and estimates weight within 10-15% by reading furniture density (solid oak vs. particle board), counting boxes and estimating their fill level, and factoring in items that weigh more than they look (cast iron, books, tools). Virtual survey tools like Yembo generate inventory counts (3 sofas, 15 boxes, 1 piano) but don't estimate per-item weight — they leave the weight judgment to the estimator, who may not be present for a virtual survey.

## What Already Exists
Yembo and MoveSnap provide video-based virtual surveys that generate itemized inventory lists. AMSA (American Moving and Storage Association) publishes standard weight tables for common household items. SmartMoving has an inventory-to-weight calculator based on industry averages. None account for the density variation within item categories — a solid hardwood dresser weighs 2-3x more than a flat-pack IKEA equivalent, but both show up as "dresser" in the inventory.

## The Customization Gap
The system needs to move beyond category-level weight tables to visual density estimation: using the video frames from a virtual survey to classify items not just by type (dresser, sofa, bookshelf) but by apparent density (solid wood vs. composite, fully loaded bookshelf vs. partially filled, box weight class based on size and contents label). This requires a computer vision layer trained on labeled moving images where items have been weighed post-move. The ground truth exists in certified scale tickets but is never linked back to the survey video.

## Target Customer
Interstate moving companies that conduct 100+ virtual surveys per month and need weight estimates within 10% to produce accurate binding quotes.

## Impact If Solved
Reduces weight estimation error from +/-20% (junior estimators with virtual surveys) to +/-8%, preventing $2,000-$5,000 per misquoted binding estimate. Enables virtual surveys to replace in-home visits for 60-70% of interstate quotes, saving $75-$150 per in-home visit in estimator time and travel.
