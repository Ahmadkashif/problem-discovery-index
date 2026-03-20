# Story Engagement Prediction for Resource Allocation

**Industry:** [[news-media-local|Local News Media]]
**Type:** High Impact
**One-liner:** Editors stop guessing which stories justify a full reporting day and start seeing predicted subscription lift, engagement depth, and share velocity before committing resources.
**Tags:** #bert #gradient-boosting #transfer-learning #attention-mechanisms #word-embeddings #linear-regression #feature-engineering #evaluation-metrics #loss-functions #gradient-descent #tacit-knowledge-ml #revenue-impact

## The Problem
Local newsroom editors receive 20–50 story pitches, tips, and beat-generated ideas per week and must allocate 10–25 reporter-days across them. The decision of which stories get deep investigation versus a quick brief versus being killed entirely is made by editorial instinct — an editor's internalized sense of which topics will resonate with the community, drive subscriptions, and generate sharing. This tacit judgment integrates community relevance (does this affect enough people?), emotional resonance (does this provoke outrage, hope, or surprise?), information exclusivity (do we have this first?), and timing (is the community primed for this?). When editors retire or leave, this judgment walks out with them, and the replacement editor spends 1–2 years recalibrating to the community.

## Why It's Unsolved
The tacit knowledge problem is severe: experienced editors cannot fully articulate why they sense a story will perform. Their judgment blends reader demographics they've internalized, historical pattern recognition across thousands of published stories, and real-time community mood — none of which is recorded in structured form. Data collection requires capturing the editor's decision context at pitch time (not just what was published), including killed stories and their counterfactual outcomes. Labeling is inconsistent because "engagement" means different things: pageviews, time-on-page, subscription conversion, social shares, and comment quality are all partially correlated but distinct signals. Deployment is hard because editors will reject a tool that feels like it overrides their professional judgment — it must augment, not replace.

## What a Solution Looks Like
A model that takes a story pitch (headline draft, 2–3 sentence summary, beat category, named entities, timing metadata) and outputs predicted engagement across multiple dimensions: estimated pageviews, predicted time-on-page, subscription conversion probability, and social share velocity. The model combines NLP features from the pitch text (BERT embeddings capturing topic, framing, and emotional valence) with tabular features (day of week, competing stories, historical beat performance, community event calendar overlap). Editors see a dashboard at the morning pitch meeting showing predicted ROI per story, with confidence intervals and explanations ("similar to the school-board story in October that drove 140 subscriptions").

## Impact If Solved
A 15–25% improvement in story-to-subscription conversion rate could mean the difference between a local newsroom surviving and closing. With ~6,000 local news organizations and average digital subscription revenue of $500K–$2M, even modest prediction gains translate to $50K–$200K in retained or new annual revenue per outlet.
