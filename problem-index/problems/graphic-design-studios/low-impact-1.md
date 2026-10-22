# Packaging Copy-to-Artwork Verification for Small Studios

**Industry:** [[graphic-design-studios|Graphic Design Studios]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Brand owners and big prepress houses verify packaging artwork against the copy deck with enterprise inspection software; the five-person studio doing the same 40-SKU line extension checks it by eye.
**Tags:** #transformers #cnns #seq2seq #object-detection #large-language-models #compliance #automation #quick-win

## The Problem
A small packaging studio wins a line extension: forty SKUs across four flavours and three pack sizes, with a bilingual version for Canada. The client's regulatory team sends a copy deck — a spreadsheet or Word file holding the ingredient statement, the allergen "Contains" line, net quantity, Nutrition Facts values, claims, the UPC for each SKU and the recycling marks. The studio's job is to make forty pieces of artwork that match it exactly, then re-match them every time the copy deck changes, which it does several times before print.

The check is done by eye, often by the same designer who typed or pasted the copy, then again by the client's proofreader on a PDF. Text has usually been converted to outlines for the printer, so a simple text compare no longer works. Errors are not cosmetic: a wrong net weight or nutrition value means scrapped printed stock and plate remakes; a missing allergen on one SKU's panel is the kind of error that ends in a recall. Undeclared allergens drove almost half of US food recalls in 2023 (PIRG).

## What Already Exists
GlobalVision Verify does text compare, spell check in 37 languages, graphics, barcode and braille inspection, and integrates with Esko WebCenter and Automation Engine — the stack brand owners, converters and large prepress houses such as SGS & Co use. Ziflow and Filestage manage proofing rounds and comments. Acrobat's compare feature diffs two PDFs. Each is either priced and integrated for an enterprise packaging operation or generic enough that it doesn't know what a copy deck, a principal display panel or an allergen statement is.

## The Customisation Gap
The small-studio version needs packaging-specific logic layered on generic document comparison:
- **The copy deck as source of truth,** parsed into a SKU-by-field matrix so each panel is checked against the right row, not against the previous version of the artwork.
- **Recognition of outlined and stylised text** on curved and rotated panels, since print-ready files rarely contain live text.
- **Rule checks that a diff can't do:** the allergen statement consistent with the ingredient list; Nutrition Facts format per 21 CFR 101.9; net quantity on the lower 30% of the principal display panel (101.105); Supplement Facts and cosmetics (MoCRA) equivalents for non-food clients.
- **Barcode decoding and grading** against the SKU's assigned UPC.
- **Dieline awareness:** copy that crosses a fold, sits in a glue flap or falls inside the bleed.
- **A change report** the client's regulatory reviewer can sign and the printer can file.

## Impact If Solved
A studio could take on regulated packaging work it currently avoids or under-prices, turn a copy-deck change around in hours rather than a day of proofreading per SKU family, and hand the client a verification record instead of a promise. The cost avoided — one plate remake or one pallet of scrapped cartons — typically exceeds a year's subscription at small-studio pricing (estimate).
