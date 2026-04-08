import requests

# This is the URL of the API endpoint for Jikan API
url = "https://api.jikan.moe/v4/anime/48736"

# This is how you make a GET request to the API endpoint using the requests library
response = requests.get(url)

if response.status_code == 200: # Status Code 200 means success
    # This converts the JSON response into a Python dictionary and ignores all the irrelevant data (outside 'data' field)
    data = response.json()['data']
    
    # Seperate data into specific fields
    url = data.get('url')
    title = data.get('title')
    score = data.get('score')
    genres = [g.get('name') for g in data.get('genres', [])]
    themes = [t.get('name') for t in data.get('themes', [])]
    demographics = [d.get('name') for d in data.get('demographics', [])]
    episodes = data.get('episodes')
    synopsis = data.get('synopsis')

    #

    # Print data
    print (f"URL: {url}")
    print (f"Title: {title}")
    print (f"Score: {score}/10")
    print (f"Genre: {genres}")
    print (f"Theme: {themes}")
    print (f"Demographics: {demographics}")
    print (f"Episodes: {episodes}")
    print (f"Synopsis: {synopsis}")
else:
    print (f"Error: {response.status_code}")