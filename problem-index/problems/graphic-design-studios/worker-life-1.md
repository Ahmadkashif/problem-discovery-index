# The Production Artist Resizing Sixty Versions

**Industry:** [[graphic-design-studios|Graphic Design Studios]]
**Type:** Worker Life Changing
**One-liner:** Once the master design is approved, a junior production artist spends the night re-laying it out by hand into sixty sizes, formats and languages; the work teaches nothing and any error on any one of them is theirs.
**Tags:** #transformers #autoregressive-models #optimization-fundamentals #feature-engineering #worker-facing #automation #workflow-orchestration

## The Problem
The creative director and the client have finally approved the master: one key visual, one headline, one lock-up. Now it has to exist in every size the launch needs — social formats in four aspect ratios, a dozen display ad sizes (300×250, 728×90, 160×600 and the rest), a print ad in three publications' specs, a retail shelf-talker, a window cling, an email header, and the whole set again in French and Spanish. That is easily sixty variants, and the launch date doesn't move.

None of them can simply be scaled. A 728×90 banner has no room for the headline's line break; a 9:16 story has room for nothing else. Each variant is re-laid out by hand in InDesign, Illustrator, Photoshop or Figma: reflow the copy, keep the logo's clear space, keep the legal line legible at its minimum size, move the product shot so it doesn't sit under the platform's interface. At fifteen to twenty minutes a variant (estimate), sixty variants is a long night. Then every one goes through proofing, and the comment that comes back on variant 47 — wrong legal line, old price, logo below minimum size — has to be fixed across every sibling.

## Why It Matters to the Worker
This is where junior designers in studios spend a large share of their first years, and it is the part of the job least connected to why they became designers. It builds no portfolio and teaches little beyond keyboard shortcuts. The hours are concentrated right before launch, on top of the rest of their work, and the repetition is physically wearing.

The errors are also personally theirs. A wrong legal line on one size out of sixty is invisible until the client or the publication spots it, and then it is the production artist's mistake, not the process's. And this is precisely the work that generative resizing tools are marketed to replace, so the people doing it carry both the tedium and the anxiety that the tedium is what's keeping them employed.

## What a Solution Looks Like
An adaptation engine inside the tools they already use. The production artist marks up the master once — which elements are locked (logo, legal, price), which can reflow, which can crop — and the system proposes every variant using the studio's own adaptation habits, learned from the masters and hand-made variants of previous jobs. Hard rules are enforced as constraints, not suggestions: logo clear space and minimum size, legal copy present and legible, safe zones per platform.

The artist reviews a contact sheet, fixes the variants that genuinely need a designer's judgement, and pushes a correction once to every affected sibling. Export follows the client's naming conventions and delivery specs automatically.

## Impact If Solved
Turning sixty hand-built variants into sixty reviewed ones could take a 15–20 hour job down to 3–4 hours of judgement and fixes (estimate), end most launch-eve all-nighters, and remove the class of error the artist is currently blamed for. The hours freed can go to the craft work juniors need to grow — if the studio chooses to give it to them.
