import os
import openai

OPENAI_KEY = os.environ.get("OPENAI_API_KEY")
if OPENAI_KEY:
    openai.api_key = OPENAI_KEY


def generate_email(prompt: str, max_tokens: int = 200) -> str:
    """Call OpenAI to generate a short email given a prompt. Returns the text.
    Falls back to a stub message if key is missing or an error occurs.
    """
    if not OPENAI_KEY:
        return f"STUB GENERATED EMAIL for prompt: {prompt}"

    try:
        resp = openai.ChatCompletion.create(
            model=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.2,
        )
        # Extract text from response
        text = resp.choices[0].message.content.strip()
        return text
    except Exception as e:
        # Fail gracefully in dev
        return f"OPENAI ERROR: {str(e)}"

