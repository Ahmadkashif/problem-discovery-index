# Lineage: Localization Services

**Industry:** [[industries/localization-services|Localization Services]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** Trados Translator's Workbench — a segment-level translation memory whose match analysis sorts every new source text into repetitions, 100% matches, fuzzy-match bands and no-matches, the basis of the "Trados grid" used to discount translation rates
**Builder:** Trados
**Builder in vault:** [[industries/localization-services|Localization Services]]
**Verification:** partial — see Sources

## The Problem That Came First

Technical documentation is mostly last year's documentation.

A software or hardware manual changes by a fraction between releases. A translation agency that received version 2 of a manual it had already translated as version 1 had two choices: retranslate the whole thing, or have someone hunt through old files for the sentences that had not changed. Both cost translator hours, and the client paid for text it had already bought once.

The waste grew with the volume of product documentation being localised into many languages at once. Every repeated sentence was paid for again, in every language.

## What Got Built

A database of previously translated sentences, consulted automatically as the translator works.

Translator's Workbench splits the source document into segments — usually sentences — and looks each one up in a **translation memory** of earlier source–target pairs. An identical segment is offered as a 100% match; a similar one as a **fuzzy match** with a percentage score; a sentence occurring several times in the new text is a repetition. Before any work starts, an analysis run counts the words in each of those bands.

That analysis is the commercially decisive part. It turned "how much of this is new?" from a guess into a report. Buyers and agencies then attached a rate to each band — full price for no-matches, less for fuzzy matches, least for 100% matches and repetitions. The practice is widely known as the **Trados discount model**, or simply the Trados grid.

A companion terminology tool, MultiTerm, shipped alongside it.

## Who Built It, And Why Them

Trados GmbH, registered in Stuttgart in 1984 by Jochen Hummel and Iko Knyphausen — and, crucially, **founded as a translation agency, not a software company.** The name stood for TRAnslation & DOcumentation Software, and one account says the firm's first aim was to bid for an IBM translation contract.

That is why it was them. A language service provider doing high-volume technical documentation felt the repetition directly, on its own margins. Trados first worked with TextTools, a translation tool from the Dutch firm INK, gaining rights to resell it in Germany in 1987 and writing an editor plug-in for it, TED, in 1988. When INK abandoned the product, Trados took the work in-house: from 1989 it specialised in software, and the editor became the first Translator's Workbench.

The decisive customer was a buyer, not a translator. In **September 1997 Microsoft decided to use Trados for its internal localization and took a 20% stake in the company.** With the largest software localization buyer standardised on it, vendors supplying that buyer had every reason to adopt the same memory and the same analysis.

## What It Cost

**The grid priced text by similarity, not by effort.** A 75% fuzzy match is discounted because it is 75% similar in characters, not because it takes 25% of the time. A 100% match can be wrong in its new context and still be paid as nearly free.

It also moved the benefit of reuse. The memory made repetition cheaper to produce, and the analysis made that saving visible to the buyer — who took it as a discount. The translator's productivity gain arrived pre-spent.

## What You Still Touch

When a post-editor today is paid a fraction of the full rate for correcting machine output, the logic is the Trados grid's: an automated estimate of how much work is "already done", converted into a discount before anyone measures the effort. That lineage is this note's reading, not a documented design choice.

- [[problems/localization-services/worker-life-1|🟢 The Post-Editor Paid by the Discount]]
- [[problems/localization-services/low-impact-1|🟡 Terminology and Translation Memory Leverage]]
- [[niches/localization-services/effort-measurement/profile|Effort Measurement]] — the measurement the grid skipped
- [[niches/localization-services/rate-structure/profile|Rate & Pricing Structure]]
- [[niches/localization-services/terminology-and-memory/profile|Terminology & Memory Health]]

**Sources:** Ignacio Garcia, *Long term memories: Trados and TM turn 20*, JoSTrans issue 4 (1984 founding by Hummel and Knyphausen as an LSP in Stuttgart; TED 1988; software specialisation from 1989; MultiTerm 1990; first Translator's Workbench 1992; September 1997 Microsoft adoption and 20% stake); Andovar, *30th Anniversary of Trados* (name expansion; IBM contract bid; INK TextTools resale rights 1987; MultiTerm 1992 and Workbench 1994 as first *Windows* versions); Wikipedia, *Trados Studio*; Petro Dudi, *Word Counts, The Trados Discount Model & Weighted Words*, and Emma Goldsmith, *Fuzzy match grids in SDL Trados Studio* (2015) (grid terminology and match bands); Training for Translators, *Translation memory discounts: yes, no, maybe?* (2008). ⚠️ **Sources disagree** on release dates — MultiTerm 1990 vs 1992, Workbench 1992 vs 1994 — plausibly DOS vs Windows editions; not resolved. ⚠️ **Not established:** when fuzzy-match discounting first became standard commercial practice, or who introduced it — the grid is attributed to Trados by name in the trade, but no dated first use was found. The IBM contract bid rests on one secondary source.
