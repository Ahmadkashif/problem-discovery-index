# Incoming Royalty Statements in Hundreds of Formats

**Industry:** [[music-publishers|Music Publishers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every publisher's royalty department turns statements from PROs, the MLC, foreign societies, sub-publishers and sync licensees into writer accounts, and the work of mapping each new format and each unmatched line is redone by hand at every company.
**Tags:** #large-language-models #feature-engineering #k-nearest-neighbors #evaluation-metrics #data-integration #automation #quick-win

## The Problem
A mid-size publisher's royalty team receives statements every month and quarter. They come from ASCAP, BMI, SESAC and GMR; from the MLC and HFA; from sub-publishers in Japan, Germany and Brazil reporting in their own layouts and currencies; from YouTube and other direct licences; and from sync licensees paying flat fees. Each statement lists earnings by work title, sometimes by society work code, sometimes by an identifier the publisher has never seen. Before any writer can be paid, every line has to be matched to a song in the publisher's database, split by the writers' shares and the deal terms (at-source or receipts basis, administration fee, co-publishing split), and posted to the right account.

Most lines match automatically. The rest do not: a title spelt differently, a work registered twice, a cue with no identifier, a sub-publisher using its local title. Those lines go into a suspense report that someone works through in a spreadsheet before the writer statement deadline, usually 60–90 days after the period closes (estimate). A sub-publisher that changes its export layout can stop the import cold.

## What Already Exists
Royalty accounting systems such as Vistex's Music Maestro and Counterpoint Suite and Curve Royalty Systems hold the song database, apply splits and produce writer statements. Import tools advertise parsers for 150 or more statement sources. General-purpose extract, transform and load (ETL) and spreadsheet tools fill the gaps, and large publishers keep in-house data teams.

## The Customisation Gap
The generic import step treats a new format as an engineering ticket and an unmatched line as a manual task. Publishing needs logic that understands its own domain. It has to recognise a society's statement layout from a sample and map it without a developer. It has to match a line to a work using the evidence a royalty analyst uses: writer names, IPI numbers, ISWC where present, local title variants, performing artist, duration and the source's past behaviour. It has to apply deal-specific rules, such as at-source versus receipts, a sub-publisher's fee, and reserves against returns. And it has to learn from every manual match, so the same unmatched title from the same society never needs a person twice. It should also flag a line whose amount looks wrong for that work and source, which is where missing income first becomes visible.

## Impact If Solved
A royalty team that clears its suspense report in days rather than weeks meets statement deadlines without overtime, pays writers on lines that would otherwise sit unallocated, and turns each newly matched title into a rule. For a publisher processing millions of statement lines a year (estimate), that is the difference between a royalty department that grows with the catalogue and one that grows with the headcount.
