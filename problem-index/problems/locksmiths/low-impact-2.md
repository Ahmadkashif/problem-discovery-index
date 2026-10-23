# The NASTF Authorisation Trail Kept in a Camera Roll

**Industry:** [[locksmiths|Locksmiths]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every automotive key code a locksmith draws through the NASTF registry needs an ownership-verified authorisation form within five days and an answer to any audit within seven, and most small firms keep that trail in photos and memory, outside the job ticket.
**Tags:** #large-language-models #cnns #transfer-learning #compliance #workflow-orchestration #data-integration #automation

## The Problem
To replace a lost key on a recent car, an independent locksmith draws the key code, immobilizer PIN or reset data from the automaker through the NASTF Secure Data Release Model. The registry's terms (8 January 2025) attach a paper trail to every draw. The credential holder must be present with the owner and the vehicle. They must verify title or registration, a US or Canadian driver's licence and the VIN match, photograph the proof, and file an electronic Customer Authorization (D1) form in the SDRM portal within five days of the automaker transaction. The registry can audit any transaction and expects an answer within seven calendar days. The account itself carries deadlines too. Each VSP ID lasts two years, renewal should start 60 days ahead, and an expired insurance certificate, licence or fidelity bond must be replaced within 15 days or every account on the business is suspended. Through all of it, the security data itself may not be stored, databased or sent electronically.

A two-truck automotive shop meets these rules with a camera roll, a notebook and a late-night session in the portal. When an audit email arrives, the owner searches photos by date to rebuild a job they did weeks ago.

## What Already Exists
NASTF's own SDRM portal takes D1 forms and holds account documents. Field-service platforms such as Workiz, Housecall Pro, Jobber and ServiceTitan schedule, invoice and take payment for the automotive job, and several market to locksmiths. Generic document-scanning and e-signature apps capture IDs and signatures.

## The Customisation Gap
None of these joins the registry trail to the job. The automotive-specific layer has to do several things. It should capture the licence, registration and VIN once at the vehicle, read the fields and check that name, address and VIN agree. It should prefill the D1 from that capture and the job, and track the five-day filing window per transaction. It should assemble an audit pack (job, invoice, photos, D1 reference) in one step, and watch the expiry dates of every account document and credential on the business. It must also hold a hard boundary: the key code and PIN never enter the system, because NASTF forbids storing them. Generic field-service software treats a car key job like any other service call. Here the job is a regulated draw of automaker security data with a repair attached.

## Impact If Solved
Separate capture and portal entry, an estimated ~5–10 minutes per automotive job, falls to about a minute inside the ticket. For a shop doing ~10–20 key jobs a week that recovers roughly 1–3 hours weekly (estimate). Answering an audit drops from an estimated ~1–3 hours of searching to minutes. The larger gain is avoiding suspension. A lapsed document or missed renewal shuts off every VSP account on the business, and with it the shop's automotive revenue, which for a specialist can run to ~$5,000–$15,000 a week (estimate).
