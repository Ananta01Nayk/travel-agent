from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


BASE_DIR = Path(__file__).resolve().parent.parent


DATA_DIR = BASE_DIR / "data"

DOCUMENT_PATH = DATA_DIR / "processed" / "documents.jsonl"

CHUNK_PATH = DATA_DIR / "chunks" / "chunks.jsonl"

VECTOR_DB_PATH = BASE_DIR / "vectordb"


PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

PINECONE_INDEX = os.getenv("PINECONE_INDEX")


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)


CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 800))

CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 150))

TOP_K = int(os.getenv("TOP_K", 5))