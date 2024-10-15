from tkinter import *
from functools import partial
import random
import pandas as pd

# users choose 3, 5, or 10 rounds
class ChooseRounds:

    def __init__(self):
        # invoke play class with three rounds for testing purposes.
        self.to_play(3)

    def to_play(self, num_rounds):
        Play(num_rounds)
        root.withdraw()  # Hide root window


class Play:

    def __init__(self, how_many):

        self.play_box = Toplevel()

        # If users press cross at top, closes help and releases help button
        self.play_box.protocol('WM_DELETE_WINDOW', partial(self.close_play))

        # Variables used to work out statistics, when game ends, etc.
        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        # Load quotes from the file
        self.all_quotes = self.get_all_quotes()

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        # Label to display the question
        self.quote_label = Label(self.quest_frame, text='What Quote is this Movie from?', font=("Arial", 14, "bold"))
        self.quote_label.grid(row=0, columnspan=3)

        # Display the randomly chosen quote
        self.current_quote = Label(self.quest_frame, text=self.get_random_quote(), font=("Arial", 12, "italic"), pady=10)
        self.current_quote.grid(row=1, columnspan=3)

        # Option Buttons Frame
        self.option_frame = Frame(self.quest_frame)
        self.option_frame.grid(row=2, pady=10)

        # Create buttons for the three options
        self.option_buttons = []
        for i in range(3):
            button = Button(self.option_frame, text=f"Option {i + 1}", width=20, height=2, font=("Arial", 10),
                            command=lambda i=i: self.to_compare(i))
            button.grid(row=0, column=i, padx=10)
            self.option_buttons.append(button)

        # Frame for Help, Reset, and Stats buttons
        self.control_frame = Frame(self.quest_frame, pady=10)
        self.control_frame.grid(row=3, pady=20)

        # Create control buttons
        self.help_button = Button(self.control_frame, text="Help", bg="#CC6600", fg="#FFFFFF", font=("Arial", 12, "bold"),
                                  width=10, command=self.get_help)
        self.help_button.grid(row=0, column=0, padx=10)

        self.reset_button = Button(self.control_frame, text="Reset", bg="#004C99", fg="#FFFFFF", font=("Arial", 12, "bold"),
                                   width=10, command=self.new_round)
        self.reset_button.grid(row=0, column=1, padx=10)

        self.stats_button = Button(self.control_frame, text="Stats", bg="#808080", fg="#FFFFFF", font=("Arial", 12, "bold"),
                                   width=10, command=self.get_stats)
        self.stats_button.grid(row=0, column=2, padx=10)

    # Function to load the quotes from the file
    def get_all_quotes(self):
        # Load the CSV or Excel file with quotes
        file_path = '/mnt/data/movie_quotes.csv'
        df = pd.read_excel(file_path)

        # Split each entry to separate quote and movie name
        quotes = df.iloc[:, 0].apply(lambda x: x.split('-')[0].strip()).tolist()
        return quotes

    # Function to randomly select a quote
    def get_random_quote(self):
        return random.choice(self.all_quotes)

    def to_compare(self, option):
        print(f"You chose option {option + 1}")

    def get_stats(self):
        print("You chose to get the statistics")

    def get_help(self):
        print("You chose to get help")

    def new_round(self):
        # Pick a new random quote for the next round
        self.current_quote.config(text=self.get_random_quote())
        print("Resetting the round...")

    def close_play(self):
        root.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Movie Questionnaire")
    ChooseRounds()
    root.mainloop()
