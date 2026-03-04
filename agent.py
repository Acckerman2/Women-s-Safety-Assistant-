"""
SheShield AI – ReAct Agent powered by LangGraph + Mistral AI.

This module builds a ReAct (Reason + Act) agent that:
1. Reasons about the user's query.
2. Uses specialised tools (law lookup, FIR process, helplines, safety plans, etc.).
3. Synthesises tool outputs into empathetic, actionable responses.
"""

from __future__ import annotations

import os
import uuid
from typing import TypedDict, Annotated, Sequence

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool
from langchain_mistralai import ChatMistralAI
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from indian_laws import (
    lookup_indian_law,
    get_fir_process,
    get_emergency_contacts,
    get_cyber_crime_help,
    get_constitutional_rights,
    get_safety_plan,
    get_ncw_complaint_process,
    get_one_stop_centre_info,
    get_government_schemes,
    get_landmark_judgments,
    get_womens_property_rights as _get_property_rights,
    get_rights_during_arrest,
    get_workplace_rights,
    get_state_helpline,
)

load_dotenv()

# ──────────────────────────────  LLM  ──────────────────────────────
def get_llm():
    """Return a Mistral chat model instance."""
    return ChatMistralAI(
        model="mistral-large-latest",
        mistral_api_key=os.getenv("MISTRAL_API_KEY", ""),
        temperature=0.3,
        max_tokens=4096,
    )


# ──────────────────────────────  Tools  ────────────────────────────

@tool
def search_indian_law(query: str) -> str:
    """Search Indian laws database for laws related to women's safety.
    Use this tool when the user asks about any law, legal right, IPC section,
    BNS section, or legal protection related to women's safety in India.
    Input should be keywords like 'rape', 'stalking', 'harassment', 'dowry',
    'domestic violence', 'cyber crime', 'acid attack', 'workplace',
    'kidnapping', 'modesty', 'marriage', 'divorce', 'property', 'child', etc."""
    return lookup_indian_law(query)


@tool
def get_fir_filing_guide() -> str:
    """Get the complete step-by-step guide for filing an FIR (First Information Report)
    in India. Also includes the NCW complaint process as an alternative.
    Use this when user asks about filing a police complaint, FIR process,
    or how to report a crime to police or NCW."""
    return get_fir_process()


@tool
def get_helpline_numbers(state: str = "") -> str:
    """Get emergency helpline numbers for women in India.
    Includes national helplines, mental health helplines, and state-wise numbers.
    Pass a state name (e.g. 'Maharashtra', 'Delhi', 'Karnataka') to get
    state-specific helplines, women's commission contact, and One Stop Centre count.
    Leave state empty for all-India numbers."""
    return get_emergency_contacts(state)


@tool
def get_cyber_crime_info() -> str:
    """Get information about cyber crime laws under IT Act and how to report
    online harassment, morphing, revenge porn, cyber stalking, or any
    online offence against women. Includes evidence preservation tips.
    Use this when user asks about online harassment or digital safety."""
    return get_cyber_crime_help()


@tool
def get_womens_constitutional_rights() -> str:
    """Get fundamental and constitutional rights guaranteed to women under the
    Indian Constitution. Also includes property rights (Hindu Succession Act,
    maintenance, Streedhan). Use when user asks about fundamental rights,
    equality, constitutional protections, or property rights."""
    return get_constitutional_rights()


@tool
def get_personal_safety_plan() -> str:
    """Get a comprehensive personal safety plan for women in India covering
    home safety, travel safety, online safety, workplace safety, and general tips.
    Includes India-specific advice (112 India app, One Stop Centres, POSH, etc.).
    Use when user asks about safety planning, prevention, or personal protection."""
    return get_safety_plan()


@tool
def get_ncw_complaint_info() -> str:
    """Get the complete process to file a complaint with the National Commission
    for Women (NCW). Includes online and offline process, what NCW can do,
    and contact details. Use when user asks about NCW or wants to escalate
    a complaint beyond police."""
    return get_ncw_complaint_process()


