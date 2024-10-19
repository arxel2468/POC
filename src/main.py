import streamlit as st
from utils.audio_processing import extract_audio_from_video, transcribe_audio, match_audio_length
from utils.video_processing import replace_audio_in_video
from utils.openai_utils import correct_transcript
from gtts import gTTS
import pyttsx3 
import os
from moviepy.editor import VideoFileClip
from config.settings import DEEPGRAM_API_KEY



def generate_speech(text: str, output_path: str) -> str:
    """Generate speech using gTTS."""
    try:
        engine = pyttsx3.init()
        engine.save_to_file(text, output_path)
        engine.runAndWait()

        # tts = gTTS(text, lang='en', slow=False)
        # tts.save(output_path)

        print(f"Audio saved to {output_path}")
        return output_path
    except Exception as e:
        print(f"Error generating speech: {str(e)}")
        return None


def main():
    st.title("Video Audio Replacement with AI-Generated Voice")

    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov"])
    
    if uploaded_file is not None:
        # Save the video file
        video_path = f"temp\\temp_{uploaded_file.name}"
        with open(video_path, 'wb') as f:
            f.write(uploaded_file.read())

        # Extract video duration
        video_clip = VideoFileClip(video_path)
        video_duration = video_clip.duration
        
        # Extract audio from the video
        audio_path = extract_audio_from_video(video_path, "temp\\temp_audio.wav")
        
        # Transcribe the audio using Deepgram
        transcript = transcribe_audio(audio_path)
        st.text_area("Original Transcript", transcript)
        
        if st.button("Correct Transcript"):
            # Correct the transcript using GPT-4o (Azure)
            corrected_transcript = correct_transcript(transcript)
            st.text_area("Corrected Transcript", corrected_transcript)
            
            # Save corrected transcript to session state
            st.session_state['corrected_transcript'] = corrected_transcript
            print("Corrected transcript saved.")
        
        # # Only show "Generate New Audio" button if the corrected transcript exists
        # if 'corrected_transcript' in st.session_state and st.button("Generate New Audio"):
            corrected_transcript = st.session_state['corrected_transcript']
            new_audio_path = generate_speech(corrected_transcript, "temp\\corrected_audio.mp3")
            print(new_audio_path)
            new_audio_path = match_audio_length(new_audio_path, video_duration * 1000)  # Convert seconds to milliseconds

            
            if new_audio_path:
                st.session_state['new_audio_path'] = new_audio_path
                
                print(st.session_state['new_audio_path'])

                
                st.audio(new_audio_path)
                st.success("New audio generated and saved.")
                print("New audio generated successfully.")
            else:
                st.error("Failed to generate audio.")
        
        # Only show "Replace Audio in Video" if new audio is generated
        # if 'new_audio_path' in st.session_state and st.button("Replace Audio in Video"):
            output_video_path = "temp\\output_video.mp4"
            replace_audio_in_video(video_path, new_audio_path, output_video_path)
            st.success(f"Video saved with replaced audio: {output_video_path}")
            st.video(output_video_path)

if __name__ == "__main__":
    main()