# Stock Media Marketplaces

## Profile
**Category:** Digital Media & Creator Economy
**Market Size:** ~$4B US revenue across stock photography, video, audio and design asset marketplaces, with subscription licensing now dominant over single-image sales
**Tech Maturity:** Strong search and delivery, unresolved economics — Shutterstock, Getty Images, Adobe Stock, Pond5, Envato, Artlist and Storyblocks index hundreds of millions of assets with increasingly capable visual search, while the question of what a contributor's work is worth when it trains a model that substitutes for the library is being settled in courtrooms and licensing negotiations rather than in anything resembling a market.
**Workforce:** Content review and moderation staff, keywording and metadata specialists, search and computer vision engineers, contributor relations, rights and legal, enterprise sales and customer support

## Key Pain Themes
Generative image and video models changed the demand side and the supply side at once. A meaningful share of the routine commercial imagery that funded the industry can now be generated, which compresses the value of the ordinary library asset. At the same time the libraries themselves are among the most valuable training corpora in existence, which some marketplaces have monetised through licensing deals with model developers and others have litigated over. Either way the contributors whose work constitutes the corpus receive compensation determined by unilateral formula rather than by anything they negotiated, and the industry has not produced a defensible answer to what any individual contribution is worth.

Around that sit the operational realities. Discovery depends entirely on metadata that contributors supply, which means an excellent asset with poor keywords is invisible. Rights clearance — model releases, property releases, trademark and editorial restrictions — determines whether an asset can be licensed commercially and is verified by review. And the contributor at the other end of all of it has no visibility into why their income moves.

## Current Tech Landscape
Search combines keyword matching with visual similarity and increasingly with multimodal embedding models that make natural-language search over images genuinely work. Automatic keywording from image content is deployed across the major platforms with human correction. Generative tools are integrated directly into several marketplaces, trained on licensed or owned corpora, with contributor compensation funds attached. Content identification handles infringement and duplicate detection. Rights metadata — releases, editorial flags, restrictions — is captured at submission and verified in review. Getty's litigation against Stability AI and the various licensing deals signed by Shutterstock and Adobe define the two strategic postures available.

## Problems
- [[problems/stock-media-marketplaces/high-impact|🔴 High Impact: Pricing a Contribution to a Model]]
- [[problems/stock-media-marketplaces/low-impact-1|🟡 Low Impact: Keywording and Discoverability]]
- [[problems/stock-media-marketplaces/low-impact-2|🟡 Low Impact: Rights Clearance and Release Verification]]
- [[problems/stock-media-marketplaces/worker-life-1|🟢 Worker Life: The Content Reviewer on the Submission Queue]]
- [[problems/stock-media-marketplaces/worker-life-2|🟢 Worker Life: The Contributor Watching an Unexplained Income]]
- [[problems/stock-media-marketplaces/ml-opportunity|🧠 ML Opportunities]]
- [[problems/stock-media-marketplaces/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These marketplaces hold something rare: a very large corpus of licensed, rights-cleared, human-described visual material with a complete record of what buyers actually searched for, selected and licensed over two decades. That combination — content, provenance, description and revealed demand — is exactly what makes it valuable as training data and exactly what would be needed to price a contributor's share of a model's output. The industry has used the corpus for the first purpose and has not attempted the second, distributing compensation by formula instead. Whatever the courts eventually decide about training on scraped data, the marketplaces with clean provenance are the only parties who could demonstrate a principled attribution, and it is the one thing that would distinguish a licensed corpus from an unlicensed one on grounds other than legal risk.
