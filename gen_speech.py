import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path


def generate_speech(script):
    client = OpenAI()
    speech_file_path = Path(__file__).parent / "speech.mp3"

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input=script,
        instructions="Speak in a engaging and positive tone to draw in the attention of viewers.",
    ) as response:
        response.stream_to_file(speech_file_path)
    