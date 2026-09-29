# Role-Based Risk Targeting

**Parent Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Category:** Low Digitized
**Contested on:** Whether the programme reflects what a person is actually exposed to and what they already know, or delivers the same thing to everyone.

## Profile

**Market Size:** ~$300M
**Share of Parent Industry:** ~10%
**Digital Adoption:** Very low — uniform assignment
**Target Buyer:** Awareness managers, HR, security leadership
**Automation Potential:** High — exposure is observable

## What Makes This a Distinct Niche

Everyone receives the same annual modules regardless of what they do, what they are exposed to, or what they already know.

The variation this ignores is enormous. A finance team handling payment instructions faces a specific, high-value, well-documented attack pattern. An executive assistant with calendar and mailbox access to leadership is a named target. A developer with production credentials, a warehouse worker with a shared terminal, a customer service agent handling account recovery, and a field engineer on a personal device all face entirely different exposure.

They all get the phishing module, the password module and the data handling module, at the same length, on the same schedule.

The consequence runs both ways. The high-exposure roles receive generic content that does not address the attacks aimed specifically at them. And everybody else spends an hour a year on content largely irrelevant to their work, which is the main reason the programme is regarded as a ritual.

The information to target exists. The identity system knows access. The finance system knows who approves payments. The organisation knows which roles have been targeted before. And the incident record knows where compromises actually occur.

## Current Tools & Gaps

Module assignment by group where the customer configures it, usually by department. Some vendors offer role-based content packs. Adaptive assignment based on simulation failure, which targets by outcome rather than by exposure. Executive-specific content in some libraries.

The gaps are that exposure is not modelled. Role grouping is by department rather than by what the role actually touches, so a department contains very different risk profiles. Access data from the identity system is not used, though it is the clearest available exposure signal. Real targeting data — who the organisation's actual attackers went after — is not fed back into assignment. Prior knowledge is not assessed, so an expert and a novice receive identical content. And nothing distinguishes the small number of genuinely high-exposure people who warrant substantially more attention.

## Problems

- [[niches/security-awareness-training/role-based-targeting/build|🔨 Build: Exposure-Based Assignment]]
- [[niches/security-awareness-training/role-based-targeting/buy|🛒 Buy: Adaptive Learning and Access Data]]
- [[niches/security-awareness-training/role-based-targeting/fix|🔧 Fix: The Warehouse Team Watches the Wire Fraud Module]]
