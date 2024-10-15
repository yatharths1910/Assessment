# Now let's modify the code to incorporate these quotes into the quiz game
from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import csv



class ChooseRounds:
    def __init__(self, quotes_data):
        self.quotes_data = quotes_data
        # Invoke play class with three rounds for testing purposes.
        self.to_play(3)

    def to_play(self, num_rounds):
        Play(num_rounds, self.quotes_data)
        root.withdraw()


class Play:
    def __init__(self, how_many, quotes_data):
        self.play_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.play_box.protocol('WM_DELETE_WINDOW', partial(self.close_play))

        # Variables used to work out statistics, when game ends etc.
        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        # Initially set rounds played and rounds won to 0
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        self.rounds_won = IntVar()
        self.rounds_won.set(0)

        # Load quotes data
        self.quotes_data = quotes_data
        self.current_quote_data = None

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        # Label to display the quote
        self.quote_label = Label(self.quest_frame, text='What Quote is this Movie from?', font=("Arial", 14, "bold"))
        self.quote_label.grid(row=0, columnspan=3)

        # Display the quote
        self.current_quote = Label(self.quest_frame, text='', font=("Arial", 12, "italic"), pady=10)
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
        self.help_button = Button(self.control_frame, text="Help", bg="#CC6600", fg="#FFFFFF",
                                  font=("Arial", 12, "bold"),
                                  width=10, command=self.get_help)
        self.help_button.grid(row=0, column=0, padx=10)

        self.reset_button = Button(self.control_frame, text="Reset", bg="#004C99", fg="#FFFFFF",
                                   font=("Arial", 12, "bold"),
                                   width=10, command=self.new_round)
        self.reset_button.grid(row=0, column=1, padx=10)

        self.stats_button = Button(self.control_frame, text="Stats", bg="#808080", fg="#FFFFFF",
                                   font=("Arial", 12, "bold"),
                                   width=10, command=self.get_stats)
        self.stats_button.grid(row=0, column=2, padx=10)

        self.load_new_quote()

    # Load quotes and movies from CSV
    def all_questions(self):
        file = open("movie_quotes.csv", "r")
        var_all_movies = list(csv.reader(file, delimiter=","))
        file.close()

    def load_new_quote(self):
        # Randomly select a quote and create a set of options (one correct, two incorrect)
        self.current_quote_data = random.choice(self.quotes_data)
        correct_movie = self.current_quote_data[1]

        # Select two random incorrect answers
        all_movies = [movie for _, movie in self.quotes_data if movie != correct_movie]
        options = random.sample(all_movies, 2) + [correct_movie]
        random.shuffle(options)

        # Update the displayed quote
        self.current_quote.config(text=f'"{self.current_quote_data[0]}"')

        # Update the option buttons
        for i, option in enumerate(options):
            self.option_buttons[i].config(text=option)

    def to_compare(self, option_index):
        selected_movie = self.option_buttons[option_index].cget('text')
        correct_movie = self.current_quote_data[1]

        if selected_movie == correct_movie:
            print(f"Correct! The quote is from '{correct_movie}'.")
        else:
            print(f"Wrong! The correct answer was '{correct_movie}'.")

        self.new_round()

    def get_stats(self):
        print("You chose to get the statistics")

    def get_help(self):
        print("You chose to get help")

    def new_round(self):
        print("Loading a new round...")
        self.load_new_quote()

    def close_play(self):
        root.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Movie Questionnaire")

    # Load the quotes from CSV
    quotes_data = load_quotes_from_csv(csv_file_path)

    ChooseRounds(quotes_data)
    root.mainloop()

