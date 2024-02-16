sample = '<video preload="none" playsinline="" style="width: 100%; height: 100%; position: absolute; background-color: black; top: 0%; left: 0%; transform: rotate(0deg) scale(1.005);" poster="https://pbs.twimg.com/amplify_video_thumb/1711075029641814016/img/hzWqDt1RxQ-liQ_1.jpg" src="blob:https://twitter.com/2a1cdc11-cc15-4c20-a386-e6bfb43779be"></video>'
import requests
import re
from bs4 import BeautifulSoup

# Define the Twitter video URL
video_url = "https://twitter.com/i/status/1711075209820745891"

# Send a GET request to the Twitter video URL
response = requests.get(video_url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the video URL in the HTML content
video_element = soup.find("meta", {"property": "og:video"})
video_url = video_element["content"]

# Extract the video ID from the video URL
video_id = re.search(r"/status/(\d+)", video_url).group(1)

# Define the download URL for the video
download_url = f"https://twitter.com/i/videos/tweet/{video_id}?src=5"

# Send a GET request to the download URL
response = requests.get(download_url)

# Extract the video URL from the response JSON data
data = response.json()
video_url = data["track"]["playbackUrl"]

# Send a GET request to the video URL and save the video
response = requests.get(video_url)
with open(f"{video_id}.mp4", "wb") as f:
    f.write(response.content)
