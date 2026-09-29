# Lineage: Cybersecurity MSSPs

**Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSPs]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** Counterpane's Sentry and Socrates — a collection appliance placed inside each client's network, forwarding firewall, IDS and server logs to a central correlation system that analysts in two Secure Operations Centers worked from
**Builder:** Counterpane Internet Security
**Builder in vault:** [[industries/cybersecurity-mssp|Cybersecurity MSSP]]
**Verification:** partial — see Sources

## The Problem That Came First

By the late 1990s a company that bought a firewall and an intrusion detection system had bought two machines that talked constantly and that nobody listened to.

The devices wrote logs and raised alarms around the clock. Reading them was the expensive part. Bruce Schneier put the arithmetic plainly in 2001: staffing security expertise 24 hours a day, 365 days a year takes **five full-time employees**, more with supervisors and specialists — and even a company that could afford that team rarely had enough attacks to keep it sharp. His other complaint was the one the industry still has: "automatic programs are plagued by false positives." Separating the real attack from the noise cost a salary per shift.

So the alarm existed and the guard did not. That gap — not the sensor — is the thing a managed security provider sells.

## What Got Built

Two pieces, described by Counterpane itself.

**Sentry** was a box installed inside the client's network. It collected, sorted and forwarded audit data from the devices already there — firewalls, IDSs, routers, servers — and presented it "in a form that the analysts can efficiently understand."

**Socrates** was the central system, spread across the company's two Secure Operations Centers. It took the Sentry streams, matched each pattern of events to a diagnosis, and then weighted that diagnosis against **client-specific information about how serious each kind of event was for that client**. A fourth process, which Counterpane called Network Intelligence, fed new attacks and vulnerabilities back into both.

The design choice is the point. Sentry did not replace the client's sensors; it sat downstream of whatever they had bought. Socrates did not replace the analyst; it decided what reached one. Correlation across the whole client base — the same attack seen at ten customers — was something no single customer could do for itself.

## Who Built It, And Why Them

Counterpane Internet Security, founded by the cryptographer Bruce Schneier in August 1999.

Schneier's argument was an outsourcing argument, and it dictated the architecture. Expertise needed rarely but immediately is always bought as a service — his analogy was the doctor you see twice a year and the fire department that has "practiced on the rest of the neighbourhood." A provider watching many networks sees each attack many times, can hire and train analysts in volume, and can keep one threat-research function current for everyone.

That only works if the provider can see into every client without owning every client's equipment — hence a uniform collection appliance at the edge and one shared correlation brain in the middle. The shape of Sentry and Socrates is the shape of the business model: **many sensors, one queue, a few experts.**

Counterpane even tried to sell the guarantee. In July 2000 it arranged Lloyd's of London cover of up to $100 million, available only to clients of its monitoring service. BT Group bought it on 25 October 2006.

## What It Cost

**Context was traded for scale.** The analyst in the operations centre sees the event, not the business behind it — Schneier conceded security engineers "only see half the information." Socrates' per-client seriousness weights were the patch, and they had to be maintained by hand for every customer.

The second cost was structural: the service's value is measured in alerts reviewed, so every new sensor feeds the queue rather than shrinking it.

## What You Still Touch

Every MSSP still runs this architecture — a collector at the client edge, a central correlation engine, a shared analyst pool, per-client tuning — now called SIEM, a log forwarder and a SOC. The 95% false-positive queue is Socrates' filtering problem at modern volume, and the per-client weights are the unlabelled context an L1 analyst still pulls up by hand.

- [[problems/cybersecurity-mssp/high-impact|🔴 SOC Alert Triage & True Positive Identification]] — the queue Socrates was built to shorten
- [[problems/cybersecurity-mssp/worker-life-1|🟢 SOC Analyst Alert Fatigue & Burnout]] — the five-person rota, at scale
- [[niches/cybersecurity-mssp/alert-triage-automation/profile|Alert Triage & Escalation Automation]]
- [[niches/cybersecurity-mssp/smb-owner-operator-security/profile|SMB Owner-Operator Security]] — the buyer the outsourcing argument was written for

**Sources:** Bruce Schneier, "Managed Security Monitoring: Network Security for the 21st Century," *Computers & Security* vol. 20 no. 6, dated 26 September 2001 (schneier.com PDF) — source for the five-FTE figure, the false-positive quote, and the Sentry / Socrates / Network Intelligence descriptions; Computerworld, "Counterpane offers Internet security insurance," 12 July 2000 (Lloyd's cover, two operations centres, Sentry probes, Socrates correlation); Wikipedia, *BT Managed Security Solutions* (founded August 1999; BT acquisition 25 October 2006); Wikipedia, *Bruce Schneier*. ⚠️ **Not established:** the date Sentry and Socrates first went into production — they are described in July 2000 and 2001 sources, but I found no launch date; the company's name at incorporation (one secondary account gives "Counterpane Information Security"; contemporaneous press uses "Counterpane Internet Security," used here); and whether Counterpane was the first managed-monitoring provider rather than an early one — I did not establish priority and do not claim it.
