import os

from openai import OpenAI
from rag.prompt import build_prompt


class DeepSeekGenerator:

    def __init__(self):
        api_key = os.getenv("DEEPSEEK_API_KEY")

        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY is not set")

        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )

        self.model = os.getenv(
            "DEEPSEEK_MODEL",
            "deepseek-v4-flash"
        )

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

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            thinking={
                "type": "disabled"
            },
        )

        return response.choices[0].message.content