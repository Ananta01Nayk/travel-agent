from vectorstore.chroma_retriever import ChromaRetriever
from rag.generator import GeminiGenerator


class TravelRAG:

    def __init__(self):
        self.retriever = ChromaRetriever()
        self.generator = GeminiGenerator()

    def ask(self, question: str, top_k: int = 5):

        # Step 1: Retrieve relevant packages
        packages = self.retriever.search(
            query=question,
            top_k=top_k
        )

        # Step 2: If nothing found
        if not packages:
            return {
                "answer": "I couldn't find any matching travel packages.",
                "sources": []
            }

        # Step 3: Generate answer using Gemini
        answer = self.generator.generate(
            question=question,
            packages=packages
        )

        # Step 4: Return answer and sources
        return {
            "answer": answer,
            "sources": packages
        }