@tool
def get_one_stop_centres() -> str:
    """Get information about One Stop Centres (Sakhi Centres) — government-run
    centres that provide FREE medical aid, legal aid, police assistance,
    counselling, and shelter to women in distress. Available in every district.
    Use when user needs immediate multi-service support or shelter."""
    return get_one_stop_centre_info()


@tool
def get_govt_schemes_for_women() -> str:
    """Get information about government schemes for women's safety and empowerment
    in India. Includes Beti Bachao Beti Padhao, One Stop Centre (Sakhi),
    Swadhar Greh, Ujjawala, Mahila Shakti Kendra, Working Women Hostel,
    and more. Use when user asks about financial aid, shelter, or government support."""
    return get_government_schemes()


@tool
def get_landmark_court_judgments() -> str:
    """Get landmark Supreme Court of India judgments on women's rights.
    Includes Vishaka (sexual harassment guidelines), Laxmi (acid attack),
    Shayara Bano (triple talaq), and more. Use when user asks about
    important court decisions or legal precedents for women's rights."""
    return get_landmark_judgments()


@tool
def get_property_rights_info() -> str:
    """Get detailed information about women's property rights in India.
    Covers Hindu Succession Act 2005 amendment (equal coparcenary rights),
    maintenance under CrPC, and Streedhan rights.
    Use when user asks about inheritance, property, maintenance, or Streedhan."""
    return _get_property_rights()


@tool
def get_arrest_rights() -> str:
    """Get information about women's rights during arrest and police encounter.
    Includes rules about female officers, timing, medical examination,
    and legal protections. Use when user or someone they know is being arrested
    or has faced police misconduct."""
    return get_rights_during_arrest()


@tool
def get_workplace_safety_info() -> str:
    """Get information about workplace rights for women in India and the
    POSH (Prevention of Sexual Harassment) Act complaint process.
    Includes ICC process, employer obligations, and legal remedies.
    Use when user faces workplace harassment or has POSH-related questions."""
    return get_workplace_rights()


@tool
def get_state_specific_helpline(state: str) -> str:
    """Get detailed helplines, women's commission contact, and One Stop Centre
    info for a specific Indian state. Input should be the state name like
    'Maharashtra', 'Delhi', 'Tamil Nadu', 'West Bengal', 'Uttar Pradesh', etc.
    Use when user mentions a specific state or needs local resources."""
    return get_state_helpline(state)


# Collect all tools
tools = [
    search_indian_law,
    get_fir_filing_guide,
    get_helpline_numbers,
    get_cyber_crime_info,
    get_womens_constitutional_rights,
    get_personal_safety_plan,
    get_ncw_complaint_info,
    get_one_stop_centres,
    get_govt_schemes_for_women,
    get_landmark_court_judgments,
    get_property_rights_info,
    get_arrest_rights,
    get_workplace_safety_info,
    get_state_specific_helpline,
]


# ──────────────────────────────  State  ────────────────────────────
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


# ──────────────────────────────  System Prompt  ────────────────────

