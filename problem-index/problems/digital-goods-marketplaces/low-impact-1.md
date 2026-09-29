# Licence Term Expression and Verification

**Industry:** [[digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every purchase carries licence terms in prose, no part of the delivery path knows what they say, and neither the buyer who wants to comply nor the creator whose terms were exceeded can establish what was permitted.
**Tags:** #large-language-models #bert #transformers #word-embeddings #evaluation-metrics #transfer-learning #compliance #data-integration

## The Problem
A buyer purchases a digital asset under a licence: personal use only, single commercial project, unlimited commercial use, extended licence for resale in a product, per-seat for a font, per-title for game content.

The terms are prose in a purchase agreement, occasionally summarised as a tier name. The file downloaded is identical regardless of tier. Nothing in the delivery, the file or the buyer's records expresses what they bought the right to do.

Both sides suffer from this. A buyer who genuinely wants to comply cannot easily determine whether their intended use is covered, particularly in a team where the person using the asset is not the person who bought it. A creator whose asset appears in a product sold ten thousand times has no way to establish what licence was purchased or by whom.

Fonts are the sharpest case. Font licensing is genuinely complex — desktop, web, app and embedding rights are separate, priced by seats or page views — and enterprise font compliance is a real and expensive problem precisely because nobody can determine what a company is entitled to use.

## What Already Exists
Marketplaces define licence tiers with written terms. Purchase records establish who bought what. Some platforms offer extended licences at higher prices. Font foundries publish detailed licensing terms and enterprise compliance services exist. Creative Commons demonstrated machine-readable licence expression decades ago and it is widely used in open content. Digital rights management exists for media and is largely absent here.

## The Customisation Gap
Licence terms are never machine readable, so nothing downstream can check anything. Structuring them — permitted uses, seat counts, distribution limits, territory, duration — is a bounded extraction problem over a document class that is fairly standardised per platform, and it is the precondition for every other improvement.

Entitlement lookup for buyers does not exist. A designer using an asset should be able to determine what their organisation is licensed for, and instead searches purchase emails.

Usage verification is unattempted. Whether an asset appears in a context exceeding its licence — a personal-use template in a commercial product, a font on a public site under a desktop licence — is detectable for many asset types and is not checked, so licence breach is discovered only when a creator happens to notice.

Team and organisational licensing is poorly modelled. Assets are bought by individuals and used by organisations, and the mismatch is where most unintentional breach originates.

## Impact If Solved
Licence terms govern every transaction in this market and are invisible to every system that handles the asset afterwards. Machine-readable terms with entitlement lookup would let compliant buyers comply — which most want to do — and give creators a basis for establishing breach beyond noticing it themselves.
