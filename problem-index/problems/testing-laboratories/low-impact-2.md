# Scoping and Quoting a Product Test Programme

**Industry:** [[testing-laboratories|Testing Laboratories]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Quote-to-cash software works for selling configurable products, but a product safety or EMC lab's quote is really a regulatory analysis — which standards apply in which markets, which tests the product's design triggers, and which existing reports can be reused.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #evaluation-metrics #feature-engineering #automation #revenue-impact

## The Problem
A manufacturer emails a product safety and EMC lab: a battery-powered smart home device with Wi-Fi and Bluetooth, to be sold in the US, Canada, the EU, the UK and Japan. Before anyone can quote, an engineer has to work out the test programme: the safety standard (IEC 62368-1 and its national deviations), EMC emissions and immunity standards, radio standards and the regulators' authorisation routes (FCC, ISED, the EU Radio Equipment Directive, UK and Japanese equivalents), battery transport and safety tests, and any energy or chemical requirements. They need the product's construction, power supply, radio modules and their existing certifications, because a pre-certified module or an existing CB Scheme report can remove whole test blocks. Then they estimate chamber days, sample quantities and engineering hours.

This takes a senior engineer hours to days per quote. Labs lose work to whoever answers first, and quotes are often wrong in both directions: missed tests become change orders and angry clients, and redundant tests make the lab uncompetitive.

## What Already Exists
CPQ platforms (Salesforce CPQ and similar) and the quoting modules inside LIMS and ERP systems handle price books, discounting and approval routing. Regulatory intelligence databases track standards and country requirements. Large certification bodies maintain internal global market access guides.

## The Customisation Gap
The lab-specific layer is the mapping from a messy product description to a defensible test plan: extracting product attributes (supply voltage, radio bands, battery chemistry, intended user, enclosure) from datasheets and emails; applying standards' scope clauses and national deviations; recognising when an existing test report or certificate can be leveraged under the CB Scheme or a module grant; converting the plan into chamber time and engineering effort that reflects the lab's actual historical durations and first-pass failure rates for similar products; and recording the reasoning so the project engineer who runs the job inherits the scope rather than rediscovering it. CPQ tools price a configuration someone already defined; here defining the configuration is the work.

## Impact If Solved
Turning a two-day scoping exercise into a reviewed draft within an hour lets a lab answer first, quote more accurately, and free senior engineers from estimating work — while cutting the change orders that sour client relationships when a missed standard surfaces halfway through testing.
