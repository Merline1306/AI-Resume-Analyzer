import os
from dotenv import load_dotenv
from ollama import chat

load_dotenv()


class OllamaService:

    def __init__(self):

        self.model = os.getenv(
            "OLLAMA_MODEL",
            "gemma3:latest"
        )

    def generate(

        self,

        prompt,

        temperature=0.3,

    ):

        response = chat(

            model=self.model,

            messages=[

                {

                    "role": "user",

                    "content": prompt

                }

            ],

            options={

                "temperature": temperature,

            }

        )

        return response.message.content