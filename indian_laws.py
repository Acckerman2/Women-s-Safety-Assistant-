"""
Indian Laws Knowledge Base for Women's Safety.

Comprehensive database of Indian laws, BNS (Bharatiya Nyaya Sanhita) sections,
IPC sections, special acts, legal procedures, government schemes, landmark
Supreme Court judgments, state-wise helplines, One Stop Centres, NCW complaint
process, and everything a woman in India needs to know for her safety and rights.
"""

# ──────────────────────────────────────────────────────────────────
#  INDIAN LAWS DATABASE
# ──────────────────────────────────────────────────────────────────

INDIAN_LAWS_DB = {
    # ── Bharatiya Nyaya Sanhita (BNS) 2023 — replaces IPC from 1 Jul 2024 ──
    "bns": {
        "title": "Bharatiya Nyaya Sanhita (BNS) 2023",
        "note": "Replaces IPC w.e.f. 1 July 2024",
        "sections": {
            "Section 63 (BNS)": {
                "old_ipc": "IPC 376",
                "offence": "Rape",
                "punishment": "Rigorous imprisonment not less than 10 years, may extend to life imprisonment and fine",
                "description": "Sexual intercourse with a woman against her will, without consent, or when she is unable to communicate consent.",
                "key_points": [
                    "Marital rape exception still exists for wife above 18 years",
                    "Consent obtained by fear, intoxication, unsoundness of mind, or impersonation is not valid consent",
                    "Attempt to rape: 5-10 years imprisonment (Section 64 BNS)",
                ]
            },
            "Section 64 (BNS)": {
                "old_ipc": "IPC 376(2)",
                "offence": "Punishment for rape in certain cases (aggravated)",
                "punishment": "Not less than 10 years RI, may extend to life imprisonment (natural life) or death",
                "description": "By police officer, public servant, armed forces member, relative/guardian, during communal violence, on pregnant woman, minor, or incapacitating victim.",
            },
            "Section 65 (BNS)": {
                "old_ipc": "IPC 376AB",
                "offence": "Rape on woman under 12 years",
                "punishment": "Not less than 20 years RI, may extend to life or death",
                "description": "Rape of a girl child below the age of 12 years.",
            },
            "Section 66 (BNS)": {
                "old_ipc": "IPC 376DA",
                "offence": "Gang rape on woman under 18",
                "punishment": "Imprisonment for life (remainder of natural life) or death",
                "description": "Gang rape of a woman under 18 years of age.",
            },
            "Section 67 (BNS)": {
                "old_ipc": "IPC 376DB",
                "offence": "Gang rape on woman under 12",
                "punishment": "Imprisonment for life or death",
                "description": "Gang rape of a girl below 12 years.",
            },
            "Section 68 (BNS)": {
                "old_ipc": "IPC 376C",
                "offence": "Intercourse by person in authority",
                "punishment": "5-10 years RI and fine",
                "description": "Sexual intercourse by superintendent/manager of jail, hospital, etc. with woman in custody.",
            },
            "Section 69 (BNS)": {
                "old_ipc": "IPC 376 related",
                "offence": "Intercourse by deceitful means / false promise of marriage",
                "punishment": "Up to 10 years imprisonment and fine",
                "description": "Sexual intercourse by employing deceitful means or making promise of marriage without intending to fulfil it.",
                "key_points": [
                    "NEW provision under BNS — did not exist in IPC",
                    "Covers false promise of marriage, impersonation, induced consent by fraud",
                ]
            },
            "Section 70 (BNS)": {
                "old_ipc": "IPC 376D",
                "offence": "Gang rape",
                "punishment": "Not less than 20 years RI, may extend to life imprisonment, and fine (paid to victim)",
                "description": "Where a woman is raped by one or more persons constituting a group, each person is deemed to have committed gang rape.",
            },
            "Section 74 (BNS)": {
                "old_ipc": "IPC 354",
                "offence": "Assault or use of criminal force on woman with intent to outrage modesty",
                "punishment": "1-5 years imprisonment and fine",
                "description": "Assault or criminal force on any woman intending to outrage or knowing it likely to outrage her modesty.",
            },
            "Section 75 (BNS)": {
                "old_ipc": "IPC 354A",
                "offence": "Sexual harassment",
                "punishment": "Up to 3 years imprisonment, or fine, or both",
                "description": "Physical contact, demand for sexual favours, showing pornography, making sexually coloured remarks.",
                "key_points": [
                    "Covers eve teasing, cat calling, unwelcome physical contact",
                    "Making sexually coloured remarks is punishable even without physical contact",
                    "Showing pornography against will is a separate offence",
                ]
            },
            "Section 76 (BNS)": {
                "old_ipc": "IPC 354B",
                "offence": "Assault with intent to disrobe",
                "punishment": "3-7 years imprisonment and fine",
                "description": "Assault or use of criminal force with intention of disrobing a woman.",
            },
            "Section 77 (BNS)": {
                "old_ipc": "IPC 354C",
                "offence": "Voyeurism",
                "punishment": "1-3 years (first offence), 3-7 years (repeat offence)",
                "description": "Watching or capturing image of a woman in a private act without consent.",
                "key_points": [
                    "Includes clicking pictures, recording videos in private spaces",
                    "MMS recording, hidden cameras in washrooms/changing rooms",
                    "Dissemination of such images is also covered",
                ]
            },
            "Section 78 (BNS)": {
                "old_ipc": "IPC 354D",
                "offence": "Stalking",
                "punishment": "Up to 3 years (first offence), up to 5 years (repeat)",
                "description": "Following, contacting, monitoring online activity despite clear disinterest by the woman.",
                "key_points": [
                    "Includes physical stalking and cyber/online stalking",
                    "Repeatedly following, watching, contacting despite disinterest",
                    "Monitoring internet/email use of a woman",
                    "Cognizable and bailable (first offence), non-bailable (repeat)",
                ]
            },
            "Section 79 (BNS)": {
                "old_ipc": "IPC 509",
                "offence": "Word, gesture or act to insult modesty of woman",
                "punishment": "Up to 3 years and fine",
                "description": "Uttering word, making sound/gesture, exhibiting object to insult modesty of a woman. Includes obscene phone calls, lewd comments.",
            },
            "Section 84 (BNS)": {
                "old_ipc": "IPC 498A",
                "offence": "Cruelty by husband or relatives of husband",
                "punishment": "Up to 3 years imprisonment and fine",
                "description": "Willful conduct likely to drive the woman to commit suicide or cause grave injury. Harassment for dowry.",
                "key_points": [
                    "Covers physical cruelty — beating, burning, injuring",
                    "Covers mental cruelty — abuse, humiliation, threats, isolation",
                    "Covers economic cruelty — not providing maintenance, taking wife's salary/property",
                    "Includes dowry-related harassment and demands",
                    "Cognizable and non-bailable offence",
                    "Complaint can be filed by wife, her relative, or any person with knowledge",
                ]
            },
            "Section 85 (BNS)": {
                "old_ipc": "IPC 304B",
                "offence": "Dowry death",
                "punishment": "Not less than 7 years, may extend to life imprisonment",
                "description": "Death of woman within 7 years of marriage under abnormal circumstances, if she was subjected to cruelty/harassment for dowry.",
                "key_points": [
                    "Presumption of dowry death if death within 7 years + evidence of harassment",
                    "Burden of proof shifts to husband and in-laws",
                    "Applies to burns, bodily injury, or suspicious death",
                ]
            },
            "Section 86 (BNS)": {
                "old_ipc": "New",
                "offence": "Abetment of suicide of woman — Expanded",
                "punishment": "Up to 10 years and fine",
                "description": "If abetment leads to suicide of a woman, especially linked to dowry harassment.",
            },
            "Section 95 (BNS)": {
                "old_ipc": "IPC 363/366",
                "offence": "Kidnapping / abduction of woman",
                "punishment": "Up to 7-10 years and fine",
                "description": "Kidnapping or abducting a woman to compel marriage or for illicit intercourse.",
                "key_points": [
                    "Section 96 BNS: Kidnapping from lawful guardianship (minor under 16 boy / 18 girl)",
                    "Section 97 BNS: Kidnapping/abduction to compel marriage – up to 10 years + fine",
                    "Section 98 BNS: Kidnapping for ransom – up to life imprisonment",
                ]
            },
            "Section 117 (BNS)": {
                "old_ipc": "IPC 326A",
                "offence": "Acid attack",
                "punishment": "Not less than 10 years, may extend to life imprisonment and fine",
                "description": "Causing permanent or partial damage to face, head, or body by acid.",
                "key_points": [
                    "Victim entitled to free medical treatment under S.357C CrPC / S.398 BNSS",
                    "Compensation from state government (minimum ₹3 lakhs)",
                    "Private hospitals CANNOT refuse treatment",
                    "Acid sale restricted — buyer ID mandatory (Supreme Court order)",
                    "Section 118 BNS: Attempt to throw acid – 5-7 years + fine",
                ]
            },
            "Section 296 (BNS)": {
                "old_ipc": "IPC 494",
                "offence": "Bigamy — marrying again during lifetime of spouse",
                "punishment": "Up to 7 years imprisonment and fine",
                "description": "Whoever marries while the marriage with existing spouse is still valid.",
            },
            "Section 302 (BNS)": {
                "old_ipc": "New provision",
                "offence": "Snatching (including chain snatching, mangalsutra snatching)",
                "punishment": "Up to 3 years imprisonment and fine",
                "description": "New offence covering snatching — particularly relevant for crimes targeting women like chain snatching.",
            },
        }
    },

    # ── Special Acts ──────────────────────────────────────────────
    "special_acts": {
        "Dowry Prohibition Act 1961": {
            "description": "Prohibits giving and taking dowry in connection with marriage.",
            "key_provisions": [
                "Section 3: Penalty for giving/taking dowry – 5 years imprisonment + fine",
                "Section 4: Penalty for demanding dowry – 6 months to 2 years + fine up to ₹10,000",
                "Any agreement for dowry is VOID",
                "Burden of proof on the person demanding dowry",
            ],
            "how_to_report": "File FIR at nearest police station; Complaint to Dowry Prohibition Officer",
        },
        "Protection of Women from Domestic Violence Act 2005 (DV Act)": {
            "description": "Civil law providing protection to women from domestic violence – physical, emotional, verbal, economic, and sexual abuse.",
            "key_provisions": [
                "Right to reside in shared household (Section 17)",
                "Protection orders (Section 18) – prohibit respondent from committing violence",
                "Residence orders (Section 19) – cannot be evicted from shared household",
                "Monetary relief (Section 20) – expenses, losses, maintenance",
                "Custody orders (Section 21) – temporary custody of children",
                "Compensation orders (Section 22) – for injuries including mental torture",
                "Covers wife, live-in partner, sister, mother, or any female in household",
                "Service Provider / Protection Officer appointed by government",
            ],
            "how_to_report": [
                "Approach Protection Officer (appointed by District Magistrate)",
                "File complaint before Judicial Magistrate First Class (JMFC)",
                "Contact local women's shelter / NGO",
                "Call Women Helpline: 181",
            ],
        },
        "Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act 2013 (POSH Act)": {
            "description": "Mandates prevention and redressal of sexual harassment at workplace.",
            "key_provisions": [
                "Every employer with 10+ employees must constitute Internal Complaints Committee (ICC)",
                "District Officer constitutes Local Complaints Committee (LCC)",
                "Complaint must be filed within 3 months of incident (extendable by 3 months)",
                "ICC must complete inquiry within 90 days",
                "Conciliation possible at request of complainant",
                "Employer penalty for non-compliance: up to ₹50,000 (first), licence cancellation (repeat)",
                "Covers physical contact, demand for favours, remarks, showing pornography, any unwelcome sexual conduct",
                "Aggrieved woman includes any woman regardless of employment status",
            ],
            "how_to_report": [
                "Submit written complaint to Internal Complaints Committee (ICC)",
                "If no ICC: approach Local Complaints Committee at district level",
                "File within 3 months (extendable by ICC for 3 more months)",
                "Can also file FIR under BNS Section 75 (IPC 354A)",
            ],
        },
        "Immoral Traffic (Prevention) Act 1956 (ITPA)": {
            "description": "Prevents trafficking of women and girls for commercial sexual exploitation.",
            "key_provisions": [
                "Section 3: Keeping a brothel – 1-3 years (first offence), 2-5 years (repeat)",
                "Section 4: Living on earnings of prostitution – up to 2 years",
                "Section 5: Procuring/inducing/taking person for prostitution – 3-7 years (adult), 7-14 years (child)",
                "Section 6: Detaining person in premises – 7 years to life imprisonment",
                "Victims are treated as persons in need of rescue, NOT criminals",
            ],
        },
        "POCSO Act 2012 (Protection of Children from Sexual Offences)": {
            "description": "Protects children under 18 from sexual abuse and exploitation.",
            "key_provisions": [
                "Penetrative sexual assault: 10-20 years + fine",
                "Aggravated penetrative sexual assault: 20 years to life or death",
                "Sexual harassment of child: up to 3 years",
                "Using child for pornographic purposes: up to 5 years",
                "Gender-neutral — protects boys and girls",
                "Mandatory reporting — failure to report is an offence",
                "Child-friendly courts and procedures",
            ],
        },
        "Indecent Representation of Women (Prohibition) Act 1986": {
            "description": "Prohibits indecent representation of women in publications, advertisements, etc.",
            "key_provisions": [
                "Bars publication/distribution of material depicting women indecently",
                "First offence: up to 2 years + fine up to ₹2,000",
                "Subsequent: 6 months to 5 years + ₹10,000-₹1,00,000",
            ],
        },
        "Hindu Marriage Act 1955 / Special Marriage Act 1954": {
            "description": "Provisions related to marriage, divorce, maintenance, and women's property rights.",
            "key_provisions": [
                "Section 13 (HMA): Grounds for divorce including cruelty, adultery, desertion",
                "Section 24 (HMA): Maintenance pendente lite — spouse can claim maintenance during divorce proceedings",
                "Section 25 (HMA): Permanent alimony and maintenance",
                "Section 125 CrPC / Section 144 BNSS: Right of wife to claim maintenance from husband",
                "Women's right to matrimonial property in marital disputes",
            ],
        },
        "Muslim Women (Protection of Rights on Marriage) Act 2019": {
            "description": "Declares instant triple talaq (talaq-e-biddat) as void and illegal.",
            "key_provisions": [
                "Instant triple talaq is void and illegal",
                "Husband can be imprisoned for up to 3 years",
                "Wife entitled to subsistence allowance",
                "Custody of minor children to the mother",
                "Offence: cognizable, compoundable, and non-bailable (bail by Magistrate)",
            ],
        },
        "Maternity Benefit Act 1961 (Amended 2017)": {
            "description": "Provides maternity benefits to women employees.",
            "key_provisions": [
                "26 weeks paid maternity leave (for first 2 children)",
                "12 weeks for third child onwards",
                "12 weeks for commissioning/adopting mother",
                "Work from home option after maternity leave (if nature of work allows)",
                "Crèche facility mandatory for establishments with 50+ employees",
                "No termination during pregnancy or maternity leave",
            ],
        },
        "Equal Remuneration Act 1976 / Code on Wages 2019": {
            "description": "Ensures equal pay for equal work regardless of gender.",
            "key_provisions": [
                "No discrimination in recruitment or wages on basis of sex",
                "Employer cannot reduce wages to comply with this Act",
                "Fine up to ₹20,000 and/or imprisonment up to 3 months",
                "Code on Wages 2019 subsumes this into a unified law",
            ],
        },
    },

    # ── Cyber Crime Laws ────────────────────────────────────────
    "cyber_laws": {
        "title": "IT Act 2000 & Cyber Crime Laws relevant to women",
        "sections": {
            "Section 66E IT Act": {
                "offence": "Violation of privacy / Voyeurism online",
                "punishment": "Up to 3 years imprisonment or fine up to ₹2 lakh",
                "description": "Capturing/publishing/transmitting images of private area of a person without consent.",
            },
            "Section 67 IT Act": {
                "offence": "Publishing obscene material electronically",
                "punishment": "First offence: 3 years + ₹5 lakh. Repeat: 5 years + ₹10 lakh",
                "description": "Publishing or transmitting obscene material in electronic form.",
            },
            "Section 67A IT Act": {
                "offence": "Publishing sexually explicit material electronically",
                "punishment": "First: 5 years + ₹10 lakh. Repeat: 7 years + ₹10 lakh",
                "description": "Publishing sexually explicit material in electronic form.",
            },
            "Section 67B IT Act": {
                "offence": "Child pornography",
                "punishment": "First: 5 years + ₹10 lakh. Repeat: 7 years + ₹10 lakh",
                "description": "Publishing/transmitting material depicting children in sexually explicit acts.",
            },
            "BNS Section 351 + 79": {
                "offence": "Online harassment / Criminal intimidation / Insult to modesty online",
                "punishment": "Varies; up to 2-3 years + fine",
                "description": "Covers cyber-bullying, threats via electronic means, and online insults to modesty of women.",
            },
        },
        "how_to_report": [
            "File complaint on National Cyber Crime Reporting Portal: cybercrime.gov.in",
            "Call Cyber Crime Helpline: 1930",
            "File FIR at nearest police station (cyber cell)",
            "Screenshot and preserve ALL evidence before reporting",
            "Report on social media platform as well",
        ],
    },

    # ── FIR Filing Process ──────────────────────────────────────
    "fir_process": {
        "title": "How to File an FIR (First Information Report)",
        "steps": [
            "1. Go to the nearest police station (jurisdiction where crime occurred, but Zero FIR can be filed at ANY station)",
            "2. Narrate the incident to the officer on duty — give date, time, place, details",
            "3. FIR is FREE — no fee required",
            "4. You can file in your language — police must translate if needed",
            "5. Get a signed copy of FIR — it is your RIGHT under Section 173 BNSS (old S.154 CrPC)",
            "6. If police refuses: approach the Superintendent of Police (SP) in writing",
            "7. If SP also refuses: approach the Judicial Magistrate under Section 175(3) BNSS",
            "8. Online FIR: Many states allow e-FIR via state police websites",
        ],
        "important_rights": [
            "Zero FIR: Can file FIR at ANY police station regardless of jurisdiction",
            "Women complainant: Statement MUST be recorded by a woman officer if available",
            "Sexual offence: Statement must be recorded at residence or place of complainant's choice (Section 183 BNSS)",
            "Medical examination: Free, can be done at ANY hospital (public or private)",
            "Police CANNOT refuse FIR for cognizable offences — it is a punishable offence",
            "NCW e-complaint: Register online at ncw.nic.in",
        ],
    },

    # ── Constitutional Rights ───────────────────────────────────
    "constitutional_rights": {
        "title": "Constitutional Rights for Women in India",
        "articles": {
            "Article 14": "Equality before law — no discrimination on grounds of sex",
            "Article 15(1)": "Prohibition of discrimination on grounds of sex",
            "Article 15(3)": "State can make special provisions for women and children",
            "Article 16": "Equal opportunity in public employment",
            "Article 21": "Right to life and personal liberty — includes right to live with dignity",
            "Article 23": "Prohibition of trafficking and forced labour",
            "Article 39(a)": "Right to adequate means of livelihood equally for men and women",
            "Article 39(d)": "Equal pay for equal work for men and women",
            "Article 42": "Just and humane conditions of work and maternity relief",
            "Article 51A(e)": "Fundamental duty to renounce practices derogatory to dignity of women",
        },
    },

    # ── Important Helplines ─────────────────────────────────────
    "helplines": {
        "title": "Important Helplines for Women in India",
        "national": {
            "Women Helpline (All India)": "181",
            "Police": "100",
            "Emergency Response (ERSS)": "112",
            "National Commission for Women (NCW)": "7827-170-170",
            "NCW WhatsApp Helpline": "7217735372",
            "Domestic Violence Helpline": "181",
            "Child Helpline (CHILDLINE)": "1098",
            "Cyber Crime Helpline": "1930",
            "Acid Attack Helpline (Toll-free)": "1800-180-7998",
            "Legal Aid (NALSA)": "15100",
            "Railway Police (RPF) for women": "182",
            "Anti-Stalking Helpline": "1091",
            "Missing Children / Women": "1094",
            "Senior Citizen Helpline": "14567",
            "Central Social Welfare Board": "011-23381685",
        },
        "mental_health": {
            "iCall (Psychosocial Helpline)": "9152987821",
            "Vandrevala Foundation (24x7)": "1860-2662-345 / 1800-2333-330",
            "NIMHANS Helpline": "080-46110007",
            "Sneha (Chennai)": "044-24640050",
            "AASRA (Mumbai)": "9820466726",
            "Connecting Trust (Bangalore)": "080-25711077",
            "Sahai Helpline (Bangalore)": "080-25497777",
            "Roshni (Hyderabad)": "040-66202000",
            "Maithri (Cochin)": "0484-2540530",
            "Sumaitri (Delhi)": "011-23389090",
            "Jeevan Aastha (Gujarat)": "1800-233-3330",
        },
        "state_wise": {
            "Delhi": {"Women Helpline": "1091 / 181", "DCW": "011-23379150 / 23370597", "Police": "100 / 112"},
            "Maharashtra": {"Women Helpline": "181 / 103", "MSCW": "022-26592707", "Cyber Cell Mumbai": "022-24910476"},
            "Karnataka": {"Women Helpline": "181", "Vanitha Sahayavani": "1091", "Bangalore Police": "080-22942222"},
            "Tamil Nadu": {"Women Helpline": "181 / 1091", "TNSCW": "044-28592750", "Kavalan SOS App": "Available on stores"},
            "Uttar Pradesh": {"Women Helpline": "181 / 1090", "Women Power Line 1090": "1090", "UP Police": "112"},
            "Rajasthan": {"Women Helpline": "181", "Abhay Command Centre": "181", "Rajasthan Police": "100"},
            "West Bengal": {"Women Helpline": "181 / 1091", "WBCW": "033-23216992", "Kolkata Police": "100"},
            "Gujarat": {"Women Helpline": "181", "Abhayam": "181", "Gujarat Police": "100"},
            "Madhya Pradesh": {"Women Helpline": "181 / 1090", "Jai Ho App": "Available", "MP Police": "100 / 112"},
            "Kerala": {"Women Helpline": "181", "Mitra Helpline": "1800-599-0100", "She-Taxi": "Available"},
            "Telangana": {"Women Helpline": "181", "SHE Teams": "100 / 7382238286", "Bharosa Centre": "040-27852470"},
            "Bihar": {"Women Helpline": "181 / 1091", "Bihar SHRC": "0612-2504010"},
            "Punjab": {"Women Helpline": "181 / 1091", "Punjab Police": "100 / 112"},
            "Haryana": {"Women Helpline": "181 / 1091", "HSCW": "0172-2583008"},
            "Odisha": {"Women Helpline": "181", "Child Helpline": "1098", "Odisha Police": "100"},
            "Assam": {"Women Helpline": "181", "Assam Police": "100"},
            "Jharkhand": {"Women Helpline": "181 / 1091", "Jharkhand Police": "100"},
            "Chhattisgarh": {"Women Helpline": "181 / 1091", "CG Police Women Cell": "0771-2511075"},
            "Uttarakhand": {"Women Helpline": "181 / 1090", "UK Police": "100 / 112"},
            "Goa": {"Women Helpline": "181 / 1091", "Goa Police": "100"},
        },
    },

    # ── State-wise One Stop Centres (Sakhi Centres) ─────────────
    "one_stop_centres": {
        "title": "One Stop Centres (Sakhi Centres) for Women",
        "description": "Under the One Stop Centre (OSC) Scheme run by Ministry of Women & Child Development, these centres provide integrated support to women affected by violence — medical aid, legal aid, police, psycho-social counselling, and shelter — ALL UNDER ONE ROOF. Available 24x7.",
        "how_to_access": [
            "Call 181 (Women Helpline) — you will be connected to nearest OSC",
            "Walk in to any One Stop Centre (Sakhi Centre) in your district",
            "Get referral from police, hospital, court, or NGO",
            "Services are FREE for all women regardless of caste, religion, or income",
        ],
        "services_provided": [
            "🏥 Medical assistance — first-aid, medical examination, treatment",
            "👮 Police facilitation — help in filing FIR, legal process",
            "⚖️ Legal aid & counselling — free legal advice and court assistance",
            "🧠 Psycho-social support — trained counsellors for trauma, PTSD",
            "🏠 Temporary shelter — safe stay up to 5 days (longer via Swadhar/Short Stay Home)",
            "📹 Video conferencing for court hearings and recording statements",
        ],
        "centres_by_state": {
            "Andhra Pradesh": 13, "Arunachal Pradesh": 3, "Assam": 33,
            "Bihar": 38, "Chhattisgarh": 28, "Delhi": 4,
            "Goa": 2, "Gujarat": 33, "Haryana": 22,
            "Himachal Pradesh": 12, "Jharkhand": 24, "Karnataka": 31,
            "Kerala": 14, "Madhya Pradesh": 52, "Maharashtra": 36,
            "Manipur": 5, "Meghalaya": 4, "Mizoram": 2,
            "Nagaland": 3, "Odisha": 30, "Punjab": 23,
            "Rajasthan": 34, "Sikkim": 2, "Tamil Nadu": 37,
            "Telangana": 31, "Tripura": 4, "Uttar Pradesh": 75,
            "Uttarakhand": 13, "West Bengal": 23,
        },
        "total_centres": "Total: 733+ One Stop Centres across India",
        "helpline": "Call 181 to locate the nearest One Stop Centre",
    },

    # ── NCW Complaint Process ───────────────────────────────────
    "ncw_complaint": {
        "title": "How to File a Complaint with National Commission for Women (NCW)",
        "about": "The NCW is a statutory body that investigates complaints related to women's rights. It can take suo motu cognizance, order investigations, and direct authorities to act.",
        "online_complaint": [
            "1. Visit: ncw.nic.in → 'Online Complaint Registration' OR ncwapps.nic.in",
            "2. Click 'Register Complaint' → Fill your details (name, address, phone, email)",
            "3. Select complaint category: Domestic Violence, Dowry Harassment, Sexual Harassment, Cyber Crime, etc.",
            "4. Describe the incident in detail — dates, persons involved, what happened",
            "5. Upload supporting documents (FIR copy, medical report, photos, screenshots)",
            "6. Submit → You will receive a Unique Complaint ID for tracking",
            "7. NCW will acknowledge within 1 week and take action",
        ],
        "offline_complaint": [
            "Write a letter/application to: Chairperson, National Commission for Women",
            "Address: Plot No. 21, Jasola Institutional Area, New Delhi – 110025",
            "Include: your name, address, phone, description of incident, relief sought",
            "Attach: copies of any complaints, FIR, medical documents",
            "You can also email: complaintcell-ncw@nic.in",
        ],
        "what_ncw_can_do": [
            "Issue notices to police / accused to appear and respond",
            "Direct the police to register FIR if they refused",
            "Recommend action against erring police officers",
            "Provide legal and medical aid",
            "Inspect institutions (jails, shelter homes, hospitals)",
            "Recommend changes in laws to the government",
            "Suo motu investigation of cases from news reports",
        ],
        "helpline": "NCW Helpline: 7827-170-170 | WhatsApp: 7217735372",
        "website": "ncw.nic.in | ncwapps.nic.in",
    },

    # ── Government Schemes for Women ────────────────────────────
    "government_schemes": {
        "title": "Government Schemes for Women's Safety & Empowerment in India",
        "schemes": {
            "Beti Bachao Beti Padhao (BBBP)": {
                "ministry": "Ministry of Women and Child Development",
                "about": "Addresses declining child sex ratio and promotes education of girl child.",
                "benefits": ["Awareness campaigns", "Multi-sectoral action in gender-critical districts", "Education incentives for girls"],
            },
            "One Stop Centre Scheme (Sakhi)": {
                "ministry": "MoWCD",
                "about": "24x7 centres providing integrated support to women affected by violence.",
                "benefits": ["Free medical, legal, police, counselling, shelter — all under one roof", "733+ centres across India", "Call 181 to access"],
            },
            "Swadhar Greh Scheme": {
                "ministry": "MoWCD",
                "about": "Shelter, food, clothing, and counselling for women in difficult circumstances.",
                "benefits": ["Women in distress — deserted, destitute, homeless", "Survivors of domestic violence, trafficking", "Women released from jail with no support", "Stay up to 3 years with rehabilitation"],
            },
            "Ujjawala Scheme": {
                "ministry": "MoWCD",
                "about": "Prevention of trafficking, rescue, rehabilitation, reintegration, and repatriation of trafficked women.",
                "benefits": ["Rescue operations", "Rehabilitation homes", "Skill training and income generation", "Psychological counselling"],
            },
            "Mahila Police Volunteers (MPV)": {
                "ministry": "MoWCD + MHA",
                "about": "Women volunteers act as link between police and community for reporting crimes against women.",
                "benefits": ["Report crimes in their locality", "Assist police in investigation", "Spread awareness about women's rights"],
            },
            "Women Helpline (181)": {
                "ministry": "MoWCD",
                "about": "24x7 toll-free pan-India helpline for women in distress.",
                "benefits": ["Immediate assistance, referral to police/hospital/shelter/legal aid", "Available in local languages", "Links to One Stop Centres"],
            },
            "Nirbhaya Fund": {
                "ministry": "Ministry of Finance (administered by MoWCD)",
                "about": "₹1,000 crore fund for projects to improve safety of women in India.",
                "benefits": ["Funds safe city projects, emergency response", "CCTV in public transport, GPS in buses", "Women safety in public spaces"],
            },
            "Pradhan Mantri Matru Vandana Yojana (PMMVY)": {
                "ministry": "MoWCD",
                "about": "Cash incentive of ₹5,000 in 3 installments for pregnant and lactating mothers.",
                "benefits": ["₹5,000 for first living child", "Partial wage compensation during pregnancy", "Improved health and nutrition"],
            },
            "Sukanya Samriddhi Yojana": {
                "ministry": "Ministry of Finance",
                "about": "Small savings scheme for girl child with high interest rate and tax benefits.",
                "benefits": ["High interest rate (~8%)", "Tax-free under Section 80C", "Account for girls below 10 years"],
            },
            "Mahila Shakti Kendra": {
                "ministry": "MoWCD",
                "about": "Community engagement for women's empowerment through college student volunteers.",
                "benefits": ["Awareness about government schemes", "Skill development", "Digital literacy", "Health and nutrition"],
            },
            "Free Legal Aid (NALSA)": {
                "ministry": "Department of Justice",
                "about": "Free legal services to women under Legal Services Authorities Act 1987.",
                "benefits": ["FREE lawyer in any court", "No income limit for women — all women eligible", "Contact District Legal Services Authority (DLSA)", "Helpline: 15100"],
            },
            "Nari Adalat (Women's Court)": {
                "ministry": "MoWCD (2023)",
                "about": "Alternative dispute resolution for women — village/ward level women's courts for speedy justice.",
                "benefits": ["Quick resolution of minor disputes", "No lawyer needed", "Free of cost", "Run by elected women representatives"],
            },
        },
    },

    # ── Landmark Supreme Court Judgments ─────────────────────────
    "landmark_judgments": {
        "title": "Landmark Supreme Court Judgments for Women's Rights in India",
        "cases": {
            "Vishaka v. State of Rajasthan (1997)": {
                "about": "Laid down guidelines for prevention of sexual harassment at workplace — became the foundation for POSH Act 2013.",
                "impact": "Every employer must have a complaints committee; Sexual harassment defined for the first time.",
            },
            "Laxmi v. Union of India (2014)": {
                "about": "Acid attack case — SC directed ban on over-the-counter sale of acid, mandatory compensation for victims.",
                "impact": "Regulation of acid sale; Minimum ₹3 lakh compensation from government; Free medical treatment.",
            },
            "Shayara Bano v. Union of India (2017)": {
                "about": "Triple Talaq declared unconstitutional and void.",
                "impact": "Led to Muslim Women (Protection of Rights on Marriage) Act 2019; Instant triple talaq made criminal offence.",
            },
            "Joseph Shine v. Union of India (2018)": {
                "about": "Section 497 IPC (adultery) struck down as unconstitutional for treating women as property of husband.",
                "impact": "Adultery no longer a criminal offence; Affirmed women's sexual autonomy.",
            },
            "Navtej Singh Johar v. Union of India (2018)": {
                "about": "Section 377 IPC decriminalised — protects LGBTQ+ women's rights.",
                "impact": "Consensual same-sex relationships between adults no longer criminal.",
            },
            "Indian Young Lawyers Association v. State of Kerala (Sabarimala Case - 2018)": {
                "about": "SC ruled women of all ages can enter Sabarimala temple — gender discrimination violates Article 25.",
                "impact": "Reinforced women's right to worship and equality in religious practice.",
            },
            "X v. Principal Secretary, Health (2022)": {
                "about": "Unmarried women also have right to abortion under MTP Act up to 24 weeks.",
                "impact": "Extended reproductive choices; Marital rape recognised as ground for abortion.",
            },
            "S. Nagalakshmi v. State (2023)": {
                "about": "Verbal and emotional abuse also constitutes domestic violence — not just physical violence.",
                "impact": "Strengthened DV Act interpretation; Mental cruelty given equal weightage.",
            },
            "Aparna Bhat v. State of MP (2021)": {
                "about": "SC strongly criticised courts for suggesting mediation/compromise in sexual offence cases, and ordering victims to tie rakhi on accused.",
                "impact": "Courts cannot order compromise in sexual assault; Victim's dignity is paramount.",
            },
        },
    },

    # ── Women's Property Rights ────────────────────────────────
    "property_rights": {
        "title": "Women's Property Rights in India",
        "hindu_law": {
            "Hindu Succession Act 1956 (Amended 2005)": [
                "Daughters have EQUAL coparcenary rights as sons in ancestral (HUF) property",
                "Daughter is a coparcener by birth — same as a son (2005 Amendment)",
                "Married or unmarried — does not matter",
                "Right to demand partition of property",
                "Right to reside in parental home even after marriage",
                "Can be appointed Karta (manager) of HUF (SC ruling 2022)",
            ],
        },
        "maintenance_rights": [
            "Section 144 BNSS (old Section 125 CrPC): Wife can claim maintenance from husband",
            "Under DV Act 2005: Monetary relief including maintenance, rent, medical expenses",
            "Under Hindu Marriage Act Section 24: Maintenance during divorce proceedings (pendente lite)",
            "Under Hindu Marriage Act Section 25: Permanent alimony after divorce",
            "Under Hindu Adoption & Maintenance Act: Right to be maintained by husband",
            "Muslim Women: Right to fair and reasonable maintenance (Shah Bano case + subsequent legislation)",
            "Christian Women: Indian Divorce Act Section 36-37: Alimony",
            "Maintenance even for live-in partner (SC rulings)",
        ],
        "streedhan": [
            "Streedhan = All property/gifts/jewellery a woman owns before and after marriage",
            "Legally belongs ONLY to the woman — husband/in-laws have NO claim",
            "Includes gifts from parents, relatives, friends at/after marriage",
            "Misuse or appropriation of Streedhan is criminal breach of trust (IPC 405/BNS 316)",
            "Woman can demand return of Streedhan at any time",
        ],
    },

    # ── Women's Rights During Arrest / Police Encounter ─────────
    "rights_during_arrest": {
        "title": "Rights of Women During Arrest & Police Encounter",
        "rights": [
            "Woman CANNOT be arrested after sunset and before sunrise (Section 46(4) CrPC / Section 35 BNSS) except in exceptional circumstances with woman Magistrate's order",
            "Only a FEMALE police officer can search a woman — no male officer allowed (Section 51 CrPC / Section 48 BNSS)",
            "Woman must be kept in separate lock-up from male arrested persons",
            "Medical examination of rape victim MUST be by a female doctor (woman practitioner) if available",
            "Statement of rape victim MUST be recorded by a woman officer if available, at victim's chosen location",
            "Victim of sexual offence CANNOT be called to police station at night for recording statement",
            "Identity of rape victim CANNOT be disclosed — Section 72 BNSS (media, social media, anyone)",
            "In-camera trial (closed court) for sexual offence cases — no public allowed",
            "Two-finger test on rape victim is UNCONSTITUTIONAL and BANNED (SC ruling)",
            "Free legal aid is guaranteed — contact DLSA / call 15100",
            "Right to inform family/friend of arrest immediately",
            "Right to consult a lawyer before and during interrogation",
        ],
    },

    # ── Workplace Rights for Women ──────────────────────────────
    "workplace_rights": {
        "title": "Workplace Rights for Women in India",
        "rights": [
            "Equal pay for equal work — mandated by Article 39(d) of Constitution & Equal Remuneration Act",
            "No night shifts without consent and safety measures (varies by state — many states now allow with conditions)",
            "Crèche facility mandatory in establishments with 50+ employees (Maternity Benefit Act)",
            "26 weeks paid maternity leave for first 2 children (Maternity Benefit Act 2017)",
            "12 weeks for third child onwards; 12 weeks for adopting mothers",
            "Work from home option post-maternity leave (if nature of work allows)",
            "Cannot be terminated during pregnancy or maternity leave",
            "Every workplace with 10+ employees MUST have Internal Complaints Committee (ICC) under POSH Act",
            "Right to complain about sexual harassment — no retaliation permitted",
            "Right to clean and safe toilets — separate washrooms for women (Factories Act)",
            "No dangerous machines operation or work near cotton openers (Factories Act)",
            "Women employees in IT/BPO sectors entitled to safe transportation if working late hours",
        ],
        "posh_process": [
            "1. File written complaint with ICC within 3 months of incident (extendable by 3 months)",
            "2. ICC can assist in writing the complaint if needed",
            "3. Woman can request conciliation — but NOT monetary settlement",
            "4. ICC must complete inquiry within 90 days",
            "5. During inquiry, woman can request transfer or leave (which shall not be deducted from normal leave)",
            "6. If found guilty: employer can terminate, deduct salary, issue warning, or take disciplinary action",
            "7. If employer has no ICC: approach Local Complaints Committee (District level)",
            "8. Appeal: Within 90 days to court/tribunal",
        ],
    },
}


