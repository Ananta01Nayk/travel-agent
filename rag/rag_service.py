from google import genai

from config.settings import GOOGLE_API_KEY
from rag.retriever import Retriever
from rag.prompt import build_prompt


class RAGService:

    def __init__(self):

        self.client = genai.Client(api_key=GOOGLE_API_KEY)

        self.retriever = Retriever()

    def chat(self, question: str):

        docs = self.retriever.retrieve(question)

        prompt = build_prompt(question, docs)

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return {
            "answer": response.text,
            "sources": [
                {
                    "title": d["title"],
                    "url": d["url"],
                    "score": d["score"]
                }
                for d in docs
            ]
        }