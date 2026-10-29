# One Evidence File per Delinquent Unit

**Niche:** [[niches/self-storage-operators/lien-enforcement-sales/profile|Lien Enforcement & Delinquent-Unit Sales]]
**Industry:** [[industries/self-storage-operators|Self-Storage Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When a lien sale is challenged, the operator has to rebuild the proof from mail receipts, emails, newspaper invoices and auction screenshots spread across five systems.
**Tags:** #large-language-models #workflow-orchestration #compliance #data-integration #evaluation-metrics #automation
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to turn a delinquent unit back into money without a wrongful-sale claim. But the money comes from two places with different competitors: tenants who pay before the sale, where outreach and payment tools compete on past-due rent recovered per delinquent unit, and contents sold at the sale, where auction marketplaces compete on the share of the balance owed that each auctioned unit recovers. Decomposed into contested sub-niches below.

## The Problem
A wrongful-sale claim asks simple questions. Was the tenant notified on time, by an allowed method, at the addresses in the lease? Was the sale advertised as the statute requires? Were the excess proceeds held? Answering them takes hours, because the facts sit in the facility software, a certified-mail vendor, an email platform, a newspaper's invoice and the auction site.

## Why Nobody Has Built This
Facility software tracks status, not evidence. Auction marketplaces see only the sale. Notice vendors see only the mail. No one owns the whole chain, and until recently the email and online-sale rules were too new for a standard.

## What to Build
An evidence ledger keyed to each delinquent unit. It applies the facility's state rules to compute every step's deadline, and collects proof as each step happens: delivery receipts, email-open evidence where the state allows it, ad tear sheets or online listing captures, sale results and surplus handling. A language model reads the signed lease to confirm email consent and the alternate contact. The file shows green or red before each step. A red file cannot proceed to sale, and the complete file exports in one click for a dispute.

## Target Customer
Directors of collections at multi-state operators and third-party managers; legal teams defending wrongful-sale claims.

## Impact If Built
Assembling a defence file falls from ~3–5 hours to minutes (estimate). Blocking sales with a broken chain prevents the claims that cost far more than the lien recovered. New York City's settlement with one operator came to $1.7M.
