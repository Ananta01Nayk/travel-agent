import chromadb
from chromadb.utils import embedding_functions

CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "travel_packages"

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="BAAI/bge-small-en-v1.5"
)

client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = client.get_collection(
    COLLECTION_NAME,
    embedding_function=embedding_function
)


class ChromaRetriever:

    def __init__(self):
        self.collection = collection

    def search(self, query: str, top_k: int = 5):

        results = self.collection.query(
            query_texts=[query],
            n_results=top_k
        )

        packages = []

        for doc, meta, distance in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        ):

            packages.append(
                {
                    "title": meta["title"],
                    "price": meta["price"],
                    "duration": meta["duration"],
                    "detail_url": meta["detail_url"],
                    "page_title": meta["page_title"],
                    "image": meta["image"],
                    "content": doc,
                    "score": round(1 - distance, 4)
                }
            )

        return packages