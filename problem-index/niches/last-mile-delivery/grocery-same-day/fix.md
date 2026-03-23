# Real-Time Substitution Communication During Picking

**Niche:** [[niches/last-mile-delivery/grocery-same-day/profile|Grocery & Same-Day Delivery]]
**Industry:** [[industries/last-mile-delivery|Last-Mile Delivery]]
**Type:** Fix (Pain Point)
**One-liner:** Shoppers making product substitutions during order fulfillment can't efficiently communicate substitution options to customers in real time — leading to unwanted substitutions that customers reject at delivery, generating returns and refund requests.
**Tags:** #large-language-models #automation #worker-facing #quick-win

## The Problem
Grocery orders have a 15-25% out-of-stock rate on individual items. When a shopper encounters an unavailable item, they must decide on a substitution: switch to a different brand, a different size, or skip the item. Instacart's platform allows real-time customer approval, but independent grocers running their own delivery have no such system — shoppers either substitute without asking (leading to unwanted items) or call the customer (time-consuming and disruptive during a 50-item pick). The substitution interaction adds 1-3 minutes per item when done by phone, and a 50-item order with 8 substitutions adds 8-24 minutes to fulfillment time.

## Why It's Still Broken
Building a real-time substitution approval flow requires: a customer-facing notification (SMS or app push), a picker-facing interface to scan the substitute and wait for approval, timeout logic (customer doesn't respond in 2 minutes — proceed with best match or skip?), and integration with the order management system to update the final order and pricing. Independent grocers lack the development resources to build this workflow. Off-the-shelf delivery platforms (Onfleet, Tookan) manage dispatch but don't handle the pre-delivery fulfillment workflow.

## What a Fix Looks Like
A substitution management module that: (1) sends the customer a text or web notification when an item is unavailable, showing the shopper's suggested substitute with photo and price; (2) gives the customer a 2-minute response window to approve, suggest an alternative, or skip the item; (3) defaults to the shopper's best judgment if the customer doesn't respond; (4) updates the order total and packing slip automatically. The shopper scans the substitute, the customer approves by text, and the pick continues without phone calls.

## Who Feels the Pain
Grocery shoppers/pickers who lose 15-30 minutes per shift on substitution phone calls, and customers who receive unwanted substitutions and lose trust in the delivery service.

## Impact If Fixed
Reducing substitution handling time from 3 minutes to 30 seconds per item saves 20-40 minutes per shift per shopper. Reducing unwanted substitution returns (5-8% of orders) by 70% saves $1.50-$3.00 per affected order in return processing costs.
