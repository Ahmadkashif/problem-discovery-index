# Card Fraud Scoring Adapted to eSIM Activation

**Niche:** [[niches/telecom-resellers/consumer-mvnos/profile|Consumer MVNOs]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Payment fraud tools judge whether a card order is stolen, but the losses at an MVNO arrive after a clean-looking activation, when a new line makes international calls or a financed phone goes missing.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #revenue-impact #data-integration #automation
**Contested on:** *Not terminal as stated.* Consumer MVNOs split into cable and converged MVNOs, which win on offloading traffic from the host network, and independent digital MVNOs, which win on keeping subscribers past acquisition payback; see the parent profile.

## The Problem
eSIM lets a subscriber join in minutes with no store visit. That suits fraud too: a new line activated with a stolen card, used for a weekend of premium-rate or international calls, then abandoned; a phone financed on a synthetic identity and shipped to a drop address; lines opened in bulk to receive verification codes. The card authorisation passes, and the loss shows up days later on the host's wholesale bill.

## What Already Exists
Card-not-present fraud platforms, covered in [[industries/payment-fraud-vendors|Payment Fraud Vendors]], score e-commerce orders on device, identity and payment signals. Identity verification vendors check documents and selfies at sign-up.

## The Customization Gap
An MVNO needs the order score extended into the first days of the line's life. That means telecom signals at activation: device identifier history, whether the number is a port-in and from where, eSIM download location versus billing address, and the plan chosen. It also means early-use signals: international or premium destinations in the first hours, data use inconsistent with the device, and many lines sharing an address or payment instrument. The decision must come with a telecom response (bar international calling, cap usage, hold device shipment), not just approve or decline.

## Target Customer
Fraud managers at digital and prepaid MVNOs that already license a payment fraud tool and want it to cover activation and early usage.

## Impact If Solved
Activation fraud is caught before the wholesale bill rather than after it. The MVNO also keeps eSIM's frictionless sign-up for the large majority of genuine subscribers instead of adding checks for everyone.