# ──────────────────────────────────────────────────────────────────
#  STATE-WISE WOMEN COMMISSION CONTACTS
# ──────────────────────────────────────────────────────────────────

STATE_WOMEN_COMMISSIONS = {
    "Delhi": {"name": "Delhi Commission for Women (DCW)", "phone": "011-23379150", "address": "C-Block, Vikas Bhawan, IP Estate, New Delhi"},
    "Maharashtra": {"name": "Maharashtra State Commission for Women", "phone": "022-26592707", "address": "Gruha Nirman Bhavan, Kalanagar, Bandra East, Mumbai"},
    "Karnataka": {"name": "Karnataka State Women's Commission", "phone": "080-22100435", "address": "No.2, Crescent Road, High Grounds, Bengaluru"},
    "Tamil Nadu": {"name": "Tamil Nadu State Commission for Women", "phone": "044-28592750", "address": "Nungambakkam, Chennai"},
    "Uttar Pradesh": {"name": "UP State Women's Commission", "phone": "0522-2306403", "address": "Lucknow"},
    "West Bengal": {"name": "WB Commission for Women", "phone": "033-23216992", "address": "Purta Bhavan, Salt Lake, Kolkata"},
    "Rajasthan": {"name": "Rajasthan State Commission for Women", "phone": "0141-2779001", "address": "Jaipur"},
    "Madhya Pradesh": {"name": "MP State Commission for Women", "phone": "0755-2551977", "address": "Bhopal"},
    "Gujarat": {"name": "Gujarat State Commission for Women", "phone": "079-23253831", "address": "Gandhinagar"},
    "Kerala": {"name": "Kerala Women's Commission", "phone": "0471-2322590", "address": "Thiruvananthapuram"},
    "Telangana": {"name": "Telangana State Women's Commission", "phone": "040-23262907", "address": "Hyderabad"},
    "Andhra Pradesh": {"name": "AP State Commission for Women", "phone": "0863-2340100", "address": "Vijayawada"},
    "Bihar": {"name": "Bihar State Women's Commission", "phone": "0612-2504010", "address": "Patna"},
    "Punjab": {"name": "Punjab State Commission for Women", "phone": "0172-2740003", "address": "Chandigarh"},
    "Haryana": {"name": "Haryana State Commission for Women", "phone": "0172-2583008", "address": "Chandigarh"},
    "Odisha": {"name": "Odisha State Commission for Women", "phone": "0674-2536625", "address": "Bhubaneswar"},
    "Assam": {"name": "Assam State Commission for Women", "phone": "0361-2237516", "address": "Guwahati"},
    "Jharkhand": {"name": "Jharkhand State Commission for Women", "phone": "0651-2400793", "address": "Ranchi"},
    "Chhattisgarh": {"name": "CG State Commission for Women", "phone": "0771-2511075", "address": "Raipur"},
    "Uttarakhand": {"name": "Uttarakhand State Commission for Women", "phone": "0135-2712620", "address": "Dehradun"},
    "Goa": {"name": "Goa State Commission for Women", "phone": "0832-2437054", "address": "Panaji"},
}


