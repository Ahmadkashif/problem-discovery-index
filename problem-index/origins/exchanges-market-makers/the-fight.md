# The Fight: From Odd-Eighth Collusion to the Latency Arms Race

**Origin:** [[origins/exchanges-market-makers/profile|Exchanges & Market Makers]]
**Outcome:** Dealer spreads collapsed under regulatory and technological pressure; the fight then moved from "who sets the spread" to "who sees the price first."

## Round One: Dealers Against Their Own Customers

For most of NASDAQ's first two decades as a quotation system, market makers quoted prices almost exclusively in even eighths of a dollar — avoiding odd-eighth quotes such as $20 1/8 or $20 3/8. In **1994**, economists William Christie and Paul Schultz published research showing this pattern was too consistent across dealers in active stocks to be coincidental, and could not reject the hypothesis of **implicit collusion to maintain a minimum quoted spread of $0.25** rather than the $0.125 a genuinely competitive market in eighths would allow.

The paper broke in national newspapers on **26–27 May 1994**. The market's own reaction was the most damning evidence of all: **the day after the story ran, dealers in stocks including Amgen, Cisco and Microsoft sharply increased their use of odd-eighth quotes, and measured spreads fell by close to half — overnight, with no new technology and no new rule.** The spreads had been a choice, not a technical constraint.

The fallout was substantial. A Department of Justice antitrust investigation produced a 1996 settlement requiring changes to trading practices and, for many of the firms involved, the taping of trader phone calls. Separate private antitrust litigation produced a **$1.03 billion class-action settlement, approved in November 1998, covering 37 brokerage firms** — at the time the largest civil antitrust settlement in US history.

## Round Two: Regulation Forces the Machines Open

The SEC followed with the **Order Handling Rules of 1997**, which required market makers to either display customer limit orders priced better than their own quote, or display any better-priced quote they had placed on an ECN in the public NASDAQ montage. Before this rule, **Instinet had been the only ECN that mattered**; the rule created the regulatory opening for new ones to compete on equal visibility.

**Island ECN**, founded 1996 by Datek's Jeff Citron and Joshua Levine, began trading in 1997, extended to Nasdaq-wide quotes by August 1997, was spun off from Datek in December 2000, and was acquired by Instinet on **20 September 2002** — the original ECN absorbing the upstart that had helped force the old dealer system open. Spreads continued to compress, and the industry moved from fractional to **decimal pricing in 2001**, a change that on its own mechanically narrowed the minimum possible spread from 12.5 cents to one cent.

## Round Three: Reg NMS and the Fight Nobody Expected

**Regulation NMS**, adopted by the SEC on **9 June 2005** and effective **29 August 2005**, was built to protect investors from "trade-throughs" — a trade executing at a worse price than a better price displayed elsewhere. Its core provision, **Rule 611**, reached full compliance on **5 February 2007** after a phased rollout.

> ### The myth to kill
> **Reg NMS Rule 611 is routinely blamed for causing the rise of high-frequency trading and market fragmentation that followed it. That is an overstatement of what the rule does.** Rule 611 bars a trading venue from executing at a price *worse* than a protected quote displayed elsewhere. **It does not require anyone to route an order to whichever venue has the best price** — it only forbids trading through a better one you can see. The rule created an incentive to be able to *see and react to* every protected quote fast enough to avoid a trade-through violation, and it is that incentive — not a routing mandate — that made speed of information newly, directly valuable across every linked venue simultaneously.

That incentive, layered onto a market now legally required to watch prices across many linked venues at once, is what turned "get the fastest link between two exchanges" into a business in its own right. That business is the subject of [[origins/exchanges-market-makers/the-mechanism|the mechanism]].

## The Honest Caveat

**This is not one continuous fight with one winner.** Round one was retail and institutional investors against a dealer cartel, and investors won, decisively, with damages paid. Round two was incumbent NASDAQ dealers against ECN entrants, and the entrants won, then were partly reabsorbed by the ECN that started it all. Round three is investors, HFT firms and exchanges in a contest over microsecond advantage that, unlike the first two, does not have a clean ending — it is still running, and [[origins/exchanges-market-makers/legacy|its legacy]] is being written into crypto exchanges today.

**Sources:** Christie & Schultz (1994), *Why Do NASDAQ Market Makers Avoid Odd-Eighth Quotes?*, Journal of Finance; CBS News, *$1B Nasdaq Settlement OK'd* (Nov 1998); FINRA Notice 97-49, compliance with SEC Order Handling Rules; Wikipedia, *Electronic communication network* (Island ECN, Instinet acquisition, 20 Sept 2002); SEC, *Regulation NMS* final rule (adopted 9 June 2005) and Rule 611 compliance-date releases (Trading Phase, 5 Feb 2007).