export interface Industry {
  id: string;
  name: string;
  category: string;
}

export const INDUSTRIES: Industry[] = [
  // HEALTHCARE & CLINICAL (8)
  { id: "behavioral-health-clinics", name: "Behavioral Health Clinics", category: "Healthcare & Clinical" },
  { id: "home-health-agencies", name: "Home Health Agencies", category: "Healthcare & Clinical" },
  { id: "dental-practices", name: "Dental Practices", category: "Healthcare & Clinical" },
  { id: "physical-therapy", name: "Physical Therapy", category: "Healthcare & Clinical" },
  { id: "medical-billing", name: "Medical Billing", category: "Healthcare & Clinical" },
  { id: "urgent-care", name: "Urgent Care", category: "Healthcare & Clinical" },
  { id: "veterinary-practices", name: "Veterinary Practices", category: "Healthcare & Clinical" },
  { id: "pharmacy-independents", name: "Independent Pharmacies", category: "Healthcare & Clinical" },

  // LEGAL (5)
  { id: "immigration-law", name: "Immigration Law Firms", category: "Legal" },
  { id: "personal-injury-law", name: "Personal Injury Law", category: "Legal" },
  { id: "estate-planning", name: "Estate Planning", category: "Legal" },
  { id: "small-law-firms", name: "Small Law Firms", category: "Legal" },
  { id: "compliance-consulting", name: "Compliance Consulting", category: "Legal" },

  // CONSTRUCTION & TRADES (10)
  { id: "general-contractors", name: "General Contractors", category: "Construction & Trades" },
  { id: "electrical-contractors", name: "Electrical Contractors", category: "Construction & Trades" },
  { id: "plumbing-contractors", name: "Plumbing Contractors", category: "Construction & Trades" },
  { id: "roofing-contractors", name: "Roofing Contractors", category: "Construction & Trades" },
  { id: "hvac-contractors", name: "HVAC Contractors", category: "Construction & Trades" },
  { id: "landscaping", name: "Landscaping", category: "Construction & Trades" },
  { id: "painting-contractors", name: "Painting Contractors", category: "Construction & Trades" },
  { id: "home-inspection", name: "Home Inspection", category: "Construction & Trades" },
  { id: "solar-installers", name: "Solar Installers", category: "Construction & Trades" },
  { id: "utility-contractors", name: "Utility Contractors", category: "Construction & Trades" },

  // REAL ESTATE (5)
  { id: "property-management", name: "Property Management", category: "Real Estate" },
  { id: "commercial-real-estate", name: "Commercial Real Estate", category: "Real Estate" },
  { id: "short-term-rentals", name: "Short-Term Rentals", category: "Real Estate" },
  { id: "real-estate-appraisers", name: "Real Estate Appraisers", category: "Real Estate" },
  { id: "hoa-management", name: "HOA Management", category: "Real Estate" },

  // LOGISTICS & SUPPLY CHAIN (5)
  { id: "freight-brokerage", name: "Freight Brokerage", category: "Logistics & Supply Chain" },
  { id: "last-mile-delivery", name: "Last-Mile Delivery", category: "Logistics & Supply Chain" },
  { id: "warehouse-3pl", name: "Warehouse / 3PL", category: "Logistics & Supply Chain" },
  { id: "customs-brokers", name: "Customs Brokers", category: "Logistics & Supply Chain" },
  { id: "cold-chain-logistics", name: "Cold Chain Logistics", category: "Logistics & Supply Chain" },

  // MANUFACTURING & INDUSTRIAL (6)
  { id: "contract-manufacturing", name: "Contract Manufacturing", category: "Manufacturing & Industrial" },
  { id: "metal-fabrication", name: "Metal Fabrication", category: "Manufacturing & Industrial" },
  { id: "food-manufacturing", name: "Food Manufacturing", category: "Manufacturing & Industrial" },
  { id: "medical-device-mfg", name: "Medical Device Manufacturing", category: "Manufacturing & Industrial" },
  { id: "electronics-contract-mfg", name: "Electronics Contract Manufacturing", category: "Manufacturing & Industrial" },
  { id: "printing-shops", name: "Printing Shops", category: "Manufacturing & Industrial" },

  // AGRICULTURE & FOOD (5)
  { id: "crop-farming", name: "Crop Farming", category: "Agriculture & Food" },
  { id: "livestock-operations", name: "Livestock Operations", category: "Agriculture & Food" },
  { id: "greenhouse-horticulture", name: "Greenhouse Horticulture", category: "Agriculture & Food" },
  { id: "food-distributors", name: "Food Distributors", category: "Agriculture & Food" },
  { id: "restaurant-suppliers", name: "Restaurant Suppliers", category: "Agriculture & Food" },

  // PROFESSIONAL SERVICES (7)
  { id: "accounting-firms-smb", name: "SMB Accounting Firms", category: "Professional Services" },
  { id: "staffing-agencies", name: "Staffing Agencies", category: "Professional Services" },
  { id: "it-managed-services", name: "IT Managed Services", category: "Professional Services" },
  { id: "marketing-agencies-smb", name: "SMB Marketing Agencies", category: "Professional Services" },
  { id: "engineering-consultants", name: "Engineering Consultants", category: "Professional Services" },
  { id: "environmental-consultants", name: "Environmental Consultants", category: "Professional Services" },
  { id: "hr-consultants", name: "HR Consultants", category: "Professional Services" },

  // RETAIL & E-COMMERCE (5)
  { id: "independent-retailers", name: "Independent Retailers", category: "Retail & E-Commerce" },
  { id: "ecommerce-sellers", name: "E-Commerce Sellers", category: "Retail & E-Commerce" },
  { id: "auto-dealers-independent", name: "Independent Auto Dealers", category: "Retail & E-Commerce" },
  { id: "specialty-food-retail", name: "Specialty Food Retail", category: "Retail & E-Commerce" },
  { id: "medical-supply-retail", name: "Medical Supply Retail", category: "Retail & E-Commerce" },

  // FINANCIAL SERVICES (6)
  { id: "independent-insurance-agents", name: "Independent Insurance Agents", category: "Financial Services" },
  { id: "mortgage-brokers", name: "Mortgage Brokers", category: "Financial Services" },
  { id: "wealth-management-rias", name: "Wealth Management RIAs", category: "Financial Services" },
  { id: "credit-unions", name: "Credit Unions", category: "Financial Services" },
  { id: "tax-prep-firms", name: "Tax Prep Firms", category: "Financial Services" },
  { id: "collections-agencies", name: "Collections Agencies", category: "Financial Services" },

  // EDUCATION (6)
  { id: "k12-private-schools", name: "K-12 Private Schools", category: "Education" },
  { id: "tutoring-centers", name: "Tutoring Centers", category: "Education" },
  { id: "vocational-schools", name: "Vocational Schools", category: "Education" },
  { id: "corporate-training", name: "Corporate Training", category: "Education" },
  { id: "language-schools", name: "Language Schools", category: "Education" },
  { id: "childcare-centers", name: "Childcare Centers", category: "Education" },

  // HOSPITALITY & FOOD SERVICE (5)
  { id: "independent-restaurants", name: "Independent Restaurants", category: "Hospitality & Food Service" },
  { id: "catering-companies", name: "Catering Companies", category: "Hospitality & Food Service" },
  { id: "hotels-boutique", name: "Boutique Hotels", category: "Hospitality & Food Service" },
  { id: "food-trucks", name: "Food Trucks", category: "Hospitality & Food Service" },
  { id: "coffee-shops-independent", name: "Independent Coffee Shops", category: "Hospitality & Food Service" },

  // TRANSPORTATION (5)
  { id: "owner-operator-trucking", name: "Owner-Operator Trucking", category: "Transportation" },
  { id: "towing-companies", name: "Towing Companies", category: "Transportation" },
  { id: "moving-companies", name: "Moving Companies", category: "Transportation" },
  { id: "charter-bus-operators", name: "Charter Bus Operators", category: "Transportation" },
  { id: "non-emergency-medical-transport", name: "Non-Emergency Medical Transport", category: "Transportation" },

  // ENERGY (2 — solar-installers and utility-contractors already in Construction)
  { id: "energy-auditors", name: "Energy Auditors", category: "Energy" },
  { id: "oil-gas-field-services", name: "Oil & Gas Field Services", category: "Energy" },

  // TECHNOLOGY (5)
  { id: "it-staffing-firms", name: "IT Staffing Firms", category: "Technology" },
  { id: "software-dev-agencies", name: "Software Dev Agencies", category: "Technology" },
  { id: "cybersecurity-mssp", name: "Cybersecurity MSSPs", category: "Technology" },
  { id: "data-analytics-consultants", name: "Data Analytics Consultants", category: "Technology" },
  { id: "cloud-infrastructure-consultants", name: "Cloud Infrastructure Consultants", category: "Technology" },

  // NONPROFIT & GOVERNMENT (4)
  { id: "nonprofits-social-services", name: "Social Services Nonprofits", category: "Nonprofit & Government" },
  { id: "faith-organizations", name: "Faith Organizations", category: "Nonprofit & Government" },
  { id: "trade-associations", name: "Trade Associations", category: "Nonprofit & Government" },
  { id: "municipal-services", name: "Municipal Services", category: "Nonprofit & Government" },

  // MEDIA & PUBLISHING (4)
  { id: "independent-publishers", name: "Independent Publishers", category: "Media & Publishing" },
  { id: "podcasting-networks", name: "Podcasting Networks", category: "Media & Publishing" },
  { id: "video-production-smb", name: "SMB Video Production", category: "Media & Publishing" },
  { id: "news-media-local", name: "Local News Media", category: "Media & Publishing" },

  // SPORTS & FITNESS (3)
  { id: "gyms-independent", name: "Independent Gyms", category: "Sports & Fitness" },
  { id: "personal-trainers", name: "Personal Trainers", category: "Sports & Fitness" },
  { id: "youth-sports-orgs", name: "Youth Sports Organizations", category: "Sports & Fitness" },

  // AUTOMOTIVE (4)
  { id: "auto-repair-shops", name: "Auto Repair Shops", category: "Automotive" },
  { id: "auto-body-shops", name: "Auto Body Shops", category: "Automotive" },
  { id: "fleet-managers", name: "Fleet Managers", category: "Automotive" },
  { id: "rv-dealerships", name: "RV Dealerships", category: "Automotive" },

  // SPECIALTY SERVICES (8)
  { id: "cleaning-companies", name: "Cleaning Companies", category: "Specialty Services" },
  { id: "pest-control", name: "Pest Control", category: "Specialty Services" },
  { id: "security-guard-firms", name: "Security Guard Firms", category: "Specialty Services" },
  { id: "event-planning", name: "Event Planning", category: "Specialty Services" },
  { id: "tattoo-studios", name: "Tattoo Studios", category: "Specialty Services" },
  { id: "funeral-homes", name: "Funeral Homes", category: "Specialty Services" },
  { id: "pet-services", name: "Pet Services", category: "Specialty Services" },
  { id: "alterations-tailoring", name: "Alterations & Tailoring", category: "Specialty Services" },

  // INSURANCE OPERATIONS (3)
  { id: "insurance-tpa", name: "Insurance TPAs", category: "Insurance Operations" },
  { id: "public-adjusters", name: "Public Adjusters", category: "Insurance Operations" },
  { id: "insurance-restoration", name: "Insurance Restoration", category: "Insurance Operations" },

  // WELLNESS & PERSONAL CARE (4)
  { id: "chiropractic-practices", name: "Chiropractic Practices", category: "Wellness & Personal Care" },
  { id: "acupuncture-practices", name: "Acupuncture Practices", category: "Wellness & Personal Care" },
  { id: "med-spas", name: "Med Spas", category: "Wellness & Personal Care" },
  { id: "hair-salons-independent", name: "Independent Hair Salons", category: "Wellness & Personal Care" },

  // GOVERNMENT-ADJACENT (3)
  { id: "grant-writers", name: "Grant Writers", category: "Government-Adjacent" },
  { id: "public-defenders", name: "Public Defenders", category: "Government-Adjacent" },
  { id: "land-surveyors", name: "Land Surveyors", category: "Government-Adjacent" },
];
