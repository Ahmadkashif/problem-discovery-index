# Diagnostic Imaging

**Parent Industry:** [[industries/veterinary-practices|Veterinary Practices]]
**Category:** Highly Automatable

## Profile
**Market Size:** $2-3B embedded (touches all veterinary segments)
**Share of Parent Industry:** Embedded across all niches
**Digital Adoption:** Medium — most practices have digital radiography hardware but interpretation is either done by the GP vet with limited confidence or sent to teleradiology services with 24-72 hour turnaround
**Target Buyer:** General practice veterinarian, radiology service provider, or veterinary imaging company
**Automation Potential:** Very High — radiograph interpretation is a visual pattern recognition task with well-defined pathologies, large existing image datasets, and a clear comparison benchmark (board-certified radiologist reads)

## What Makes This a Distinct Niche
Every veterinary practice with diagnostic capability takes radiographs — it is the most common advanced diagnostic in companion animal medicine. But the vast majority of GP vets lack confidence in their radiograph interpretation. A 2019 survey found that 60% of GP vets felt "somewhat" or "not confident" in their ability to interpret thoracic radiographs. The result is a two-tier system: the vet takes the radiograph, makes a preliminary assessment, and either (a) acts on their own interpretation (risking missed findings) or (b) sends the image to a teleradiology service (VetCT, IDEXX Telemedicine, Antech Imaging) for a board-certified radiologist read. Teleradiology costs $30-80 per study and takes 24-72 hours for a routine read, creating a gap between when the vet needs an answer (during the appointment) and when the specialist provides one. For urgent cases — suspected foreign body, pneumothorax, fracture — this delay is clinically unacceptable. The opportunity is an AI screening layer that provides immediate, point-of-care abnormality detection on radiographs, bridging the gap between the vet's uncertain preliminary read and the delayed specialist interpretation.

## Current Tools & Gaps
Digital radiography hardware (IDEXX, Sound-Eklin, MinXray) is standard in practices grossing over $500K. IDEXX and Antech offer teleradiology services integrated with their imaging platforms. SignalPET has launched an AI radiograph interpretation tool for veterinary use, providing automated findings for canine and feline thoracic and abdominal radiographs. However, SignalPET's adoption remains limited — many practices are unaware of it, skeptical of AI accuracy, or resistant to adding another subscription. The gap is not the absence of AI imaging tools but rather their integration into the clinical workflow at the point of care — providing real-time screening results on the same screen where the vet views the radiograph, rather than requiring a separate upload and login.

## Problems
- [[niches/veterinary-practices/diagnostic-imaging/build|🔨 Build: Real-Time AI Radiograph Screening at Point of Care]]
- [[niches/veterinary-practices/diagnostic-imaging/buy|🛒 Buy: SignalPET Integration Layer for Legacy PACS Systems]]
- [[niches/veterinary-practices/diagnostic-imaging/fix|🔧 Fix: Teleradiology Turnaround for Urgent Cases]]
