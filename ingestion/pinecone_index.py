import json
from pathlib import Path

from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

from config.settings import (
    PINECONE_API_KEY,
    PINECONE_INDEX,
    EMBEDDING_MODEL,
)

# Paths

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "data" / "chunks" / "chunks.jsonl"

# Load Embedding Model

print("Loading embedding model...")
model = SentenceTransformer(EMBEDDING_MODEL)

# Connect Pinecone

pc = Pinecone(api_key=PINECONE_API_KEY)

index = pc.Index(PINECONE_INDEX)

print("Connected to Pinecone")

# Read Chunks & Upload

batch = []

BATCH_SIZE = 100

with open(INPUT_FILE, "r", encoding="utf-8") as f:

    for line in tqdm(f):

        chunk = json.loads(line)

        embedding = model.encode(
            chunk["content"],
            normalize_embeddings=True
        ).tolist()

        batch.append(
            {
                "id": chunk["chunk_id"],
                "values": embedding,
                "metadata": {
                    "title": chunk["title"],
                    "url": chunk["url"],
                    "page_type": chunk["page_type"],
                    "content": chunk["content"]
                }
            }
        )

        if len(batch) >= BATCH_SIZE:
            index.upsert(vectors=batch)
            batch = []

# Upload remaining vectors
if batch:
    index.upsert(vectors=batch)

print("Indexing completed successfully!")