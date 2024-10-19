from moviepy.editor import VideoFileClip, AudioFileClip

def replace_audio_in_video(video_path: str, audio_path: str, output_path: str):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)
    
    # Set audio to video and ensure duration sync
    video = video.set_audio(audio)
    video_duration = video.duration
    audio_duration = audio.duration

    # Trim the video if the audio is shorter or pad the audio if the video is longer
    if video_duration > audio_duration:
        video = video.subclip(0, audio_duration)
    elif audio_duration > video_duration:
        silence = AudioFileClip("temp\\1sec_silence.mp3").subclip(0, audio_duration - video_duration)
        audio = concatenate_audioclips([audio, silence])
        video = video.set_audio(audio)

    video.write_videofile(output_path, codec='libx264', audio_codec="aac")
