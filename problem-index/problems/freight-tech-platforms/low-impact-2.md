# Accessorial Documentation and Billing Rules

**Industry:** [[freight-tech-platforms|Freight Tech Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Document capture from proof of delivery paperwork is a solved commodity, and whether a detention or lumper charge actually gets paid depends on shipper-specific evidence rules that live in a contract nobody has encoded.
**Tags:** #large-language-models #bert #transformers #feature-engineering #evaluation-metrics #transfer-learning #compliance #revenue-impact

## The Problem
Beyond the linehaul rate, freight generates accessorial charges: detention, layover, lumper fees, driver assist, redelivery, truck ordered not used, fuel surcharge adjustments. They are a meaningful share of margin, and whether they get paid depends entirely on documentation.

Each shipper has its own rules. One requires an in-and-out time stamped by the facility. Another accepts a signed bill of lading with handwritten times. Another requires notification within twenty-four hours through a portal. Another disallows detention entirely for the first three hours regardless of what happened. These rules sit in a master transportation agreement negotiated years ago, and the billing clerk processing a claim knows some of them.

So charges go unbilled because nobody was sure they would stick, or get billed and denied, and the denial arrives weeks later as a short payment with a code that explains little. Both outcomes are margin that the broker or carrier earned and did not collect.

## What Already Exists
Document capture from bills of lading, proof of delivery and lumper receipts is mature and accurate. Freight audit and payment providers process invoices at scale and catch rate discrepancies. TMS platforms support accessorial codes and charge entry. EDI standards cover the transaction formats. Visibility platforms produce timestamped arrival and departure data.

## The Customisation Gap
The rules are contractual and unstructured. The master agreement with each shipper defines what evidence supports which charge under which conditions, in prose, in a document stored somewhere. Nothing extracts those terms into a machine-checkable form, so compliance with them depends on a clerk's memory of a contract they may never have read.

Extracting accessorial terms from transportation agreements is a well-shaped document task on a document class that is fairly standardised in structure and highly variable in specifics. Once extracted, every charge can be checked against its own evidence requirement before submission, and the missing document can be requested while the driver is still reachable rather than three weeks later.

The second gap is the denial loop. Short payments arrive with reason codes and no analysis. Which shippers deny which charges at what rate, and which evidence patterns survive, is directly measurable from the platform's own billing history and would tell a broker exactly which charges are worth pursuing — and which contract terms to renegotiate at renewal.

## Impact If Solved
Accessorial revenue is real margin in a business with thin margins, and a substantial share of it is abandoned before submission because nobody was confident it would be paid. Encoding the contract terms and checking evidence before submission converts a guess into a decision, on documents already being captured.
