# AI-Powered Voice and Text Order Processing

**Niche:** [[niches/restaurant-suppliers/order-intake-automation/profile|Order Intake Automation]]
**Industry:** [[industries/restaurant-suppliers|Restaurant Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product converts a chef's phone call, voicemail, or text message into a structured ERP order — transcribing "Hey, I need 20 strips, 10 filets, 30 pounds of wings, and a case of ranch" into the correct SKUs, quantities, and customer account without human intervention.
**Tags:** #bert #speech-recognition #named-entity-recognition #nlp #automation #ai-agent

## The Problem
A chef calls their supplier at 4:30 PM and leaves a voicemail: "It's Tony from Roma Pizza, I need my usual proteins plus add 20 pounds of Italian sausage and give me two cases of San Marzano tomatoes instead of one this week." This 15-second message contains: customer identification (Tony from Roma Pizza), a reference to a standing order ("my usual proteins"), two modifications (add Italian sausage, double the tomatoes), and implicit delivery scheduling (standard delivery day). An office staff member spends 5-10 minutes translating this into an ERP order: looking up Tony's account, finding his last protein order, adding the sausage by searching the catalog for the correct SKU, modifying the tomato quantity, and confirming the delivery date. Multiply by 100 orders per day, and 2-3 staff members spend 4-6 hours on this mechanical translation.

## Why Nobody Has Built This
Converting natural-language food orders to structured ERP entries requires solving multiple NLP problems: (1) speech-to-text on noisy kitchen phone calls and accented English, (2) customer identification from voice or phone number, (3) product entity recognition ("strips" = NY Strip Steak, "San Marzanos" = San Marzano Whole Peeled Tomatoes 28oz), (4) implicit reference resolution ("my usual" = last week's order for this customer), (5) quantity and unit normalization ("20 pounds" vs. "two cases" — are these equivalent for this product?), and (6) ERP SKU mapping against the supplier's specific product catalog. Each problem is solvable with current NLP/ASR technology, but the end-to-end pipeline connecting a voicemail to an ERP order entry has not been productized for food distribution.

## What to Build
An AI order processing system that: (1) receives orders via phone (answered by AI voice agent or transcribed from voicemail), text message, and email, (2) transcribes and parses orders using speech recognition and NER fine-tuned on food distribution vocabulary, (3) maps parsed items to the supplier's product catalog using fuzzy matching and customer purchase history for disambiguation, (4) resolves implicit references ("my usual" → last comparable order from this customer), (5) generates a structured order for human review (office staff sees the parsed order with confidence scores and confirms or corrects), and (6) learns from corrections to improve accuracy over time. Target: 80-85% of orders processed with no human intervention after initial 30-day training period.

## Target Customer
Operations managers at restaurant suppliers processing 50+ phone/text orders per day. Approximately 3,000-5,000 US suppliers at this scale. Price model: $0.50-$1.00 per order processed, or $500-$1,500/month flat rate.

## Impact If Built
Order processing labor reduced by 60-70%, saving $60K-$150K annually in office staff time. Order entry errors reduced from 3-5% to under 1% through automated catalog matching with confirmation. Order cutoff bottleneck eliminated — AI processes orders in real time rather than batching at 5 PM. Office staff redeployed from data entry to customer service and problem resolution.
