import os

from dotenv import load_dotenv
from google import genai

from rag.prompt import build_prompt

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY not found. Please add it to your .env file."
    )

client = genai.Client(api_key=api_key)


class GeminiGenerator:

    def generate(self, question: str, packages: list):

        documents = []

        for package in packages:

            documents.append(
                {
                    "title": package.get("title", ""),
                    "price": package.get("price", ""),
                    "duration": package.get("duration", ""),
                    "includes": package.get("includes", []),
                    "detail_url": package.get("detail_url", ""),
                    "page_title": package.get("page_title", ""),
                    "content": package.get("content", ""),
                }
            )

        prompt = build_prompt(question, documents)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text