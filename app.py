from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ingestion.loader import DocumentLoader
from ingestion.chunker import Chunker
from ingestion.embedded import Embedder

from vectorstore.faiss_store import FAISSStore
from retrieval.retriever import Retriever

from generation.prompt_builder import PromptBuilder
from generation.llm import LLM

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Load everything once
# -----------------------------
loader = DocumentLoader()
docs = loader.load_pdfs("data")

chunker = Chunker()
chunks = chunker.split_documents(docs)

embedder = Embedder()
texts, embeddings = embedder.create_embeddings(chunks)

store = FAISSStore()
index = store.build_index(embeddings)

retriever = Retriever()
prompt_builder = PromptBuilder()
llm = LLM()

# -----------------------------
# Request schema
# -----------------------------

class QueryRequest(BaseModel):
    question: str

# -----------------------------
# API Route
# -----------------------------

@app.post("/ask")
def ask_question(request: QueryRequest):

    retrieved_chunks = retriever.retrieve(
        request.question,
        embedder,
        index,
        texts
    )

    prompt = prompt_builder.build_prompt(
        request.question,
        retrieved_chunks
    )

    response = llm.generate(prompt)

    return {
        "question": request.question,
        "answer": response,
        "retrieved_chunks": retrieved_chunks
    }