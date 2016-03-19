from tkinter.ttk import *
from tkinter import *

import gui_display_v2

class App:

    def __init__(self):
        root = Tk()
        gui_display_v2.Window(root)
        root.mainloop()

if __name__ == "__main__":
    sys.exit(App())
