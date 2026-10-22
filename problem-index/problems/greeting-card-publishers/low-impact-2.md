# Scan-Based Trading Settlement and Card Shrink

**Industry:** [[greeting-card-publishers|Greeting Card Publishers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** EDI platforms move the documents scan-based trading needs, but nothing reconciles what a publisher shipped, what scanned, what came back and what vanished in a card department of a thousand pockets.
**Tags:** #change-point-detection #bayesian-inference #hypothesis-testing #descriptive-statistics #data-integration #automation #revenue-impact

## The Problem
Under scan-based trading the publisher owns every card on the retailer's fixture until it scans at the register, and is paid for what sells, generally within 10–15 days according to American Greetings' 2011 filing. Shrink (theft, damage, cards scanned under the wrong code, cards that never reached the pocket) is the publisher's loss, at a negotiated rate, in one of the highest-shrink categories in a supermarket. Seasonal cards add a second flow: after the holiday, unsold cards are pulled, and credits or destroy authorisations are processed against each store.

Reconciling these flows is a monthly argument. Shipments by store, sales reports by store and UPC, seasonal pull-backs and merchandiser counts arrive in different systems and at different grains. The publisher's account team tries to work out whether a store's apparent shrink is theft, a scanning problem (a cashier ringing every card as one UPC), a receiving error or a merchandiser who never stocked the shipment. By the time it is settled, the money has often been written off.

## What Already Exists
EDI providers such as SPS Commerce and TrueCommerce carry orders, advance ship notices and point-of-sale reports between suppliers and retailers, and TrueCommerce markets scan-based trading support. Retail analytics platforms visualise point-of-sale data, and consumer-goods firms use trade promotion and deduction management tools to dispute retailer deductions.

## The Customisation Gap
Cards break the assumptions. A card department holds hundreds to over a thousand UPCs, each selling a few units a week, so ordinary out-of-stock and shrink thresholds misfire on small numbers. The adaptation needs: unit reconciliation per store and pocket across shipments, scans, merchandiser counts and seasonal returns; detection of scan errors such as one UPC suddenly selling for many pockets; shrink estimates with uncertainty so that a store is flagged only when the evidence supports it; seasonal pull-back and destroy credits matched to what was actually shipped for that season; and a dispute pack per store in the retailer's settlement format. The logic is card-specific because the unit of account (the pocket) and the seasonal take-back exist nowhere else in the retailer's supplier base.

## Impact If Solved
Shrink claims backed by store-level evidence recover money that is currently written off. Scanning and receiving problems get fixed at the store rather than absorbed, and account teams spend line-review time on assortment instead of arguing over the last quarter's settlement.
