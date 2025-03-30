import os
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.VideoClip import TextClip
from moviepy.config import change_settings
from dotenv import load_dotenv

load_dotenv()
change_settings({"IMAGEMAGICK_BINARY": os.getenv("IMAGEMAGICK_BINARY")})  # Adjust path to your installation

def create_video_with_audio(video_path, audio_path, subtitles_path, output_path):
    """
    Creates a video with audio and subtitles, where the length matches the audio.
    
    Args:
        video_path (str): The path to the video file.
        audio_path (str): The path to the audio file.
        subtitles_path (str): The path to the subtitles file.
        output_path (str): The path to save the output video.
    """
    try:
        # Load the video and audio
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)
        
        # Get the duration of the audio
        audio_duration = audio.duration
        print(f"Audio duration: {audio_duration} seconds")
        
        # If video is shorter than audio, we can loop it
        if video.duration < audio_duration:
            # Calculate how many times we need to loop the video
            n_loops = int(audio_duration / video.duration) + 1
            video = video.loop(n=n_loops)  # Create a looped version
        
        # Trim the video to match the audio duration
        video = video.subclip(0, audio_duration)
        
        # Make a generator that returns a TextClip when called with consecutive text
        generator = lambda txt: TextClip(
            txt,
            font="./fonts/KOMIKAX_.ttf",
            fontsize=50,
            color="white",
            stroke_color="black",
            stroke_width=2,
        )

        # Burn the subtitles into the video
        subtitles = SubtitlesClip(subtitles_path, generator)
        # Trim subtitles to match audio duration
        subtitles = subtitles.subclip(0, audio_duration)
        
        result = CompositeVideoClip([
            video,
            subtitles.set_pos(("center", "center"))
        ])

        # Add the audio
        result = result.set_audio(audio)

        # Write the final video 
        result.write_videofile(output_path)
        
        print(f"Final video created at {output_path}")
        
        # Clean up resources
        video.close()
        audio.close()
        result.close()

        return output_path
            
    except Exception as e:
        print(f"Error creating video: {e}")
        raise
