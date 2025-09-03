import whisper

# Load a smaller Whisper model (try "medium" first)
model = whisper.load_model("small")


# Path to your video file
video_path = "/workspaces/video-to-text-transcribe/ssvid.net--Full-History-of-Korea-in-5-Minutes_1080p.mp4"

# Transcribe the video
result = model.transcribe(video_path, language="en")

# Save transcript to file
with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("✅ Transcription complete! The full transcript is saved in transcript.txt")
