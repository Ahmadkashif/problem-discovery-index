# AI-Powered POD Quality Gate at Capture Time

**Niche:** [[niches/last-mile-delivery/proof-of-delivery-documentation/profile|Proof-of-Delivery Documentation & Disputes]]
**Industry:** [[industries/last-mile-delivery|Last-Mile Delivery]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No system evaluates a POD photo's evidentiary quality in real time at the moment the driver captures it — checking that the address number is visible, the package is identifiable, and the image is adequately lit — and prompts a retake before the driver walks away.
**Tags:** #cnns #gradient-boosting #compliance #quick-win

## The Problem
A driver photographs a package on a porch, taps "delivered," and walks away. Later, when the customer claims DBNR, the claims analyst pulls up the photo and finds: the address number isn't visible (the photo shows a generic brown porch), the package blends into the background, and the image is underexposed. This photo can't be used to defend against the claim — the carrier pays the refund. If the driver had been prompted to retake the photo with the address visible, the claim would have been defensible. But by the time the claims team reviews the photo, the driver is 30 stops past that address.

## Why Nobody Has Built This
Real-time photo quality assessment on a mobile device requires: a lightweight CNN that can run on-device in <1 second, training data of POD photos labeled by evidentiary quality criteria (address visible, package identifiable, adequate lighting), and integration with the delivery app's photo capture workflow. The technical capability exists (mobile-deployed CNNs are standard), but no delivery platform vendor has invested in this because POD quality is treated as a training issue ("tell drivers to take better photos") rather than a technology problem.

## What to Build
A mobile-deployed photo quality model that: (1) assesses each POD photo immediately after capture for address visibility, package identifiability, and lighting quality; (2) prompts the driver to retake if any criterion fails ("address number not visible — please include the house number in the photo"); (3) stores the quality score with the delivery record for claims processing; (4) provides fleet-level POD quality metrics for driver performance management.

## Target Customer
Claims managers at DSPs and regional carriers where DBNR claim costs exceed $50K annually. Approximately 5,000 delivery operations process significant DBNR claim volumes.

## Impact If Built
Improving POD photo quality from 60% evidentiary-grade to 90%+ reduces claim payout rate by 30-50%. For a DSP paying $200K annually in DBNR claims, this saves $60K-$100K per year. Driver retake prompts add <10 seconds per stop where triggered.
