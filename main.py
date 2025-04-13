
from audio.extractor import extract_audio
from transcription.transcriber import transcribe_audio
from voice_cloning.cloner import clone_and_generate
from audio.replacer import replace_audio

def main():
    video_path = "examples/sample_video.mp4"
    extracted_audio = "output/original_audio.wav"
    transcript_path = "output/transcript.txt"
    cloned_audio_path = "output/cloned_audio.wav"
    final_video_path = "output/dubbed_video.mp4"

    # Step 1: Extract audio
    extract_audio(video_path, extracted_audio)

    # Step 2: Transcribe using Whisper
    transcription = transcribe_audio(extracted_audio)
    with open(transcript_path, "w") as f:
        f.write(transcription)

    # Step 3: Clone voice + synthesize new audio
    clone_and_generate(extracted_audio, transcription, cloned_audio_path)

    # Step 4: Replace audio in video
    replace_audio(video_path, cloned_audio_path, final_video_path)

    print("✅ Dubbing complete! Check 'output/dubbed_video.mp4'")

if __name__ == "__main__":
    main()
