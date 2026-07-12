from modules.ai.ollama_service import OllamaService

ai = OllamaService()

print(
    ai.generate(
        "Explain ATS score in one paragraph."
    )
)