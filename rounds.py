from tkinter import *
from functools import partial  # To prevent unwanted windows


class ChooseRounds:

    def __init__(self):
        button_fg = "#46C5F9"
        button_font = ("Arial", "13", "bold")
        bg_color = "#E3D0C6"  # Background color

        # Set up GUI Frame
        self.intro_frame = Frame(padx=10, pady=10, bg=bg_color)
        self.intro_frame.grid()

        # heading and brief instructions
        self.intro_heading_label = Label(self.intro_frame, text="Movie Questionnaire",
                                         font=("Spicy Rice", "24"), bg=bg_color)
        self.intro_heading_label.grid(row=0)

        choose_instructions_txt = (
            "In each round you will be given a quote from a "
            "movie and you have 3 options to get the "
            "correct movie. \n\n\n"
            "To begin please type below how many rounds "
            "you would like to play:"
        )
        self.choose_instructions_label = Label(
            self.intro_frame,
            text=choose_instructions_txt,
            wraplength=300,
            justify="center",
            bg=bg_color,
        )
        self.choose_instructions_label.grid(row=1)

        self.round_frame = Frame(self.intro_frame, bg=bg_color)
        self.round_frame.grid(row=2)

        self.round_entry = Entry(
            self.round_frame,
            font=("Arial", "14"),
        )
        self.round_entry.grid(row=0, padx=10, pady=10)

        self.submit_button = Button(
            self.round_frame,
            text="Start",
            command=self.start_game,
            bg=button_fg,
            font=button_font,
        )
        self.submit_button.grid(row=0, padx=10, pady=10, column=1)

        self.output_label = Label(self.round_frame, text="", fg="#9C0000", bg=bg_color)
        self.output_label.grid(row=2)

    def start_game(self):
        try:
            rounds = int(self.round_entry.get())
            if rounds <= 0:
                raise ValueError("The number of rounds must be greater than 0.")

            self.output_label.config(text="", fg="#9C0000")
            self.intro_frame.grid_forget()
            root.withdraw()  # Hide the main window
            Play(rounds)

        except ValueError:
            self.output_label.config(text="Please enter a valid number to continue")


class Play:

    def __init__(self, how_many):
        self.play_box = Toplevel()
        bg_color = "#f0f0f0"  # Background color

        # If users press cross at top, closes help and
        # 'releases' help button
        self.play_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_play))

        self.quest_frame = Frame(self.play_box, padx=10, pady=10, bg=bg_color)
        self.quest_frame.grid()

        rounds_heading = "Choose - Round 1 of {}".format(how_many)
        self.choose_heading = Label(self.quest_frame, text=rounds_heading,
                                    font=("Arial", "16", "bold"), bg=bg_color)
        self.choose_heading.grid(row=0)

        self.control_frame = Frame(self.quest_frame, bg=bg_color)
        self.control_frame.grid(row=6)

        self.start_over_button = Button(self.control_frame, text="Start again",
                                        command=self.close_play)
        self.start_over_button.grid(row=0, column=2)

    def close_play(self):
        # reshow root (ie: choose rounds) and end current
        # game / allow new game to start
        root.deiconify()
        self.play_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Movie Quotes")
    ChooseRounds()
    root.mainloop()
