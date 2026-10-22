# A Pronunciation Guide Built Before the First Word Is Recorded

**Niche:** [[niches/recording-studios/audiobook-production/profile|Audiobook Production]]
**Industry:** [[industries/recording-studios|Recording Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every audiobook starts with a narrator or researcher looking up names, places and foreign terms one by one, and a mispronunciation caught in proofing costs a pickup session.
**Tags:** #large-language-models #transformers #seq2seq #k-nearest-neighbors #automation #worker-facing #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor is fighting to deliver finished hours a publisher accepts, but on a lead title the account goes to whoever casts and directs the performance listeners single out, and on backlist and independent volume it goes to whoever needs the fewest edit, proof and pickup hours per finished hour. Decomposed into contested sub-niches below.

## The Problem
Before recording, someone has to decide how to say every unusual word: character names, real places, medical and legal terms, phrases in other languages, and the author's own inventions. Narrators search pronunciation sites, watch interviews to hear how a real person says their name, and email the author. Mistakes surface in proofing or, worse, in listener reviews, and each one becomes a pickup that has to be re-recorded and matched to the original performance.

## Why Nobody Has Built This
Pronunciation dictionaries cover common words; the hard cases are proper nouns and invented terms that no dictionary holds. Publishers rarely keep a pronunciation record across a series or an author's books, so the research is repeated by each narrator. The market of production houses is fragmented and small per firm.

## What to Build
A pre-production tool that extracts every candidate hard word from the manuscript, ranks them by difficulty, retrieves audio evidence (author interviews, place-name recordings, prior audiobooks in the series), proposes a pronunciation with sources and phonetic spelling, and produces a guide the narrator, director and proofer share. Approved pronunciations are stored per author and series and reused automatically. The proofing tool then checks the recording against the guide.

## Target Customer
Audiobook production houses and publishers' in-house audio teams producing hundreds of titles a year, and independent narrators who prep their own books.

## Impact If Built
Prep time per title falls from hours of searching to a review of a few dozen flagged words, and mispronunciation pickups, among the costliest to fix because they recur through a book, mostly disappear.
