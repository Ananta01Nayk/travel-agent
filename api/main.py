from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from rag.rag_pipeline import TravelRAG
from api.schemas import ChatRequest, ChatResponse

app = FastAPI(
    title="Travel Agent API",
    version="1.0.0",
    description="AI Travel Assistant using RAG"
)

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rag = TravelRAG()


@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Travel Agent API is running."
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = rag.ask(request.question)

    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"]
    )