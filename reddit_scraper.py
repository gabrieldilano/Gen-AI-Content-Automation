import os
import random
import praw
from dotenv import load_dotenv

def estimate_speech_duration(text, words_per_minute=150):
    """
    Estimates the speech duration in minutes based on word count
    
    Args:
        text (str): The text to estimate
        words_per_minute (int): Average reading speed
        
    Returns:
        float: Estimated duration in minutes
    """
    # Count words by splitting on whitespace
    word_count = len(text.split())
    
    # Calculate duration in minutes
    duration = word_count / words_per_minute
    
    return duration

def scrape_random_top_story(max_duration_minutes=1.5, max_attempts=20):
    """
    Scrapes a random top story from Reddit that fits within speech time limit
    
    Args:
        max_duration_minutes (float): Maximum speech duration in minutes
        max_attempts (int): Maximum number of posts to check
        
    Returns: 
        dict with title and content of a random top post
    """
    # Load environment variables
    load_dotenv()
    
    # Initialize Reddit API client
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT", "RandomStoryScript:v1.0")
    )
    
    # Get top posts from a popular subreddit
    subreddit = reddit.subreddit("relationship_advice")
    top_posts = list(subreddit.hot(limit=50))  # Get top 50 hot posts to have more options
    
    # Shuffle posts to randomize the order
    random.shuffle(top_posts)
    
    # Try posts until we find one that fits our duration limit
    attempts = 0
    for post in top_posts:
        attempts += 1
        if attempts > max_attempts:
            print(f"Checked {max_attempts} posts without finding one short enough. Using the shortest one.")
            # If we've checked too many, just return the shortest so far
            return shortest_story
            
        # Extract title and content
        post_title = post.title
        
        # If it's a text post, get the content; otherwise, get the URL
        if post.is_self:
            post_content = post.selftext
        else:
            # Skip link posts as they don't have enough content
            continue
            
        # Skip empty content
        if not post_content.strip():
            continue
            
        # Calculate total text (title + content)
        total_text = f"{post_title}\n\n{post_content}"
        
        # Estimate speech duration
        duration = estimate_speech_duration(total_text)
        
        # Track the shortest story found so far (in case we don't find any under max_duration)
        if 'shortest_duration' not in locals() or duration < shortest_duration:
            shortest_duration = duration
            shortest_story = {
                "title": post_title,
                "content": post_content,
                "url": f"https://www.reddit.com{post.permalink}",
                "estimated_duration": duration
            }
        
        # Check if this post fits our criteria
        if duration <= max_duration_minutes:
            print(f"Found story with estimated duration of {duration:.2f} minutes")
            return {
                "title": post_title,
                "content": post_content,
                "url": f"https://www.reddit.com{post.permalink}",
                "estimated_duration": duration
            }
    
    # If we get here, we didn't find any stories under the limit
    print(f"No stories found under {max_duration_minutes} minutes. Using shortest (est. {shortest_duration:.2f} min)")
    return shortest_story


def prepare_reddit_story():
    """
    Scrapes a random top story from Reddit and saves it to a file.
    """
    
    # Get a story that's short enough for TTS
    story = scrape_random_top_story(max_duration_minutes=1.5)
    
    # Open file with UTF-8 encoding explicitly
    with open("script.txt", "w", encoding="utf-8") as file:
        title = story["title"]
        content = story["content"]
        file.write(f"{title}\n\n{content}")
    
    # Print information about the story
    estimated_minutes = story.get("estimated_duration", 0)
    estimated_seconds = int(estimated_minutes * 60)
    print(f"Script written to script.txt (est. duration: {estimated_minutes:.2f} min or {estimated_seconds} sec)")
    
    return title + "\n\n" + content