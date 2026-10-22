# Termination and Reversion Dates Buried in Old Agreements

**Industry:** [[music-publishers|Music Publishers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Contract management software can store a publishing agreement, but it does not compute when the Copyright Act lets a writer take the song back or when a sub-publishing term lapses, so publishers and writers' estates find those dates by reading paper.
**Tags:** #large-language-models #transformers #seq2seq #evaluation-metrics #compliance #automation

## The Problem
A catalogue is a stack of agreements: songwriter deals, co-publishing deals, administration deals, sub-publishing deals by territory and catalogue purchases, some signed in the 1970s on typewritten pages. Each carries dates that change who owns or collects a song. Section 203 of the Copyright Act lets an author terminate a grant made on or after 1 January 1978 during a five-year window that opens 35 years after publication or 40 years after the grant, whichever comes first. Notice must be served two to ten years before the chosen effective date and recorded with the Copyright Office before it. Older grants follow a separate regime under Section 304. Contractual reversions add more triggers: rights that return if a song is not exploited, if an advance is not paid, or when a term ends, often with a retention period during which the old publisher keeps collecting.

Missing one of these dates is expensive in both directions. A writer's estate that misses a window has to wait or loses the chance. A publisher that does not see a notice coming loses a song it was valuing as permanent, and a catalogue buyer that misses one has overpaid.

## What Already Exists
Contract lifecycle management platforms such as Ironclad, DocuSign CLM and Agiloft store agreements, extract common clauses and send renewal alerts. Rights systems such as Vistex's Counterpoint record territories and terms for administration. Music lawyers keep their own calendars of termination windows for clients.

## The Customisation Gap
Generic software reads renewal and expiry dates. It does not know copyright law. A publishing version would need to do several things. It would extract the grant date, the publication date of each work and whether the author personally executed the grant, which decides whether Section 203 applies at all. It would treat works made for hire as not terminable. It would compute the window, the earliest and latest service dates and the recordation deadline for every song and every grant. It would read reversion and retention clauses into machine-checkable triggers. And it would join all of this to the song's earnings, so the dates with money attached surface first. Each date has to be sourced to a page and a clause, because the reader is a lawyer who will not act on an unsupported field.

## Impact If Solved
A publisher, estate or catalogue buyer would see every terminable or reverting song in a catalogue, with the window and the earnings at stake, instead of finding out from a notice in the post. For a buyer in due diligence, a list that once took a lawyer weeks to compile becomes a report that is checked rather than built.
