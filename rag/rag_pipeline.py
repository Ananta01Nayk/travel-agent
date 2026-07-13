from vectorstore.chroma_retriever import ChromaRetriever
from rag.generator import GeminiGenerator


class TravelRAG:

    def __init__(self):
        self.retriever = ChromaRetriever()
        self.generator = GeminiGenerator()

        # Messages that should NOT trigger package retrieval
        self.greetings = {
            "hi",
            "hello",
            "hey",
            "hii",
            "hiii",
            "good morning",
            "good afternoon",
            "good evening",
            "how are you",
            "thanks",
            "thank you",
            "ok",
            "okay",
            "bye",
            "hello bharti"
        }

    def ask(self, question: str, top_k: int = 5):

        query = question.strip().lower()

        # Greeting Detection

        if query in self.greetings:

            return {
                "answer": (
                    "Hello! 👋 I'm Bharti, your AI travel assistant.\n\n"
                    "I can help you find the best travel packages across India.\n\n"
                    "Tell me your destination, budget, duration, or the type of trip you're planning."
                ),
                "sources": []
            }

        # Retrieve Packages

        packages = self.retriever.search(
            query=question,
            top_k=top_k
        )

        print("=" * 50)
        print("Question:", question)
        print("Retrieved Packages:", len(packages))

        for i, package in enumerate(packages):
            print(f"{i + 1}. {package.get('title')}")

        print("=" * 50)

        # No Results

        if not packages:
            return {
                "answer": (
                    "Sorry, I couldn't find any travel packages matching your request.\n\n"
                    "Try mentioning a destination like Goa, Kerala, Rajasthan, Kashmir, Assam, or your preferred budget and trip duration."
                ),
                "sources": []
            }

        # Generate AI Response

        answer = self.generator.generate(
            question=question,
            packages=packages
        )

        # Return Response

        return {
            "answer": answer,
            "sources": packages
        }