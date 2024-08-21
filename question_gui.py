from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random


class ChooseRounds:

    def __init__(self):

            Play(5)



class Play:

    def __init__(self, how_many):
        self.play_box = Toplevel()
        bg_color = "#f0f0f0"  # Background color

        # If users press cross at top, closes help and
        # 'releases' help button
        self.play_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_play))

        # get all the quotes for use in game
        self.all_quotes = self.get_all_quotes

        self.quiz_frame = Frame(self.play_box, padx=10, pady=10, bg=bg_color)
        self.quiz_frame.grid()

        rounds_heading = "Choose - Round 1 of {}".format(how_many)
        self.choose_heading = Label(self.quiz_frame, text=rounds_heading,
                                    font=("Josefin Sans", "16", "bold"), bg=bg_color)
        self.choose_heading.grid(row=0)

        self.control_frame = Frame(self.quiz_frame, bg=bg_color)
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
