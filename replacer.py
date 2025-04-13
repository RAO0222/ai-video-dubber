
from moviepy.editor import VideoFileClip, AudioFileClip

def replace_audio(video_path, new_audio_path, output_path):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(new_audio_path)
    final_video = video.set_audio(audio)
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
