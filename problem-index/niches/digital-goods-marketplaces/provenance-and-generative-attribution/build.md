# A Checkbox Asking If It Was Generated

**Niche:** [[niches/digital-goods-marketplaces/provenance-and-generative-attribution/profile|Provenance & Generative Attribution]]
**Industry:** [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Marketplaces decide what may be sold on the basis of an uploader ticking a box, on a question the uploader frequently cannot answer accurately about their own work.
**Tags:** #compliance #diffusion-models #transformers #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #contrastive-learning
**Contested on:** Every serious competitor in this niche is fighting to establish what an asset was made from before it is listed for sale — and whoever can answer that decides what a marketplace is allowed to sell.

## The Problem
A creator makes a template. Some elements were drawn, some generated, some assembled from a pack bought elsewhere whose own provenance is unknown, and one texture came from a model trained on this marketplace's catalogue. The upload form asks: is this AI-generated? There is no honest answer to that question as posed, and the platform makes a listing decision on it. Buyers then resell the work into contexts — advertising, publishing, games — where their own clients now ask for provenance, and neither the buyer nor the platform nor often the creator can supply one.

## Why Nobody Has Built This
The question arrived faster than any answer and the category's response was a policy checkbox. Detection of generated content is unreliable and getting harder, so a detection-first strategy fails — this is why the obvious approach has not worked and why the record-keeping approach is the one available. Provenance standards exist but require adoption across a tool chain nobody controls. And clarifying provenance risks invalidating a large part of the existing catalogue, which nobody wants to discover.

## What to Build
Build the record rather than chase the detection. Capture provenance at creation through integrations with the tools creators use, since the only reliable moment to know what an asset was made from is while it is being made — this is the design principle the whole niche turns on and it reframes the problem from forensics to record-keeping. Adopt and propagate existing content credential standards rather than inventing one, because the value is entirely in interoperability. Represent provenance as a composition rather than a binary, as real assets are mixtures and any yes-or-no field is wrong for most of the catalogue. Use detection as a corroborating signal with calibrated confidence, never as a verdict, since false accusations of generation are professionally damaging and detection cannot support them. Verify what can be verified — bought components against their marketplace records, which is exact where detection is probabilistic. Give buyers a provenance statement they can pass to their client, which is the commercial driver and the thing buyers are beginning to be required to produce. Let creators record their process voluntarily and benefit from it commercially, which is how coverage actually grows. Establish what happens when a model was trained on the platform's own catalogue, since this is the sharpest conflict in the category and every platform is avoiding stating a position. Handle the pre-existing catalogue explicitly with an unknown state rather than assuming, which is honest and avoids a retroactive judgement nobody can support. And track provenance coverage as a catalogue metric, because it is the asset that will decide which marketplaces enterprise buyers can use.

## Target Customer
Digital goods marketplaces, the enterprise buyers now required to state provenance, creative tool vendors, and the creators whose work trains the models.

## Impact If Built
Detection is unreliable and worsening, which is why a detection-first strategy fails and record-keeping at creation is the available route. Provenance as a composition rather than a binary fits the actual catalogue, and a passable provenance statement is what enterprise buyers are starting to require.
