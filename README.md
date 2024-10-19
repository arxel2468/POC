# Video Audio Replacement with AI-Generated Voice

This project replaces the audio of a video file with AI-generated speech. It uses **Azure OpenAI GPT-4o** to correct transcriptions of audio and **pyttsx3** to generate speech. The new audio is synchronized with the video, ensuring proper timing and smooth output.

## Features
- Transcribes audio from a video file
- Corrects the transcription using GPT-4o (Azure OpenAI)
- Replaces the original video audio with AI-generated speech
- Synchronizes audio with video for perfect duration matching

## Requirements
To run this project, ensure you have the following installed:
- **Python 3.10+**
- **Streamlit**
- **MoviePy**
- **Pydub**
- **Pyttsx3**
- **Azure OpenAI GPT-4o**

## Installation

1. Clone the repository:
    ```bash
    git clone [repository_url]
    cd [repository_name]
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    Create a `.env` file in the project root and add your API key and endpoint:
    ```text
    AZURE_OPENAI_KEY=[enter api key here] 
    AZURE_OPENAI_ENDPOINT=https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run src/main.py
    ```

2. Upload a video file in MP4 or MOV format.

3. Follow the UI steps:
    - Transcribe audio
    - Correct the transcript (using GPT-4o)
    - Generate new audio (AI-generated voice)
    - Replace the audio in the video

4. Download or view the final video with replaced audio.

## Files
- **`main.py`**: The main entry point for the Streamlit app.
- **`video_processing.py`**: Handles video-related functions like replacing audio.
- **`audio_processing.py`**: Manages audio extraction, transcription, and synchronization.
- **`connect.py`**: Contains the connection logic for Azure OpenAI API.

## Troubleshooting

- **Audio/Video Sync Issues**: If you experience lag in audio or video, check the `match_audio_length` function to ensure proper speed adjustments are being applied to the audio.
- **API Key Error**: Ensure that your `.env` file contains the correct Azure OpenAI API key and endpoint.
  
## Dependencies
- **Azure OpenAI GPT-4o**
- **MoviePy**
- **Pyttsx3**
- **Pydub**
- **Streamlit**

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