# ───────────────────────────────────────────────────────────────
# TOOL FUNCTIONS — used by the ReAct agent
# ───────────────────────────────────────────────────────────────

def lookup_indian_law(query: str) -> str:
    """
    Search the Indian laws database for laws related to the query.
    Returns relevant laws, sections, punishments, and descriptions.
    """
    query_lower = query.lower()
    # Build keyword list and also add common synonyms
    keywords = set(query_lower.split())
    synonym_map = {
        "rape": ["rape", "sexual", "intercourse", "assault"],
        "dowry": ["dowry", "dahej", "stridhan", "streedhan"],
        "domestic": ["domestic", "cruelty", "husband", "marital", "violence"],
        "harassment": ["harassment", "stalking", "eve", "teasing", "molestation"],
        "cyber": ["cyber", "online", "internet", "digital", "morphing", "revenge"],
        "acid": ["acid", "burn"],
        "child": ["child", "minor", "pocso", "girl"],
        "workplace": ["workplace", "office", "posh", "employer", "icc"],
        "trafficking": ["trafficking", "immoral", "prostitution"],
        "divorce": ["divorce", "maintenance", "alimony", "separation"],
        "marriage": ["marriage", "bigamy", "talaq", "nikah"],
        "kidnapping": ["kidnapping", "abduction", "kidnap"],
        "property": ["property", "succession", "inheritance", "streedhan"],
        "modesty": ["modesty", "insult", "gesture", "disrobe", "voyeurism"],
        "maternity": ["maternity", "pregnancy", "pregnant", "leave"],
    }
    expanded_keywords = set(keywords)
    for word in keywords:
        for _, synonyms in synonym_map.items():
            if word in synonyms:
                expanded_keywords.update(synonyms)

    results = []

    # Search BNS sections
    bns = INDIAN_LAWS_DB["bns"]["sections"]
    for sec_name, details in bns.items():
        searchable = f"{sec_name} {details.get('offence', '')} {details.get('description', '')} {details.get('old_ipc', '')}".lower()
        kp_text = " ".join(details.get("key_points", []))
        searchable += " " + kp_text.lower()
        if any(word in searchable for word in expanded_keywords):
            result = f"**{sec_name}** (replaces {details.get('old_ipc', 'N/A')})\n"
            result += f"  📌 Offence: {details['offence']}\n"
            result += f"  ⚖️ Punishment: {details['punishment']}\n"
            result += f"  📋 Description: {details['description']}\n"
            if "key_points" in details:
                result += "  🔑 Key Points:\n" + "\n".join(f"    • {kp}" for kp in details["key_points"])
            results.append(result)

    # Search special acts
    for act_name, details in INDIAN_LAWS_DB["special_acts"].items():
        searchable = f"{act_name} {details['description']}".lower()
        prov_text = " ".join(details.get("key_provisions", []))
        searchable += " " + prov_text.lower()
        if any(word in searchable for word in expanded_keywords):
            result = f"📜 **{act_name}**\n  {details['description']}\n"
            result += "  Key Provisions:\n" + "\n".join(f"    • {p}" for p in details.get("key_provisions", []))
            if "how_to_report" in details:
                if isinstance(details["how_to_report"], list):
                    result += "\n  How to Report:\n" + "\n".join(f"    → {r}" for r in details["how_to_report"])
                else:
                    result += f"\n  How to Report: {details['how_to_report']}"
            results.append(result)

    # Search cyber laws
    cyber = INDIAN_LAWS_DB["cyber_laws"]["sections"]
    for sec_name, details in cyber.items():
        searchable = f"{sec_name} {details.get('offence', '')} {details.get('description', '')}".lower()
        if any(word in searchable for word in expanded_keywords):
            result = f"💻 **{sec_name}**\n"
            result += f"  📌 Offence: {details['offence']}\n"
            result += f"  ⚖️ Punishment: {details['punishment']}\n"
            result += f"  📋 Description: {details['description']}"
            results.append(result)

    if not results:
        return ("No specific law found for this query. Try searching with keywords like: "
                "rape, harassment, dowry, stalking, domestic violence, cyber crime, acid attack, "
                "workplace, marriage, divorce, trafficking, kidnapping, modesty, voyeurism, "
                "property, maintenance, maternity, child abuse, molestation.")

    return "\n\n---\n\n".join(results[:10])


