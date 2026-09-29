# Contextual Targeting and Brand Suitability From Transcripts

**Industry:** [[audio-adtech-networks|Audio Adtech Networks]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Transcription made audio content readable, and the industry used it to build the same blunt keyword blocklists that defunded news on the open web.
**Tags:** #bert #transformers #large-language-models #word-embeddings #transfer-learning #evaluation-metrics #compliance #contrastive-learning

## The Problem
Audio advertising historically had no content signal at all: a buyer knew the show and nothing about the episode. Transcription changed that, and the first application was brand safety — scanning transcripts for terms an advertiser would not want to appear beside.

The result has been the open web's history repeated at speed. Keyword-based exclusion is blunt: a news podcast discussing a tragedy is blocked, a true crime show is blocked wholesale despite an engaged and commercially attractive audience, a medical show is blocked for clinical vocabulary. Publishers report meaningful revenue loss from exclusions that have little to do with actual brand risk, and the shows hit hardest are news and current affairs — the same pattern that damaged web journalism funding, now arriving in audio.

The positive side of contextual targeting, which is the genuinely valuable half, is far less developed. Knowing what an episode is actually about, at the level of topic, treatment and sentiment, would let a buyer find relevant inventory across a long tail of shows they have never heard of. Mostly what exists is category tags and a blocklist.

## What Already Exists
Sounder, Barometer and Podscribe all provide transcription-based classification for brand suitability, and they are ahead of where the channel was three years ago. Transcription itself is cheap and accurate. The IAB and GARM frameworks give a shared suitability vocabulary. Some platforms offer contextual segments built from transcripts. Spotify and other platform owners have internal content understanding considerably beyond what they expose.

## The Customisation Gap
Suitability is a relationship between an advertiser and a piece of content, and it is being scored as a property of the content. The same episode is unsuitable for one brand and perfectly aligned for another, and a single universal risk score cannot express that — so it is set conservatively and over-blocks, which is how the reach destruction happens.

The fix is per-advertiser policy applied to content understanding rather than keyword matching: a model that reads what the episode is about and how the subject is treated — discussed analytically, depicted, endorsed — and evaluates it against that advertiser's stated concerns, with the specific passage and a reason attached. Treatment is the distinction keyword matching structurally cannot make, and it is the distinction that determines almost every real suitability judgement.

On the targeting side, the gap is representation rather than classification. Embedding episodes by what they are actually about lets a buyer target a theme across a long tail of shows, which is where audio's unsold inventory lives and where a small show's engaged audience is most undervalued. Category taxonomies cannot do this and are what the market currently uses.

And the publisher needs to see the cost. A show blocked by an advertiser's policy should generate a visible, appealable record — which brand, which passage, what reason — instead of silent revenue loss the publisher can only infer from a fill rate.

## Impact If Solved
Blunt exclusion is removing real revenue from exactly the shows the channel most needs to sustain, and it is doing so on evidence that would not survive inspection. Per-advertiser suitability based on treatment rather than keywords restores reach without increasing genuine risk, and embedding-based contextual targeting is the mechanism by which the long tail of audio inventory becomes findable and sellable at all.
