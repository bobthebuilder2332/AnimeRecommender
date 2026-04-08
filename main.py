import requests

# This is the URL of the API endpoint for Jikan API
url = "https://api.jikan.moe/v4/anime/1"

# This is how you make a GET request to the API endpoint using the requests library
response = requests.get(url)

if response.status_code == 200: # Status Code 200 means success
    # This converts the JSON response into a Python dictionary and ignores all the irrelevant data
    data = response.json()['data']
    
    # Seperate data into specific fields
    url = data.get('url')
    title = data.get('title')
    score = data.get('score')
    episodes = data.get('episodes')
    synopsis = data.get('synopsis')
    
    # Print data
    print (f"URL: {url}\nTitle: {title}\nScore: {score}/10\nEpisodes: {episodes}\nSynopsis: {synopsis}")
else:
    print (f"Error: {response.status_code}")