def get_fir_process() -> str:
    """Get the complete FIR filing process and important rights."""
    fir = INDIAN_LAWS_DB["fir_process"]
    result = f"## {fir['title']}\n\n"
    result += "### Steps:\n" + "\n".join(fir["steps"])
    result += "\n\n### 🔑 Important Rights of Women:\n" + "\n".join(f"• {r}" for r in fir["important_rights"])

    # Also include NCW complaint as alternative
    ncw = INDIAN_LAWS_DB["ncw_complaint"]
    result += f"\n\n## Alternative: {ncw['title']}\n"
    result += "### Online:\n" + "\n".join(ncw["online_complaint"])
    result += f"\n\n📞 {ncw['helpline']}\n🌐 {ncw['website']}"
    return result


def get_emergency_contacts(state: str = "") -> str:
    """Get emergency helpline numbers for women in India, optionally filtered by state."""
    helplines = INDIAN_LAWS_DB["helplines"]

    result = "## 🚨 Emergency Helplines for Women in India\n\n"

    # National helplines
    result += "### 📞 National Helplines:\n"
    for name, number in helplines["national"].items():
        result += f"📞 **{name}**: {number}\n"

    # State-specific if requested
    state_lower = state.strip().lower()
    if state_lower:
        state_data = helplines.get("state_wise", {})
        for sname, sdetails in state_data.items():
            if state_lower in sname.lower():
                result += f"\n### 🏛️ {sname} Helplines:\n"
                for service, num in sdetails.items():
                    result += f"📞 **{service}**: {num}\n"
                # Add state women's commission
                if sname in STATE_WOMEN_COMMISSIONS:
                    swc = STATE_WOMEN_COMMISSIONS[sname]
                    result += f"\n🏛️ **{swc['name']}**\n"
                    result += f"   Phone: {swc['phone']}\n"
                    result += f"   Address: {swc['address']}\n"
    else:
        # Show all state-wise numbers
        result += "\n### 🏛️ State-wise Helplines:\n"
        for sname, sdetails in helplines.get("state_wise", {}).items():
            women_hl = sdetails.get("Women Helpline", "181")
            result += f"📍 **{sname}**: {women_hl}\n"

    # Mental health helplines
    result += "\n### 💛 Mental Health Helplines:\n"
    for name, number in helplines["mental_health"].items():
        result += f"📞 **{name}**: {number}\n"

    # One Stop Centre info
    result += f"\n### 🏠 One Stop Centres (Sakhi): {INDIAN_LAWS_DB['one_stop_centres']['total_centres']}\n"
    result += "Call **181** to locate the nearest One Stop Centre in your district.\n"

    return result


