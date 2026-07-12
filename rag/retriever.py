from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

from config.settings import (
    PINECONE_API_KEY,
    PINECONE_INDEX,
    EMBEDDING_MODEL,
    TOP_K,
)


class Retriever:

    def __init__(self):

        self.model = SentenceTransformer(EMBEDDING_MODEL)

        self.pc = Pinecone(api_key=PINECONE_API_KEY)

        self.index = self.pc.Index(PINECONE_INDEX)

    def retrieve(self, query: str):

        embedding = self.model.encode(
            query,
            normalize_embeddings=True
        ).tolist()

        results = self.index.query(
            vector=embedding,
            top_k=TOP_K,
            include_metadata=True
        )

        documents = []

        for match in results["matches"]:

            metadata = match["metadata"]

            documents.append(
                {
                    "score": match["score"],
                    "title": metadata.get("title"),
                    "url": metadata.get("url"),
                    "page_type": metadata.get("page_type"),
                    "content": metadata.get("content"),
                }
            )

        return documents