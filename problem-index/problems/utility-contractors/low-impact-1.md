# PACP/MACP Pipe Condition Assessment Coding Automation from CCTV Footage

**Industry:** [[utility-contractors|Utility Contractors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** NASSCO PACP/MACP coding software exists for manual defect logging, but automating the coding from CCTV footage video — identifying each defect frame, assigning the correct PACP code, and generating the condition report — requires a municipal pipe inspection-specific computer vision model that no general-purpose platform provides.
**Tags:** #cnns #object-detection #semantic-segmentation #transfer-learning #loss-functions #backpropagation #evaluation-metrics #gradient-descent #automation #compliance

## The Problem

NASSCO PACP (Pipeline Assessment Certification Program) and MACP (Manhole Assessment Certification Program) are the standards for documenting sewer and water main condition from CCTV inspection footage. PACP coding requires a certified technician to watch inspection footage in real time and enter codes for every observed defect: root intrusion (grade and type), cracking (type and clock position), deformation, infiltration, deposits, and construction joints — each with standardized code identifiers and severity grades.

A certified PACP coder can process inspection footage at approximately 1-1.5× real time — a 30-minute pipe inspection run requires 30-45 minutes of coding. Utilities running large inspection programs code thousands of footage hours annually. Municipal inspection programs operate at the larger pipe diameters (6"-24" and larger) where the PACP defect distribution differs from residential plumbing.

## What Already Exists

WinCan AI and Envirosight's AI Assist provide automated PACP coding for municipal sewer inspection. These products target the 6"+ municipal pipe size range with good coverage. Residential plumbing pipe (3"-6") is the gap addressed separately in plumbing contracting.

## The Customisation Gap

For utility contractors doing municipal inspection work, the gap is: (1) automated coding at the PACP-certified level of accuracy (AI Assist from Envirosight is close but requires significant review of automated codes); (2) integration with the utility's specific asset management system (Hansen, Lucity, IBM Maximo) for defect data import; (3) custom report templates that match the utility owner's specification rather than the PACP standard report format. The asset management integration and report customization are the remaining gaps after the automated coding models from WinCan and Envirosight.

## Impact If Solved

Reduces CCTV coding labor from 1:1 footage:coding ratio to 4:1 or better. Enables expansion of inspection programs without proportional increase in certified coder staffing — the binding constraint for most utilities' inspection programs.