def get_cyber_crime_help() -> str:
    """Get information about cyber crime laws and how to report online harassment."""
    cyber = INDIAN_LAWS_DB["cyber_laws"]
    result = f"## 💻 {cyber['title']}\n\n"
    for sec_name, details in cyber["sections"].items():
        result += f"**{sec_name}** — {details['offence']}\n"
        result += f"  ⚖️ Punishment: {details['punishment']}\n"
        result += f"  📋 {details['description']}\n\n"
    result += "### 🚨 How to Report Cyber Crime:\n"
    result += "\n".join(f"→ {step}" for step in cyber["how_to_report"])
    result += "\n\n### ⚠️ IMPORTANT — Preserve Evidence:\n"
    result += "• Take screenshots of ALL harassment (messages, posts, profiles)\n"
    result += "• Save URLs (web addresses) — copy and paste them\n"
    result += "• Note the date, time, username/profile of harasser\n"
    result += "• Do NOT delete anything — evidence is crucial for FIR\n"
    result += "• Record call logs if harassed via calls\n"
    result += "• Save email headers if harassed via email\n"
    return result


def get_constitutional_rights() -> str:
    """Get constitutional rights guaranteed to women in India."""
    cr = INDIAN_LAWS_DB["constitutional_rights"]
    result = f"## 🇮🇳 {cr['title']}\n\n"
    for article, desc in cr["articles"].items():
        result += f"**{article}**: {desc}\n"

    # Add property rights
    pr = INDIAN_LAWS_DB["property_rights"]
    result += f"\n\n## 🏠 {pr['title']}\n\n"
    result += "### Hindu Succession Act 1956 (Amended 2005):\n"
    for point in pr["hindu_law"]["Hindu Succession Act 1956 (Amended 2005)"]:
        result += f"• {point}\n"
    result += "\n### Maintenance Rights:\n"
    for point in pr["maintenance_rights"]:
        result += f"• {point}\n"
    result += "\n### Streedhan (Woman's Own Property):\n"
    for point in pr["streedhan"]:
        result += f"• {point}\n"

    return result


