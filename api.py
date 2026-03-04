"""
SheShield AI – FastAPI Backend with built-in Chat UI.

Serves a full HTML chat interface at "/" and REST API at /chat.
Single service — no separate frontend needed.
"""

from __future__ import annotations

import os
import uuid
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage

from agent import chat

load_dotenv()

# ──────────────────────────── App ──────────────────────────────
app = FastAPI(
    title="SheShield AI API",
    description="Women's Safety Assistant API powered by Mistral AI + LangGraph ReAct Agent",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS — allow any frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ──────────────────────── In-memory sessions ───────────────────
sessions: dict[str, list[BaseMessage]] = {}


# ──────────────────────── Schemas ──────────────────────────────
class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=5000, description="User message")
    session_id: Optional[str] = Field(None, description="Session ID for conversation continuity")


class ChatResponse(BaseModel):
    reply: str
    session_id: str


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


# ──────────────────────── HTML Chat UI ─────────────────────────

CHAT_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SheShield AI – Women's Safety | India</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🛡️</text></svg>">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;background:#f5f3ff;color:#333;display:flex;height:100vh;overflow:hidden}

/* Sidebar */
.sidebar{width:300px;background:linear-gradient(180deg,#fff5f5 0%,#f8f0ff 50%,#fff 100%);border-right:1px solid #ece3f6;overflow-y:auto;padding:1.2rem;flex-shrink:0}
.sidebar h2{font-size:1.3rem;color:#9b1b30;margin-bottom:0.2rem}
.sidebar .sub{font-size:0.8rem;color:#888;margin-bottom:1rem;font-style:italic}
.sidebar hr{border:none;border-top:1px solid #ece3f6;margin:0.8rem 0}
.s-card{background:#fff;border:1px solid #ece3f6;border-radius:12px;padding:0.9rem;margin-bottom:0.7rem;box-shadow:0 2px 6px rgba(0,0,0,0.03)}
.s-card h4{color:#9b1b30;font-size:0.88rem;margin-bottom:0.4rem}
.s-card p{font-size:0.78rem;color:#555;margin:0.15rem 0;line-height:1.4}
.s-card .hl{color:#d63384;font-weight:600}

/* Main */
.main{flex:1;display:flex;flex-direction:column;min-width:0}

/* Header */
.hero{background:linear-gradient(135deg,#ff6b35 0%,#d63384 50%,#6f42c1 100%);padding:1.3rem 1.5rem 1rem;text-align:center;flex-shrink:0}
.hero h1{color:#fff;font-size:1.8rem;font-weight:700}
.hero p{color:rgba(255,255,255,0.92);font-size:0.95rem;margin-top:0.3rem;font-weight:300}
.hero .badge{display:inline-block;background:rgba(255,255,255,0.2);padding:0.15rem 0.7rem;border-radius:20px;font-size:0.75rem;color:#fff;margin-top:0.4rem;font-weight:500}

/* Emergency banner */
.emergency{background:linear-gradient(90deg,#fee2e2,#fecaca);border:2px solid #f87171;border-radius:12px;padding:0.8rem 1rem;margin:0.8rem 1rem 0;flex-shrink:0}
.emergency h4{color:#dc2626;font-size:0.88rem;margin-bottom:0.3rem}
.emergency p{color:#991b1b;font-size:0.82rem;margin:0.1rem 0}
.emergency .big{font-size:1rem;font-weight:700}

/* Quick actions */
.quick-wrap{padding:0.8rem 1rem 0;flex-shrink:0}
.quick-wrap h3{font-size:0.95rem;color:#555;margin-bottom:0.5rem}
.quick-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.q-btn{background:#fff;border:1px solid #e0d4f5;border-radius:10px;padding:0.55rem 0.4rem;text-align:center;cursor:pointer;transition:all 0.2s;font-size:0.72rem;font-weight:600;color:#444;font-family:'Inter',sans-serif}
.q-btn:hover{border-color:#d63384;box-shadow:0 3px 12px rgba(214,51,132,0.12);transform:translateY(-1px)}
.q-btn .ico{font-size:1.2rem;display:block;margin-bottom:0.2rem}

/* Chat area */
.chat-area{flex:1;overflow-y:auto;padding:1rem;display:flex;flex-direction:column;gap:0.7rem}
.msg{max-width:85%;padding:0.8rem 1rem;border-radius:14px;font-size:0.88rem;line-height:1.55;word-wrap:break-word}
.msg.user{align-self:flex-end;background:linear-gradient(135deg,#d63384,#6f42c1);color:#fff;border-bottom-right-radius:4px}
.msg.bot{align-self:flex-start;background:#fff;color:#333;border:1px solid #e8e8e8;border-bottom-left-radius:4px;box-shadow:0 1px 4px rgba(0,0,0,0.04)}
.msg.bot h1,.msg.bot h2,.msg.bot h3{font-size:1rem;color:#9b1b30;margin:0.5rem 0 0.3rem}
.msg.bot h4,.msg.bot h5{font-size:0.92rem;color:#6f42c1;margin:0.4rem 0 0.2rem}
.msg.bot strong{color:#d63384}
.msg.bot ul,.msg.bot ol{margin:0.3rem 0 0.3rem 1.2rem}
.msg.bot li{margin:0.15rem 0}
.msg.bot code{background:#f3f0ff;padding:0.1rem 0.3rem;border-radius:4px;font-size:0.82rem}
.msg.bot hr{border:none;border-top:1px solid #eee;margin:0.5rem 0}
.msg.bot p{margin:0.3rem 0}
.typing{align-self:flex-start;background:#fff;border:1px solid #e8e8e8;border-radius:14px;padding:0.8rem 1.2rem;display:none}
.typing .dots{display:inline-flex;gap:4px}
.typing .dots span{width:8px;height:8px;background:#d63384;border-radius:50%;animation:bounce 1.4s infinite}
.typing .dots span:nth-child(2){animation-delay:0.2s}
.typing .dots span:nth-child(3){animation-delay:0.4s}
@keyframes bounce{0%,80%,100%{transform:translateY(0)}40%{transform:translateY(-8px)}}

/* Input */
.input-bar{padding:0.8rem 1rem;background:#fff;border-top:1px solid #eee;display:flex;gap:0.5rem;flex-shrink:0}
.input-bar input{flex:1;border:1.5px solid #e0d4f5;border-radius:12px;padding:0.7rem 1rem;font-size:0.9rem;font-family:'Inter',sans-serif;outline:none;transition:border 0.2s}
.input-bar input:focus{border-color:#d63384}
.input-bar button{background:linear-gradient(135deg,#d63384,#6f42c1);color:#fff;border:none;border-radius:12px;padding:0.7rem 1.3rem;font-size:0.9rem;font-weight:600;cursor:pointer;font-family:'Inter',sans-serif;transition:transform 0.1s}
.input-bar button:hover{transform:scale(1.03)}
.input-bar button:disabled{opacity:0.5;cursor:not-allowed}

/* Mobile */
@media(max-width:768px){
    .sidebar{display:none}
    .quick-grid{grid-template-columns:repeat(2,1fr)}
    .hero h1{font-size:1.4rem}
    .msg{max-width:95%}
}
</style>
<!-- Markdown rendering -->
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
</head>
<body>

<!-- Sidebar -->
<div class="sidebar">
    <h2>🛡️ SheShield AI</h2>
    <p class="sub">India's Women Safety Assistant</p>
    <hr>
    <div class="s-card">
        <h4>🚨 Emergency Helplines</h4>
        <p>📞 <span class="hl">Emergency (ERSS):</span> <b>112</b></p>
        <p>📞 <span class="hl">Police:</span> <b>100</b></p>
        <p>📞 <span class="hl">Women Helpline:</span> <b>181</b></p>
        <p>📞 <b>NCW:</b> 7827-170-170</p>
        <p>📞 <b>Cyber Crime:</b> 1930</p>
        <p>📞 <b>Legal Aid (NALSA):</b> 15100</p>
        <p>📞 <b>Railway Police:</b> 182</p>
        <p>📞 <b>Child Helpline:</b> 1098</p>
    </div>
    <div class="s-card">
        <h4>💛 Mental Health</h4>
        <p>📞 <b>Vandrevala:</b> 1860-2662-345</p>
        <p>📞 <b>iCall:</b> 9152987821</p>
        <p>📞 <b>AASRA:</b> 9820466726</p>
    </div>
    <div class="s-card">
        <h4>⚖️ Key Laws (BNS 2023)</h4>
        <p>• <b>BNS 63</b> (IPC 376) – Rape</p>
        <p>• <b>BNS 70</b> – Gang Rape</p>
        <p>• <b>BNS 75</b> (354A) – Harassment</p>
        <p>• <b>BNS 78</b> (354D) – Stalking</p>
        <p>• <b>BNS 84</b> (498A) – Cruelty</p>
        <p>• <b>BNS 85</b> (304B) – Dowry death</p>
        <p>• <b>BNS 117</b> (326A) – Acid attack</p>
        <p>• <b>POSH Act 2013</b> – Workplace</p>
        <p>• <b>DV Act 2005</b> – Domestic violence</p>
    </div>
    <div class="s-card">
        <h4>📱 Safety Apps</h4>
        <p>• <b>112 India</b> – ERSS SOS</p>
        <p>• <b>Himmat Plus</b> – Delhi Police</p>
        <p>• <b>My Safetipin</b> – Safety scores</p>
        <p>• <b>Shake2Safety</b> – Shake to alert</p>
    </div>
    <div class="s-card">
        <h4>🌐 Important Websites</h4>
        <p>• <b>cybercrime.gov.in</b></p>
        <p>• <b>ncw.nic.in</b></p>
        <p>• <b>nalsa.gov.in</b></p>
    </div>
    <hr>
    <p style="text-align:center;font-size:0.72rem;color:#aaa;margin-top:0.5rem">Built with ❤️ for women's safety<br>Mistral AI + LangGraph</p>
</div>

<!-- Main content -->
<div class="main">
    <div class="hero">
        <h1>🛡️ SheShield AI</h1>
        <p>Your trusted AI assistant for women's safety, Indian laws &amp; emergency help</p>
        <span class="badge">🇮🇳 Made for Women in India</span>
    </div>

    <div class="emergency">
        <h4>⚠️ In Immediate Danger?</h4>
        <p><span class="big">📞 112</span> (Emergency) &nbsp;|&nbsp; <span class="big">📞 100</span> (Police) &nbsp;|&nbsp; <span class="big">📞 181</span> (Women Helpline)</p>
    </div>

    <div class="quick-wrap" id="quickWrap">
        <h3>💡 How can I help you today?</h3>
        <div class="quick-grid">
            <div class="q-btn" onclick="sendQuick('I am in an emergency situation in India. What should I do? Give me all emergency numbers and steps.')"><span class="ico">🚨</span>Emergency</div>
            <div class="q-btn" onclick="sendQuick('What are the key Indian laws (BNS and IPC) for women\\'s protection? Include sections for rape, harassment, stalking, dowry, domestic violence with punishments.')"><span class="ico">📜</span>Indian Laws</div>
            <div class="q-btn" onclick="sendQuick('How do I file an FIR in India? Complete process, my rights, and Zero FIR.')"><span class="ico">⚖️</span>File FIR</div>
            <div class="q-btn" onclick="sendQuick('How to report cyber crime against women in India? IT Act laws and where to report?')"><span class="ico">💻</span>Cyber Crime</div>
            <div class="q-btn" onclick="sendQuick('How do I file a complaint with the National Commission for Women (NCW)?')"><span class="ico">🏛️</span>NCW Complaint</div>
            <div class="q-btn" onclick="sendQuick('What are One Stop Centres (Sakhi Centres)? Services and how to find one?')"><span class="ico">🏠</span>One Stop Centre</div>
            <div class="q-btn" onclick="sendQuick('What are my rights under the POSH Act? How to file a workplace harassment complaint?')"><span class="ico">💼</span>Workplace Safety</div>
            <div class="q-btn" onclick="sendQuick('What government schemes are available for women in India? Shelter, financial aid, skill programs.')"><span class="ico">📋</span>Govt Schemes</div>
        </div>
    </div>

    <div class="chat-area" id="chatArea"></div>
    <div class="typing" id="typing"><div class="dots"><span></span><span></span><span></span></div></div>

    <div class="input-bar">
        <input type="text" id="msgInput" placeholder="Ask about Indian laws, helplines, safety tips... 💬" onkeydown="if(event.key==='Enter')sendMsg()">
        <button id="sendBtn" onclick="sendMsg()">Send ➤</button>
    </div>
</div>

<script>
let sessionId = null;
const chatArea = document.getElementById('chatArea');
const typing = document.getElementById('typing');
const msgInput = document.getElementById('msgInput');
const sendBtn = document.getElementById('sendBtn');
const quickWrap = document.getElementById('quickWrap');

function addMsg(text, role) {
    const div = document.createElement('div');
    div.className = 'msg ' + role;
    if (role === 'bot') {
        div.innerHTML = marked.parse(text);
    } else {
        div.textContent = text;
    }
    chatArea.appendChild(div);
    chatArea.scrollTop = chatArea.scrollHeight;
}

function setLoading(on) {
    typing.style.display = on ? 'block' : 'none';
    sendBtn.disabled = on;
    if (on) chatArea.scrollTop = chatArea.scrollHeight;
}

async function sendQuick(text) {
    quickWrap.style.display = 'none';
    await doSend(text);
}

async function sendMsg() {
    const text = msgInput.value.trim();
    if (!text) return;
    msgInput.value = '';
    quickWrap.style.display = 'none';
    await doSend(text);
}

async function doSend(text) {
    addMsg(text, 'user');
    setLoading(true);
    try {
        const res = await fetch('/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message: text, session_id: sessionId})
        });
        const data = await res.json();
        if (res.ok) {
            sessionId = data.session_id;
            addMsg(data.reply, 'bot');
        } else {
            addMsg('⚠️ Error: ' + (data.detail || 'Something went wrong'), 'bot');
        }
    } catch (e) {
        addMsg('⚠️ Network error. Emergency numbers: 112 (ERSS) | 100 (Police) | 181 (Women Helpline)', 'bot');
    }
    setLoading(false);
    msgInput.focus();
}
</script>
</body>
</html>"""


# ──────────────────────── Routes ───────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the chat UI."""
    return CHAT_HTML


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check for Render / monitoring."""
    return HealthResponse(
        status="healthy",
        service="SheShield AI API",
        version="2.0.0",
    )


@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Send a message to SheShield AI and get a response.

    - Creates a new session if `session_id` is not provided.
    - Maintains conversation history within a session.
    """
    # Get or create session
    session_id = request.session_id or str(uuid.uuid4())
    history = sessions.get(session_id, [])

    try:
        # Call the ReAct agent
        reply = chat(request.message, history if history else None)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Agent error: {str(e)}",
        )

    # Update session history
    history.append(HumanMessage(content=request.message))
    history.append(AIMessage(content=reply))
    sessions[session_id] = history

    # Limit history to last 20 messages to prevent memory issues
    if len(sessions[session_id]) > 20:
        sessions[session_id] = sessions[session_id][-20:]

    return ChatResponse(reply=reply, session_id=session_id)


@app.delete("/session/{session_id}")
async def clear_session(session_id: str):
    """Clear conversation history for a session."""
    if session_id in sessions:
        del sessions[session_id]
        return {"status": "cleared", "session_id": session_id}
    return {"status": "not_found", "session_id": session_id}


@app.get("/sessions/count")
async def session_count():
    """Get active session count (admin/monitoring)."""
    return {"active_sessions": len(sessions)}
