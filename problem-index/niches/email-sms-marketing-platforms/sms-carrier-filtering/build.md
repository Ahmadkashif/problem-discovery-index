# An Error Code That Means Six Things

**Niche:** [[niches/email-sms-marketing-platforms/sms-carrier-filtering/profile|SMS Carrier Filtering]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Carriers filter on undisclosed criteria and return a code that means blocked, or unreachable, or rate-limited, or something else, and the brand cannot tell which.
**Tags:** #gradient-boosting #evaluation-metrics #confidence-intervals #compliance #change-point-detection #hypothesis-testing #descriptive-statistics #automation
**Contested on:** Every serious competitor in this niche is fighting to decode why carriers filter what they filter and navigate the registration regime that gates every brand — and whoever does that turns an opaque gatekeeper relationship into something a brand can manage.

## The Problem
A campaign goes out and a portion of messages come back with an error code. That code, depending on the carrier and the aggregator path, may mean the handset is unreachable, the number is invalid, the content was filtered, the sender was rate-limited, the campaign registration is insufficient, or something unstated. The brand treats them all as failures of the same kind, retries or does not, and learns nothing. Filtering is the single largest determinant of whether a text programme works and the only feedback about it is a code that conflates the causes.

## Why Nobody Has Built This
Carriers do not publish their criteria and have a legitimate reason not to, since disclosure helps the abusers the filtering exists to stop — the opacity is deliberate and defensible, which is why decoding rather than disclosure is the route. Codes are passed through several layers that each lose information. Expertise lives in a small practitioner community and in aggregator relationships. And the consequence lands on the brand rather than on the platform.

## What to Build
Decode the responses and model the filtering. Build a mapping from code, carrier, aggregator path and context to a probable cause, learned from outcomes across thousands of senders, which is the core and is possible only with a corpus — one brand's codes are uninterpretable and a million brands' codes are a dataset. Distinguish transient from persistent failures, since retrying a filtered message and retrying an unreachable handset are opposite decisions and they currently look identical. Model what content and sending patterns trigger filtering, from observed outcomes rather than from published rules, which is where the practical guidance comes from. Detect carrier behaviour changes across the corpus, which arrive without notice and affect many senders at once. Attribute filtering to registration and classification problems specifically, since a substantial share is a paperwork failure rather than a content one and the remedies are entirely different. Manage throughput allocation actively, because it is a real constraint that most brands do not know they are hitting. Give the brand a diagnosis and a specific remedy rather than a failure count. Maintain the carrier and aggregator relationships as a platform function, since individual brands have no standing and this is a genuine service. Report a filtering rate by carrier as a standing metric, which most brands cannot currently compute. And measure recovery after remediation, since that closes the loop and builds the mapping.

## Target Customer
Messaging platforms and aggregators, brands running text programmes at scale, and the deliverability teams treating carrier failures as noise.

## Impact If Built
The opacity is deliberate and defensible, so decoding rather than disclosure is the route, and one brand's codes are uninterpretable while a million brands' codes are a dataset. Separating registration failures from content filtering matters because the remedies are entirely different.
