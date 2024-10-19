# openai_utils.py: Handle Azure OpenAI GPT-4o communication
import requests
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

def correct_transcript(transcript: str) -> str:
    """Corrects the transcript using GPT-4o."""
    headers = {
        'Content-Type': 'application/json',
        'api-key': f'{os.getenv('AZURE_OPENAI_KEY')}'
    }

    data = {
        'messages': [{'role': 'user', 'content': f"Trascribe this text into proper grammer and remove 'ummm hmmmm' kind of texts {transcript}"}],
        'max_tokens': len(transcript)
    }

    response = requests.post(f'{os.getenv('AZURE_OPENAI_ENDPOINT')}', headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return transcript
