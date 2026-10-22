# A Counter Check-Risk Score Trained on Your Own Returns

**Niche:** [[niches/money-service-businesses/check-cashing-centres/profile|Check Cashing & Neighbourhood Financial Service Centres]]
**Industry:** [[industries/money-service-businesses|Money Service Businesses]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A senior teller can spot a bad payroll check at a glance; the chain's history of every check it cashed and every one that came back has never been used to teach anyone else.
**Tags:** #tacit-knowledge-ml #cnns #gradient-boosting #object-detection #evaluation-metrics #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to cash a stranger's payroll, government or insurance check on the spot without eating a returned item, and whoever judges check risk most accurately at the counter takes the account.

## The Problem
A teller decides in under a minute whether to cash a check: is the payor real and good for it, is the check genuine and unaltered, is the customer the payee. Experienced tellers catch counterfeit payroll checks from fonts, check stock, MICR line alignment and amounts that do not fit the employer, and new tellers do not. Returned items are written off store by store.

## Why Nobody Has Built This
Chains are small software buyers and the vendors serving them sell point-of-sale and compliance features. Return data is held in accounting, separate from the check images. Retail check guarantee services judge the payer's account, not the payroll check's authenticity.

## What to Build
A model trained on the chain's own check images and outcomes: image features of check stock, MICR and printing compared with the payor's previously cashed checks; payor history (prior checks, returns, amount ranges, pay cycle); and customer history. The teller sees a risk band and the reason ("payroll font differs from this employer's last 40 checks"), and every override is recorded as a label.

## Target Customer
Owners and operations directors of multi-store check-cashing chains.

## Impact If Built
Returned-item losses fall, new tellers decide like senior ones, and the senior tellers' read becomes a store-wide asset rather than a personal one.
