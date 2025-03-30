import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path


def generate_speech(script):
    """
    Generate speech from script using OpenAI's TTS API.
    
    Args:
        script (str): The text to convert to speech
        
    Returns:
        str: Path to the generated audio file
    """
    try:
        client = OpenAI()
        speech_file_path = Path(__file__).parent / "speech.mp3"

        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="coral",
            input=script,
            instructions="Speak in a engaging and positive tone to draw in the attention of viewers.",
        ) as response:
            response.stream_to_file(speech_file_path)
            
        # Verify the file was created
        if not speech_file_path.exists():
            raise FileNotFoundError(f"Audio file was not created at {speech_file_path}")
            
        return str(speech_file_path)
    except Exception as e:
        print(f"Error generating speech: {str(e)}")
        return None
    