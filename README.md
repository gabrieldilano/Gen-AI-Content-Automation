# AI Content Automation Tools

This repository contains scripts for automating content creation using AI tools.

## Scripts

### 1. Video Generation with Custom Audio (`video_gen.py`)

This script combines a video file with a custom audio track, ensuring the video matches the audio duration.

```python
python video_gen.py
```

Requirements:
- A video file (default: "MC Parkour.mp4")
- An audio file (default: "speech.mp3") 
- MoviePy library (`pip install moviepy`)

The script will:
1. Load the video and audio files
2. Loop the video if it's shorter than the audio
3. Create a new video with the original video visuals and your custom audio
4. Save the result as "final_video.mp4"

### 2. AI Image Generation from Script (`image_gen.py`)

This script analyzes a text script, groups sentences into pairs, and generates relevant images using DALL-E 2. It can also create a slideshow video from the generated images.

```python
python image_gen.py
```

Requirements:
- A script file (default: "generated_script.txt")
- An audio file (default: "speech.mp3")
- OpenAI API key (will prompt if not set as environment variable)
- Required libraries:
  ```
  pip install openai nltk pillow requests moviepy
  ```

The script will:
1. Read your script and divide it into sentence pairs
2. Generate 10 images using DALL-E 2 that match the content of each pair
3. Download and save the images
4. Create a slideshow video with the images timed to your audio file
5. Save the result as "slideshow_video.mp4"

## Usage Tips

### Setting OpenAI API Key

Set your OpenAI API key as an environment variable:

Windows:
```
set OPENAI_API_KEY=your-api-key-here
```

Mac/Linux:
```
export OPENAI_API_KEY=your-api-key-here
```

Or the script will prompt you to enter it.

### Customizing Output

You can modify the script variables to customize:
- Input/output file paths
- Number of images to generate
- Image display duration in the slideshow

## Example Workflow

1. Generate a script using an AI tool
2. Save the script as "generated_script.txt"
3. Record audio of the script as "speech.mp3" 
4. Run `image_gen.py` to create images and a slideshow video
5. Alternatively, use `video_gen.py` to combine an existing video with your audio 