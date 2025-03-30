from script_gen import generate_script
from gen_speech import generate_speech
from subtitle_gen import generate_subtitles
from video_gen import create_video_with_audio
from reddit_scraper import prepare_reddit_story
import os
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

video_path = "MC Parkour.mp4"
output_path = "final_video.mp4"

# Check if video file exists
if not os.path.exists(video_path):
    print(f"Error: Video file '{video_path}' not found!")
    exit(1)

"""# Generate the script
script = generate_script()

# Write script with consistent encoding
with open('script.txt', 'w', encoding='utf-8') as file:
    file.write(script)
    print("Script written to script.txt")"""

script = prepare_reddit_story()

# Generate speech from script
audio_file_path = generate_speech(script)
if not audio_file_path or not os.path.exists(audio_file_path):
    print(f"Error: Failed to generate audio file at {audio_file_path}")
    exit(1)

print(f"Speech generated at {audio_file_path}")
    
# Give the system a moment to ensure the audio file is fully written
time.sleep(1)

# Verify audio file exists and has content
if not os.path.exists(audio_file_path):
    print(f"Error: Audio file not found at {audio_file_path}")
    exit(1)

audio_size = os.path.getsize(audio_file_path)
if audio_size == 0:
    print(f"Error: Audio file is empty at {audio_file_path}")
    exit(1)

print(f"Audio file verified: {os.path.abspath(audio_file_path)} (size: {audio_size} bytes)")

# Generate subtitles
subtitles_path = generate_subtitles(audio_file_path)
print(f"Subtitles generated at {subtitles_path}")

# Create final video with word-by-word subtitles
create_video_with_audio(
    video_path=video_path,
    audio_path=audio_file_path,
    subtitles_path=subtitles_path,
    output_path=output_path,
)
