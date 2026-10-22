# Yearbook, ID and SIS Deliverables From Picture Day

**Industry:** [[portrait-photography-studios|Portrait Photography Studios]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every school expects the same outputs from picture day, a yearbook file, ID cards and student-system images, and every studio rebuilds them by hand for each school's roster, publisher and ID template.
**Tags:** #large-language-models #k-nearest-neighbors #feature-engineering #evaluation-metrics #data-integration #automation #compliance

## The Problem
A school photography contract is won as much on what the school gets for free as on the portraits families buy. District RFPs spell it out: every enrolled child photographed whether or not the family orders; ID cards produced on site or within ten days of picture day, sometimes a safety ID for every child; images loaded into the student information system; a yearbook file delivered after the final retake day, including staff; and a perpetual licence for district use. Each of these is a data job. The studio starts from a roster exported by the school office, which arrives as a spreadsheet with legal names, missing new enrolments, inconsistent grade and homeroom codes, and students who left in September. On the day, barcode or QR cards tie each child to a frame, until a child loses the card, swaps it with a friend or is photographed on retake day under a nickname.

Afterwards, someone at the studio reconciles images to the roster, marks absentees, merges retakes, removes children whose parents opted out of directory information, and produces three or four outputs in three or four formats. Errors are public: the wrong name under a photo in the yearbook, a missing child in the ID run, a student's image in the system attached to a sibling.

## What Already Exists
Volume ordering platforms handle part of it: GotPhoto, for example, sorts barcode-scanned images into student galleries and exports PSPA yearbook files directly. Yearbook publishers' platforms import PSPA packages, and ID card software prints from image folders. Generic spreadsheet and data-cleaning tools (Excel, Power Query, OpenRefine) are what most studios use to fix rosters.

## The Customisation Gap
The PSPA standard is a tab-delimited INDEX.TXT with a fixed field order, but versions disagree: the 2014 guideline keeps eleven default fields, a later guideline sets a thirteen-field minimum, and individual publishers ask for six- or seven-column variants with their own image sizes. Student information systems each want their own photo import naming. ID templates vary by district logo, barcode type and grade. The industry-specific logic that needs layering on is: roster reconciliation across picture day, retake day and mid-year enrolments, with fuzzy matching of legal and preferred names; opt-out handling tied to the school's directory-information notice; one deliverable profile per school and publisher that generates every output from one reconciled record; and an audit of which images went where, to answer a district's privacy agreement. None of the generic tools knows what a homeroom, a retake or a PSPA volume field is.

## Impact If Solved
A data coordinator who now spends most of October fixing rosters and re-exporting files could produce every school's deliverables from one reconciled record in minutes, and the studio stops losing contracts over a misnamed yearbook page or a late ID run, which are the errors a principal remembers at renewal.
