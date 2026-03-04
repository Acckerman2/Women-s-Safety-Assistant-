"""
SheShield AI – Women's Safety Assistant (India)
Single-page Streamlit app with built-in ReAct agent.
"""

import os
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from agent import chat


# ───────────────────────── Page Config ──────────────────────────
st.set_page_config(
    page_title="SheShield AI – Women's Safety | India",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ───────────────────────── Custom CSS ───────────────────────────
st.markdown("""
<style>
/* ── Global ─────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ── Hide default Streamlit ─────────────────────────── */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* ── Gradient Header ────────────────────────────────── */
.hero-header {
    background: linear-gradient(135deg, #ff6b35 0%, #d63384 50%, #6f42c1 100%);
    padding: 2rem 2rem 1.5rem 2rem;
    border-radius: 16px;
    margin-bottom: 1.5rem;
    text-align: center;
    box-shadow: 0 8px 32px rgba(214, 51, 132, 0.25);
}
.hero-header h1 {
    color: white;
    font-size: 2.2rem;
    font-weight: 700;
    margin: 0;
    letter-spacing: -0.5px;
}
.hero-header p {
    color: rgba(255,255,255,0.92);
    font-size: 1.05rem;
    margin-top: 0.5rem;
    font-weight: 300;
}
.hero-header .india-badge {
    display: inline-block;
    background: rgba(255,255,255,0.2);
    padding: 0.2rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    color: white;
    margin-top: 0.5rem;
    font-weight: 500;
}

/* ── Quick Action Cards ─────────────────────────────── */
.quick-actions {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    margin-bottom: 1.5rem;
}
.action-card {
    background: white;
    border: 1px solid #e8e8e8;
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
    transition: all 0.2s ease;
    cursor: pointer;
}
.action-card:hover {
    border-color: #d63384;
    box-shadow: 0 4px 16px rgba(214,51,132,0.15);
    transform: translateY(-2px);
}
.action-card .icon { font-size: 1.6rem; margin-bottom: 0.3rem; }
.action-card .label { font-size: 0.85rem; font-weight: 600; color: #333; }
.action-card .desc { font-size: 0.72rem; color: #888; margin-top: 2px; }

/* ── Chat Messages ──────────────────────────────────── */
.stChatMessage {
    border-radius: 12px !important;
    margin-bottom: 0.6rem !important;
}

/* ── Sidebar ────────────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #fff5f5 0%, #f8f0ff 50%, #fff 100%);
}
.sidebar-card {
    background: white;
    border-radius: 12px;
    padding: 1rem;
    margin-bottom: 0.8rem;
    border: 1px solid #ece3f6;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.sidebar-card h4 { margin: 0 0 0.5rem 0; color: #9b1b30; font-size: 0.95rem; }
.sidebar-card p, .sidebar-card li { font-size: 0.82rem; color: #555; margin: 0.2rem 0; }
.sidebar-card .highlight { color: #d63384; font-weight: 600; }

/* ── Emergency Banner ───────────────────────────────── */
.emergency-banner {
    background: linear-gradient(90deg, #fee2e2, #fecaca);
    border: 2px solid #f87171;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin-bottom: 1rem;
}
.emergency-banner h4 { color: #dc2626; margin: 0 0 0.4rem 0; font-size: 0.95rem; }
.emergency-banner p { color: #991b1b; font-size: 0.85rem; margin: 0.15rem 0; }
.emergency-banner .big-number { font-size: 1.1rem; font-weight: 700; }
</style>
""", unsafe_allow_html=True)

# ───────────────────────── Sidebar ──────────────────────────────
with st.sidebar:
    st.markdown("## 🛡️ SheShield AI")
    st.markdown("*India's Women Safety Assistant*")
    st.markdown("---")

    # Emergency numbers — India only
    st.markdown("""
    <div class="sidebar-card">
        <h4>🚨 Emergency Helplines (India)</h4>
        <p>📞 <b class="highlight">Emergency (ERSS):</b> <b>112</b></p>
        <p>📞 <b class="highlight">Police:</b> <b>100</b></p>
        <p>📞 <b class="highlight">Women Helpline:</b> <b>181</b></p>
        <p>📞 <b>NCW:</b> 7827-170-170</p>
        <p>📞 <b>Cyber Crime:</b> 1930</p>
        <p>📞 <b>Legal Aid (NALSA):</b> 15100</p>
        <p>📞 <b>Domestic Violence:</b> 181</p>
        <p>📞 <b>Railway Police (RPF):</b> 182</p>
        <p>📞 <b>Child Helpline:</b> 1098</p>
    </div>
    """, unsafe_allow_html=True)

    # Mental health helplines
    st.markdown("""
    <div class="sidebar-card">
        <h4>💛 Mental Health Support</h4>
        <p>📞 <b>Vandrevala Foundation:</b> 1860-2662-345</p>
        <p>📞 <b>iCall:</b> 9152987821</p>
        <p>📞 <b>AASRA:</b> 9820466726</p>
        <p>📞 <b>Snehi:</b> 044-24640050</p>
    </div>
    """, unsafe_allow_html=True)

    # Key Laws
    st.markdown("""
    <div class="sidebar-card">
        <h4>⚖️ Key Laws (BNS 2023 / IPC)</h4>
        <p>• <b>BNS 63</b> (IPC 376) – Rape</p>
        <p>• <b>BNS 70</b> – Gang Rape</p>
        <p>• <b>BNS 69</b> – False promise of marriage</p>
        <p>• <b>BNS 74</b> (IPC 354) – Assault on women</p>
        <p>• <b>BNS 75</b> (354A) – Sexual harassment</p>
        <p>• <b>BNS 78</b> (354D) – Stalking</p>
        <p>• <b>BNS 84</b> (498A) – Cruelty by husband</p>
        <p>• <b>BNS 85</b> (304B) – Dowry death</p>
        <p>• <b>BNS 117</b> (326A) – Acid attack</p>
        <p>• <b>POSH Act 2013</b> – Workplace</p>
        <p>• <b>DV Act 2005</b> – Domestic violence</p>
        <p>• <b>POCSO Act 2012</b> – Child safety</p>
    </div>
    """, unsafe_allow_html=True)

    # Safety apps — India
    st.markdown("""
    <div class="sidebar-card">
        <h4>📱 Safety Apps (India)</h4>
        <p>• <b>112 India</b> – ERSS SOS App</p>
        <p>• <b>Himmat Plus</b> – Delhi Police</p>
        <p>• <b>My Safetipin</b> – Safety scores</p>
        <p>• <b>Shake2Safety</b> – Shake to alert</p>
        <p>• <b>Kavalan SOS</b> – Tamil Nadu Police</p>
    </div>
    """, unsafe_allow_html=True)

    # Important websites
    st.markdown("""
    <div class="sidebar-card">
        <h4>🌐 Important Websites</h4>
        <p>• <b>cybercrime.gov.in</b> – Report cyber crime</p>
        <p>• <b>ncw.nic.in</b> – NCW complaints</p>
        <p>• <b>wcd.nic.in</b> – Women & Child Dev.</p>
        <p>• <b>nalsa.gov.in</b> – Free legal aid</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.history = []
        st.rerun()

    st.markdown(
        "<p style='text-align:center; font-size:0.75rem; color:#aaa; margin-top:1rem;'>"
        "Built with ❤️ for women's safety in India<br>"
        "Powered by Mistral AI + LangGraph</p>",
        unsafe_allow_html=True,
    )

# ───────────────────────── Header ───────────────────────────────
st.markdown("""
<div class="hero-header">
    <h1>🛡️ SheShield AI</h1>
    <p>Your trusted AI assistant for women's safety, Indian laws & emergency help</p>
    <span class="india-badge">🇮🇳 Made for Women in India</span>
</div>
""", unsafe_allow_html=True)

# ───────────────────────── Emergency Banner ─────────────────────
st.markdown("""
<div class="emergency-banner">
    <h4>⚠️ In Immediate Danger?</h4>
    <p><span class="big-number">📞 112</span> (Emergency) &nbsp;|&nbsp; <span class="big-number">📞 100</span> (Police) &nbsp;|&nbsp; <span class="big-number">📞 181</span> (Women Helpline)</p>
    <p>📍 Share your live location with a trusted person via WhatsApp. Go to nearest police station or One Stop Centre (Sakhi).</p>
</div>
""", unsafe_allow_html=True)

# ───────────────────────── Helper: call agent directly ──────────
def get_agent_response(message: str) -> str:
    """Call the ReAct agent directly and return the response."""
    try:
        history = st.session_state.get("history", [])
        reply = chat(message, history if history else None)
        # Update history
        st.session_state.history.append(HumanMessage(content=message))
        st.session_state.history.append(AIMessage(content=reply))
        # Keep history manageable (last 20 messages)
        if len(st.session_state.history) > 20:
            st.session_state.history = st.session_state.history[-20:]
        return reply
    except Exception as e:
        return (f"⚠️ An error occurred: {str(e)}\n\n"
                "Meanwhile, here are emergency numbers:\n"
                "- 📞 **Emergency (ERSS)**: 112\n"
                "- 📞 **Police**: 100\n"
                "- 📞 **Women Helpline**: 181\n"
                "- 📞 **NCW**: 7827-170-170\n"
                "- 📞 **Cyber Crime**: 1930")

# ───────────────────────── Session State ────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "history" not in st.session_state:
    st.session_state.history = []

# ───────────────────────── Quick Actions ────────────────────────
QUICK_ACTIONS = [
    ("🚨 Emergency Help", "I am in an emergency situation in India and need immediate help. What should I do? Give me all emergency numbers and steps."),
    ("📜 Indian Laws", "What are the key Indian laws (BNS and IPC) for women's protection? Include sections for rape, harassment, stalking, dowry, domestic violence, and acid attack with punishments."),
    ("⚖️ File FIR", "How do I file an FIR in India? What is the complete process, my rights, and how can I file a Zero FIR?"),
    ("💻 Cyber Crime", "How to report online harassment or cyber crime against women in India? What are the IT Act laws and where do I report?"),
    ("🏛️ NCW Complaint", "How do I file a complaint with the National Commission for Women (NCW)? What is the online and offline process?"),
    ("🏠 One Stop Centre", "What are One Stop Centres (Sakhi Centres)? Where can I find one and what services do they provide?"),
    ("💼 Workplace Safety", "What are my rights under the POSH Act? How do I file a complaint against workplace sexual harassment?"),
    ("📋 Govt Schemes", "What government schemes are available for women's safety and empowerment in India? Include shelter, financial aid, and skill programs."),
    ("🏡 Property Rights", "What are women's property rights in India? Explain Hindu Succession Act, maintenance rights, and Streedhan."),
    ("⚖️ Landmark Cases", "What are the landmark Supreme Court judgments for women's rights in India? Vishaka, Laxmi, Shayara Bano, etc."),
    ("👮 Arrest Rights", "What are my rights if I am being arrested by police? Rules about female officers, timing, and protections."),
    ("🛡️ Safety Plan", "Give me a comprehensive personal safety plan for women in India covering home, travel, online, and workplace safety."),
]

# Only show quick actions if conversation is empty
if not st.session_state.messages:
    st.markdown("#### 💡 How can I help you today?")
    # First row — 3 most important
    cols = st.columns(3)
    for idx in range(3):
        label, prompt = QUICK_ACTIONS[idx]
        with cols[idx]:
            if st.button(label, key=f"qa_{idx}", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.spinner("🛡️ SheShield is thinking..."):
                    response = get_agent_response(prompt)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()

    # Remaining rows — 3 per row
    for row_start in range(3, len(QUICK_ACTIONS), 3):
        cols = st.columns(3)
        for col_idx, qa_idx in enumerate(range(row_start, min(row_start + 3, len(QUICK_ACTIONS)))):
            label, prompt = QUICK_ACTIONS[qa_idx]
            with cols[col_idx]:
                if st.button(label, key=f"qa_{qa_idx}", use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": prompt})
                    with st.spinner("🛡️ SheShield is thinking..."):
                        response = get_agent_response(prompt)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    st.rerun()

    # State selector for state-specific help
    st.markdown("---")
    st.markdown("#### 📍 Get Help for Your State")
    state = st.selectbox(
        "Select your state for local helplines & resources:",
        ["-- Select State --", "Andhra Pradesh", "Assam", "Bihar", "Chhattisgarh",
         "Delhi", "Goa", "Gujarat", "Haryana", "Jharkhand", "Karnataka",
         "Kerala", "Madhya Pradesh", "Maharashtra", "Odisha", "Punjab",
         "Rajasthan", "Tamil Nadu", "Telangana", "Uttar Pradesh", "West Bengal"],
        key="state_selector"
    )
    if state != "-- Select State --":
        if st.button(f"📞 Get {state} Helplines & Resources", use_container_width=True, key="state_btn"):
            prompt = f"Give me all helplines, women's commission contact, and One Stop Centre info for {state}."
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.spinner("🛡️ Fetching state resources..."):
                response = get_agent_response(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

# ───────────────────────── Chat Display ─────────────────────────
for message in st.session_state.messages:
    avatar = "👩" if message["role"] == "user" else "🛡️"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# ───────────────────────── Chat Input ───────────────────────────
if user_input := st.chat_input("Ask about Indian laws, helplines, safety tips... 💬"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="👩"):
        st.markdown(user_input)

    with st.chat_message("assistant", avatar="🛡️"):
        with st.spinner("🛡️ SheShield is thinking..."):
            response = get_agent_response(user_input)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
