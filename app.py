from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from agent import run_agent

app = FastAPI(title="Starter Python AI Agent", version="0.1.0")


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="Prompt for the AI agent")


class ChatResponse(BaseModel):
    reply: str


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest) -> ChatResponse:
    try:
        reply = run_agent(payload.message)
        return ChatResponse(reply=reply)
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Agent execution failed: {exc}") from exc
