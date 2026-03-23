# Shadow IT Discovery in School Districts

**Niche:** [[niches/cybersecurity-mssp/k12-school-security/profile|K-12 School District Security]]
**Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSP]]
**Type:** Fix (Pain Point)
**One-liner:** Teachers and administrators independently sign up for 30-50 unapproved SaaS applications per school year, creating FERPA compliance gaps and unmonitored attack surfaces that the district IT team does not know exist.
**Tags:** #automation #compliance #data-integration #quick-win

## The Problem
A third-grade teacher signs up for a free educational game platform using her school email and creates student accounts with real student names and grade levels. The platform was never reviewed for FERPA compliance, has no data privacy agreement with the district, and stores student data on servers the district has no visibility into. Multiply this by 200 teachers across the district, each trying 3-5 new platforms per year, and the district has 600-1,000 unapproved applications with student data. The district IT team is aware of 50-100 approved platforms. The remaining 500+ are shadow IT — unknown, unmonitored, and uncontrolled.

## Why It's Still Broken
Teachers adopt EdTech tools to improve student engagement, and the district's formal approval process takes 2-6 months (vendor review, privacy assessment, board approval). Teachers bypass the process because waiting 4 months for approval of a free math game is impractical. The district IT team has no visibility into SaaS sign-ups because teachers use Google SSO or direct email registration, neither of which generates an IT alert. Blocking all unapproved websites would cripple educational innovation. The IT team needs discovery, not prevention — know what is being used, assess the risk, and retroactively approve or remediate.

## What a Fix Looks Like
A CASB-lite (Cloud Access Security Broker) deployment designed for K-12 that: (1) monitors DNS and web traffic to identify SaaS applications accessed from district networks and devices, (2) cross-references discovered applications against the district's approved vendor list, (3) flags unapproved applications that appear to be receiving student data (registration with student names, login patterns suggesting student accounts), (4) auto-generates vendor assessment requests for unapproved applications above a usage threshold, and (5) provides a monthly shadow IT report for the district IT director. Must be deployable via the district's existing firewall or DNS infrastructure without additional hardware.

## Who Feels the Pain
District IT directors who discover unapproved EdTech applications only when a vendor has a data breach, and MSSPs who cannot protect district networks when 30% of the attack surface is invisible.

## Impact If Fixed
Discovers 80-90% of shadow IT applications within 30 days of deployment. Reduces FERPA compliance exposure by identifying unapproved vendors processing student data. Provides MSSPs with a differentiated K-12 service offering worth $300-$800/month per district.
