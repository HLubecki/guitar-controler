from tkinter import *
from osc import *


root = Tk()
root.title("try")
root.geometry("750x250")


b_solo = Button(root,
                text=" solo ",
                background="white",
                fg="black",
                bg="orange",
                font=("Impact", 50),
                command=solo_preset)

b_rythm = Button(root,
                 text=" rythm ",
                 background="white",
                 fg="black",
                 bg="yellow",
                 font=("Impact", 50),
                 command=rythm_preset)

b_clean = Button(root,
                 text=" clean ",
                 background="white",
                 fg="black",
                 bg="light green",
                 font=("Impact", 50),
                 command=clean_preset)

root.bind('<7>', solo_preset)
root.bind('<8>', rythm_preset)
root.bind('<9>', clean_preset)

b_solo.grid(column=1, row=1, padx=15, pady=50)

b_rythm.grid(column=2, row=1, padx=15, pady=50)

b_clean.grid(column=3, row=1, padx=15, pady=50)

root.mainloop()
