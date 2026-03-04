# 🛡️ SheShield AI – Women's Safety Assistant (India)

A professional AI-powered chatbot built to help women in India with **Indian laws (BNS/IPC), emergency helplines, government schemes, NCW complaints, One Stop Centres, property rights, workplace safety (POSH), and comprehensive safety plans**.

Built with a **ReAct Agent** architecture — the AI reasons about your query, looks up actual Indian laws from a built-in knowledge base of **19 BNS sections, 10 special acts, cyber laws, 12 government schemes, 9 landmark Supreme Court judgments, and state-wise helplines for 20 states**, then provides verified, actionable responses.

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40-red?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-0.3-green)
![LangGraph](https://img.shields.io/badge/LangGraph-ReAct_Agent-purple)
![Mistral AI](https://img.shields.io/badge/Mistral_AI-LLM-orange)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **ReAct Agent (14 Tools)** | LangGraph ReAct loop with 14 specialised tools for Indian women's safety |
| 📜 **Indian Laws DB** | BNS 2023 (19 sections), IPC, POSH, DV Act, POCSO, Cyber laws, Constitutional rights |
| 🚨 **Emergency Help** | National + state-wise helplines for 20 states, mental health helplines |
| 🏠 **One Stop Centres** | Info on 700+ Sakhi Centres — free medical, legal, police, shelter, counselling |
| 🏛️ **NCW Complaints** | Complete online/offline process to file complaint with National Commission for Women |
| ⚖️ **FIR Filing Guide** | Step-by-step process with Zero FIR rights, women's rights during filing |
| 📋 **Government Schemes** | 12 schemes — Beti Bachao Beti Padhao, Ujjawala, Swadhar Greh, and more |
| ⚖️ **Landmark Judgments** | 9 Supreme Court landmark cases — Vishaka, Laxmi, Shayara Bano, etc. |
| 🏡 **Property Rights** | Hindu Succession Act, maintenance, Streedhan |
| 👮 **Arrest Rights** | Women's rights during arrest and police encounter |
| 👔 **Workplace Safety** | POSH Act process, ICC complaints, employer obligations |
| 💻 **Cyber Crime** | IT Act sections, cybercrime.gov.in, evidence preservation guide |
| 📍 **State-wise Resources** | Helplines, women's commissions, One Stop Centres for 20 states |
| 🛡️ **Safety Planning** | India-specific safety plan — 112 India app, Sakhi Centres, code words, and more |
| 📡 **FastAPI Backend** | REST API with session management, CORS, health checks |
| 🎨 **Professional UI** | India-themed Streamlit interface with 12 quick actions + state selector |
| 🌐 **Render Ready** | Separate services for API and UI, auto-deploy from GitHub |

---

## 🏗️ Architecture

```
┌─────────────────┐     HTTP/JSON     ┌──────────────────────────────────┐
│   Streamlit UI  │ ◄──────────────► │        FastAPI Backend           │
│   (app.py)      │    /chat API      │         (api.py)                 │
└─────────────────┘                   └──────────┬───────────────────────┘
                                                 │
                                      ┌──────────▼───────────────────────┐
                                      │     LangGraph ReAct Agent        │
                                      │         (agent.py)               │
                                      │                                  │
                                      │  ┌─────────┐   ┌─────────────┐  │
                                      │  │  Agent   │──►│  Tool Node  │  │
                                      │  │ (Mistral)│◄──│             │  │
                                      │  └─────────┘   └──────┬──────┘  │
                                      │                        │         │
                                      └────────────────────────┼─────────┘
                                                               │
                                      ┌────────────────────────▼─────────┐
                                      │      Indian Laws Knowledge Base  │
                                      │        (indian_laws.py)          │
                                      │                                  │
                                      │  • BNS 2023 Sections (19)         │
                                      │  • Special Acts (10 acts)          │
                                      │  • Cyber Laws (IT Act)             │
                                      │  • FIR Filing Process              │
                                      │  • Constitutional Rights           │
                                      │  • Helplines (National + 20 States)│
                                      │  • One Stop Centres (Sakhi)        │
                                      │  • NCW Complaint Process           │
                                      │  • Government Schemes (12)         │
                                      │  • Landmark Judgments (9)          │
                                      │  • Property Rights                 │
                                      │  • Arrest Rights                   │
                                      │  • Workplace Rights (POSH)         │
                                      │  • State Women Commissions (21)    │
                                      │  • Safety Plans                    │
                                      └──────────────────────────────────┘
```

**ReAct Loop**: Agent → (thinks) → calls tool(s) → gets data → (thinks again) → responds to user

---

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone <your-repo-url>
cd demo-project
pip install -r requirements.txt
```

### 2. Set API Key

```bash
cp .env.example .env
# Edit .env → add your Mistral API key from https://console.mistral.ai/
```

### 3. Run (Easy Way)

```bash
python start.py
```

This starts **both** FastAPI (port 8000) and Streamlit (port 8501) together.

### 3b. Run (Manual)

```bash
# Terminal 1: FastAPI backend
uvicorn api:app --reload --port 8000

# Terminal 2: Streamlit frontend
streamlit run app.py
```

### 4. Open

- **Frontend**: http://localhost:8501
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Service info |
| `GET` | `/health` | Health check |
| `POST` | `/chat` | Send message, get AI response |
| `DELETE` | `/session/{id}` | Clear session history |
| `GET` | `/sessions/count` | Active session count |

### Example API Call

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What are the laws against stalking in India?"}'
```

---

## 🌐 Deploy to Render

1. Push to **GitHub**.
2. Go to [render.com](https://render.com) → **New** → **Blueprint**.
3. Connect your GitHub repo — Render detects `render.yaml` automatically.
4. It creates 2 services:
   - **sheshield-api** — FastAPI backend
   - **sheshield-ui** — Streamlit frontend
5. Add `MISTRAL_API_KEY` to the **sheshield-api** service environment variables.
6. Update `API_URL` in **sheshield-ui** to point to your API service URL.
7. Deploy 🚀

---

## 📁 Project Structure

```
demo-project/
├── .streamlit/
│   └── config.toml           # Streamlit theme & server config
├── agent.py                   # LangGraph ReAct agent with tools
├── api.py                     # FastAPI backend with session management
├── app.py                     # Streamlit frontend (connects to FastAPI)
├── indian_laws.py             # Indian laws knowledge base & tool functions
├── start.py                   # Launch both servers together
├── requirements.txt           # Python dependencies
├── render.yaml                # Render Blueprint (2 services)
├── .env.example               # Environment variable template
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

---

## 🔑 Environment Variables

| Variable | Where | Description |
|----------|-------|-------------|
| `MISTRAL_API_KEY` | API server | Mistral AI API key |
| `API_URL` | Streamlit | FastAPI backend URL (default: `http://localhost:8000`) |

---

## 📜 Indian Laws Covered

### BNS 2023 (Bharatiya Nyaya Sanhita) — 19 Sections
| BNS Section | Old IPC | Offence |
|-------------|---------|---------|
| Section 63 | 376 | Rape |
| Section 64 | 376(2) | Aggravated rape |
| Section 65 | 376AB | Rape on child under 12 |
| Section 66 | 376DA | Gang rape on minor |
| Section 69 | New | False promise of marriage |
| Section 70 | 376D | Gang rape |
| Section 74 | 354 | Assault to outrage modesty |
| Section 75 | 354A | Sexual harassment |
| Section 76 | 354B | Assault to disrobe |
| Section 77 | 354C | Voyeurism |
| Section 78 | 354D | Stalking |
| Section 84 | 498A | Cruelty by husband |
| Section 85 | 304B | Dowry death |
| Section 87 | 363/366 | Kidnapping woman |
| Section 95 | 509 | Insult to modesty |
| Section 117 | 326A | Acid attack |
| Section 296 | New | Bigamy |
| Section 302 | 356 | Snatching |

### Special Acts (10)
- Protection of Women from Domestic Violence Act 2005
- Sexual Harassment at Workplace (POSH) Act 2013
- Dowry Prohibition Act 1961
- POCSO Act 2012
- Immoral Traffic Prevention Act 1956
- Muslim Women Protection Act 2019
- Maternity Benefit Act 1961 (amended 2017)
- Equal Remuneration Act 1976
- Hindu Succession Act 1956 (amended 2005)
- Pre-Conception and Pre-Natal Diagnostic Techniques (PCPNDT) Act 1994

### Cyber Laws
- IT Act Sections 66E, 67, 67A, 67B
- Cyber Crime Reporting: cybercrime.gov.in / Helpline 1930

### Government Schemes (12)
- Beti Bachao Beti Padhao (BBBP)
- One Stop Centre (Sakhi)
- Swadhar Greh (shelter)
- Ujjawala (anti-trafficking)
- Mahila Shakti Kendra
- Working Women Hostel
- Nari Adalat
- STEP (Support to Training & Employment)
- Mahila Police Volunteers
- Nirbhaya Fund
- Sukanya Samriddhi Yojana
- PM Matru Vandana Yojana

### Landmark Supreme Court Judgments (9)
- Vishaka v. State of Rajasthan (workplace harassment)
- Laxmi v. Union of India (acid attack)
- Shayara Bano v. Union of India (triple talaq)
- Joseph Shine v. Union of India (adultery)
- Independent Thought v. Union of India (child marriage/rape)
- Sakshi v. Union of India (child sexual abuse)
- Navtej Singh Johar v. Union of India (bodily autonomy)
- Indian Young Lawyers Assn v. State of Kerala (Sabarimala)
- D.K. Basu v. State of West Bengal (arrest rights)

### State Coverage
- **Helplines**: 20 states with dedicated women helplines
- **Women's Commissions**: 21 state women commission contacts
- **One Stop Centres**: 700+ centres across India

---

## 📞 Emergency Helplines

| Service | Number |
|---------|--------|
| Women Helpline | 181 |
| Police | 100 |
| Emergency (ERSS) | 112 |
| NCW | 7827-170-170 |
| Cyber Crime | 1930 |
| Child Helpline | 1098 |
| Legal Aid (NALSA) | 15100 |
| iCall (Mental Health) | 9152987821 |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| LLM | Mistral AI (`mistral-large-latest`) |
| Agent | LangGraph ReAct Agent + LangChain Tools |
| Backend | FastAPI + Uvicorn |
| Frontend | Streamlit |
| Knowledge Base | Python (indian_laws.py) |
| Deployment | Render Blueprint |

---

## 📄 License

MIT License – Free to use and modify.

---

> *Built with ❤️ for women's safety and empowerment.*
