import asyncio
from deepgram import Deepgram
import os
from moviepy.editor import AudioFileClip
import speech_recognition as sr
from pydub import AudioSegment
from pydub.effects import speedup
import sys
import wave
import soundfile as sf
import pyrubberband as pyrb
                     
    

# Create a wrapper to run the async function in a synchronous environment
def transcribe_audio(audio_path: str) -> str:
    print(audio_path, type(audio_path))
    # return asyncio.run(transcribe_audio_async(audio_path))
    r = sr.Recognizer()
    # audio object
    audio = sr.AudioFile(audio_path)
    with audio as source:
        audio = r.record(source)                  
        result = r.recognize_google(audio)
        
    print(result)

    return result

def extract_audio_from_video(video_path: str, output_audio_path: str) -> str:
    """Extract audio from a video file and save it as a WAV file."""
    video_audio_clip = AudioFileClip(video_path)
    video_audio_clip.write_audiofile(output_audio_path)
    return output_audio_path


def match_audio_length(audio_path, target_duration):
    """Adjust the length of the audio to match the video duration."""
    print(audio_path)
    audio = AudioSegment.from_wav(audio_path)
    audio_duration = len(audio)  # Get the current audio duration in milliseconds


    audio.export("file.wav", format="wav")
    y, sr= sf.read("file.wav")
    # Play back at extra low speed
    y_stretch = pyrb.time_stretch(y, sr, 0.5)
    # Play back extra low tones
    y_shift = pyrb.pitch_shift(y, sr, 0.5)
    sf.write("temp\\analyzed_filepathX5.wav", y_stretch, sr, format='wav')

    sound = AudioSegment.from_wav("temp\\analyzed_filepathX5.wav")
    sound.export("temp\\analyzed_filepathX5.mp3", format="mp3")

    # Play back at low speed
    y_stretch = pyrb.time_stretch(y, sr, 0.75)
    # Play back at low tones
    y_shift = pyrb.pitch_shift(y, sr, 0.75)
    sf.write("temp\\analyzed_filepathX75.wav", y_stretch, sr, format='wav')

    sound = AudioSegment.from_wav("temp\\analyzed_filepathX75.wav")
    sound.export("temp\\analyzed_filepathX75.mp3", format="mp3")

    # Play back at 1.5X speed
    y_stretch = pyrb.time_stretch(y, sr, 1.5)
    # Play back two 1.5x tones
    y_shift = pyrb.pitch_shift(y, sr, 1.5)
    sf.write("temp\\analyzed_filepathX105.wav", y_stretch, sr, format='wav')

    sound = AudioSegment.from_wav("temp\\analyzed_filepathX105.wav")
    sound.export("temp\\analyzed_filepathX105.mp3", format="mp3")

    # Play back at same speed
    y_stretch = pyrb.time_stretch(y, sr, 1)
    # Play back two smae-tones
    y_shift = pyrb.pitch_shift(y, sr, 1)
    sf.write("temp\\analyzed_filepathXnormal.wav", y_stretch, sr, format='wav')

    sound = AudioSegment.from_wav("temp\\analyzed_filepathXnormal.wav")
    adjusted_audio_path="temp\\adjusted_audio.mp3"
    sound.export(adjusted_audio_path, format="mp3")
    return adjusted_audio_path
