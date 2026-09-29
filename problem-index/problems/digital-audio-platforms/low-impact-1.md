# Discovery for a Catalogue Nobody Can Listen Through

**Industry:** [[digital-audio-platforms|Digital Audio Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Over a hundred thousand tracks arrive daily into a system whose recommendations are optimised for engagement, which reliably favours what is already familiar.
**Tags:** #contrastive-learning #autoencoders #dimensionality-reduction #graph-neural-networks #transformers #k-nearest-neighbors #evaluation-metrics #transfer-learning

## The Problem
Recommendation on these platforms is excellent at its stated objective and the objective is engagement — minutes listened, sessions continued, skips avoided. That objective has a consistent bias: familiar and low-risk material performs better in the short term than unfamiliar material, so an engagement-optimised system converges toward what a listener already likes and toward what is already popular.

For the catalogue this is decisive. A new track by an unknown artist has no listening history, so a collaborative-filtering system has nothing to work with, and the audio-similarity fallback places it next to whatever it sounds like — which usually means next to something better known that will be recommended instead. The result is that the overwhelming majority of uploaded music receives almost no plays ever, and the distribution of listening is far more concentrated than the distribution of catalogue.

Editorial playlists were the counterweight and have become a bottleneck of their own: a small number of curators make decisions with enormous consequence, pitched by labels with the resources to pitch, which reproduces the concentration by a different route.

## What Already Exists
The recommendation systems here are among the most sophisticated deployed anywhere — collaborative filtering, sequence models, audio embeddings, contextual personalisation. Spotify's discovery features and Apple's editorial hybrid are both mature. Audio understanding models tag genre, mood, instrumentation and similarity across the whole catalogue automatically. Pandora's music analysis heritage is the oldest content-based approach in the field. Artist-facing tools show where streams came from and which playlists carried them.

## The Customisation Gap
The gap is objective rather than capability. A system optimised for immediate engagement will underweight discovery because discovery is a delayed and uncertain payoff — a listener who finds a new favourite is worth more over a year and less over a session. Optimising for long-horizon listener value, or explicitly for successful introductions, is a different objective function and produces different recommendations, and essentially nothing in the market is built that way.

Cold start is the concrete technical gap. With a hundred thousand daily uploads and no behavioural signal, the only route is content and context: what the recording sounds like, who made it, who they have worked with, where they play live, which small communities are already talking about them. Combining audio embeddings with the artist's collaboration and scene graph gives a genuinely informative prior that pure audio similarity does not, and it is what would let a new recording find its first thousand listeners without an editorial decision.

The second gap is measuring discovery honestly. Platforms report streams, and the quantity that matters to an artist is whether a listener became a repeat listener. Introduction-to-retention is computable and is the metric that would tell everyone which recommendation surfaces actually build audiences rather than just generating plays.

And artists need to see it. What a working artist most needs is where their audience is concentrated, which cities, which adjacent artists, which of their tracks converts a first-time listener into a returning one — an analytics product that exists in a thin form and could be far richer from the same data.

## Impact If Solved
The gap between catalogue size and listening concentration is the defining economic fact of streaming, and it is produced in large part by an objective function chosen for session metrics. Cold-start models built on content and scene structure give new recordings a route to an audience that does not require an editorial gatekeeper, and measuring introduction-to-retention rather than streams would tell the industry, for the first time, which of its discovery mechanisms actually build careers.
