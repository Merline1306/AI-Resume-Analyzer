try:
    from modules.ai.gemini_service import GeminiService
except ImportError:
    from modules.ai.gemini_service import GeminiService

try:
    gemini = GeminiService()
    response = gemini.generate(
        "Say hello in one sentence."
    )
    print(response)
except Exception as exc:
    print(f"Gemini test failed: {exc}")