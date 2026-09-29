# One Request, Six Disconnected Traces

**Niche:** [[niches/headless-commerce-vendors/cross-vendor-observability/profile|Cross-Vendor Observability]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Distributed tracing propagates context across service boundaries and stops at every vendor boundary, which is where all the interesting boundaries in this architecture are.
**Tags:** #graph-theory #data-integration #evaluation-metrics #automation #workflow-orchestration #confidence-intervals #descriptive-statistics #compliance
**Contested on:** Every serious competitor in this niche is fighting to make one trace span six companies' systems — and whoever does that solves the category's acknowledged weak point, because the standard exists and stops at every vendor boundary.

## The Problem
A product page takes four seconds. The retailer's trace shows their own rendering at eighty milliseconds and three outbound calls totalling three and a half seconds. Which of those three calls was slow, why, and whether the slowness was in the vendor's processing, in a downstream dependency of theirs, or in the network, is unavailable. Each vendor has a trace of their own portion and none of them is connected to the others or to the retailer's. The customer experienced one request; the systems observing it hold six fragments; and the standard for joining them is implemented by everybody inside their own boundary and by nobody across one.

## Why Nobody Has Built This
Propagating trace context across a commercial boundary requires both parties to agree, and neither has an obligation. Vendors regard their internal traces as internal and returning timing detail as exposing their architecture. There is no commerce-specific convention for what a span should contain. And the retailer, who needs it most, has the least leverage with the vendors individually.

## What to Build
Propagate what you can and demand the rest. Instrument the retailer's side of every vendor call with full timing, error and retry detail, which is entirely within their control and immediately turns three opaque calls into three measured boundaries — this is available today and is most of the diagnostic value. Propagate trace context outbound to every vendor whether or not they use it, since it costs nothing and works the moment they do. Require vendors to accept and return trace context as a procurement term, which is a small technical ask and a straightforward contractual one, and is the coordination step the category has not taken. Ask vendors to return their own processing time in a response header at minimum, which distinguishes network from processing and is the single most useful thing a vendor can provide without exposing anything. Define a commerce span convention — cart operation, price calculation, inventory check, tax call — so that traces from different vendors are comparable, which is a convention exercise that would benefit everybody and that a standards body or a leading vendor could start. Correlate customer sessions to traces, which the fix note develops. Build the composed view as a product independent of any vendor, since the independent position is the one that can span them. And report per-boundary latency contribution to the customer journey, because that is the number that assigns responsibility.

## Target Customer
Retail platform engineering, the vendors in the composition, observability vendors, and the standards communities that could define the convention.

## Impact If Built
The standard is implemented by everybody inside their own boundary and by nobody across one, which is where every interesting boundary is. Retailer-side instrumentation of each vendor call is available today and delivers most of the diagnostic value without anybody's agreement.
