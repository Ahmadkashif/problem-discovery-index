# Document Extraction Extended to the Claim Package

**Niche:** [[niches/freight-tech-platforms/freight-document-accessorial-billing/profile|Document & Accessorial Billing]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Extraction from a photographed bill of lading is a solved commodity every freight vendor already sells, and it extracts the fields for an invoice while the information that decides whether an accessorial is paid sits in the same image unread.
**Tags:** #cnns #transformers #large-language-models #evaluation-metrics #confidence-intervals #data-integration #automation #compliance
**Contested on:** Every serious competitor in freight billing is fighting to get an accessorial charge paid on first submission against a specific shipper's evidence rules — and whoever holds first-pass payment rate highest takes the account.

## The Problem
A driver photographs the delivery paperwork. Extraction pulls the delivery date, the signature presence and the piece count, which is what the invoice needs. The same document frequently carries the arrival and departure times written by the receiver, a notation about a lumper fee paid, an exception noted on the freight, and a stamp indicating a detention acknowledgement. None of those are extracted, because the extraction was configured for invoicing, and each of them is exactly the evidence an accessorial claim requires.

## What Already Exists
Freight document capture is a mature product category with strong accuracy on standard bill of lading and proof of delivery formats. Handwriting recognition has improved substantially and handles the printed-and-annotated documents typical of freight. Mobile capture with quality checking at the point of photography is standard. Extraction of arbitrary fields from semi-structured documents using layout-aware models is commodity. Everything needed already exists inside the products being sold.

## The Customization Gap
The adaptation is to extract for the claim rather than for the invoice. It requires: (1) target fields expanded to everything an accessorial requires — handwritten arrival and departure times, lumper receipts, exception notations, detention acknowledgements, seal numbers — with handwriting handled as a first-class case rather than as a degraded one; (2) quality checking at capture, since a photograph that is unreadable is discovered days later in billing and by then the driver is four states away, and a prompt to retake at the dock costs seconds; (3) completeness checking against the specific shipper's requirements at the moment of capture, so the driver is told what else is needed while they are still standing there — which is the highest-leverage intervention available in this niche; (4) confidence-gated human review on the fields that carry money, because a mis-read arrival time is a charge that fails or a claim that is wrong; and (5) assembling the extracted evidence into the submission package automatically rather than into a database.

## Target Customer
Carriers and brokerages, freight audit providers, and the document capture vendors already serving them who could extend their extraction targets.

## Impact If Solved
Completeness checking at the dock converts an evidence problem discovered in billing into a thirty-second correction at the point of delivery, which is where the entire loss can be prevented. The extraction capability is already purchased by most of these companies; what is missing is pointing it at the fields that decide whether an accessorial gets paid.
