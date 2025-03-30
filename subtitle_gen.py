import os
import assemblyai as aai
from dotenv import load_dotenv

def generate_subtitles(audio_path: str):
    """
    Generates subtitles from a given audio file and returns the path to the subtitles.

    Args:
        audio_path (str): The path to the audio file to generate subtitles from.

    Returns:
        str: The generated subtitles
        
    """
    load_dotenv(".env")

    aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
    
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_path)
    subtitles = transcript.export_subtitles_srt(chars_per_caption=13)

    with open("subtitles.srt", "w") as file:
        file.write(subtitles)
    
    return "subtitles.srt"
