# connect.py: Test Azure OpenAI GPT-4o connectivity
import streamlit as st
import requests
from config.settings import AZURE_OPENAI_KEY, AZURE_OPENAI_ENDPOINT

def main():
    st.title("Azure OpenAI GPT-4o Connectivity Test")

    if st.button("Test Connection"):
        if AZURE_OPENAI_KEY and AZURE_OPENAI_ENDPOINT:
            try:
                headers = {
                    "Content-Type": "application/json",
                    "api-key": AZURE_OPENAI_KEY,
                }

                data = {
                    "messages": [{"role": "user", "content": "Test message"}],
                    "max_tokens": 50,
                }

                response = requests.post(AZURE_OPENAI_ENDPOINT, headers=headers, json=data)

                if response.status_code == 200:
                    result = response.json()
                    st.success(result["choices"][0]["message"]["content"].strip())
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Exception: {str(e)}")
        else:
            st.warning("Please provide Azure OpenAI credentials.")

if __name__ == "__main__":
    main()
