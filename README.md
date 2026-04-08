# Anime Recommender

A simple and minimalistic program that recommends the user a new anime to watched based on a title they input. Also displays details regarding any anime (doesn't have to be the same one) next to the recommendations

## Features

* Uses Jikan API, which scrapes from MyAnimeList.net
  * One of the largest anime databases with over 23,000 anime entries
* Comprehensive list of details for most titles
* Extensive list of crowdscourced recommendations
* Error handling if data is missing
* Easy to use split screen layout with dynamic sizing window

## Built With

* Jikan API to get data
* Python 3.14.3
* Tkinter library for window and GUI
* Requests library for API communication

## How to use

1. Install Python 3.14 or newer
2. Clone this repository
3. Set up a virtual environment (venv)
4. Install the Requests library (Tkinter typically comes pre-installed with Python)
5. Run the file "main.py"
6. Enter a MyAnimeList anime ID into a field
7. Press the button to get details (left side) or recommendations (right side)

Distributed under MIT license
