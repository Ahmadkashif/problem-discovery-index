# Purchase Limits Counted per Account

**Niche:** [[niches/ticketing-agencies/onsale-bot-enforcement/profile|Onsale Bot & Purchase-Limit Enforcement]]
**Industry:** [[industries/ticketing-agencies|Ticketing & Reservation Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** A four-ticket limit is enforced per account, so a broker with a thousand accounts has a four-thousand-ticket limit.
**Tags:** #dbscan #logistic-regression #evaluation-metrics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to stop one buyer from holding many accounts at an onsale without blocking real fans, and whoever catches the most limit-breaking account clusters at a false-block rate the artist will tolerate takes the account.

## The Problem
Onsale limits are checked against the account, and sometimes the card, at checkout. Accounts are cheap to create, cards can be issued virtually, and the limit binds only the fan with one account.

## Why It's Still Broken
Linking accounts to people is hard and error-prone, and a wrongly cancelled order is a public complaint. Checking only the account is easy to defend, even though it does not work.

## What a Fix Looks Like
Count the limit against a resolved buyer identity (account, payment tokens, device, address and delivery destination), cap at checkout on high-confidence links, and review medium-confidence clusters before tickets are delivered.

## Who Feels the Pain
Fans shut out of onsales, artists blamed for resale prices, and ticketers facing BOTS Act scrutiny.

## Impact If Fixed
The advertised limit becomes a real limit, and the cost of running an account farm rises sharply.
