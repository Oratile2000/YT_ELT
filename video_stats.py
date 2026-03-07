import requests


#Global variable for the API key, which is used to authenticate requests to the YouTube Data API. 
API_KEY = "AIzaSyCUfZpT7phJDvRMtQwVgwbAgOk4tzkV9UU"
CHANNEL_ID = "MrBeast"  # MrBeast's channel ID

#Set the url to the YouTube Data API endpoint for retrieving video statistics, including the video ID and the part parameter set to statistics. Then, make a GET request to the API and return the response as a JSON object.
#Set the url value
url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_ID}&key={API_KEY}"

response = requests.get(url)
print(response.json())  # Print the response as a JSON object
















##Get data from the API and print the response as a JSON object. Using video ID "dQw4w9WgXcQ" as an example to test the function.
# def get_video_stats(video_id):
#     url = f"https://youtube.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={API_KEY}"
#     response = requests.get(url)
#     return response.json()

#print(get_video_stats("dQw4w9WgXcQ"))   Example video ID for testing