def get_safety_plan() -> str:
    """Provide a comprehensive personal safety plan for women in India."""
    return """## 🛡️ Personal Safety Plan for Women in India

### 🚨 EMERGENCY — If in IMMEDIATE DANGER:
• Dial **112** (ERSS) — works even without network/balance
• Dial **100** (Police) or **181** (Women Helpline)
• Use **112 India App** — SOS button sends location to police
• Press power button 3 times quickly on most smartphones → triggers emergency SOS

### 🏠 At Home:
• Keep important documents safe — Aadhaar, PAN, passport, bank passbooks, marriage certificate, property papers
• Keep photocopies with a trusted person (parent, sibling, friend)
• Have a packed emergency bag: documents, cash (₹5,000-10,000), medicines, clothes, phone charger
• Save emergency numbers on speed dial (181, 100, 112, family members)
• Share live location with 2-3 trusted contacts on WhatsApp (Settings → Privacy → Live Location)
• Know all exits of your home and building
• If facing domestic violence: call 181, approach Protection Officer, or walk into any One Stop Centre

### 🚶 While Travelling:
• Share live location on WhatsApp with family every time you travel
• Avoid isolated areas, especially at night
• Keep phone fully charged; always carry a power bank
• Use verified rides (Ola/Uber) — share trip details with family
• Note auto/taxi/cab number — WhatsApp it to someone before sitting
• Install safety apps: **112 India**, **Shake2Safety**, **My Safetipin**, **Himmat Plus (Delhi Police)**
• In trains: Women-only compartment (Pink coaches), RPF helpline **182**
• In Delhi Metro: First coach reserved for women
• Keep pepper spray / safety alarm in your bag (legal in India)

### 💻 Online Safety:
• Never share phone number, home address, workplace on social media
• Keep all social media profiles PRIVATE
• Enable Two-Factor Authentication (2FA) on WhatsApp, Instagram, Facebook, email
• Use strong, unique passwords — different for every account
• Screenshot and save ALL evidence of harassment immediately
• Block and report harassers on the platform
• File complaint on **cybercrime.gov.in** or call **1930**
• Never meet online strangers alone

### 👔 At Workplace:
• Know your company's POSH policy — ask HR for a copy
• Know your ICC (Internal Complaints Committee) members by name
• Document EVERYTHING — save emails, messages, screenshots, note witnesses
• Report to ICC within 3 months (extendable by 3 more months)
• If no ICC: approach Local Complaints Committee (District Officer)
• You CANNOT be penalised, transferred, or fired for filing a genuine POSH complaint
• Free legal aid available: call NALSA helpline **15100**

### 🏛️ Know Where to Go:
• **Police Station** — File FIR (Zero FIR at ANY station)
• **One Stop Centre (Sakhi)** — Call 181 to find nearest one — free medical, legal, police, counselling, shelter
• **Protection Officer** — District level, for domestic violence cases
• **District Legal Services Authority (DLSA)** — Free lawyer → call 15100
• **National Commission for Women** — ncw.nic.in / call 7827-170-170
• **Mahila Court / Nari Adalat** — Fast-track courts for women's cases
• **Cyber Crime Cell** — cybercrime.gov.in / call 1930

### 💡 General Tips:
• Trust your instincts — if something feels wrong, LEAVE immediately
• Learn basic self-defense (many police stations offer free classes)
• Code word system with family/friends — a secret word that means "I'm in danger, come get me"
• Keep emergency contacts on a paper in your wallet (in case phone is taken)
• Know your rights — you have the legal right to say NO
• NO dowry — demanding/giving dowry is a CRIME
• Your body, your choice — nobody can touch you without your consent
"""


