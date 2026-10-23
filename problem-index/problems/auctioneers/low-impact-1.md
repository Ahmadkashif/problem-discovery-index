# Lot Cataloguing for Every Bidding Platform

**Industry:** [[auctioneers|Auctioneers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Photo-to-listing AI already drafts titles and descriptions for marketplace sellers; auction cataloguing needs lotting decisions, defensible condition language and each bidding platform's own categories, and still gets done one lot at a time.
**Tags:** #large-language-models #transformers #cnns #object-detection #transfer-learning #automation #data-integration

## The Problem
After the consignment is signed, someone has to turn a house, a shop or a machine shed into a catalogue. That means deciding what becomes a lot (one chair or a set of six; a box of hand tools or the one good plane pulled out of it), photographing each lot from several angles, writing a title buyers will search for, describing maker, model, material, age and condition, and assigning it to a category on the platform the sale runs on. A 600-lot estate sale (illustrative) is days of work for a two-person crew, and the description written at speed on lot 412 is the one a bidder quotes back in a dispute. If the same sale is cross-listed, the categories, field names and image rules change from Proxibid to HiBid to LiveAuctioneers.

## What Already Exists
General marketplace tools draft listings from photos (eBay's AI listing assistant, multichannel tools such as Vendoo or List Perfectly for resellers), and Auction Technology Group has built an in-house model that predicts lot categories from current and historical inventory. Clerking software such as Auction Flex imports consignor inventory from spreadsheets and prints catalogues; Wavebid and AuctionMethod include mobile cataloguing apps that attach photos to lot numbers. Vision models can name many mass-produced items from a photo.

## The Customisation Gap
Auction cataloguing has needs the reseller tools ignore. Lotting is a value decision: grouping low-value items so they sell, splitting out the piece that would carry a lot on its own, and keeping a consignor's items separate for settlement. Condition language must be consistent and cautious ("as is, where is", "not tested", "losses to veneer") because it is part of the terms of sale and the basis of disputes. Restricted items need flags before listing: firearms that must go through a licensed dealer, ivory and tortoiseshell under federal and state wildlife law, hazardous materials, titled vehicles and trailers. Each platform wants its own category tree and fields, and equipment lots need serial numbers, hours and specification fields matched to the model. Finally, the cataloguer's draft must be fast to correct in bulk on a tablet in a garage with poor signal.

## Impact If Solved
A cataloguing tool that proposes lots, drafts titles and condition notes in the firm's own house style, flags restricted items and maps to every platform's categories could plausibly halve photography-to-listing time (estimate), let a small firm take on more consignments in the busy season, and reduce the "not as described" disputes that cost auctioneers refunds and reviews.
