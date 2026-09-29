# Unauthorised Redistribution as Direct Substitution

**Industry:** [[digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** High Impact
**One-liner:** A digital good copies perfectly at zero cost, so redistribution is not leakage but substitution for a sale, and enforcement is delegated to individual creators filling in takedown forms.
**Tags:** #cnns #contrastive-learning #transformers #dimensionality-reduction #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #revenue-impact

## The Problem
A creator sells a template, a font, a set of presets or a plugin. Somebody buys it and uploads it to a file-sharing site, a forum, a membership group or a competing marketplace. Everyone who downloads it there is a sale that did not happen.

Unlike physical goods there is no degradation, no logistics and no marginal cost, so a single leak serves an unlimited audience indefinitely. For creators in categories where this is endemic, the redistributed copies substantially exceed legitimate sales.

The response is notice and takedown. A creator discovers a copy — usually by searching for their own product name, manually, in their own time — and files a notice. The site may comply. The file reappears within days elsewhere or under a different name. The creator files again.

This is an unfunded enforcement burden placed on the party least able to carry it. A solo creator earning modestly cannot run a monitoring operation, so most do nothing, and the ones who try spend hours a week on it instead of creating.

Meanwhile the platform holds every asset it has ever sold, which is the reference corpus any detection system would need.

## Why It's Unsolved
The economics of enforcement are the real obstacle rather than the technology. Fingerprinting and perceptual matching work well for images, audio and video, and the difficulty is who pays to run the searching at scale for products that individually earn small amounts.

Some asset types genuinely resist fingerprinting. A font file, a code plugin, a spreadsheet template and a set of parameter presets are functional artefacts where perceptual hashing does not straightforwardly apply — though file-level and structural fingerprinting can work and is rarely tried.

Watermarking has an adoption problem more than a technical one. Per-purchase watermarks that identify the original buyer are feasible for many asset types and are used almost nowhere, partly because creators fear degrading the product and partly because nobody has built it into the delivery path.

Jurisdictional reach limits what any notice achieves. The largest redistribution hubs operate where notices are ignored, which caps what an individual creator can accomplish regardless of effort.

And the platform's incentives are weak. Redistribution costs the creator directly and the platform only through the commission on lost sales, which is a fraction of the harm.

## What a Solution Looks Like
Detection as a platform service rather than a creator obligation. The platform holds the asset corpus and can run continuous matching against public sources at a scale no individual creator can, which is the fundamental argument for centralising it.

Per-purchase watermarking built into delivery, invisibly where the asset type permits, so that a leaked copy identifies its origin. This changes the deterrent structure entirely and is technically available for images, video, audio, documents and many design assets.

Fingerprinting for functional assets. Structural signatures for code, glyph-level signatures for fonts and parameter signatures for presets are all feasible and are essentially unexplored because the industry assumed fingerprinting meant perceptual hashing.

Automated notice generation and tracking, so a creator confirms rather than composes, with reappearance monitored automatically.

Honest measurement of the scale, which nobody has. Estimating what redistribution actually costs a category is the finding that would justify the investment, and it is currently an anecdote.

## Impact If Solved
Redistribution is a direct substitution for sales in a market where the good costs nothing to copy, and enforcement is delegated to solo creators with no capacity to enforce. Centralising detection and building watermarking into delivery moves the burden to the party with the corpus, the scale and the technical means — and is the only intervention that changes the economics rather than processing their consequences.