def get_ncw_complaint_process() -> str:
    """Get the complete process to file a complaint with the National Commission for Women."""
    ncw = INDIAN_LAWS_DB["ncw_complaint"]
    result = f"## 🏛️ {ncw['title']}\n\n"
    result += f"📋 {ncw['about']}\n\n"

    result += "### 🌐 Online Complaint (Recommended):\n"
    for step in ncw["online_complaint"]:
        result += f"{step}\n"

    result += "\n### ✉️ Offline Complaint (By Post/In Person):\n"
    for step in ncw["offline_complaint"]:
        result += f"• {step}\n"

    result += "\n### 💪 What NCW Can Do:\n"
    for action in ncw["what_ncw_can_do"]:
        result += f"• {action}\n"

    result += f"\n📞 {ncw['helpline']}\n"
    result += f"🌐 {ncw['website']}\n"
    return result


def get_one_stop_centre_info() -> str:
    """Get information about One Stop Centres (Sakhi Centres) for women."""
    osc = INDIAN_LAWS_DB["one_stop_centres"]
    result = f"## 🏠 {osc['title']}\n\n"
    result += f"📋 {osc['description']}\n\n"

    result += "### 🚪 How to Access:\n"
    for step in osc["how_to_access"]:
        result += f"• {step}\n"

    result += "\n### 🎯 Services Provided (FREE):\n"
    for service in osc["services_provided"]:
        result += f"{service}\n"

    result += f"\n### 📊 {osc['total_centres']}\n"
    result += "Centres by State (count):\n"
    for state, count in osc["centres_by_state"].items():
        result += f"  📍 {state}: {count} centres\n"

    result += f"\n📞 **{osc['helpline']}**\n"
    return result


