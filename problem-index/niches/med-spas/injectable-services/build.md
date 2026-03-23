# Visual Injection Mapping & Product Utilization Tracker

**Niche:** [[niches/med-spas/injectable-services/profile|Injectable Services (Botox/Fillers)]]
**Industry:** [[industries/med-spas|Med Spas]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool provides a visual, visit-over-visit injection map that tracks exactly where product was placed on a patient's face and how their anatomy responds over time.
**Tags:** #cnn #object-detection #computer-vision #tacit-knowledge-ml #revenue-impact

## The Problem
Experienced injectors develop mental models of each patient's facial anatomy — where Botox was placed last time, how many units, how the patient metabolized it, where filler migrated. This tacit knowledge is lost when the patient sees a different injector, when notes are vague ("20 units frontalis, 20 units glabella"), or when the injector leaves the practice. The visual, spatial nature of injection planning doesn't map well to text-based charting. A new injector inheriting a patient has to essentially start from scratch, risking overcorrection, product waste, and patient dissatisfaction.

## Why Nobody Has Built This
Building a visual injection mapping tool requires: (1) a standardized facial anatomy model that can be annotated with injection points, (2) photo overlay capabilities to map annotations onto actual patient photos, (3) temporal tracking to show how injection plans evolved across visits, and (4) outcome correlation to connect injection patterns with patient satisfaction. This is a specialized computer vision + clinical documentation intersection that med spa software companies haven't prioritized because text-based notes are "good enough" for billing compliance.

## What to Build
A visual injection charting tool where the injector taps injection points on a patient photo or 3D face model, records units/volume per point, and the system builds a longitudinal injection history. Over time, the system identifies: "this patient metabolizes Botox faster in the frontalis — consider 25 units instead of 20" or "filler placed here migrated inferiorly by visit 3." Integrated with before/after photo comparison for outcome tracking.

## Target Customer
Med spa owners with 2+ injectors sharing a patient base, and high-volume injectors treating 15+ patients daily who cannot rely on memory.

## Impact If Built
Reduces product waste by 10-15% through precision dosing, improves patient satisfaction through treatment continuity, and protects the practice against injector turnover by externalizing tacit anatomical knowledge.
