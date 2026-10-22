# Licence Terms That Travel With Every File

**Niche:** [[niches/commercial-photographers/solo-commercial-photographers/profile|Solo Commercial Photographers]]
**Industry:** [[industries/commercial-photographers|Commercial Photographers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The licence a solo photographer negotiated lives in a PDF in their inbox; the image file the client passes around carries nothing but the camera's serial number.
**Tags:** #large-language-models #feature-engineering #data-integration #compliance #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a solo photographer's shoot into a licence that is quoted, signed, attached to the files and paid again on renewal, and whoever makes usage collectable without a producer or rep takes the photographer.

## The Problem
Once delivered, an image travels: the client's marketing team sends it to a printer, an agency, a partner, a magazine. The licence terms don't travel with it. Nobody downstream knows the image was licensed for one year of web use, so it ends up in a trade-show banner and a reprinted brochure three years later, unbilled.

## Why Nobody Has Built This
Rights metadata standards exist (IPTC fields, the PLUS licensing vocabulary) but are filled in by hand, if at all, and are stripped by many platforms. Licensing tools and delivery tools are sold separately, so nothing writes the agreed terms into the files automatically.

## What to Build
A licence engine that reads the signed estimate or contract, turns the usage into structured terms with a language model, writes them into each delivered file's metadata (licensee, permitted uses, territory, expiry, contact for extensions), keeps a ledger keyed to image fingerprints so terms survive metadata stripping, and sends the photographer and the client renewal notices before expiry with a pre-priced extension.

## Target Customer
Self-employed commercial photographers doing a mix of brand, architectural and agency work, typically billing $60,000–$250,000 a year (estimate).

## Impact If Built
Downstream users can see the terms, renewals become routine invoices, and the photographer has a clean record for any later dispute. That plausibly recovers several thousand dollars a year in extensions that now go unbilled (estimate).
