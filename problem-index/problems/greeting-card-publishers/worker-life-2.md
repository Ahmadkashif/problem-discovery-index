# The Production Artist Cutting Foil and Emboss Masks

**Industry:** [[greeting-card-publishers|Greeting Card Publishers]]
**Type:** Worker Life Changing
**One-liner:** Every approved card design with foil, embossing, glitter or a die cut has to be hand-separated into press-ready layers, and the production artist doing it at the end of every seasonal deadline gets back her evenings if the first draft of each mask is done for her.
**Tags:** #semantic-segmentation #cnns #transfer-learning #evaluation-metrics #worker-facing #automation #quick-win

## The Problem
A premium card is rarely just four-colour print. The approved design has gold foil on the lettering, a blind emboss on the flowers, glitter on the snow, a spot gloss on the ornament, and a die-cut window in the front panel. Each effect needs its own separation: a vector mask for the foil die, a greyscale or vector file for the emboss plate with the correct depth, a glitter adhesive layer, a die line, bleed and trapping tuned so the foil registers against the print. The production artist (sometimes called a prepress or mechanical artist) builds these by hand in Illustrator, path by path, from art that the illustrator painted without thinking about any of it.

The work arrives in waves. When a seasonal line is approved, hundreds of designs hit production at once, the printer's slot is fixed, and any separation error shows up as a rejected proof, a foil that bleeds into the type, or a die that cuts through the caption. Variants multiply the load: the same design at different sizes, a boxed-card version, a matching gift bag.

## Why It Matters to the Worker
Tracing every petal for an emboss plate is skilled, slow and unrewarding, and it compresses into crunch weeks before print deadlines that nobody in production sets. Errors are hers even when the art was impossible to separate cleanly. The skill she has (knowing how foil spreads on a particular stock, how deep an emboss can go before it cracks the paper, where a die line can safely run) is valuable and largely invisible, because the visible part of the job is mask-cutting.

## What a Solution Looks Like
A tool inside her existing software that proposes each separation from the approved art and a mark-up of which elements get which effect: candidate foil, emboss, glitter and spot-gloss masks as editable vector paths, die lines snapped to safe zones, and warnings where fine type sits under foil or an emboss crosses a fold. She corrects rather than draws, and her corrections train the next draft. Rules learned from the printer's proof rejections (minimum line weights, trap widths per stock) are checked before the file leaves.

## Impact If Solved
If first drafts take even half the tracing time (estimate), a production team clears a seasonal line days sooner, with fewer proof rejections. The production artist spends her hours on the judgement calls about stock, depth and registration rather than on path-cutting at midnight.
