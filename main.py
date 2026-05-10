from ingestion.loader import DocumentLoader
from ingestion.chunker import Chunker
from ingestion.embedded import Embedder

from vectorstore.faiss_store import FAISSStore
from retrieval.retriever import Retriever

from generation.prompt_builder import PromptBuilder
from generation.llm import LLM

# Load documents
loader = DocumentLoader()
docs = loader.load_pdf("data/ThesisDocument.pdf")

# Chunk documents
chunker = Chunker()
chunks = chunker.split_documents(docs)

# Embeddings
embedder = Embedder()
texts, embeddings = embedder.create_embeddings(chunks)

# Build FAISS index
store = FAISSStore()
index = store.build_index(embeddings)

# User query
query = input("Ask Question: ")

# Retrieval
retriever = Retriever()
retrieved_chunks = retriever.retrieve(
    query,
    embedder,
    index,
    texts
)

# Prompt construction
prompt_builder = PromptBuilder()
prompt = prompt_builder.build_prompt(
    query,
    retrieved_chunks
)

print("\nRetrieved Chunks:\n")

for chunk in retrieved_chunks:
    print(chunk)
    print("=" * 50)
print("\nFinal Prompt:\n")
print(prompt)

# LLM generation
llm = LLM()
response = llm.generate(prompt)

print("\nAnswer:\n")
print(response)