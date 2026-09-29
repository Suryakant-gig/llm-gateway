from app.services.llm import call_groq, call_gemini


def route_request(message: str, model: str = "auto"):
    if model == "groq":
        return call_groq(message)

    if model == "gemini":
        return call_gemini(message)

    # auto
    return call_groq(message)