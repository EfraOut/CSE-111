import tkinter as tk
import number_entry as numy
from math import pi


def main():
        
    root = tk.Tk()

    frm_main = tk.Frame(root, background='yellow')
    frm_main.master.title('Circle stuff')
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    populate_main_window(frm_main)

    root.mainloop()


def populate_main_window(frm_main):

    # Create a label that displays "Radius"
    lbl_radius = tk.Label(frm_main, text='Radius:', background='red')
    lbl_results = tk.Label(frm_main, text='Area:', background='green')

    ent_area = numy.IntEntry(frm_main, 1, 90, width=5)
    lbl_area = tk.Label(frm_main, width=8, background='grey70')


    # Layout labels in a grid
    lbl_radius.grid(  row=0, column=0, padx=3, pady=3,)
    ent_area.grid(  row=0, column=1, padx=3, pady=3)
    lbl_results.grid(  row=0, column=2, padx=3, pady=3)
    lbl_area.grid( row=0, column=3, padx=3, pady=3)


    def calc(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the user's age.
            radius = ent_area.get()

            # Compute the user's slowest and
            # fastest beneficial heart rates.
            area = pi * radius ** 2

            # Display the slowest and fastest benficial
            # heart rates for the user to see.
            lbl_area.config(text=f"{area:.2f}")

        except ValueError:
            # When the user deletes all the digits in the age
            # entry box, clear the slowest and fastest labels.
            lbl_area.config(text="")

    ent_area.bind("<KeyRelease>", calc)


main()