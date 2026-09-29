# Lineage: Product Design Studios

**Industry:** [[industries/product-design-studios|Product Design Studios]]
**Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**The tool:** Sketch — the Mac vector editor for screen interfaces, first released 7 September 2010, whose reusable Symbols and later open `.sketch` file format made a design a structured, component-based file
**Builder:** Bohemian Coding
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A studio designing an app interface spends its time drawing the same few objects over and over: buttons, list rows, navigation bars, text fields. Each appears on dozens of screens, at several sizes, for several devices.

The tool the trade used for this was not built for it. **Photoshop** began in 1987 as Thomas Knoll's program to display greyscale images on a monochrome Mac screen; version 1.0 shipped on **19 February 1990** as a photo-retouching tool. An interface drawn in it was a stack of pixel layers. A button was not a thing, it was an arrangement of pixels that happened to look like one, and changing it meant finding and editing every copy by hand.

That was tolerable while a studio shipped a website at one width. It stopped being tolerable when the iPhone and its successors multiplied every screen by devices, orientations and pixel densities. **The cost of a design change scaled with the number of places the object had been pasted.**

## What Got Built

**A drawing tool that treated an interface as objects rather than pixels.**

Sketch was first released on **7 September 2010** by Bohemian Coding, a small Dutch developer, for the Mac only. It was built for designing the UI and UX of mobile apps and the web and deliberately carries no print-design features. Shapes are vectors, so one drawing exports cleanly at every screen density.

Two later pieces made it the studio's working format:

| Artefact | Date | What it did |
|---|---|---|
| Sketch 3 | April 2014 (3.0.1 released 19 Apr) | The earliest version in Sketch's public release archive |
| **Symbols** | not dated this session | A master component whose instances update everywhere when the source changes, with per-instance overrides for text, colour and images |
| **Sketch 43** | 6 April 2017 | Moved the `.sketch` file to a ZIP archive of JSON, so other tools could read and generate documents without opening Sketch |

Symbols are the load-bearing piece. A button became a single source with instances, and editing the source changed every screen. **That is the design system, expressed as a file feature.**

## Who Built It, And Why Them

A small independent shop, and the reason is what it did not have to protect.

Adobe owned the designer's desktop through Photoshop, Illustrator and Fireworks, each built around print, photography or the early web, and each with a large installed base whose workflows a redesign would break. A company with no print product and no legacy customers could build only the subset an interface designer needed and leave everything else out. Sketch's own positioning — UI and UX only, no print, Mac only — reads as exactly that bet.

Sketch won an **Apple Design Award in 2012**.

**This note does not establish the founders' own account of why they built it.** The interview and launch post Wikipedia cites could not be retrieved this session, so the motive above is inferred from the product's scope, not from its makers.

## What It Cost

**Mac only.** A studio whose client or developers ran Windows could not open its files, so handoff went through exported images, spec plugins and third-party viewers — the gap Figma, launched publicly on 27 September 2016, later attacked by running in a browser.

And the component lived in the designer's file, not in the product's code. A Symbol updates every screen in the document; it does not update the button engineers actually shipped. **Sketch made the design system cheap to draw and did nothing to keep it true.**

## What You Still Touch

Every design tool now has components with instances and overrides, and every studio delivers a "component library" alongside the screens. That library begins drifting from production code the week the studio leaves, because the component was invented as a drawing feature, not as a contract with the codebase.

- [[problems/product-design-studios/low-impact-1|🟡 Design Systems That Decay After Handoff]] — Symbols' missing half
- [[problems/product-design-studios/worker-life-1|🟢 The Designer in Round Six of Stakeholder Opinion]]
- [[niches/product-design-studios/design-system-durability/profile|Design System Durability]]
- [[niches/product-design-studios/deliverable-production/profile|Deliverable Production & Handoff]]

**Sources:** WebSearch was unavailable this session (session cap reached); research was by WebFetch on known URLs. Wikipedia, *Sketch (software)* (first release 7 September 2010; Sketch B.V. formerly Bohemian Coding; UI/UX focus, no print features; Apple Design Award 2012; left the Mac App Store December 2015); Sketch's own release archive (3.0.1 on 19 April 2014, version 43 on 6 April 2017); Sketch developer documentation, *File format* (ZIP of JSON, introduced in Sketch 43) and help documentation, *Symbols* (sources, instances, overrides); Wikipedia, *Adobe Photoshop* (Knoll 1987, 1.0 on 19 February 1990) and *Figma* (public release 27 September 2016). ⚠️ **Not established:** the founders' names and the company's founding city — widely attributed to Pieter Omvlee and Emanuel Sá, but the Wikipedia article checked names neither, Sketch's about page names neither, and the cited LayerVault interview and 2011 launch post were unreachable (host down; archive blocked). The date Symbols were introduced is also unconfirmed and left undated in the table.