SYSTEM_PROMPT = """You are **SheShield AI** 🛡️ — India's advanced women's safety assistant specialising in Indian law, women's rights, and protection mechanisms.

## Your Mission:
Help women in India understand their legal rights, access helplines, file complaints, find government support, and stay safe — with accurate, verified, empathetic guidance.

## Your Capabilities — 14 Specialised Tools:
You have access to the following tools. **ALWAYS use the appropriate tools** to provide accurate, verified information. Do NOT rely on memory alone for legal sections or helpline numbers — use the tools.

## When to use each tool:
- **search_indian_law**: Any question about specific laws, IPC/BNS sections, legal punishments, women's rights under specific acts (dowry, POSH, DV Act, POCSO, trafficking, marriage laws, etc.)
- **get_fir_filing_guide**: Filing FIR, police complaint, reporting a crime, Zero FIR, NCW complaint process
- **get_helpline_numbers**: Emergency contacts, helplines, support organizations. Pass a state name for state-specific numbers
- **get_cyber_crime_info**: Online harassment, morphing, revenge porn, cyber stalking, digital threats, OTP fraud
- **get_womens_constitutional_rights**: Fundamental rights, equality, constitutional protections, property rights
- **get_personal_safety_plan**: Safety tips, self-defense advice, prevention strategies, emergency preparedness
- **get_ncw_complaint_info**: Filing complaint with National Commission for Women (NCW), escalation beyond police
- **get_one_stop_centres**: Information about Sakhi Centres — free medical, legal, police, shelter, counselling services
- **get_govt_schemes_for_women**: Government schemes — Beti Bachao Beti Padhao, Ujjawala, Swadhar Greh, financial aid, scholarships
- **get_landmark_court_judgments**: Landmark Supreme Court judgments — Vishaka, Laxmi, Shayara Bano, etc.
- **get_property_rights_info**: Property rights — Hindu Succession Act, maintenance, Streedhan, inheritance
- **get_arrest_rights**: Women's rights during arrest — female officers, timing restrictions, medical exam rules
- **get_workplace_safety_info**: Workplace rights, POSH Act, ICC process, employer obligations
- **get_state_specific_helpline**: State-specific helplines, state women's commission, and One Stop Centre info

## Response Guidelines:
1. **ALWAYS use tools first** before responding to any legal, safety, or helpline question. Use MULTIPLE tools if the question spans multiple areas.
2. Be **empathetic, warm, and non-judgmental**. Never blame the victim. Use reassuring language.
3. Provide **actionable steps** — tell them exactly what to do, step by step.
4. Include **relevant BNS sections (new) and IPC sections (old)** with punishments when discussing legal matters.
5. **ALWAYS** include at minimum these helplines: Women Helpline 181, Police 100, Emergency 112.
6. For emergencies, prioritise **immediate safety** above EVERYTHING — first step is always "Call 112 NOW".
7. Use **clear formatting** with emojis, bold text, numbered lists, and headers.
8. If the user mentions a specific **state**, use get_state_specific_helpline to provide local resources.
9. If the user's situation is unclear, ask clarifying questions — but still provide general guidance while asking.
10. For greetings, introduce yourself briefly and list 3-4 things you can help with.
11. Recommend consulting a lawyer for complex legal matters — mention free legal aid at NALSA helpline 15100.
12. Always respond in the language the user writes in (Hindi, English, etc.) — but default to English.

## Critical Rules:
- Jurisdiction: **INDIA ONLY** — all laws, sections, and helplines are Indian.
- Never provide diagnoses or medical treatment advice — recommend calling 112 or going to hospital.
- Never dismiss or minimise someone's experience.
- If someone is in immediate danger: Call 112 → Then 100 → Then 181 → Go to nearest police station or One Stop Centre.
"""


# ──────────────────────────────  Nodes  ────────────────────────────

def _sanitize_messages(messages: list[BaseMessage]) -> list[BaseMessage]:
    """
    Aggressively fix duplicate tool_call IDs that cause Mistral API 400 errors.

    Strategy: assign a FRESH unique ID to every single tool_call encountered,
    and remap the corresponding ToolMessage.tool_call_id references.  This
    guarantees zero collisions regardless of how LangGraph accumulates messages.
    Also cleans additional_kwargs["tool_calls"] which langchain-mistralai uses.
    """
    id_remap: dict[str, str] = {}   # old_id -> new_id
    sanitized: list[BaseMessage] = []

    for msg in messages:
        # --- AIMessage with tool_calls: give every call a fresh ID ---
        if isinstance(msg, AIMessage) and getattr(msg, "tool_calls", None):
            new_tool_calls = []
            for tc in msg.tool_calls:
                old_id = tc.get("id", "") or ""
                new_id = f"call_{uuid.uuid4().hex[:24]}"
                id_remap[old_id] = new_id
                new_tool_calls.append({**tc, "id": new_id})

            # Also fix additional_kwargs["tool_calls"] if present
            new_kwargs = dict(msg.additional_kwargs) if msg.additional_kwargs else {}
            if "tool_calls" in new_kwargs and isinstance(new_kwargs["tool_calls"], list):
                fixed_ak = []
                for ak_tc in new_kwargs["tool_calls"]:
                    ak_id = ak_tc.get("id", "") or ""
                    mapped = id_remap.get(ak_id, f"call_{uuid.uuid4().hex[:24]}")
                    fixed_ak.append({**ak_tc, "id": mapped})
                new_kwargs["tool_calls"] = fixed_ak

            msg = AIMessage(
                content=msg.content or "",
                tool_calls=new_tool_calls,
                additional_kwargs=new_kwargs,
            )
            sanitized.append(msg)

        # --- ToolMessage: remap to its parent's new ID ---
        elif isinstance(msg, ToolMessage):
            old_tc_id = getattr(msg, "tool_call_id", "") or ""
            new_tc_id = id_remap.get(old_tc_id, old_tc_id)
            msg = ToolMessage(
                content=msg.content,
                tool_call_id=new_tc_id,
                name=getattr(msg, "name", ""),
            )
            sanitized.append(msg)

        else:
            sanitized.append(msg)

    return sanitized


