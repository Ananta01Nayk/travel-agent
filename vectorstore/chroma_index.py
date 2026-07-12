import json
from pathlib import Path

import chromadb
from chromadb.utils import embedding_functions

# Configuration

DATA_PATH = Path("data/processed/package_documents.jsonl")
CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "travel_packages"

# Embedding Model

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="BAAI/bge-small-en-v1.5"
)

# Create Chroma Client

client = chromadb.PersistentClient(path=CHROMA_PATH)

# Delete old collection (development only)
try:
    client.delete_collection(COLLECTION_NAME)
    print("Old collection deleted.")
except:
    pass

collection = client.create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_function,
)

print("Collection created.")

# Read Package Documents

documents = []
metadatas = []
ids = []

with open(DATA_PATH, "r", encoding="utf-8") as f:

    for line in f:

        package = json.loads(line)

        documents.append(package["embedding_text"])

        ids.append(package["id"])

        metadata = {
            "title": package["title"],
            "price": package["price"],
            "duration": package["duration"],
            "detail_url": package["detail_url"],
            "page_title": package["page_title"],
            "image": package["image"],
            "includes": ", ".join(package["includes"]),
            "raw_text": package["raw_text"]
        }

        metadatas.append(metadata)

# Insert into ChromaDB

BATCH_SIZE = 100

for i in range(0, len(documents), BATCH_SIZE):

    collection.add(
        ids=ids[i:i+BATCH_SIZE],
        documents=documents[i:i+BATCH_SIZE],
        metadatas=metadatas[i:i+BATCH_SIZE],
    )

print("=" * 60)
print("Indexing Completed Successfully")
print(f"Total Packages : {len(documents)}")
print(f"Collection     : {COLLECTION_NAME}")
print("=" * 60)