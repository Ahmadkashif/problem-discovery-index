# Multi-Platform Content Adaptation

**Industry:** [[news-media-local|Local News Media]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic summarization tools exist but cannot adapt a 1,200-word local news article into a newsletter lead, a social caption, an Apple News brief, and an app push notification while preserving local voice, sourcing standards, and AP style.
**Tags:** #large-language-models #transfer-learning #attention-mechanisms #transformers #word-embeddings #entropy-cross-entropy-kl-divergence #automation

## The Problem
A single local news story must appear in 4–6 formats: the full web article, a newsletter excerpt (150 words with a hook), a Facebook post (50 words with engagement framing), a Twitter/X post (280 characters), an Apple News summary, and a mobile push notification (90 characters). Digital producers manually rewrite each version, spending 15–25 minutes per story across platforms. A newsroom publishing 15–30 stories per day burns 4–12 producer-hours daily on reformatting — time that produces zero original journalism.

## What Already Exists
General-purpose LLM summarization (ChatGPT, Claude, Jasper) can condense text, and social media scheduling tools (Buffer, Hootsuite) allow cross-posting. WordPress plugins like Jeevi or Jeeves offer basic excerpt generation.

## The Customisation Gap
Local news has specific constraints that generic tools ignore: AP style compliance (datelines, attribution formatting, number rules), local voice consistency (a folksy Midwest weekly reads differently from a hard-news metro digital outlet), sourcing integrity (summaries must not imply claims the original story hedged), legal sensitivity (crime reporting requires careful language around suspects vs. convicted), and platform-specific engagement patterns that vary by community. A local outlet in a college town optimizes social posts differently than one in a retirement community. The tool must learn the outlet's voice from its archive and enforce its editorial standards automatically.

## Impact If Solved
Reclaiming 4–8 producer-hours per day gives a 20-person newsroom the equivalent of one full-time reporter's output redirected to original coverage. For a newsroom spending $45K–$65K annually on digital production labor, this represents $20K–$35K in effective labor reallocation.
