# Cyber Insurance Compliance Evidence Gap

**Niche:** [[niches/cybersecurity-mssp/smb-owner-operator-security/profile|SMB Owner-Operator Security]]
**Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSP]]
**Type:** Fix (Pain Point)
**One-liner:** SMBs purchase cyber insurance but cannot prove they met the policy's security requirements (MFA, endpoint protection, backup testing) when filing a claim — and insurers deny claims for non-compliance at increasing rates.
**Tags:** #compliance #automation #data-integration #quick-win

## The Problem
Cyber insurance carriers have tightened underwriting requirements: policies now mandate MFA on all remote access, endpoint detection on all devices, backup testing frequency, security awareness training, and email filtering. SMB owner-operators check "yes" on the application because their MSP told them "we handle that." When a ransomware incident occurs and the SMB files a $200K claim, the insurer investigates: was MFA actually enabled on all accounts? Were backups actually tested? Was endpoint protection on every device? If the SMB cannot produce evidence of compliance at the time of the incident, the claim is denied. Claim denials for security control non-compliance have increased 300% since 2023.

## Why It's Still Broken
SMBs delegate security controls to their MSP but have no documentation proving the controls are in place. The MSP enables MFA for remote access but does not document it in a format the insurance adjuster can review. Backups are configured but never formally tested — the MSP's monitoring dashboard shows "backup successful" but this is not evidence of recovery testing. Security awareness training was completed once during onboarding but not annually as the policy requires. The SMB has no "compliance posture dashboard" showing continuous evidence of meeting insurance requirements.

## What a Fix Looks Like
A cyber insurance compliance evidence generator that: (1) maps the SMB's insurance policy security requirements to specific technical controls, (2) continuously monitors control status (is MFA enabled on all accounts? Is EDR agent running on all endpoints? When was the last backup test?), (3) generates a monthly compliance posture report matching policy requirements to evidence, (4) alerts when a control falls out of compliance (employee disabled MFA, new endpoint without EDR), and (5) produces a pre-packaged evidence bundle for insurance claims (timestamped proof of control status at incident time). Integrates with common MSP tools (Datto, ConnectWise, Kaseya) to gather evidence automatically.

## Who Feels the Pain
SMB owners who face claim denial after a cyber incident because they cannot prove policy compliance, and MSPs who face liability claims from clients whose insurance was denied due to controls the MSP was supposed to manage.

## Impact If Fixed
Prevents cyber insurance claim denials — average denied claim costs the SMB $200K-$500K in unrecovered losses. Reduces MSP liability exposure for security control gaps. Generates $100-$300/month per client for the MSSP/MSP providing the compliance evidence service.
