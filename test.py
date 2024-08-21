import tkinter as tk
import random
import pandas as pd

# Load the CSV data
csv_file_path = "/mnt/data/movie_quotes.csv"  # Path to the newly converted CSV file
data = pd.read_csv(csv_file_path)

# Create the main application window
root = tk.Tk()
root.title("Movie Questionnaire")
root.geometry("400x300")
root.config(bg="lightgrey")

# Function to load a new quote and options
def load_new_question():
    row = data.sample().iloc[0]
    quote = row['quote']
    correct_answer = row['movie']
    options = list(data['movie'].sample(2))
    options.append(correct_answer)
    random.shuffle(options)

    # Update the GUI elements with new data
    quote_label.config(text=f'"{quote}"')
    option1_button.config(text=options[0])
    option2_button.config(text=options[1])
    option3_button.config(text=options[2])

# Function to reset the quiz
def reset_quiz():
    load_new_question()

# Quote Label
quote_label = tk.Label(root, text='"Quote"', font=("Arial", 14), bg="lightgrey", wraplength=300)
quote_label.pack(pady=20)

# Options Buttons
option1_button = tk.Button(root, text="Option 1", width=15, height=2)
option1_button.pack(pady=5)

option2_button = tk.Button(root, text="Option 2", width=15, height=2)
option2_button.pack(pady=5)

option3_button = tk.Button(root, text="Option 3", width=15, height=2)
option3_button.pack(pady=5)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=reset_quiz, bg="lightblue", width=10)
reset_button.pack(side=tk.BOTTOM, pady=20)

# Load the first question
load_new_question()

# Start the main loop
root.mainloop()
