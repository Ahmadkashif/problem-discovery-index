# Lineage: Bug Bounty Platforms

**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** Netscape's "Bugs Bounty" — a published cash-and-merchandise reward, up to about $1,000, for outsiders who reported security flaws in the Navigator 2.0 beta
**Builder:** Netscape
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A browser shipped to millions of strangers had more testers outside the company than inside it, and the outside ones were not being paid.

By the mid-1990s Netscape was releasing public betas of Navigator. The people who found its security holes first were often not Netscape engineers. They were users — many of them working programmers — who posted fixes and workarounds on technical forums and an unofficial Netscape FAQ. That was free review, but uncontrolled: a flaw posted publicly was a flaw every attacker could read before Netscape had shipped a patch.

The expensive step was not finding bugs. It was getting the finder to tell the vendor first, privately, instead of telling the internet.

## What Got Built

A standing offer with a price on it.

Netscape announced the programme for the **Navigator 2.0 beta**, dated in most accounts to **October 1995**. Outsiders who found and reported security bugs received cash — up to about **$1,000** for the most critical — alongside T-shirts and merchandise from the Netscape shop. According to its originator it grew out of an earlier non-cash scheme, the "Netscape Champions", which rewarded community bug-reporters with merchandise and parties. The public announcement framed it as quality assurance: rewarding users for quickly identifying and reporting bugs would "encourage an extensive, open review" of the browser.

Everything a modern programme contains is present in miniature: a defined target, a reporting channel to the vendor, and a payment scaled to severity.

## Who Built It, And Why Them

**Netscape**, on the proposal of **Jarrett Ridlinghafer**, a technical-support engineer who later ran its worldwide support operations. In his own account to *The Register* in 2016, he had noticed the community fixing Netscape's bugs for free; asked in the executive pitch whether outsiders would really find bugs better than Netscape's engineers, he answered, "They already are." The engineering vice-president, Rick Schell, initially objected; marketing chief Mike Homer and CEO Jim Barksdale were persuaded.

Why Netscape and not an operating-system vendor is distribution and speed. Netscape was a young company shipping public betas of internet-facing code to an enormous audience, in a market where being first mattered more than being finished. It could not hire enough testers to match its user base, and the user base was already testing. A bounty converted existing unpaid review into a private disclosure channel for the price of a T-shirt budget. An earlier precedent exists — Hunter & Ready offered a Volkswagen Beetle in 1983 to anyone finding a bug in its VRTX operating system ("Get a bug if you find a bug") — but that was a marketing stunt about reliability, not a standing security-disclosure channel.

## What It Cost

**The researcher does the work before knowing whether it will be paid.**

A bounty buys results, not effort. The vendor pays only for valid, in-scope, previously unknown findings, so the cost of every duplicate, every out-of-scope finding and every rejected severity claim falls on the finder. That is the design's efficiency and its unfairness at once, and it shaped the industry: a public programme attracts volume, most of the volume is invalid, and someone qualified must read all of it. The metric that came with the model — bugs reported, dollars paid — counts purchases, not whether the product became safer.

## What You Still Touch

Every programme page listing targets, exclusions and a reward table is Netscape's offer with a platform in the middle. The platforms that arrived later did not change the bargain; they took over triage and payment.

- [[problems/bug-bounty-platforms/worker-life-1|🟢 The Researcher Who Was Six Hours Late]] — paid-for-results, applied to a duplicate
- [[problems/bug-bounty-platforms/low-impact-1|🟡 Triage Volume and Duplicate Detection]] — the volume a public offer invites
- [[problems/bug-bounty-platforms/high-impact|🔴 Nobody Measures Whether the Programme Bought Security]] — counting purchases
- [[niches/bug-bounty-platforms/submission-deduplication/profile|Submission Deduplication & Filtering]]
- [[niches/bug-bounty-platforms/scope-specification/profile|Scope Specification]]

**Sources:** *The Register*, "Bug bounty hunters score big dollars and the boom's only just begun", 22 February 2016 (Ridlinghafer interview: Netscape Champions precursor, merchandise then cash, up to about $1,000, the pitch and "They already are", Schell, Homer, Barksdale); Wikipedia, *Bug bounty program* (Hunter & Ready 1983, VRTX, Volkswagen Beetle; Netscape 1995 for Navigator 2.0 beta); Cobalt and Intigriti blog histories (date 10 October 1995; the "extensive, open review" quote, attributed there to "Matt Horner", almost certainly a misspelling of Mike Homer); Wikipedia talk page and about.me profile for Ridlinghafer's support-engineer role (secondary, self-described). ⚠️ **Not established:** the launch date. Secondary blogs give 10 October 1995; *The Register* places cash rewards "around 1996"; a biography attributed to Ridlinghafer says he coined the phrase in "early 1996". I could not retrieve Netscape's original press release (web.archive.org was unreachable this session), so "October 1995" is unconfirmed. Whether Netscape's terms paid only the first reporter of a bug was not found; the "previously unknown" condition above describes today's industry practice, not a documented Netscape term.
