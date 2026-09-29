# Menu Item Mapping Across Channels

**Industry:** [[restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Middleware that syncs menus between the POS and the delivery marketplaces is a solved, competitive category, and every new restaurant still has a human build the same menu five times because no two channels model a modifier the same way.
**Tags:** #bert #word-embeddings #large-language-models #k-nearest-neighbors #transfer-learning #data-integration #workflow-orchestration

## The Problem
A restaurant's menu now exists in five to nine places: the POS, its own website and app, three delivery marketplaces, a kiosk, a QR-code table ordering flow, and a third-party loyalty system. Each must reflect the same food, the same prices — often deliberately different prices per channel — and the same modifiers, and each models modifiers differently.

The POS may treat "no onions" as a modifier on a required group; one marketplace treats it as an option in an optional group with its own pricing rules; another has a nested structure with different cardinality constraints; a third does not permit negative modifiers at all and expects a separate item. Item names are truncated differently. Photographs are required in some channels and not others. Availability windows differ.

So a menu build specialist does it by hand, per channel, at onboarding, and then again whenever the restaurant changes the menu — which for an independent restaurant is constantly. Discrepancies accumulate silently, and the restaurant discovers them when a customer receives the wrong food or when a channel is selling an item at last spring's price.

## What Already Exists
Menu integration middleware is a mature category: Deliverect, Chowly, Otter, Olo Rails and the marketplaces' own POS integrations. All of them sync a menu between systems and handle the mechanics of publishing. POS vendors ship menu management. Marketplaces publish menu APIs with documented schemas.

## The Customisation Gap
The middleware moves menus; it does not reconcile ontologies. Given a POS menu whose modifier structure does not have a valid representation in a target channel, someone must decide how to express it, and that decision is made by a human once per restaurant per channel and then frozen.

The unexploited asset is that the vendor has seen the same problem tens of thousands of times. The mapping from a POS modifier structure to a given marketplace's schema, for a given cuisine and service style, is highly repetitive across restaurants. Learning the mapping from historical builds — and proposing it for confirmation instead of presenting an empty form — is a well-shaped problem on data the vendors have and have never treated as a corpus.

The second gap is drift detection. Once a menu is live across nine channels, nothing checks that they still agree. Comparing item sets, prices and availability across channels daily, and flagging divergence, is trivially buildable and universally absent, and it catches the errors that actually cost restaurants money.

## Impact If Solved
Menu build is the largest single line in onboarding cost for every platform in the category and the most common reason a restaurant delays going live on a profitable channel. Drift is a silent revenue leak that operators discover from customer complaints. Both are addressable from data the vendors already hold.
