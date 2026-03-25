import requests

def generate_answer(query, context):
    prompt = f"""
    You are a research assistant.

    Answer ONLY from the context below.

    Context:
    {context}

    Question:
    {query}
    """

    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        data = res.json()

        if "response" in data:
            return data["response"]
        else:
            return f"⚠️ Unexpected response: {data}"

    except Exception as e:
        return f"❌ Error: {str(e)}"