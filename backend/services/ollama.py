import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

def generate_summary_for_student(name: str, age: int, email: str) -> str:
    prompt = (
    f"Write a short, warm third-person summary of the following student's profile "
    f"Keep it natural and grounded — no exaggeration, no flattery, and no extra commentary"
    f"Include all the details provided"
    f"Don't generate the same response everytime\n\n"
    f"Name: {name}\nAge: {age}\nEmail: {email}"
    )


    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except requests.RequestException as e:
        raise RuntimeError(f"Ollama API error: {str(e)}")
