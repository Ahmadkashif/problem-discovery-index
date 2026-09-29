# Comparables Drawn From Listings Nobody Bought

**Niche:** [[niches/online-marketplaces/pricing-and-reference-values/profile|Pricing & Reference Values]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** The comparable prices a seller sees are asking prices on active listings, which are disproportionately the ones that did not sell, so the visible market is an index of optimism.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #probability-distributions #evaluation-metrics #revenue-impact #quick-win #survival-analysis
**Contested on:** Every serious competitor in this niche is fighting to tell a seller what their one-of-a-kind item is actually worth and a buyer whether a price is fair — and whoever does that takes the transaction, because without a reference both sides are guessing and most guesses end in no sale.

## The Problem
A seller researches their price by browsing similar items. Everything they can see is an active listing with an asking price. Items priced correctly sold and vanished from view; items priced too high are still there, which is why they are visible. The seller is therefore looking at a sample biased toward the overpriced, anchors on it, prices high, and joins the same population — where they in turn become somebody else's comparable. The bias is structural, it compounds, and it operates on every marketplace where sold prices are not shown.

## Why It's Still Broken
Showing sold prices is technically trivial and commercially fraught: sellers dislike it because it reduces their pricing latitude, and platforms worry about lowering average selling prices and therefore take rate. Some categories have privacy concerns about transaction prices. And the survivorship bias is invisible to the seller, who reasonably assumes that what they can see is the market.

## What a Fix Looks Like
Show what sold, not what is asked. Display completed sale prices with dates and attributes as the primary comparable set, which is the fix, is technically trivial, and removes a structural bias the whole market is currently anchored to. Show the asking-price distribution alongside it with the sell-through rate at each level, so a seller can see that items above a certain price rarely sell rather than being told not to price there. Report time-to-sale with each comparable, since a sale after six months and a sale in three days are different evidence. Correct for survivorship explicitly where sold prices cannot be shown, presenting active listings weighted by their eventual outcome rather than raw. Show the gap between asking and sold in the category, which is a single number that makes the bias legible to a seller immediately. Address the take-rate objection with evidence rather than assumption, since a market where things sell faster at accurate prices may generate more revenue than one where inventory sits — and that is a measurable question no operator appears to have run. Handle the privacy question by aggregating rather than by withholding. And let sellers see their own sold history against the category, which is the most persuasive evidence a seller can receive.

## Who Feels the Pain
Sellers anchored on a visible market composed mostly of failures; buyers who cannot tell whether a price is reasonable; and operators whose inventory sits because the whole market is pricing off the unsold.

## Impact If Fixed
Sold prices are trivial to show and remove a structural bias the entire market anchors to. The gap between asking and sold prices in a category is one number that makes the bias legible to a seller instantly.
