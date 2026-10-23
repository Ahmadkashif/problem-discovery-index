# AI Agents & Platform Opportunities — Auctioneers

**Industry:** [[auctioneers|Auctioneers]]

---

## 1. Consignment Walkthrough and Proposal Agent
#ai-agent #tacit-knowledge-ml #large-language-models #gradient-boosting #confidence-intervals #revenue-impact

**Concept:** An agent the auctioneer runs on a phone during a walkthrough. It listens to the narration and watches the video, drafts an item inventory with estimate ranges and comparables, records the auctioneer's own adjustments as the firm's estimate ledger, and turns the result into a consignment proposal: expected proceeds range, recommended format (absolute, reserve, guarantee), venue for specialist pieces, marketing plan and a contract carrying the terms the state requires.
**Inputs:** Walkthrough video and voice; the firm's past estimates and hammers; public price results; the firm's commission schedule and contract templates; the state's licensing and contract rules.
**Outputs / Actions:** Draft inventory and estimate ledger; proposal letter and contract for signature; flagged pieces to route to specialist houses; later, estimate-versus-hammer reports by estimator and category.
**Why now:** Vision-language models can draft item lists from video and voice cheaply, and price-realised archives have grown into the tens of millions of lots, so a defensible range with comparables can appear during the meeting rather than days after.
**Market:** Independent auction firms of 2–30 people (~4,000–6,000 firms, estimate) paying per consignment or per seat; the strongest buyers are estate and equipment auctioneers who compete for consignments against firms promising higher numbers. No existing buyer category; clerking vendors and bidding platforms are the natural distribution partners.

---

## 2. Catalogue-to-Platform Agent
#ai-agent #large-language-models #cnns #object-detection #automation #worker-facing

**Concept:** An agent that takes the cataloguer's photos and turns them into a finished, multi-platform catalogue: proposes lots, drafts titles and condition notes in house style, checks restricted items, maps each lot to every platform's categories and fields, sequences lots for bidding, and publishes to the chosen platforms with the consignor codes settlement needs.
**Inputs:** Photo sets; consignor inventory; the firm's style guide and past catalogues; platform category trees and listing rules; restricted-item rules.
**Outputs / Actions:** Lot list with drafted text and flags for cataloguer review; platform-ready listings published through each platform's upload format; a lot-order recommendation; a list of pieces worth specialist attention.
**Why now:** Multimodal models now identify mass-produced items and read maker's marks and serial plates well enough to draft, not just tag, and platforms have opened white-label and cross-listing (ATG's atgXL) that reward fast, consistent catalogues.
**Market:** Firms already paying for clerking software and platform fees; competes with cataloguing features the platforms build for themselves (ATG's category prediction) and with reseller listing tools. Differentiates on lotting, condition discipline and multi-platform output.

---

## 3. Post-Sale Settlement and Pickup Agent
#ai-agent #gradient-boosting #large-language-models #compliance #workflow-orchestration #automation

**Concept:** An agent that runs everything after the hammer: invoices and payment reminders, card retries and deposit holds for risky bidders, second-chance offers on unpaid lots, pickup scheduling and reminders, shipping quotes, drafted replies to routine and condition questions, consignor settlement under each contract's terms, and reconciliation of platform payouts to the escrow account against the state's deadline.
**Inputs:** Sale results from the clerking system and platforms; payment processor events; bidder histories; consignor contracts; bank feeds for the trust account; the state's escrow and record-keeping rules.
**Outputs / Actions:** Sent invoices and reminders; booked pickup slots; relisted or re-offered lots; consignor statements and payments for approval; escrow reconciliation with late-deposit alerts; an audit file for the licensing board.
**Why now:** Payment, messaging and banking APIs are standard, bidding platforms now process most payments themselves, and language models can handle routine bidder correspondence with a human approving exceptions.
**Market:** Every firm running online timed auctions; priced per sale or as an add-on to clerking software. Clerking vendors (Auction Flex, Wavebid, AuctionMethod) are both competitors and channels.

---

## 4. Liquidation Value Platform for Asset-Based Lending Appraisers
#ai-platform #gradient-boosting #monte-carlo-methods #confidence-intervals #evaluation-metrics #revenue-impact

**Concept:** A platform for the appraisal and liquidation firms that value inventory and machinery for asset-based lenders. It structures every appraisal's net orderly liquidation value by asset class and recovery assumption, joins it to the firm's own liquidation outcomes when collateral is later sold, and forecasts recovery ranges for new appraisals with the comparables and recovery history behind them.
**Inputs:** The firm's historical appraisals and recovery assumptions; its own auction and liquidation results; equipment and inventory price indices; borrower inventory data supplied for each engagement.
**Outputs / Actions:** Recovery forecasts with intervals; appraisal-versus-realised scorecards by asset class and appraiser; flagged appraisals whose assumptions diverge from history; drafts of the recurring re-appraisal.
**Why now:** Asset-based lending has grown alongside private credit (estimate), and the large appraisal-liquidation firms changed hands in 2024–2025 (Oaktree into Great American Group, ORIX into Hilco), putting pressure on margins and on proving accuracy.
**Market:** A dozen or so large and mid-size appraisal and liquidation firms; a small market of firms with real budgets. Borrower data arrives under engagement confidentiality, which limits pooling across clients; the platform must run on each firm's own records.
