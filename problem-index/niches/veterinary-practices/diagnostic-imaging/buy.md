# SignalPET Integration Layer for Legacy PACS Systems

**Niche:** [[niches/veterinary-practices/diagnostic-imaging/profile|Diagnostic Imaging]]
**Industry:** [[industries/veterinary-practices|Veterinary Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** SignalPET's AI radiograph analysis exists but requires a separate upload workflow — most practices won't adopt it until findings appear automatically on their existing imaging workstation without changing their diagnostic routine.
**Tags:** #data-integration #workflow-orchestration #automation #quick-win

## The Problem
SignalPET offers AI-powered veterinary radiograph analysis that detects common abnormalities in canine and feline thoracic and abdominal views. The technology works — peer-reviewed studies show sensitivity comparable to general practitioners and improving toward specialist-level for common findings. But adoption remains limited because SignalPET operates as a standalone platform: the vet takes a radiograph on their existing system (IDEXX, Sound-Eklin, Fuji), then must separately upload the image to SignalPET's platform (or configure DICOM routing), wait for analysis, and view findings in a separate browser window. This 3-5 minute workflow addition doesn't sound like much, but in a busy practice taking 8-15 studies per day, it is enough friction to prevent adoption. Vets want findings to appear on the same screen where they view the radiograph, as automatically as the image itself appears after exposure.

## What Already Exists
SignalPET's analysis engine processes canine and feline radiographs and returns structured findings with confidence scores and annotated images. Their platform supports DICOM integration for automated image routing from compatible systems. IDEXX, Sound-Eklin, and other imaging hardware vendors have PACS (Picture Archiving and Communication Systems) that display and store radiographic images — some cloud-based, some local-server-based, some proprietary.

## The Customization Gap
The gap is a DICOM middleware layer that automatically routes images from any veterinary PACS to SignalPET (or a comparable AI analysis engine) and returns findings to the same PACS for inline display alongside the original image — all without the vet doing anything beyond their normal radiograph capture workflow. This middleware needs to: (1) support DICOM routing from the 5-6 most common veterinary PACS platforms (IDEXX ImageVault, Sound-Eklin, Asteris Keystone, Antech/VetConnect PLUS, eFilm), (2) handle the round-trip: send image to AI, receive findings, and inject annotated overlay back into the PACS viewer within 30-60 seconds, (3) manage authentication and subscription validation per-practice, and (4) provide a fallback display (browser-based findings page) for PACS systems that don't support overlay injection. Sold as a per-study fee ($3-5) or monthly subscription ($149-249/month) bundled with the AI analysis cost.

## Target Customer
Veterinary practices that have evaluated SignalPET or similar AI imaging tools but rejected them due to workflow friction, and practices with legacy PACS systems that are not natively compatible with AI analysis platforms.

## Impact If Solved
Removes the primary adoption barrier for AI radiograph screening in veterinary practice — workflow friction. Practices that adopt inline AI screening report 15-25% increases in radiographic study ordering (vets order more X-rays when they're confident in interpretation) and 30-40% reduction in teleradiology submissions for routine studies. For SignalPET or a comparable AI vendor, this integration layer could double their addressable market by making the product accessible to practices on legacy imaging infrastructure.
