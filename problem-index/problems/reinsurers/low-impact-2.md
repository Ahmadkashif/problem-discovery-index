# Renewal Wording Compared Against the Expiring Contract

**Industry:** [[reinsurers|Reinsurers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** At every renewal a treaty wording is redrafted against the expiring contract and the market's model clauses, and the changes that matter most after a loss — event definitions, hours clauses, exclusions — are found by reading.
**Tags:** #large-language-models #transformers #bert #word-embeddings #evaluation-metrics #compliance #automation

## The Problem
A treaty is agreed on a slip or term sheet at the renewal, and the full wording follows, often weeks later. The wording defines what one loss occurrence is: the hours clause that groups damage into a single event (commonly ~72 hours for windstorm and ~168 hours for earthquake or flood), the territorial scope, how ultimate net loss is calculated, which reinstatements are paid and at what premium, and which perils are excluded. Cyber and communicable disease exclusions, usually based on market model clauses, were rewritten across the market after 2020. A cedent's wording drifts from year to year through small edits by brokers and lawyers, and different reinsurers on the same programme may sign slightly different versions.

The drift matters only after an event. Then a claims team discovers that a wildfire burning over ten days, or a run of convective storms, falls inside one event under this cedent's wording and two under another's. The reinsurer pays one more reinstatement than it priced for, or argues over an exclusion it thought was standard. Wording specialists compare documents by eye, under the same renewal pressure as everyone else.

## What Already Exists
Contract-review AI built for legal and procurement work (Kira, Luminance, Harvey and contract lifecycle platforms), document comparison in word processors, Lloyd's and London market contract-certainty processes, and market model clause libraries published by the Lloyd's Market Association and others.

## The Customisation Gap
Generic contract AI finds that a clause changed. It does not know what the change does to the reinsurer's exposure. The reinsurance-specific layer is: a clause taxonomy for treaty wordings (event definition, hours clause, ultimate net loss, reinstatements, territorial scope, exclusions, claims cooperation and control, commutation, insolvency and offset); recognition of market model clauses and deviations from them; a per-cedent history of each clause across renewals; and an impact view that runs the changed event definition against historical event footprints to show what it would have done to past losses. The comparison must also follow the slip-to-wording gap, where the agreed terms and the issued wording disagree.

## Impact If Solved
A renewal wording reviewed by clause type in an hour rather than a day (estimate), with every deviation from the expiring contract and from the model clause flagged and explained. That removes a class of post-event disputes that otherwise surface months after the loss, when the reinsurer has already reserved for a different answer.
