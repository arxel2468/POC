# settings.py: Load environment variables from .env file
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Fetch API keys and credentials
AZURE_OPENAI_KEY = os.getenv('AZURE_OPENAI_KEY')
AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')
GOOGLE_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY')
PLAY_HT_API_KEY = os.getenv('PLAY_HT_API_KEY')
PLAY_HT_USER_ID = os.getenv('PLAY_HT_USER_ID')

# Other configurations can be added here
