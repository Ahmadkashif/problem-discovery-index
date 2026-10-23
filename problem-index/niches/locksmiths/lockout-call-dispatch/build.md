# A Binding Quote in the First Minute of the Call

**Niche:** [[niches/locksmiths/lockout-call-dispatch/profile|Lockout Call Capture, Upfront Quoting & Dispatch]]
**Industry:** [[industries/locksmiths|Locksmiths]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The honest locksmith loses lockout calls to networks quoting a fake low price because it can't quote a real one fast enough with confidence.
**Tags:** #large-language-models #gradient-boosting #feature-engineering #evaluation-metrics #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to answer the emergency lockout call first with a binding price and a verified, licensed technician, and whoever completes the most calls at the quoted price takes the account.

## The Problem
A caller locked out of a 2019 sedan in a supermarket car park asks "how much?" The honest answer depends on the lock, the vehicle, the time of night and the distance. Owners give a wide range or "depends", and the caller hangs up and tries the number that said $29. The firm that could have done the job fairly loses it to the one that won't.

## Why Nobody Has Built This
Lockout firms are small and their job data sits in disconnected call logs and invoices. Quoting has been treated as the owner's personal skill. Nobody has joined call content to billed outcomes to show that a binding price can be calculated.

## What to Build
A quoting engine inside the call flow. Speech is transcribed and the job details extracted (vehicle or property, lock type, location, time). A model trained on the firm's own completed jobs predicts minutes and the likely method. The engine produces a binding price band and an arrival time, which the caller accepts by text before dispatch. Jobs that exceed the band are reviewed, and the band tightens as data accumulates. Optional pooling across firms through a platform speeds learning for small shops.

## Target Customer
Multi-truck lockout and residential locksmith firms competing on search and ads; [[industries/answering-services|answering services]] and platforms serving them.

## Impact If Built
More calls convert, fewer price disputes and chargebacks occur, and the firm has a documented record of honouring quotes. That record is the opposite of the scam pattern the trade is known for.
