
import ffmpeg

def extract_audio(video_path, output_audio_path):
    ffmpeg.input(video_path).output(output_audio_path, acodec='pcm_s16le', ac=1, ar='16k').run(overwrite_output=True)