def get_government_schemes() -> str:
    """Get information about government schemes for women's safety and empowerment in India."""
    schemes_data = INDIAN_LAWS_DB["government_schemes"]
    result = f"## 🇮🇳 {schemes_data['title']}\n\n"

    for name, details in schemes_data["schemes"].items():
        result += f"### 🏛️ {name}\n"
        result += f"  Ministry: {details['ministry']}\n"
        result += f"  About: {details['about']}\n"
        result += "  Benefits:\n"
        for benefit in details["benefits"]:
            result += f"    • {benefit}\n"
        result += "\n"
    return result


def get_landmark_judgments() -> str:
    """Get landmark Supreme Court judgments for women's rights in India."""
    jdata = INDIAN_LAWS_DB["landmark_judgments"]
    result = f"## ⚖️ {jdata['title']}\n\n"

    for case_name, details in jdata["cases"].items():
        result += f"### 📜 {case_name}\n"
        result += f"  About: {details['about']}\n"
        result += f"  Impact: {details['impact']}\n\n"
    return result


def get_womens_property_rights() -> str:
    """Get detailed information about women's property rights in India."""
    pr = INDIAN_LAWS_DB["property_rights"]
    result = f"## 🏠 {pr['title']}\n\n"

    result += "### Hindu Succession Act 1956 (Amended 2005):\n"
    for point in pr["hindu_law"]["Hindu Succession Act 1956 (Amended 2005)"]:
        result += f"• {point}\n"

    result += "\n### Maintenance Rights (All Religions):\n"
    for point in pr["maintenance_rights"]:
        result += f"• {point}\n"

    result += "\n### Streedhan (Woman's Own Property):\n"
    for point in pr["streedhan"]:
        result += f"• {point}\n"
    return result


def get_rights_during_arrest() -> str:
    """Get information about women's rights during arrest and police encounter."""
    data = INDIAN_LAWS_DB["rights_during_arrest"]
    result = f"## 👮 {data['title']}\n\n"
    for right in data["rights"]:
        result += f"• {right}\n"
    return result


def get_workplace_rights() -> str:
    """Get information about workplace rights for women in India and POSH procedure."""
    data = INDIAN_LAWS_DB["workplace_rights"]
    result = f"## 👔 {data['title']}\n\n"

    result += "### Rights:\n"
    for right in data["rights"]:
        result += f"• {right}\n"

    result += "\n### POSH Complaint Process:\n"
    for step in data["posh_process"]:
        result += f"{step}\n"
    return result


def get_state_helpline(state: str) -> str:
    """Get helplines and women's commission contact for a specific Indian state."""
    state_lower = state.strip().lower()
    result = ""

    # State helplines
    state_wise = INDIAN_LAWS_DB["helplines"].get("state_wise", {})
    found = False
    for sname, sdetails in state_wise.items():
        if state_lower in sname.lower():
            found = True
            result += f"## 📞 {sname} — Women's Safety Helplines\n\n"
            for service, num in sdetails.items():
                result += f"📞 **{service}**: {num}\n"

            # State women's commission
            if sname in STATE_WOMEN_COMMISSIONS:
                swc = STATE_WOMEN_COMMISSIONS[sname]
                result += f"\n### 🏛️ {swc['name']}\n"
                result += f"📞 Phone: {swc['phone']}\n"
                result += f"📍 Address: {swc['address']}\n"

            # One Stop Centre count
            osc = INDIAN_LAWS_DB["one_stop_centres"]["centres_by_state"]
            if sname in osc:
                result += f"\n### 🏠 One Stop Centres in {sname}: {osc[sname]} centres\n"
                result += "Call **181** to locate the nearest one.\n"

    if not found:
        result = f"State '{state}' not found. Available states: " + ", ".join(state_wise.keys())
        result += "\n\n📞 Meanwhile, call national helplines: 181 (Women) | 100 (Police) | 112 (Emergency)"

    # Always append national helplines
    result += "\n\n### National Helplines (available everywhere):\n"
    result += "📞 **Women Helpline**: 181\n"
    result += "📞 **Police**: 100\n"
    result += "📞 **Emergency (ERSS)**: 112\n"
    result += "📞 **NCW**: 7827-170-170\n"
    result += "📞 **Cyber Crime**: 1930\n"
    result += "📞 **Legal Aid (NALSA)**: 15100\n"

    return result
