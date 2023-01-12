from youtube_transcript_api import YouTubeTranscriptApi

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# video_url = "https://www.youtube.com/watch?v=0Mt_JJ3gRI4"
transcript = YouTubeTranscriptApi.get_transcript(video_url)

print(transcript)