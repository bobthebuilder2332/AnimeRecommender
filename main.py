import requests # Used to handle HTTP requests to the API
import tkinter as tk # Used to create a GUI for the application / seperate window
from tkinter import scrolledtext # Used to create a scrollable text widget for displaying results; doesn't import automatically with tkinter, so it needs to be imported separately


# Define global variables
BASE_URL = "https://api.jikan.moe/v4/anime" # The base URL for Jikan API; constants use uppercase

# Function to fetch anime details
def get_details():
    anime_id = entry_left.get() # Get the ID from the entry widget
    url = f"{BASE_URL}/{anime_id}"
    response = requests.get(url)

    # Clear the box before displaying new results
    results_area_left.config(state = 'normal') # Enable the text widget to allow changes
    results_area_left.delete(1.0, tk.END) # Clear the text widget by deleting

    if response.status_code == 200: # Jikan API success code
        # Unpack JSON response and keep relevant data
        data = response.json()['data']

        # In case API response is broken/empty
        if data:
            # Seperate data into variables; use a default with .get() to prevent crashes if missing data
            title = data.get('title', "Unknown Title")
            score = data.get('score', "N/A")
            genres = [g.get('name') for g in data.get('genres', [])]
            themes = [t.get('name') for t in data.get('themes', [])]
            demographics = [d.get('name') for d in data.get('demographics', [])]
            episodes = data.get('episodes', "N/A")
            synopsis = data.get('synopsis', "No synopsis available")

            # Refining lists for readability; if list is empty, set to "N/A"
            genres = ", ".join(genres)  if genres else "N/A"
            themes = ", ".join(themes) if themes else "N/A"
            demographics = ", ".join(demographics) if demographics else "N/A"

            # Update the result label with the fetched details
            result_text = (
                f"Title: {title}\n"
                f"Score: {score}/10\n"
                f"Genre: {genres}\n"
                f"Theme: {themes}\n"
                f"Demographics: {demographics}\n"
                f"Episodes: {episodes}\n"
                f"Synopsis:\n{synopsis}"
            )

            results_area_left.insert(tk.INSERT, result_text) # Insert the result text into the text widget
        else:
            results_area_left.insert(tk.INSERT, "No data found")
    else:
        results_area_left.insert(tk.INSERT, f"Error: {response.status_code}") # If the API request fails, display the error code in the text widget

    results_area_left.config(state = 'disabled') # Disable the text widget to prevent user editing


# Function to generate anime recommendations
def get_recommendations():
    anime_id = entry_right.get()
    url = f"{BASE_URL}/{anime_id}/recommendations"
    response = requests.get(url)

    results_area_right.config(state = 'normal')
    results_area_right.delete(1.0, tk.END)

    if response.status_code == 200:
        data = response.json()['data']
        recommendations = []

        if data:
            for item in data[:40]: # Limit to top 40 recommendations
                title = item['entry']['title']
                recommendations.append(title)

            result_text = "\n".join(f" - {r}" for r in recommendations)

            results_area_right.insert(tk.INSERT, result_text)
        else:
            results_area_right.insert(tk.INSERT, "No recommendations found")
    else:
        results_area_right.insert(tk.INSERT, f"Error: {response.status_code}")
    
    results_area_right.config(state = 'disabled')


# Window setup (contains and holds everything)
root = tk.Tk() # The primary or "base" window is called root
root.title("Anime Recommender")
root.geometry("1200x700")


# Frame setup (Organize the window into sections)
left_frame = tk.Frame(root)
left_frame.pack(side = "left", fill = "both", expand = True, padx = 10, pady = 10)

right_frame = tk.Frame(root)
right_frame.pack(side = "right", fill = "both", expand = True, padx = 10, pady = 10)


# Widgets setup (Components of the window)

# Left frame widgets (Details)
lbl_title_left = tk.Label(left_frame, text = "Anime Details") # Creates label
lbl_title_left.pack(pady = 10)

lbl_instruction_left = tk.Label(left_frame, text = "Enter Anime ID:")
lbl_instruction_left.pack(pady = 5)

entry_left = tk.Entry(left_frame) # Creates an entry widget for user input
entry_left.pack(pady = 5)

btn_left = tk.Button(left_frame, text = "Fetch Data", command = get_details) # Creates a button that will call the getDetails function when clicked
btn_left.pack(pady = 5)

results_area_left = tk.scrolledtext.ScrolledText(left_frame, width = 40, height = 25, wrap = tk.WORD) # tk.WORD wrapping moves the entire word to the next line instead of just wrapping the remainder of the word
results_area_left.pack(pady = 10, padx = 10, fill = 'both', expand = True)
results_area_left.config(state = 'disabled')

# Right frame widgets (Recommendations)
lbl_title_right = tk.Label(right_frame, text = "Anime Recommendations")
lbl_title_right.pack(pady = 10)

lbl_instruction_right = tk.Label(right_frame, text = "Enter Anime ID:")
lbl_instruction_right.pack(pady = 5)

entry_right = tk.Entry(right_frame)
entry_right.pack(pady = 5)

btn_right = tk.Button(right_frame, text = "Get Recommendations", command = get_recommendations)
btn_right.pack(pady = 5)

results_area_right = tk.scrolledtext.ScrolledText(right_frame, width = 40, height = 25, wrap = tk.WORD)
results_area_right.pack(pady = 10, padx = 10, fill = 'both', expand = True)
results_area_right.config(state = 'disabled')


# This starts the GUI event loop, allowing the window to be displayed and interact with the user; required to prevent the window from closing immediately after program execution
root.mainloop()