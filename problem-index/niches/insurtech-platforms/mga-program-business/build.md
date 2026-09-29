# A Continuous Programme Performance Signal

**Niche:** [[niches/insurtech-platforms/mga-program-business/profile|MGA & Programme Business]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An MGA's programme lives or dies on its loss ratio and the MGA sees that number quarterly, reconstructed by hand from a carrier's bordereau, by which point three months of writing has already happened.
**Tags:** #survival-analysis #time-series-forecasting #bayesian-inference #change-point-detection #confidence-intervals #evaluation-metrics #revenue-impact #data-integration
**Contested on:** Every serious competitor serving MGAs is fighting to give a programme a reliable loss ratio signal early enough to correct it — and whoever shortens the time from inception to a trustworthy performance picture takes the programme.

## The Problem
A programme writes for nine months. The loss experience is reported to the MGA quarterly, in arrears, in a file that has to be matched against its own policy records before it means anything. In month ten it becomes apparent that a particular segment of the book — one distribution channel, one class, one geography — is developing badly and has been since month three. Seven months of writing at the wrong price or the wrong appetite is frequently enough to end a programme. The signals that would have shown it earlier exist: claim frequency by cohort, first-notice patterns, the segments where claims are arriving faster than expected, all of which are visible well before a loss ratio stabilises.

## Why Nobody Has Built This
The data is split across parties by the structure of the arrangement, and joining it requires the carrier or the administrator to provide claims data at a granularity and cadence they have not historically provided. Neither side has pushed hard, because the MGA is the junior party in the relationship and the carrier's own reporting cycle is quarterly. On the analytical side, an early loss ratio is genuinely unreliable — the credibility problem is real, and a programme manager reacting to two months of noise makes things worse — which has been used as a reason to wait rather than as a reason to model the uncertainty properly.

## What to Build
A continuous performance view built on frequency and development rather than on a raw loss ratio. Claim counts by exposure cohort arrive faster and are more credible early than paid amounts, and frequency deterioration is the leading indicator that matters. Development modelling estimates ultimate from what is known with an explicit credibility weighting, so the signal is presented with the uncertainty it actually has rather than as a number to react to. Segment-level monitoring is the point: a programme is rarely uniformly bad, and the segments that are deteriorating — a channel, a class, a state, a producer — are detectable long before the aggregate moves. Alerts are calibrated to avoid the noise problem, with explicit statements of how much credibility the current data carries. The same view serves the carrier and reinsurer, which is what makes it obtainable: the data-sharing arrangement is easier to negotiate when all three parties get the instrument.

## Target Customer
MGAs and programme administrators, the carriers and reinsurers providing capacity, and the MGA platform vendors competing on speed to market who could compete on performance visibility.

## Impact If Built
Programmes fail because deterioration is recognised late, and the cost of late recognition is borne by everyone in the arrangement — the MGA loses the programme, the carrier takes the losses, the distribution loses a market. Segment-level frequency monitoring turns a quarterly reconstruction into a continuous instrument and buys the months in which a correction is still possible.
