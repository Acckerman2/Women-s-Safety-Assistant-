"""
SheShield AI – FastAPI Backend.

Provides REST API endpoints for the women's safety chatbot.
Connects the Streamlit frontend to the LangGraph ReAct agent.
"""

from __future__ import annotations

import os
import uuid
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
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

# CORS — allow Streamlit and any frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ──────────────────────── In-memory sessions ───────────────────
# Maps session_id → list of BaseMessage
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


# ──────────────────────── Routes ───────────────────────────────

@app.get("/", response_model=HealthResponse)
async def root():
    """Health check / landing endpoint."""
    return HealthResponse(
        status="healthy",
        service="SheShield AI – Women's Safety Assistant",
        version="2.0.0",
    )


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
