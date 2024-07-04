from tkinter import *
from osc import *


def a(event):
    print(123)


root = Tk()
root.title("try")
root.geometry("750x250")

root.bind('<7>', solo_preset)
root.bind('<8>', rythm_preset)
root.bind('<9>', clean_preset)

root.mainloop()
