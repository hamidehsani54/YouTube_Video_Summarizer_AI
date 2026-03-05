from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_transcript(url):
    video_id = extract_video_id(url)
    if not video_id:
        return None

    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)

        full_text = " ".join([entry.text for entry in transcript])
        return full_text

    except Exception as e:
        print("Transcript error:", e)
        return None