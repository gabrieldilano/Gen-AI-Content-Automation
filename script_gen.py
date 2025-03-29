from openai import OpenAI
import os
from dotenv import load_dotenv

def generate_script():
    # Load environment variables from .env file
    load_dotenv()

    # Initialize OpenAI client
    client = OpenAI()

    # Generate script using OpenAI API
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Write a 60-second script for an Instagram Reel / YouTube Short that delivers maximum brainrot energy. The video should be chaotic, fast-paced, and full of absurd humor. It must revolve around Minecraft and Roblox, featuring exaggerated reactions, ridiculous scenarios, and meme-worthy moments. Include relevant memes from 2024 and beyond. The script should be engaging and entertaining, appealing to a younger audience. Make sure to include a catchy hook at the beginning to grab attention. Write the script so that it is only the dialogue and intended to be placed into a text to speech generator. The script should be in English and should not include any additional explanations or context. The script should be formatted as a single block of text without any line breaks or special characters. The script should be exactly 60 seconds long when read aloud and exactly 20 sentences."}
        ]
    )

    # Print the generated script
    return(response.choices[0].message.content)