def agent_node(state: AgentState) -> dict:
    """The ReAct agent node — reasons and decides whether to use tools."""
    llm = get_llm()
    llm_with_tools = llm.bind_tools(tools)

    messages = list(state["messages"])

    # Prepend system prompt if not already there
    if not messages or not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages

    # Sanitize ALL tool_call IDs to fresh UUIDs (fixes Mistral API 400 error)
    messages = _sanitize_messages(messages)

    # Retry once: if Mistral still complains, strip all tool context and retry
    try:
        response = llm_with_tools.invoke(messages)
    except Exception as e:
        if "Duplicate tool call id" in str(e) or "3230" in str(e):
            # Nuclear option: strip all tool-related messages and retry
            clean = [m for m in messages
                     if isinstance(m, (SystemMessage, HumanMessage))
                     or (isinstance(m, AIMessage) and m.content and not getattr(m, "tool_calls", None))]
            response = llm_with_tools.invoke(clean)
        else:
            raise

    return {"messages": [response]}


def should_continue(state: AgentState) -> str:
    """Decide if agent should use tools or finish."""
    last_message = state["messages"][-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return "end"


# ──────────────────────────────  Graph  ────────────────────────────

def build_graph():
    """Build the ReAct agent graph with tool-calling loop."""
    workflow = StateGraph(AgentState)

    # Nodes
    workflow.add_node("agent", agent_node)
    workflow.add_node("tools", ToolNode(tools))

    # Entry
    workflow.set_entry_point("agent")

    # Edges — ReAct loop
    workflow.add_conditional_edges(
        "agent",
        should_continue,
        {
            "tools": "tools",   # Agent wants to use a tool → go to tool node
            "end": END,          # Agent is done → finish
        },
    )
    workflow.add_edge("tools", "agent")  # After tool execution → back to agent

    return workflow.compile()


# Singleton graph instance
graph = build_graph()


def chat(user_message: str, history: list[BaseMessage] | None = None) -> str:
    """
    Send a message to the ReAct agent and return the assistant's reply.

    Parameters
    ----------
    user_message : str
        The latest message from the user.
    history : list[BaseMessage] | None
        Previous conversation messages.

    Returns
    -------
    str
        The assistant's text reply.
    """
    messages: list[BaseMessage] = []
    if history:
        # Strip tool-related messages from history to avoid
        # duplicate tool_call ID errors on subsequent turns.
        # Keep only Human/AI messages that have actual text content.
        for m in history:
            if isinstance(m, HumanMessage):
                messages.append(m)
            elif isinstance(m, AIMessage) and m.content:
                # Keep only the text content, drop tool_calls
                messages.append(AIMessage(content=m.content))
            # Skip ToolMessage and AIMessage without content (pure tool-call msgs)
    messages.append(HumanMessage(content=user_message))

    try:
        result = graph.invoke({"messages": messages})
    except Exception as e:
        if "Duplicate tool call id" in str(e) or "3230" in str(e):
            # Last resort: send only the current message with no history
            result = graph.invoke({"messages": [HumanMessage(content=user_message)]})
        else:
            raise

    # Get the last AI message (skip tool messages)
    ai_messages = [m for m in result["messages"] if isinstance(m, AIMessage) and m.content]
    if ai_messages:
        return ai_messages[-1].content
    return "I'm here to help. Could you please tell me more about your situation?"
