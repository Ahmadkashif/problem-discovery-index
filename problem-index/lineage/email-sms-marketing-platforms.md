# Lineage: Email & SMS Marketing Platforms

**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** the open-tracking pixel — a 1×1 image in an HTML email whose URL carries the recipient's identity, so that fetching the image is logged as an "open"
**Builder:** unknown — searched, not established
**Builder in vault:** n/a
**Verification:** partial — see Sources

## The Problem That Came First

A bulk sender could see that a message had left. It could not see what happened next.

SMTP answers one question: did the receiving server accept the message? Acceptance says nothing about whether it reached an inbox or was read, and the read receipts in the mail standards were optional for the recipient's software.

For a list-based marketer this was a cost problem. Without a signal of attention there was no way to tell a reader from an abandoned mailbox, to compare subject lines, or to show the paying client a number.

## What Got Built

Once mail clients rendered HTML, a message could contain an image hosted on the sender's server. The sender gave every recipient a different image URL — a one-pixel transparent graphic with the recipient's address or an ID in the query string. When the client displayed the message it fetched the image, and the sender's server logged the request.

**That log line became the open.** Divide the logged recipients by the number delivered and you have the open rate — the number email marketing has organised around ever since.

By November 1999 the practice was established enough to be documented from the outside. Richard M. Smith's *Web Bug FAQ*, version 1.0, dated 11 November 1999, defines a web bug as a graphic "designed to monitor who is reading the Web page or Email message" and lists what it was used for in email: to learn whether and when a message was read, to measure how many people viewed a campaign, and — the use that became the industry's list hygiene — to find people who do not view junk messages so they can be "removed from the list." That last line is the sunset policy, fully formed.

## Who Built It, And Why Them

**The builder is not established.** I found no first sender, first email service provider or patent that credibly claims the invention; secondary histories attach no name or date.

What can be said is *who needed it*, and that explains the shape. A November 1999 *Forbes* piece describes a competitive field of outsourced email-marketing firms — MessageMedia already public, Exactis.com and Digital Impact heading the same way. Firms that sold mailing as a service had to report results to clients, and an open count was the only per-recipient signal a mail pipeline could collect without any cooperation from the receiving side. It required nothing from the mailbox provider or the reader. That is why it won: it was the one measurement a sender could build alone.

## What It Cost

The pixel does not measure reading. It measures an image fetch, and it borrowed the meaning of reading for as long as image fetches happened only when a person looked.

That assumption was broken by the receiving side, twice. In December 2013 Gmail began routing images through its own proxy servers, which hid recipients' IP addresses and devices and cached the image so repeat opens stopped registering. Then Apple announced Mail Privacy Protection at WWDC on 7 June 2021 and shipped it with iOS 15 on 20 September 2021: Apple Mail downloads remote content in the background whether or not the user opens the message. Every such message now registers as opened. Industry measurements reported total open rates rising from about 23% to about 41% within six months.

The deeper cost: because senders built the measurement alone, they never secured a delivery signal from those who hold one — mailbox providers and, for SMS, carriers.

## What You Still Touch

Every "opened" figure on a campaign dashboard is still a count of pixel fetches, inflated by however many recipients use Apple Mail — and segments, send-time models and sunset rules still read it.

- [[problems/email-sms-marketing-platforms/high-impact|🔴 Nobody Tells You Whether the Message Arrived]] — the question the pixel stood in for, never answered
- [[problems/email-sms-marketing-platforms/low-impact-1|🟡 Send Timing and Frequency Optimisation]] — tuned against opens
- [[problems/email-sms-marketing-platforms/worker-life-2|🟢 The Deliverability Specialist Arguing With a Postmaster]]
- [[niches/email-sms-marketing-platforms/engagement-signal-reconstruction/profile|Engagement Signal Reconstruction]]
- [[niches/email-sms-marketing-platforms/list-health-and-reactivation/profile|List Health & Reactivation]] — the 1999 "remove the non-viewers" rule
- [[niches/email-sms-marketing-platforms/email-inbox-placement/profile|Email Inbox Placement]]

**Sources:** Richard M. Smith, *The Web Bug FAQ*, version 1.0, 11 November 1999 (EFF archive; definition and list of email uses quoted); Wikipedia, *Spy pixel*; Len Shneyder, "Email's humble beginnings and the birth of tracking pixels," MarTech/Marketing Land, 4 December 2018 (HTML email enabled the 1×1 pixel; names no inventor); *Forbes*, "The check is in the E-mail," November 1999 (MessageMedia, Exactis.com, Digital Impact as competing email-marketing firms — seen via search summary only); Litmus, "Gmail adds image caching" and related coverage (image proxy rolled out from 12 December 2013); Litmus, Mailmodo and AWS Messaging Blog on Mail Privacy Protection (announced 7 June 2021, shipped 20 September 2021); Omeda, "The Impact of Apple's Mail Privacy Protection – 6 Months Later" (open-rate rise 22.6% → 40.5%; one vendor's customer base, not an industry census). ⚠️ **Not established:** who first put a tracking pixel in a marketing email, or when. Searched Wikipedia, trade histories and ESP-era press for a first user, a first ESP report of "opens", or an originating patent; found none that credibly claims it. A later USPTO patent (7,680,892) on monitoring email recipient behaviour surfaced in search and is not evidence of origin. The Forbes article was not read in full.
