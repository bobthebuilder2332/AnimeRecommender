import requests # Used to handle HTTP requests to the API
import tkinter as tk # Used to create a GUI for the application / seperate window
from tkinter import scrolledtext # Used to create a scrollable text widget for displaying results; doesn't import automatically with tkinter, so it needs to be imported separately

# Function to fetch anime details
def get_details():
    id = entry.get() # Get the ID from the entry widget
    url = f"https://api.jikan.moe/v4/anime/{id}"
    response = requests.get(url)

    # Clear the box before displaying new results
    results_area.config(state = 'normal') # Enable the text widget to allow changes
    results_area.delete(1.0, tk.END) # Clear the text widget by deleting

    if response.status_code == 200: # Jikan API success code
        # Seperate data into variables
        data = response.json()['data']
        title = data.get('title')
        score = data.get('score')
        genres = [g.get('name') for g in data.get('genres', [])]
        themes = [t.get('name') for t in data.get('themes', [])]
        demographics = [d.get('name') for d in data.get('demographics', [])]
        episodes = data.get('episodes')
        synopsis = data.get('synopsis')

        # Update the result label with the fetched details; use += to add data because triple quote fstrings take the indent as part of the stirng
        result_text = f"Title: {title}\n"
        result_text += f"Score: {score}/10\n"
        result_text += f"Genre: {', '.join(genres)}\n"
        result_text += f"Theme: {', '.join(themes)}\n"
        result_text += f"Demographics: {', '.join(demographics)}\n"
        result_text += f"Episodes: {episodes}\n"
        result_text += f"Synopsis: {synopsis}"

        results_area.insert(tk.INSERT, result_text) # Insert the result text into the text widget
    else:
        results_area.config(text = f"Error: {response.status_code}")

    results_area.config(state = 'disabled') # Disable the text widget to prevent user editing


# Window setup (contains and holds everything)
root = tk.Tk() # The primary or "base" window is called root
root.title("Anime Recommender")
root.geometry("1200x700")


# Widgets setup (Components of the window)
label_instruction = tk.Label(root, text = "Enter Anime ID:") # Creates label
label_instruction.pack(pady = 5) # Adds the label to the window and adds some vertical padding

entry = tk.Entry(root) # Creates an entry widget for user input
entry.pack(pady = 5)

button = tk.Button(root, text = "Fetch Data", command = get_details) # Creates a button that will call the getDetails function when clicked
button.pack(pady = 5)

results_area = tk.scrolledtext.ScrolledText(root, width = 100, height = 30, wrap = tk.WORD) # tk.WORD wrapping moves the entire word to the next line instead of just wrapping the remainder of the word
results_area.pack(pady = 5)
results_area.config(state = 'disabled')


# This starts the GUI event loop, allowing the window to be displayed and interact with the user; required to prevent the window from closing immediately after program execution
root.mainloop()