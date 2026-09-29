# Detection Across Surfaces That Do Not Cooperate

**Industry:** [[brand-protection-firms|Brand Protection Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Counterfeits are found by matching images and keywords across marketplaces, and the sellers who matter have learned exactly what that matches on.
**Tags:** #cnns #contrastive-learning #transformers #bert #graph-neural-networks #dimensionality-reduction #evaluation-metrics #k-nearest-neighbors

## The Problem
Detection means scanning marketplaces, social platforms, app stores, messaging channels and domain registrations for listings that appear to infringe. The standard methods are keyword matching against brand and product names and image matching against the brand's own catalogue.

Sophisticated sellers defeat both. Brand names are misspelled, transliterated, spaced or replaced with recognisable substitutes; product images are cropped, watermarked, mirrored, colour-shifted or replaced with photographs of the genuine article while the goods shipped are not; listings describe the product without naming the brand and rely on search behaviour and social referral to find buyers.

The surfaces also differ enormously in accessibility. Marketplaces vary in what they expose; social platforms have restricted programmatic access considerably; messaging channels and private groups, where a growing share of the trade happens, are largely unobservable; and live commerce is ephemeral by design.

And the determination itself is hard. An image matching the brand's catalogue may be a counterfeit listing, a legitimate reseller using the manufacturer's photography, a parallel import, a repair service or a review. Image match is evidence of the image, not of the goods.

## What Already Exists
The firms run large-scale scraping and matching operations with image similarity, text matching and seller attribute analysis. Platform programmes provide privileged search and reporting access for enrolled brands. Test purchasing provides ground truth on physical goods and is expensive and slow. Domain monitoring uses registration feeds and certificate transparency. Some firms apply machine learning to listing classification with results they do not publish.

## The Customisation Gap
Matching needs to operate on the product rather than on the image. Representations that survive cropping, mirroring, colour shift and watermarking — and that capture what the product is rather than which photograph was used — are what defeat the standard evasions, and they are a well-understood problem in visual retrieval that this field applies unevenly.

Text needs the same treatment. Brand references survive misspelling, transliteration, spacing and substitution, and matching on the reference rather than the string is what catches the listings designed to evade keyword search.

Seller behaviour is the signal the evaders cannot easily remove. Pricing relative to the genuine article, inventory depth, shipping origin and speed, account age, review velocity and catalogue breadth together characterise a counterfeit operation in ways that are stable across listing-level evasion.

And the legitimate-use distinction has to be built in rather than bolted on. Resale, parallel import, repair, compatible parts, parody and criticism are lawful uses that look similar to detection, and a system optimised only for recall will hit all of them — which is the overreach problem, and it is a modelling choice rather than an accident.

## Impact If Solved
Detection determines what enforcement can act on, and the standard methods are well understood by the operators who matter. Product-level visual representation, reference-level text matching and seller behaviour modelling would catch the operations that currently evade, while explicit legitimate-use classification would stop the programme hitting resellers and critics — which is the other half of the same problem.
