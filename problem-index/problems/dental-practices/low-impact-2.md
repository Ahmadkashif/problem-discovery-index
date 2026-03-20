# Multi-System Dental Imaging Unification

**Industry:** [[dental-practices|Dental Practices]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Dental practices use 3-4 separate imaging software systems that don't talk to each other or to the practice management system, creating a fragmented visual record that wastes clinical time and hinders treatment planning.
**Tags:** #cnns #object-detection #semantic-segmentation #transfer-learning #data-integration

## The Problem
A modern dental practice uses intraoral cameras, digital X-ray sensors (periapical and bitewing), panoramic radiographs, and increasingly cone beam CT (CBCT) scanners. Each imaging device typically comes with its own proprietary software for capture, viewing, and annotation. When the dentist is treatment planning, they need to pull up images from multiple applications — flipping between Dexis for X-rays, Planmeca Romexis for the CBCT, and the intraoral camera software — rather than seeing a unified image timeline for the patient.

## What Already Exists
DICOM (the medical imaging standard) is partially adopted in dental, and some imaging platforms support it. Apteryx (XVWeb), DEXIS, and Schick by Dentsply Sirona each offer imaging management. Open Dental and some PMSs have basic image bridges.

## The Customisation Gap
Dental imaging unification requires understanding dental-specific image types (periapical vs. bitewing vs. pano vs. CBCT), tooth-numbering systems, and the clinical workflow of comparing images over time (e.g., tracking a lesion across three bitewings taken over 18 months). Medical PACS systems don't understand dental anatomy. The integration needs to map images to specific teeth, support side-by-side comparison across modalities, and feed into the treatment planning workflow in the PMS.

## Impact If Solved
Saves dentists 5-10 minutes per patient in image retrieval and cross-referencing. Improves treatment planning accuracy by providing a complete visual record in one view. Reduces the $2,000-$5,000/year per practice spent on redundant imaging software licenses.
